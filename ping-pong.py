from pygame import*


window = display.set_mode((600, 500))
display.set_caption('Ping-Pong')

background = transform.scale(image.load('images.png'), (600, 500))

speed_x = 3
speed_y = 3
FPS = 60
clock = time.Clock()


#класс для спрайтов


class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_size_x, player_size_y, player_speed,):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (player_size_x, player_size_y))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update_l(self):
        key_pressed = key.get_pressed()
    
        if key_pressed[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if key_pressed[K_DOWN] and self.rect.y < 480:
            self.rect.y += self.speed

    def update_r(self):
        key_pressed = key.get_pressed()
    
        if key_pressed[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if key_pressed[K_s] and self.rect.y < 480:
            self.rect.y += self.speed

ball = GameSprite('ball.jpeg', 200, 200, 50, 50, 3)
rocket_l = Player('rocket.jpeg', 10, 200, 50, 150, 3)
rocket_r = Player('rocket.jpeg', 560, 200, 50, 150, 3)

#текст
font.init()
lose = font.SysFont('Arial', 36)
win_right = lose.render('Игрок справа побеждает!', True, (0, 255, 0))
win_left = lose.render('Игрок слева побеждает!', True, (0, 255, 0))
lose_right = lose.render('Игрок справа проигрывает!', True, (255, 0, 0))
lose_left = lose.render('Игрок слева проигрывает!', True, (255, 0, 0))

#игровой цикл >
game = True
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    
    
    window.blit(background, (0, 0))
    
    rocket_r.update_r()
    rocket_l.update_l()


    ball.rect.x += speed_x
    ball.rect.y += speed_y

    if sprite.collide_rect(ball, rocket_l) or sprite.collide_rect(ball, rocket_r):
        speed_x *= -1

    if ball.rect.y > 450 or ball.rect.y < 0:
        speed_y *= -1
        
    if ball.rect.x < 0:
        window.blit(win_right, (140, 120))
        window.blit(lose_left, (125, 320))
    if ball.rect.x > 600:
        window.blit(win_left, (140, 120))
        window.blit(lose_right, (125, 320))

    
    rocket_l.reset()
    rocket_r.reset()

    ball.reset()

    display.update()


    clock.tick(FPS)
    



