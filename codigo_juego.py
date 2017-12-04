from pygame_functions import *


#constantes y set ups
screenSize(900,500)
setBackgroundImage("fondo1.png")
makeMusic("batalla.mp3")
playMusic()
#paredes
pared_izq = makeSprite("pared_lateral.png")#creamos la pared de la izquierda
moveSprite(pared_izq,0,0)
showSprite(pared_izq)

pared_der= makeSprite("pared_lateral.png")#creamos la pared derecha
moveSprite(pared_der,895,0)
showSprite(pared_der)


piso= makeSprite("pared_piso.png")#el piso nos sirve de referecia para poder hacer un efecto de gravedad
moveSprite(piso,0,498)#importante si queremos que salte y al caer no se caiga infinitamente
showSprite(piso)

#plataforma 1
plataforma1= makeSprite("pv1.png")#una plataforma donde poder esquivar ataques
moveSprite(plataforma1,50,380)
showSprite(plataforma1)

plataforma_abajo1= makeSprite("estan.png")#una plataforma donde poder esquivar ataques
moveSprite(plataforma_abajo1,50,405)


#plataforma 2
plataforma2= makeSprite("pv1.png")#una plataforma donde poder esquivar ataques
moveSprite(plataforma2,200,280)
showSprite(plataforma2)

plataforma_abajo2= makeSprite("estan.png")#una plataforma donde poder esquivar ataques
moveSprite(plataforma_abajo2,200,300)

#plataforma 3

plataforma3= makeSprite("pv1.png")#una plataforma donde poder esquivar ataques
moveSprite(plataforma3,360,180)
showSprite(plataforma3)

plataforma_abajo3= makeSprite("estan.png")#una plataforma donde poder esquivar ataques
moveSprite(plataforma_abajo3,360,200)

#plataforma 4

plataforma4= makeSprite("pv1.png")#una plataforma donde poder esquivar ataques
moveSprite(plataforma4,520,280)
showSprite(plataforma4)

plataforma_abajo4= makeSprite("estan.png")#una plataforma donde poder esquivar ataques
moveSprite(plataforma_abajo4,520,300)

#plataforma 5

plataforma5= makeSprite("pv1.png")#una plataforma donde poder esquivar ataques
moveSprite(plataforma5,650,380)
showSprite(plataforma5)

plataforma_abajo5= makeSprite("estan.png")#una plataforma donde poder esquivar ataques
moveSprite(plataforma_abajo5,650,400)

#plataforma 6

plataforma6= makeSprite("pv1.png")#una plataforma donde poder esquivar ataques
moveSprite(plataforma6,360,385)
showSprite(plataforma6)

plataforma_abajo6= makeSprite("estan.png")#una plataforma donde poder esquivar ataques
moveSprite(plataforma_abajo6,360,400)

#sprites
mario =  makeSprite("phd.png")#personaje que controla el jugador
addSpriteImage(mario,"phdizq.png")
zelda = makeSprite("robotinizq.png")#player2
addSpriteImage(zelda,"robotinder.png")
proyectil1 = makeSprite("proyectil1.png")
addSpriteImage(proyectil1,"proyectil2.png")
proyectil2 = makeSprite("proyectil3.png")
addSpriteImage(proyectil2,"proyectil4.png")

#VIDA DE LOS PERSOAJES

vida1 = 1000
vida2 = 1000

#TEXTO QUE DICE LA VIDA
texto_vida1 = makeLabel("Ph.D : 1000 HP",28,8,0,"green")#la vida del personaje 1
showLabel(texto_vida1)

texto_vida2 = makeLabel("ROBOTIN: 1000 HP",28,680,0,"green")#la vida del personaje 1
showLabel(texto_vida2)

#TEXTO QUE DICE EL GANADOR
ganador1 = makeLabel("GANDOR : Ph.D ",40,300,230,"lightgreen")
ganador2 = makeLabel("GANDOR : ROBOTIN ",40,300,230,"lightgreen")
#MOSTRANDO LOS PERSONAJES
showSprite(mario)#mostramos a nuestro personaje
showSprite(zelda)#mostramos al enemigo


#variables relacionadas con el movimiento
gravedad1 =0
gravedad2=0
#jugador 1
jugador1_posx = 250#es la posicion que se actualiza cuando se oprimen las teclas der o izq
jugador1_posy = 420#el piso empieza ahi para el srite del jugador
velocidad_de_salto1 = 0#hace referencia a el estado del salto sin que se oprima ninguna letra

#jugador 2
jugador2_posx = 500#es la posicion que se actualiza cuando se oprimen las teclas der o izq
jugador2_posy = 40
velocidad_de_salto2 = 0

#proyectil
posy1_coin = 0
vel1_coin = 0
dir_proyectil1=1

#proyectil2
posy2_coin = 0
vel2_coin = 0

bandera = True
while(bandera==True):
    #las gravedades dw ambos jugadores
    gravedad1+=0.1
    gravedad2+=0.1

    #COLISIONES CON PAREDES

    #colisiones con paredes del JUGADOR 1
    if touching(mario,pared_izq):#colision con pared izquierda
        jugador1_posx+=3
    if touching(mario,pared_der):#colision con pared derecha
        jugador1_posx-=3
    if touching(mario,piso):#colision con el piso
        jugador1_posy =440
        gravedad1=0
    # colisiones con paredes del JUGADOR 2
    if touching(zelda,pared_izq):#colision con pared izquierda
        jugador2_posx+=3
    if touching(zelda,pared_der):#colision con pared derecha
        jugador2_posx-=3
    if touching(zelda,piso):
        jugador2_posy = 440
        gravedad2 = 0#es necesario volverla a igualar a cero, porque por el loop haria que la gravedad fuera
                  #a lo largo del juego, infinita
    if touching(proyectil1,pared_der)or touching(proyectil1,pared_izq) :#si el proyectil toca alguna de las paredes laterales se esconde
        hideSprite(proyectil1)
    if touching(proyectil2,pared_der)or touching(proyectil2,pared_izq) :#no elimino el sprite porque se quiebra el juego
        hideSprite(proyectil2)#esto genera que quiza, el jugador contrario reciba daño de la "nada" en el caso de que se choque contra la pared
    #un proyectil, y el jugdor se devuelva



    #COLISIONES CON PLATAFORMAS

    # colisiones con las plataformas JUGADOR 1
    if touching(mario,plataforma1):#parte de arriba PLATAFORMA 1
       jugador1_posy-=1.2
       gravedad1=0
    if touching(mario,plataforma_abajo1):#parte de abajo PLATAFORMA 1
       jugador1_posy+=15
    if touching(mario,plataforma2):#parte de arriba PLATAFORMA 2
       jugador1_posy-=1.1
       gravedad1=0
    if touching(mario,plataforma_abajo2):#parte de abajo PLATAFORMA 2
       jugador1_posy+=15
    if touching(mario,plataforma3):#parte de arriba PLATAFORMA 3
       jugador1_posy-=1.1
       gravedad1=0
    if touching(mario,plataforma_abajo3):#parte de abajo PLATAFORMA 3
       jugador1_posy+=15
    if touching(mario,plataforma4):#parte de arriba PLATAFORMA 4
       jugador1_posy-=1.1
       gravedad1=0
    if touching(mario,plataforma_abajo4):#parte de abajo PLATAFORMA 4
       jugador1_posy+=15
    if touching(mario,plataforma5):#parte de arriba PLATAFORMA 5
       jugador1_posy-=1.1
       gravedad1=0
    if touching(mario,plataforma_abajo5):#parte de abajo PLATAFORMA 5
       jugador1_posy+=15
    if touching(mario,plataforma6):#parte de arriba PLATAFORMA 6
       jugador1_posy-=1.1
       gravedad1=0
    if touching(mario,plataforma_abajo6):#parte de abajo PLATAFORMA 6
       jugador1_posy+=15

    # colisiones con las plataformas JUGADOR 2
    if touching(zelda,plataforma1):#parte de arriba PLATAFORMA 1
        jugador2_posy-=2
        gravedad2=0
    if touching(zelda,plataforma_abajo1):#parte de abajo PLATAFORMA 1
        jugador2_posy+=15
    if touching(zelda,plataforma2):#parte de arriba PLATAFORMA 2
       jugador2_posy-=2
       gravedad2=0
    if touching(zelda,plataforma_abajo2):#parte de abajo PLATAFORMA 2
       jugador2_posy+=15
    if touching(zelda,plataforma3):#parte de arriba PLATAFORMA 3
       jugador2_posy-=2
       gravedad2=0
    if touching(zelda,plataforma_abajo3):#parte de abajo PLATAFORMA 3
       jugador2_posy+=15
    if touching(zelda,plataforma4):#parte de arriba PLATAFORMA 4
       jugador2_posy-=2
       gravedad2=0
    if touching(zelda,plataforma_abajo4):#parte de abajo PLATAFORMA 4
       jugador2_posy+=15
    if touching(zelda,plataforma5):#parte de arriba PLATAFORMA 5
       jugador2_posy-=2
       gravedad2=0
    if touching(zelda,plataforma_abajo5):#parte de abajo PLATAFORMA 5
       jugador2_posy+=15
    if touching(zelda,plataforma6):#parte de arriba PLATAFORMA 6
       jugador2_posy-=2
       gravedad2=0
    if touching(zelda,plataforma_abajo6):#parte de abajo PLATAFORMA 6
       jugador2_posy+=15
    #CONTROLES

    #CONTROLES JUGADOR 1
    if keyPressed("left"):#se mueve a la izquierda
        jugador1_posx -= 2
        changeSpriteImage(mario,1)
        changeSpriteImage(proyectil1,1)
        vel1_coin = -8
    if keyPressed("right"):#se mueve a la derecha
        jugador1_posx += 2
        changeSpriteImage(mario,0)
        changeSpriteImage(proyectil1,0)
        vel1_coin = 8
    if keyPressed("up"):#salta
        velocidad_de_salto1 = -5
    else: velocidad_de_salto1=0
    jugador1_posy += velocidad_de_salto1 + gravedad1
    #lanzar proyectil
    if keyPressed("down"):
        showSprite(proyectil1)
        posy1_coin = jugador1_posx



    posy1_coin +=vel1_coin
    moveSprite(proyectil1, posy1_coin, jugador1_posy)
    moveSprite(mario, jugador1_posx, jugador1_posy)


    #CONTROLES JUGADOR 2
    if keyPressed("a"):
        jugador2_posx-=2
        changeSpriteImage(zelda,0)
        changeSpriteImage(proyectil2, 1)
        vel2_coin = 8


    if keyPressed("d"):
        jugador2_posx+=2
        changeSpriteImage(zelda,1)
        changeSpriteImage(proyectil2, 0)
        vel2_coin = -8

    if keyPressed("w"):
        velocidad_de_salto2 = -5
    else:
        velocidad_de_salto2 = 0
    jugador2_posy += velocidad_de_salto2 + gravedad2

    if keyPressed("s"):
        showSprite(proyectil2)
        posy2_coin = jugador2_posx


    posy2_coin -=vel2_coin
    moveSprite(proyectil2, posy2_coin, jugador2_posy)
    moveSprite(zelda,jugador2_posx,jugador2_posy)


    #EVENTOS
    if touching(proyectil1,zelda):
        vida2-=1
        hideSprite(proyectil1)
        changeLabel(texto_vida2, "ROBOTIN : "+str(int(vida2)),"green")
        if(vida2<500):
            changeLabel(texto_vida2, "ROBOTIN : " + str(int(vida2)), "yellow")
        if (vida2 < 200):
            changeLabel(texto_vida2, "ROBOTIN : " + str(int(vida2)), "red")
        if(vida2<=0):
            changeLabel(texto_vida2, "ROBOTIN : muerto " , "black")
            killSprite(zelda)

    if touching(proyectil2,mario):
        hideSprite(proyectil2)
        vida1-=1
        hideSprite(proyectil1)
        changeLabel(texto_vida1, "Ph.D: " + str(int(vida1)), "green")
        if (vida1 < 500):
            changeLabel(texto_vida1, "Ph.D:  " + str(int(vida1)), "yellow")
        if (vida1 < 200):
            changeLabel(texto_vida1, "Ph.D: " + str(int(vida1)), "red")
        if (vida1 <= 0):
            changeLabel(texto_vida1, "Ph.D: muerto ", "black")
            killSprite(mario)

    if vida1<=0 or vida2<=0:
        hideAll()
        hideLabel(texto_vida1)
        hideLabel(texto_vida2)
        if vida1>0:
            showLabel(ganador1)
        if vida2>0:
            showLabel(ganador2)
        setBackgroundImage("YouWin.png")



endWait()
