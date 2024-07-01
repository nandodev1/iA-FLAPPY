from pygame.locals import *
from pygame import Surface 
from pygame.transform import scale2x, rotate, scale
from spriteStripAnim import SpriteStripAnim

SPEED_GAME = 2

class Obj:
	def __init__(self, x, y, lar, alt, color=(0, 0, 0), name='') -> None:
		self.name = name
		self.x = x
		self.y = y
		self.lar = lar
		self.alt = alt
		self.color = color
		self.sprits = []
		self.image = Surface(self.get_rect().size).convert()
	def get_rect(self):
		return Rect(self.x, self.y, self.lar, self.alt)
	def collide(self, obj2):
		return self.get_rect().colliderect(obj2.get_rect())
	def loop(self):
		pass
		
class ChecPoint(Obj):
	def __init__(self, x, y, alt, lar):
		super().__init__(x, y, alt, lar)
	def loop(self):
		self.x -= SPEED_GAME

class Player(Obj):
    def __init__(self, x, y, lar, alt, file_img, qt_frames, color, frames):
        super().__init__(x, y, lar * 2, alt * 2, color)
        self.acel = 0
        for i in range(0, qt_frames):
            self.sprits.append(SpriteStripAnim(file_img, (0,0, lar, alt), qt_frames, 0, True, frames))
        self.image = self.sprits[0].next()
        self.anti_gravity = 0
        self.angle = 0
        self.active = True
        self.score = 0

    def loop(self):
        self.image = self.sprits[0].next()
        self.image = scale2x(self.image)
        self.image = rotate(self.image, self.angle)
        self.acel += 0.2
        self.y += 0.005 + self.acel - self.anti_gravity

        if self.anti_gravity > 0:
            self.anti_gravity -= 0.02

        if self.angle > -90:
            self.angle -= 2

        if not self.active:
            self.x -= SPEED_GAME;
            if self.angle > -90:
                self.angle -= 2

    def jump(self):
        if self.active:
            self.anti_gravity = 5
            self.angle = 30
            self.acel = 0

class Tubo(Obj):
    def __init__(self, x, y, lar, alt, file_img, qt_frames, color, frames):
        super().__init__(x, y, lar, alt, color)
    def loop(self):
        self.x -= SPEED_GAME

class Tubo_i(Tubo):
    def __init__(self, x, y, lar, alt, file_img, qt_frames, color, frames):
        super().__init__(x, y, lar, alt,  file_img, qt_frames, color, frames)
        for i in range(0, qt_frames):
            self.sprits.append(SpriteStripAnim(file_img, (0, 0, lar/2, alt/2), qt_frames, 0, True, frames))
        self.image = self.sprits[0].next()
        self.image = scale2x(self.image)

class Tubo_s(Tubo):
    def __init__(self, x, y, lar, alt, file_img, qt_frames, color, frames):
        super().__init__(x, y, lar, alt, file_img, qt_frames, color, frames)
        for i in range(0, qt_frames):
            self.sprits.append(SpriteStripAnim(file_img, (0, 160 - (( self.alt/100) * 50), lar/2, alt/2), qt_frames, 0, True, frames))
        self.sprits[0].next()
        self.image = self.sprits[0].next()
        self.image = scale2x(self.image)

class Palco(Obj):
    def __init__(self, x, y, file_img, qt_frames, lar, alt, frames):
        super().__init__(x, y, lar, alt)
        for i in range(0, qt_frames):
            self.sprits.append(SpriteStripAnim(file_img, (0,0, lar, alt), qt_frames, 0, True, frames))
        self.image = self.sprits[0].next()
        self.image = scale2x(self.image)
    def get_rect(self):
        return Rect(self.x, self.y, self.lar, self.alt)
        
class Chao(Palco):
	def __init__(self, x, y, file_img, qt_frames, lar, alt, frames):
		super().__init__(x, y, file_img, qt_frames, lar * 2, alt * 2, frames)
	def loop(self):
		self.x -= SPEED_GAME
		if self.x <= -286:
			self.x = 286
