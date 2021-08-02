import pygame, time, random
from PPlay.window import *
from PPlay.gameimage import *
from PPlay.sprite import *



#inicialização
janela = Window(800, 590)
janela.set_title("Joguinho")
janela.set_background_color([255,255,0])
teclado = Window.get_keyboard()

fundo = GameImage("fundo.png")

y_pos = 500
x_pos = 700
turbo = Sprite("turbo.png", 1)


padE = Sprite ("pad1.png", 1)
padD = Sprite ("pad2.png", 1)
bola = Sprite("bola.png", 1)
bola.x = janela.width/2 - bola.width/2
bola.y = janela.height/2 - bola.height/2

padE.x = 5
padE.y = janela.height/2 - padE.height/2
padD.x = janela.width - padD.width - 5
padD.y = janela.height/2 - padD.height/2

pontD = 0
pontE = 0

velPad = 300
velPad2 = 0

velx = 300
vely = 250


start_time = time.time()
x = 1
counter = 0

iaPad = True



#GameLoop
while(True):


    #FPS
    counter+=1
    if (time.time() - start_time) > x :
        counter = 0
        start_time = time.time()



    pontuD = str(pontD)
    pontuE = str(pontE)
    #entrada de dados
    if teclado.key_pressed("UP") and (padD.y >= 0):
        padD.y = padD.y - velPad*janela.delta_time()
    if teclado.key_pressed("DOWN") and (padD.y + padD.height<= janela.height):
        padD.y = padD.y + velPad*janela.delta_time()
    if teclado.key_pressed("W") and (padE.y >= 0):
        padE.y = padE.y - velPad*janela.delta_time()
    if teclado.key_pressed("S") and (padE.y + padE.height<= janela.height):
        padE.y = padE.y + velPad*janela.delta_time()
    
    if (bola.collided(padD)) or (bola.collided(padE)):
        velx *=-1
    
    if bola.x <= 0:
        pontE += 1
        bola.x = janela.width/2 - bola.width/2
        bola.y = janela.height/2 - bola.height/2

    if bola.x + bola.width >= janela.width:
        pontD += 1
        bola.x = janela.width/2 - bola.width/2
        bola.y = janela.height/2 - bola.height/2

    #IA
    if(iaPad):
        bolaToFollow = bola

        if(bolaToFollow.x < janela.width / 2):
            if(bolaToFollow.y > padE.y):
                padE.y += 0.5 + velPad2 * janela.delta_time()
            else:
                padE.y -= 0.5 + velPad2 * janela.delta_time()

            #pad1.y = bola.y
            
            if (padE.y < 0):
                padE.y = 0
            if(padE.y + padE.height > janela.height):
                padE.y = janela.height - padE.height


        
        
    #update dos game objects
    bola.move_x(velx*janela.delta_time())
    bola.move_y(vely*janela.delta_time())
    #Física
    if (bola.x + bola.width >= janela.width) or (bola.x <= 0):
        velx *=-1
    
    if (bola.y + bola.height >= janela.height) or (bola.y <= 0):        
        vely *=-1


    turbo.set_position(x_pos, y_pos)
    if(bola.collided(turbo)):
        velx = velx + velx*0.3
        vely = vely + vely*0.3
        y_pos = random.randint(0, 500)
        x_pos = random.randint(0, 710)
    

    



    

    #desenho dos game objects
    
    fundo.draw()
    janela.draw_text(pontuD, 7, janela.height/10, size=30, color=(0,0,0), font_name="Arial", bold=False, italic=False)
    janela.draw_text(pontuE, janela.width - 25, janela.height/10, size=30, color=(0,0,0), font_name="Arial", bold=False, italic=False)
    janela.draw_text("FPS: " + str(round(counter / (time.time() - start_time))), 50, janela.height/11, size=30, color=(0,0,0), font_name="Arial", bold=False, italic=False)
    padE.draw()
    padD.draw()
    turbo.draw()
    bola.draw()
    janela.update()