from pygame import *

class GameSprite(sprite.Sprite):
    def __init__(self, play_image, play_x, play_y, play_speed):
        super().__init__()
        self.image = transform.scale(image.load(play_image), (65, 65))
        self.speed = play_speed
        self.rect = self.image.get_rect()
        self.rect_x = play_x
        self.rect_y = play_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

win_width = 700
win_height = 500

window = display.set_mode((win_width, win_height))
display.set_caption("Maze")
bg = transform.scale(image.load("bg.jpg"), (win_width, win_height))

player = GameSprite('hero.png', 5, win_height - 80,4)
monster = GameSprite('cyborg.png', win_width - 80,280,2)
player = GameSprite('treaure.png', win_width - 120, win_height - 80,0)

game = True
clock = time.Clock()
FPS = 60

mixer.init()
mixer.music.load("bwomp.ogg")
mixer.music.play()

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False

    window.blit(bg, (0,0))
    player.reset()
    monster.reset()

    display.update()
    clock.tick(FPS)