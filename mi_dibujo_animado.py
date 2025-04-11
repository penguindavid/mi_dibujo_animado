import pygame
import sys
import random

# Colores
rojo = (255, 105, 97)
azul = (0, 0, 255)
verde = (0, 255, 0)
rosado = (255, 192, 203)
negro = (0, 0, 0)
amarillo = (255, 255, 0)
blanco = (225, 225, 225)
naranja = (255, 165, 0)
cian = (81, 209, 246)
lila_pastel = (204, 160, 221)
gris_oscuro = (127, 127, 127)

# Inicializar Pygame
pygame.init()
ventana = pygame.display.set_mode((500, 500))
pygame.display.set_caption("Electrike")

clock = pygame.time.Clock()

###########################
# Bucle principal del juego
###########################
while True:
    # Ciclo para la detección de los eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()


 # Dibujar un rectangulo 
    pygame.draw.rect(ventana, negro, (150,250, 60,40)) 
    # rectangulo sin relleno,esquina sup. izq: (100,100),esquina. inf. der: (150,200). 
    pygame.draw.rect(ventana,cian , ((10,50),(480,390)),) # cuadrado gris parte superior 1
     #dibujar linea 
    for _ in range(100):
   
        linea = random.randint(50, 50 + 400)
        lineas = random.randint(100, 100 + 350)
        lineac = random.randint(50, 50 + 400)
        lineav = random.randint(100, 100 + 350)
        
        color_linea = random.choice([rojo, azul, verde, rosado, amarillo, naranja, cian])

        pygame.draw.line(ventana, color_linea, (linea, lineas), (lineac, lineav))
    pygame.draw.rect(ventana, rojo, (110,100,195,60)) # cuadrado gris
    pygame.draw.rect(ventana, gris_oscuro, (150,140,120,140)) # cuadrado lila 
    pygame.draw.rect(ventana, lila_pastel, (165,145,95,100)) # cara
    pygame.draw.circle(ventana,amarillo,(210,190),50) # boca
    pygame.draw.circle(ventana,rojo,(210,215),10) # ojo 1
    pygame.draw.circle(ventana,blanco,(230,185),10) # pupila 1
    pygame.draw.circle(ventana,negro,(230,185),5) # ojo 2
    pygame.draw.circle(ventana,blanco,(190,185),10) # pupila2 
    pygame.draw.circle(ventana,negro,(190,185),5) # cuadrado gris parte superior 1
    pygame.draw.rect(ventana, gris_oscuro, (110,100,195,60)) # cuadrado gris parte superior 2
    pygame.draw.rect(ventana, gris_oscuro, (160,80,100,80)) # circulo de parte derecha
    pygame.draw.circle(ventana, gris_oscuro,(450,300), 50 )
    pygame.draw.rect(ventana, rojo, (300,250,150,90)) 
    pygame.draw.rect(ventana, rojo, (120,250,350,100)) # cuadrado rojo 
    pygame.draw.rect(ventana, rojo, (150,245,259,150)) # rueda 
    pygame.draw.circle(ventana, gris_oscuro, (167,400), 50 ) 
    pygame.draw.circle(ventana, gris_oscuro, (269,400), 50 ) 
    pygame.draw.circle(ventana, gris_oscuro, (370,400), 50 ) # Dibujar un rectangulo 
    pygame.draw.rect(ventana, negro, (280,390, 60,40)) 
    pygame.draw.rect(ventana, negro, (190,390, 60,40)) 
    pygame.draw.rect(ventana, negro, (330,205, 50,40)) 
    pygame.draw.rect(ventana, negro, (310,205, 90,20))# Rellenar la ventana de color



    # Texto
    fuente_arial = pygame.font.SysFont("Arial", 23, True, True)
    texto1 = fuente_arial.render("Colegio San Jose de Guanenta", True, negro)
    texto2 = fuente_arial.render("David Santiago Mácias Maldonado", True, negro)
    texto3 = fuente_arial.render("especialidad de sistemas", True, negro)

    ventana.blit(texto1, (80, 10))
    ventana.blit(texto2, (50, 450))
    ventana.blit(texto3, (80, 30))

    # Actualizar la visualización
    pygame.display.flip()
    clock.tick(60)


