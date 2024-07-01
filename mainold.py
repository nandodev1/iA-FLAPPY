from random import randint

#---------------------------------------------------------
#IAS
#---------------------------------------------------------

class Perc:

    def __init__(self) -> None:
        self.pesos = []
        for i in range(0, 2):
            self.pesos.append(randint(-1000, 1000))

    def out(self, entradas:list)->int:
            soma = 0
            for p in range(0, len(self.pesos)):
                soma += self.pesos[p] * entradas[p]
            if soma > 0:
                 return soma
            return 0
        
class rede:
    def __init__(self) -> None:
        #camada 1
        self.c1p1 = Perc()
        self.c1p2 = Perc()

        #camada 2
        self.c2p1 = Perc()
        self.c2p2 = Perc()

        #camada 3
        self.c3p1 = Perc()

    def out(self, entrada):

        out_c1 = self.c1p1.out(entrada), self.c2p2.out(entrada)
        out_c2 = self.c1p1.out(out_c1), self.c2p2.out(out_c1)

        return self.c3p1.out((out_c1, out_c2))

#-------------------------------------------------------------
# LOOP game
#-------------------------------------------------------------
import pygame
 
# access to key coordinates
from pygame.locals import *

#=================================================================
#Objetos gmaes
#=================================================================

class Square(pygame.sprite.Sprite):
    def __init__(self, x, y, cor):
        super(Square, self).__init__()
        self.cor = cor
        self.surf = pygame.Surface((x, y))

        self.surf.fill(self.cor)
        self.rect = self.surf.get_rect()
 
fundo = Rect(0, 0, 800, 600)
 

class Passagem(Square):
    def __init__(self, x1, x2, start) -> None:
        self.x1= x1
        self.x2 = x2
        self.square1 = Square(50, 600, (0, 250, 0))
        self.square2 = Square(50, 600, (0, 250, 0))
        self.x = start
        self.y = 0
    def loop(self):
        self.x -= 0.1
        screen.blit(self.square1.surf, (self.x, self.y - 600 + self.x1))
        screen.blit(self.square2.surf, (self.x, self.y + self.x2 + self.x1))
    def collide(self, sprite):
        if (sprite.y > (self.y + self.x1) or sprite.y < (self.x1 + self.x2)) and self.x < 100 and self.x > 50:
            return False
        return True

class Player:
    def __init__(player):
        player.x = 100
        player.y = 300
        player.acel_queda = 0
        player.square4 = Square(20, 20, ( 100, 150, 0))
    def loop(player):
        player.acel_queda += 0.0008
        player.y += 0.1 + player.acel_queda
        screen.blit(player.square4.surf, (player.x, player.y))
    def jump(player):
        player.y -= 35;
        player.acel_queda = 0

tubos = []

tubos.append(Passagem(randint(1, 5) * 100, 100, 800))
tubos.append(Passagem(randint(1, 5) * 100, 100, 1000))
tubos.append(Passagem(randint(1, 5) * 100, 100, 1200))
tubos.append(Passagem(randint(1, 5) * 100, 100, 1400))

players = []
players.append(Player())

pygame.init()
 
screen = pygame.display.set_mode((800, 600))
 
# Variable to keep our game loop running
gameOn = True

time = 0

while gameOn:
    time += 1
    for event in pygame.event.get():
         
        # Check for KEYDOWN event
        if event.type == KEYDOWN:

            if event.key == K_BACKSPACE:
                gameOn = False
            if event.key == K_SPACE:
                players[0].jump()
                 
        # Check for QUIT event
        elif event.type == QUIT:
            gameOn = False
            
 
    pygame.draw.rect(screen, ( 5,10 ,10),fundo)

    i = -1
    qt_obs = len(tubos) - 1
    while i < qt_obs:
        i += 1
        if tubos[i].x <= -50:
            tubos.remove(tubos[i])
            i -= 1
            qt_obs -= 1

    if len(tubos) < 4:
        tubos.append(Passagem(randint(1, 5) * 100, 100, 800))
         
    for obs in tubos:
        obs.loop()
 
    for plr in players:
        plr.loop()

    for obs in tubos:
        player = players[0]
        p1_r = player.square4.rect
        p1 = Rect(p1_r[0] + player.x , p1_r[1] +  player.y, p1_r[2] + player.x, p1_r[3] + player.y)
        if obs.collide(player):
            pass
 
    pygame.display.flip()
    
#-------------------------------------------------------------
# MAIN
#-------------------------------------------------------------

def main():
     r = rede()
     r.out([2, 2])

if __name__ == '__main__':
     main()