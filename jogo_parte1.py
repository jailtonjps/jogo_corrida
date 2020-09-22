import pygame
pygame.init()
x = 400
y = 300
pos_x = 170
pos_y = 800
velocidade = 10
velocidade_outros = 20

fundo = pygame.image.load('pista.png')
carro = pygame.image.load('carro.png')
carro2 = pygame.image.load('carro2.png')
arvore = pygame.image.load('arvore.png')
arvore2 = pygame.image.load('arvore2.png')

janela = pygame.display.set_mode((780, 550))
pygame.display.set_caption("Criando jogo com Python")

janela_aberta = True
while janela_aberta:
    pygame.time.delay(50)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            janela_aberta = False

    comandos = pygame.key.get_pressed()
    if comandos[pygame.K_UP]:
        y -= velocidade
    if comandos[pygame.K_DOWN]:
        y += velocidade
    if comandos[pygame.K_LEFT]:
        x -= velocidade
    if comandos[pygame.K_RIGHT]:
        x += velocidade

    if (pos_y <= -200):
        pos_y = 600

    pos_y -= velocidade_outros

    janela.blit(fundo,(0,0))
    janela.blit(carro,(x,y))
    janela.blit(carro2,(pos_x,pos_y))
    janela.blit(arvore,(pos_x + 450,pos_y +400))
    janela.blit (arvore2, (pos_x + 400, pos_y + 80))

    pygame.display.update()


pygame.quit()

