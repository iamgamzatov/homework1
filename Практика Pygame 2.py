import pygame
import sys
import random


class Player(pygame.sprite.Sprite):
   
    def __init__(self, x, y, all_sprites, bullets):
        super().__init__()
        img = pygame.image.load('1.png')
        self.image = pygame.transform.scale(img, (500, 300))

        self.rect = self.image.get_rect()
        self.rect.center = (x, y)

        self.speed = 5

        self.all_sprites = all_sprites
        self.bullets = bullets

        self.shoot_delay = 250
        self.last_shot = pygame.time.get_ticks()

    def update(self, screen_width, screen_height):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            self.rect.x -= self.speed

        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            self.rect.x += self.speed

        if keys[pygame.K_UP] or keys[pygame.K_w]:
            self.rect.y -= self.speed

        if keys[pygame.K_DOWN] or keys[pygame.K_s]:
            self.rect.y += self.speed

        if keys[pygame.K_SPACE]:
            self.shoot()

        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > screen_width:
            self.rect.right = screen_width

        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.bottom > screen_height:
            self.rect.bottom = screen_height

    def shoot(self):
        now = pygame.time.get_ticks()
        if now - self.last_shot > self.shoot_delay:
            self.last_shot = now
            bullet = Bullet(self.rect.centerx, self.rect.top)
            # ОШИБКА 2: было self.all_sprites.add(self.bullet) — атрибута self.bullet нет.
            # И в all_sprites пуля вообще не добавлялась. Исправлено на bullet.
            self.all_sprites.add(bullet)
            self.bullets.add(bullet)


class Enemy(pygame.sprite.Sprite):  
    def __init__(self, screen_width):
        super().__init__()
        vrag_img = random.choice(['vrag1.png', 'vrag2.png', 'vrag3.png'])

        img = pygame.image.load(vrag_img)
        self.image = pygame.transform.scale(img, (100, 100))

        self.rect = self.image.get_rect()

        self.rect.x = random.randint(0, screen_width - self.rect.width)
        self.rect.y = random.randint(-100, -40)
        self.speed = random.randint(2, 6)

    def update(self, screen_width, screen_height):
        self.rect.y += self.speed

        if self.rect.top > screen_height:
            self.rect.x = random.randint(0, screen_width - self.rect.width)
            self.rect.y = random.randint(-100, -40)
            self.speed = random.randint(2, 6)


class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        img_png = random.choice(['3.png', '4.png'])
        img = pygame.image.load(img_png)
        self.image = pygame.transform.scale(img, (100, 100))

        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.bottom = y
        self.speed = -10

    def update(self, screen_width, screen_height):
        self.rect.y += self.speed
        if self.rect.bottom < 0:
            self.kill()


class Game:
    def __init__(self):
        pygame.init()

        # ОШИБКА 3 (опечатка): было screen_widht. Работало, но это ловушка.
        # Переименовали в screen_width по всему коду.
        self.screen_width = 1920
        self.screen_height = 1080
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        pygame.display.set_caption("PYGAME GAME")

        self.clock = pygame.time.Clock()
        self.fps = 60
        self.is_running = True

        self.all_sprites = pygame.sprite.Group()
        self.enemies = pygame.sprite.Group()
        self.bullets = pygame.sprite.Group()

        # Теперь Player принимает 4 аргумента — совпадает с сигнатурой __init__.
        self.player = Player(
            self.screen_width // 2,
            self.screen_height // 2,
            self.all_sprites,
            self.bullets,
        )
        self.all_sprites.add(self.player)

        for _ in range(8):
            enemy = Enemy(self.screen_width)
            self.all_sprites.add(enemy)
            self.enemies.add(enemy)

    def run(self):
        while self.is_running:
            self._check_events()
            self._update()
            self._draw()

            self.clock.tick(self.fps)
        pygame.quit()
        sys.exit()

    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.is_running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.is_running = False

    def _update(self):
        # ВАЖНО: сигнатура update у всех спрайтов должна быть (self, w, h),
        # иначе pygame.sprite.Group.update() упадёт на несовпадении аргументов.
        self.all_sprites.update(self.screen_width, self.screen_height)

    def _draw(self):
        self.screen.fill((40, 44, 52))
        self.all_sprites.draw(self.screen)

        pygame.display.flip()


if __name__ == "__main__":
    game = Game()
    game.run()