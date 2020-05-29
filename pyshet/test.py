import random

level = 4
def numSUm(tx):
    a = int(tx[0])+int(tx[2])
    return a

def numText(level):
    data = [ 
                "0+1=",
                "1+0=",
                "0+2=",
                "2+0=",
                "1+1=",
                "0+3=",
                "3+0=",
                "1+2=",
                "2+1=",
                "0+4=",
                "4+0=",
                "1+3=",
                "3+1=",
                "2+2=",
                "0+5=",
                "5+0=",
                "1+4=",
                "4+1=",
                "2+3=",
                "3+2=",
                "0+6=",
                "6+0=",
                "1+5=",
                "5+1=",
                "2+4=",
                "4+2=",
                "3+3=",
                "0+7=",
                "7+0=",
                "1+6=",
                "6+1=",
                "2+5=",
                "5+2=",
                "3+4=",
                "4+3=",
                "0+8=",
                "8+0=",
                "1+7=",
                "7+1=",
                "2+6=",
                "6+2=",
                "3+5=",
                "5+3=",
                "4+4=",
                "0+9=",
                "9+0=",
                "1+8=",
                "8+1=",
                "2+7=",
                "7+2=",
                "3+6=",
                "6+3=",
                "4+5=",
                "5+4=",
                "0+10=",
                "10+0=",
                "1+9=",
                "9+1=",
                "2+8=",
                "8+2=",
                "3+7=",
                "7+3=",
                "4+6=",
                "6+4=",
                "5+5=",
    ]
    stage = [stage1, stage2, stage3, stage4, stage5, stage6, stage7, stage8, stage9, stage10,]
    levelUp = []
    for i in range(level):
        levelUp += stage[i]
    return levelUp

'''im1 = pygame.image.load('1.png')
im2 = pygame.image.load('2.png')
im3 = pygame.image.load('3.png')
im4 = pygame.image.load('7.png')
im5 = pygame.image.load('5.png')
im6 = pygame.image.load('6.png')
im7 = pygame.image.load('7.png')
im8 = pygame.image.load('8.png')
im9 = pygame.image.load('9.png')
im10 = pygame.image.load('10.png')'''



def numText(level):
    stage1 = [ 
                "0+1=",
                "1+0="      
    ]
    stage2 = [ 
                "0+2=",
                "2+0=",
                "1+1="
    ]
    stage3 = [ 
                "0+3=",
                "3+0=",
                "1+2=",
                "2+1="
    ]
    stage4 = [ 
                "0+4=",
                "4+0=",
                "1+3=",
                "3+1=",
                "2+2="
    ]
    stage5 = [ 
                "0+5=",
                "5+0=",
                "1+4=",
                "4+1=",
                "2+3=",
                "3+2="
    ]
    stage6 = [ 
                "0+6=",
                "6+0=",
                "1+5=",
                "5+1=",
                "2+4=",
                "4+2=",
                "3+3="
    ]
    stage7 = [ 
                "0+7=",
                "7+0=",
                "1+6=",
                "6+1=",
                "2+5=",
                "5+2=",
                "3+4=",
                "4+3="
    ]
    stage8 = [ 
                "0+8=",
                "8+0=",
                "1+7=",
                "7+1=",
                "2+6=",
                "6+2=",
                "3+5=",
                "5+3=",
                "4+4="
    ]
    stage9 = [ 
                "0+9=",
                "9+0=",
                "1+8=",
                "8+1=",
                "2+7=",
                "7+2=",
                "3+6=",
                "6+3=",
                "4+5=",
                "5+4="
    ]
    stage10 = [ 
                "1+9=",
                "9+1=",
                "2+8=",
                "8+2=",
                "3+7=",
                "7+3=",
                "4+6=",
                "6+4=",
                "5+5="
    ]
    stage = [stage1, stage2, stage3, stage4, stage5, stage6, stage7, stage8, stage9, stage10]
    levelUp = []
    for i in range(level):
        levelUp += stage[i]
    return levelUp


    def numVariant(summa):
    variant = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    variant.remove(summa)
    random.shuffle(variant)
    a = variant[:4]
    a.append(summa)
    random.shuffle(a)
    return a