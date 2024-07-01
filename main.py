import pygame
from pygame import draw, mouse
from pygame.locals import *
from random import randint
from atores import Player, Tubo_s, Tubo_i, Palco, Chao, Obj, ChecPoint

WIDTH = 286
HEIGTH = 506
FPS = 60
frames = FPS / 12
BOX_SHOW = True

def main():
	
	pygame.init()
	screen = pygame.display.set_mode((WIDTH, HEIGTH))

#====================================================
#ATORES
#====================================================

	atores = []
	for i in range(0, 0):
		atores.append(Player(50, randint(0, 300), 17, 12, 'bird2.png', 3, (0,0,255), frames))
	atores.append(Player(50, randint(0, 300), 17, 12, 'bird.png', 3, (0,0,255), frames))

	obstacles = []

	fundo = Palco(0, 0, 'paisagem.png', 2, 144, 253, 1)
	chao = Chao(0, 420, 'chao.png', 1, 164, 56, 1)
	chao2 = Chao(WIDTH, 420, 'chao.png', 1, 164, 56, 1)

	obstacles.append(chao)
	obstacles.append(chao2)
	
	teto = Obj(0, 0, WIDTH, 1)
	
	obstacles.append(teto)
	
	check_points = []
#========================================================

	t_i = 0
	clock = pygame.time.Clock()
	gameOn = True
	while gameOn:
		for event in pygame.event.get():
         
			# Check for KEYDOWN event
			if event.type == KEYDOWN:

				if event.key == K_BACKSPACE:
					gameOn = False
				if event.key == K_CAPSLOCK:
					atores[0].jump()
				if event.key == K_SPACE:
					for ator in atores:
						ator.jump()
                 
			# Check for QUIT event
			elif event.type == QUIT:
				gameOn = False

		screen.fill(Color('blue'))
 
		obstacles.reverse()
    
		t_i += 1
		if (t_i % 95) == 0:
			tam_tube =  randint(0, int(HEIGTH / 100) - 2) * 100
			if tam_tube == 0:
				tam_tube = 10
			obstacles.append(Tubo_s(WIDTH, 0, 52, tam_tube, 'tubos.png', 2, (0, 255, 255), 1))
			obstacles.append(Tubo_i(WIDTH, tam_tube + 110, 52, HEIGTH - 100 - tam_tube, 'tubos.png', 2, (0, 255, 255), 1))
	
			check_point = ChecPoint(0, 50, 101, 50)
			check_points.append(check_point)

		obstacles.reverse()

		for obs in obstacles:
			for ator in atores:
				if ator.collide(obs):
					ator.active = False

		screen.blit(fundo.image, (fundo.x, fundo.y))
    
		for ator in atores:
			screen.blit(ator.image, (ator.x, ator.y))

		for obs in obstacles:
			screen.blit(obs.image, (obs.x, obs.y))

		for ator in atores:
			ator.loop()
    
		for obs in obstacles:
			obs.loop()
			
		
		for obs in obstacles:
			if obs.x < -52 and type(obs) != type(Obj(0,0,0,0)) and type(obs) != type(Chao(0, 420, 'chao.png', 1, 164, 56, 1)):
				obstacles.remove(obs)
				
		if BOX_SHOW:
			for obs in obstacles:
				pygame.draw.rect(screen, (0, 255, 0), obs.get_rect())
		
		if BOX_SHOW:
			for cp in check_points:
				pygame.draw.rect(screen, (0, 0, 255), cp.get_rect())
			
		
		for ator in atores:
			if not ator.active and ator.x < -50:
				atores.remove(ator)
            
		pygame.display.flip()
		clock.tick(FPS)

if __name__ == '__main__':
	main()
