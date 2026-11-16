import pygame
import sys
import random
import datetime


class Player(pygame.sprite.Sprite):
    # ОШИБКА 1: раньше было def __init__(self, x, y): — не хватало all_sprites и bullets,
    # а в Game.__init__ передавалось 4 аргумента. Добавили параметры.
    def __init__(self, x, y, all_sprites, bullets):
        super().__init__()

        self.image = pygame.Surface((50, 50))
        self.image.fill((97, 175, 239))

        self.rect = self.image.get_rect()
        self.rect.center = (x, y)

        self.speed = 5

        # ОШИБКА (потенциальная): раньше параметр назывался bullet (ед.ч.),
        # а ниже использовалось self.bullets (мн.ч.) — переименовали для единообразия.
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


class Enemy(pygame.sprite.Sprite):  # ОШИБКА (косметика): было Emeny — опечатка.
    def __init__(self, screen_width):
        super().__init__()
        self.image = pygame.Surface((40, 40))
        self.image.fill((224, 100, 117))
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
        self.image = pygame.Surface((6, 15))
        self.image.fill((229, 192, 123))
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.bottom = y
        self.speed = -10

    def update(self, screen_width, screen_height):
        self.rect.y += self.speed
        if self.rect.bottom < 0:
            self.kill()


class Game:
    def __init__(self, game_duration):
        pygame.init()

        # ОШИБКА 3 (опечатка): было screen_widht. Работало, но это ловушка.
        # Переименовали в screen_width по всему коду.
        self.screen_width = 800
        self.screen_height = 600
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        pygame.display.set_caption("PYGAME GAME")

        self.clock = pygame.time.Clock()
        self.fps = 60
        self.is_running = True

        self.game_over = False
        self.score = 0
        self.game_duration = game_duration
        self.start_ticks = pygame.time.get_ticks()
        self.time_left = game_duration
        self.font = pygame.font.SysFont('arial', 40, bold=True)
        self.big_font = pygame.font.SysFont('arial', 40, bold=True)


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
            if not self.game_over:
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
        seconds_passed = (pygame.time.get_ticks() - self.start_ticks) / 1000
        self.time_left = max(0.0, self.game_duration - seconds_passed)

        if self.time_left <= 0:
            self.game_over = True
            self._save_results()
            return

        # ВАЖНО: сигнатура update у всех спрайтов должна быть (self, w, h),
        # иначе pygame.sprite.Group.update() упадёт на несовпадении аргументов.
        self.all_sprites.update(self.screen_width, self.screen_height)

        hits = pygame.sprite.groupcollide(self.enemies, self.bullets, True, True)

        for _ in hits:
            self.score += 10
            enemy = Enemy(self.screen_width)
            self.all_sprites.add(enemy)
            self.enemies.add(enemy)

    def _save_results(self):
        now = datetime.datetime.now()
        line = f'{now}Время: {self.game_duration}сек | Очки: {self.score}\n'
        with open ('result.txt', 'a', encoding='utf-8')as file:
            file.write(line)


    def _draw(self):
        self.screen.fill((40, 44, 52))
        self.all_sprites.draw(self.screen)

        score_text = self.font.render(
            f'Счет: {self.score}', True, (152, 195, 121)
        )
        time_text = self.font.render(
            f'Время: {self.time_left:.1f}c', True, (229, 192, 123)
        )

        self.screen.blit(score_text, (15, 15))
        self.screen.blit(time_text, (-15,-15))

        if self.game_over:
            over_text = self.big_font.render(
                "Время вышло!", True, (224, 100,177)
            )
            final_score = self.font.render(
                f'Итоговый счет: {self.score}', True, (255,255,255)
            )
            self.screen.blit(
                over_text,
                over_text.get_rect(
                    center = (self.screen_width // 2, self.screen_height // 2 - 30)
                ),

            )

            self.screen.blit(
                final_score,
                final_score.get_rect(
                    center = (self.screen_width // 2, self.screen_height // 2 +20)
                ),
            )


        pygame.display.flip()


if __name__ == "__main__":
    user_input = input('Сколько секунд будете играть? ')
    duration = int(user_input) if user_input.isdigit() else 30
    game = Game(duration)
    game.run()