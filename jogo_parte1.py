import pygame
from random import randint
pygame.init()
x = 205  # max 470 min 205
y = 100
pos_x = 170
pos_y = 800
pos_y_a = 800
pos_y_b = 800

velocidade = 10
velocidade_outros = 15

fundo = pygame.image.load('pista.png')
carro = pygame.image.load('carro.png')
carro2 = pygame.image.load('carro2.png')
carro3 = pygame.image.load('carro3.png')
arvore = pygame.image.load('imagem/arvore2.png')
arvore2 = pygame.image.load('imagem/arvore3.png')

janela = pygame.display.set_mode((780, 550))
pygame.display.set_caption("Criando jogo com Python")

janela_aberta = True
while janela_aberta:
    pygame.time.delay(50)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            janela_aberta = False

    comandos = pygame.key.get_pressed()

    if comandos[pygame.K_RIGHT] and x <= 470:
        x += velocidade
    if comandos[pygame.K_LEFT] and x >= 205:
        x -= velocidade

    if (pos_y <= -180) and (pos_y_a <= -200) and (pos_y_b <= -180) :
        pos_y = randint (800,2000)
        pos_y_a = randint (800,2000)
        pos_y_b = randint (800,2000)

    pos_y -= velocidade_outros
    pos_y_a -= velocidade_outros +2
    pos_y_b -= velocidade_outros +10

    janela.blit(fundo,(0,0))
    janela.blit(carro,(x,y))
    janela.blit(carro2,(pos_x,pos_y))
    janela.blit (carro3, (pos_x + 240, pos_y_a))
    janela.blit(arvore,(pos_x + 450,pos_y +400))
    janela.blit (arvore2, (pos_x + 430, pos_y + 100))

    pygame.display.update()


pygame.quit()

