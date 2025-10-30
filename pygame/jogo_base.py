import pygame
import sys 

pygame.init()

LARGURA = 800
ALTURA = 600

tela =pygame.display.set_mode((LARGURA,ALTURA))
pygame.display.set_caption("jogo de movimento e colissão")

AZUL =(0,120,255)
VERDE =(0,255,0)
VERMELHO = (255,0,0)

#jogador 
jogador = pygame.Rect(100,300,50,50)

#obstaculo
obstaculo = pygame.Rect(500,300,50,50)

#definindo a velocidade
velocidade = 5

#clock para contolar fps
clock =pygame.time.Clock()


tela.fill(VERDE)
pygame.draw.rect(tela,AZUL,jogador)
pygame.draw.rect(tela,VERMELHO,obstaculo)
pygame.display.flip()

while (True):
    for evento in pygame.event.get():
        if(evento.type == pygame.QUIT):
            pygame.quit()
            sys.exit()

    #teclas pressionadas 
    Teclas = pygame.key.get_pressed()

    if Teclas[pygame.K_UP]:
        jogador.y -= velocidade
    if Teclas[pygame.K_DOWN]:
        jogador.y += velocidade
    if Teclas[pygame.K_LEFT]:
        jogador.x -= velocidade
    if Teclas[pygame.K_RIGHT]:
        jogador.x += velocidade


#correção : limitar o jogador dentro da tela
    jogador .x =max(0,min(jogador.x, LARGURA - jogador.width))
    jogador .y =max(0,min(jogador.y, ALTURA - jogador.height))

#correção : detecção de colisão (o titulo promete colisão)

    if jogador .colliderect(obstaculo):
        print("colisão  detectada")

#remderização 
    tela.fill(AZUL)
    pygame.draw.rect(tela,VERDE,jogador)
    pygame.draw.rect(tela,VERMELHO,obstaculo)
    pygame.display.flip()

    clock.tick(60)




