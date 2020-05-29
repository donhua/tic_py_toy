"""
This file is a part of My-PyChess application.

Here I have written a python interface class for stockfish chess engine.
This is used in the singleplayer mode of My-PyChess.
"""

import queue
import subprocess
import threading

_LEVELDATA = (
    (0, 20, 1),
    (2, 80, 1),
    (5, 120, 2),
    (9, 200, 4),
    (12, 300, 6),
    (15, 400, 8),
    (17, 500, 10),
    (19, 700, 12),
    (20, 900, 16),
)

# StockFish class to interface with stockfish chess engine.
class StockFish:
    def __init__(self, path="stockfish", level=1):
        self.moveSequence = ""
        self.skill, self.movetime, self.depth = _LEVELDATA[level - 1]

        self.thread = threading.Thread()
        self.q = queue.Queue(1)

        try:
            self.stockfish = subprocess.Popen(
                path,
                universal_newlines=True,
                stdin=subprocess.PIPE,
                stdout=subprocess.PIPE,
            )

            if self.stockfish.stdout.readline().split()[0].lower() == "stockfish":
                self.active = True
                self._put("uci")
                self.setOption("Skill Level", self.skill)
            else:
                self.active = False
                self.stockfish.terminate()

        except:
            self.active = False

    def _raiseErrorIfInactive(self):
        if not self.active:
            raise RuntimeError("Intergration with stockfish engine has failed")

    def _put(self, command):
        self._raiseErrorIfInactive()
        self.stockfish.stdin.write(f"{command}\n")
        self.stockfish.stdin.flush()

    def _isReady(self):
        self._raiseErrorIfInactive()
        self._put("isready")
        while True:
            if self.stockfish.stdout.readline().strip() == "readyok":
                return

    def _engine(self):
        self._isReady()
        self._put(f"position startpos moves {self.moveSequence.strip()}")
        self._put(f"go depth {self.depth} movetime {self.movetime}")
        while True:
            msg = self.stockfish.stdout.readline().strip().split(" ")
            if msg[0] == "bestmove":
                if msg[1] == "(none)":
                    self.q.put(None)
                else:
                    self.q.put(msg[1])
                break

    def isActive(self):
        return self.active

    def startGame(self, moves=""):
        self._isReady()
        self._put("ucinewgame")
        self.moveSequence = moves

    def setOption(self, name, value):
        self._isReady()
        self._put(f"setoption name {name} value {value}")

    def startEngine(self):
        self._raiseErrorIfInactive()
        if not self.thread.is_alive() and self.q.empty():
            self.thread = threading.Thread(target=self._engine)
            self.thread.start()
        else:
            raise RuntimeError("Could not start engine")

    def makeMove(self, move):
        self.moveSequence += " " + move
        self.startEngine()

    def getMove(self, block=True):
        self._raiseErrorIfInactive()
        if not self.hasMoved() and not block:
            self._put("stop")
        
        enginemove = self.q.get()
        self.moveSequence += " " + enginemove
        return enginemove

    def hasMoved(self):
        self._raiseErrorIfInactive()
        return not self.q.empty() and not self.thread.is_alive()

    def undo(self):
        self._raiseErrorIfInactive()
        if not self.thread.is_alive():
            temp = self.moveSequence.strip().split(" ")
            if len(temp) not in [0, 1]:
                self.moveSequence = " ".join(temp[:-2])

    def close(self):
        self._isReady()
        self._put("quit")
        self.stockfish.terminate()
        self.active = False

# A simple function to test wether a stockfish executable works or not.
# Path to stockfish must be specified as an argument
def teststockfish(path):
    fish = StockFish(path)
    stat = fish.isActive()
    if stat:
        fish.close()
    return stat

s = StockFish()