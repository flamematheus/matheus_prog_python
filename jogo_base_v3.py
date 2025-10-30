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
BRANCO =(255,255,255) #versão 3 adicionando cor branca par ao texto

#jogador 
jogador = pygame.Rect(100,300,50,50)

#obstaculo
obstaculo = pygame.Rect(500,300,50,50)

#definindo a velocidade
velocidade = 5

#adiciondo vidas
vidas = 3

#adição : controla colisão fps
colidindo = False

#versão 3 variavel para controlar o game over
game_over = False

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

        #versão 3 : detectar a tecla presionada durante o game  over
        if (game_over and evento.type == pygame.KAYDOWN):
            if evento.kay == pygame .K_y:
                vidas = 3
                jogador.x =100
                jogador.y =300     
                game_over =False

            elif evento.kay == pygame.K_n:
                pygame.quit()
                sys.exit()

    # se o jogo terminou , mostra  a tela game over 
    if game_over:
        tela.fill((0,0,0))
        #versão :3 mostrar a mensagem game over
        fonte_grande = pygame.font.SysFont(None,72)
        texto_gameover = fonte_grande.render("GAMER OVER",True,VERMELHO)
        tela.blit(texto_gameover,(LARGURA//2 - texto_gameover.get_width()//2,ALTURA//2 -50))

        #versão 3 : mostra a pergunta para recomeçar 
        fonte_pequena = pygame.font.FontType(None,36)
        fonte_pequena = pygame.font.SysFont("deseja continuar ? (Y/N)",True,BRANCO)
        tela.blit(texto_pergunta,(LARGURA//2 - texto_pergunta.get_width()//2,ALTURA//2 +50))

        pygame.display.flip()
        clock.tick(60)
        continue #versão 3: pular o resto do loop enquanto  estuver em game over




    #teclas pressionadas 
    Teclas = pygame.key.get_pressed()

    #salvando a ultima posição do jogador para restaurar quando colidir
    jogador_anterior = jogador.copy()

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
        if not colidindo :
            vidas -=1
        print(f"colisão  detectada!vidas restantes {vidas}") # feedback visual no console
        colidindo = True

        #verificar o game over
        if vidas <=0:
            print("game over")
            pygame.quit()
            sys.exit()
        jogador = jogador_anterior    
    else:
        colidindo = False

#remderização 
    tela.fill(AZUL)
    pygame.draw.rect(tela,VERDE,jogador)
    pygame.draw.rect(tela,VERMELHO,obstaculo)
    pygame.display.flip()

    fonte = pygame.font.SysFont(None,36)
    texto_vidas = fonte.render(f"vidas{vidas}",True,(255,255,255))
    tela.blit(texto_vidas,(10,10))
    pygame.display.flip()


    #corrção : controle fps para movimentar mais suave
    clock.tick(60)