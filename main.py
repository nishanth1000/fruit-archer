
#FRUIT ARCHER
#BY - - NISHANTH K

#Icons made by <a href="https://www.flaticon.com/authors/eight-black-dots" title="Eight Black Dots">Eight Black Dots</a> from <a href="https://www.flaticon.com/" title="Flaticon"> www.flaticon.com</a>

import pygame as p
import sys , random
p.init()

welcome = True
y=161
fruitposx = [672,544,416]
fruitposy = [33,97,161,225,289,353]
swordpos = [48,49,50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70,
            71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91,
            92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109,
            110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126,
            127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143,
            144, 145, 146, 147, 148, 149, 150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 160,
            161, 162, 163, 164, 165, 166, 167, 168, 169, 170, 171, 172, 173, 174, 175, 176, 177, 178]
score = 0
life = 5


screen  = p.display.set_mode((800,450))
p.display.set_caption('FRUIT ARCHER')

font = p.font.SysFont('Showcard Gothic',50)
font1 = p.font.SysFont('Showcard Gothic',35)
font3 = p.font.SysFont('Poor Richard',25,bold=True)
font2 = p.font.SysFont('Bernard MT Condensed',30)

start = False

icon = p.image.load('img files/sword.png')
sword  = p.image.load('img files/sword.png')
apple = p.image.load('img files/apple.png')
coconut = p.image.load('img files/coconut.png')
pear = p.image.load('img files/pear.png')
strawberry = p.image.load('img files/strawberry.png')
orange = p.image.load('img files/orange.png')
pineapple = p.image.load('img files/pineapple.png')

fruits = [apple,coconut,pear,strawberry,orange,pineapple]

p.display.set_icon(icon)
p.display.update()

s1=int(random.choice(fruitposx))
t1=int(random.choice(fruitposy))
u1=(random.choice(fruits))

s2=int(random.choice(fruitposx))
t2=int(random.choice(fruitposy))
u2=(random.choice(fruits))
p.mixer.init()
p.mixer.music.load('img files/[iSongs.info] 01 - Emitemitemito-[AudioTrimmer.com].mp3')
p.mixer.music.set_volume(0.5)
p.mixer.music.play(-1)

while True:
    screen.fill((255,255,255))
    screen.blit(sword,(50, y))
    lifetxt = 'LIFE : ' + str(life)
    scoretxt = 'SCORE : ' + str(score)

    if(welcome == True):
        txt1 = font.render('FRUIT ARCHER',True,(25,25,25));screen.blit(txt1, (220, 40))
        txt2 = font1.render('WELCOME', True, (25,25,25));screen.blit(txt2, (450, 150))
        txt3 = font3.render('Press UP and DOWN to move the KNIFE.',True,(25,25,25));screen.blit(txt3,(300,220))
        txt4 = font3.render('More Fruits you smash more Points you get.',True,(25,25,25));screen.blit(txt4,(290,250))
        txt5 = font3.render('You have 5 life to play.',True,(25,25,25));screen.blit(txt5,(380,280))
        txt6 = font3.render('Losing a fruit will reduce a LIFE.',True,(25,25,25));screen.blit(txt6,(330,310))
        txt7 = font3.render('Hit SPACE to Start.',True,(25,25,25));screen.blit(txt7,(430,360))

    if(start == True):
        txt8 = font3.render(lifetxt, True, (25, 25, 25));screen.blit(txt8, (25, 15))
        txt9 = font3.render(scoretxt, True, (25, 25, 25));screen.blit(txt9, (650, 15))
        screen.blit(u1,(s1,t1))
        if(s1 != s2 and t1 != t2):
            screen.blit(u2,(s2,t2))
        s1 -=0.3
        s2 -=0.2

        if(s1 <=1):
            life  = life - 1
            s1=int(random.choice(fruitposx))
            t1=int(random.choice(fruitposy))
            u1=(random.choice(fruits))

        if (s2 <= 1):
            life  = life - 1
            s2 = int(random.choice(fruitposx))
            t2 = int(random.choice(fruitposy))
            u2 = (random.choice(fruits))

    if(life == 0):
        start = False
        txt10 = font.render('YOUR LOST.',True,(25,25,25));screen.blit(txt10,(330,130))
        txt11 = font.render('YOUR '+scoretxt,True,(25,25,25));screen.blit(txt11,(300,200))
        txt12 = font2.render('Press ESC to Leave.',True,(25,25,25));screen.blit(txt12,(370,270))

    if(int(s1) in swordpos and y==t1):
        score = score + 1
        s1 = int(random.choice(fruitposx))
        t1 = int(random.choice(fruitposy))
        u1 = (random.choice(fruits))


    if (int(s2) in swordpos and y == t2):
        score = score + 1
        s2 = int(random.choice(fruitposx))
        t2 = int(random.choice(fruitposy))
        u2 = (random.choice(fruits))


    for event in p.event.get():

        if(event.type == p.QUIT):
            p.quit()
            sys.exit()

        if(event.type == p.KEYDOWN):
            if(event.key == p.K_ESCAPE):
                p.quit()
                sys.exit()

            if (event.key == p.K_SPACE):
                welcome = False
                start = True

            if(welcome == False):

                if(event.key == p.K_UP):
                    if(y>(0)):
                        y=y-64


                if(event.key == p.K_DOWN):
                    if(y<290):
                        y=y+64



    p.display.update()

p.quit()