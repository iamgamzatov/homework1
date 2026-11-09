import pygame
import sys

class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()

        self.image = pygame.image.load('1.png').convert_alpha() 
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)

        self.speed = 5

    def update(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            self.rect.x -= self.speed

        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            self.rect.x += self.speed

        if keys[pygame.K_UP] or keys[pygame.K_w]:
            self.rect.y -= self.speed

        if keys[pygame.K_DOWN] or keys[pygame.K_s]:
            self.rect.y += self.speed


class Game:
    def __init__(self):
        pygame.init

        self.screen_widht = 1920
        self.screen_hight = 1080
        self.screen = pygame.display.set_mode ((self.screen_widht, self.screen_hight))
        pygame.display.set_caption("Моя игра")

        self.clock = pygame.time.Clock()
        self.fps = 144

        self.is_running = True

        self.player = Player(self.screen_widht // 2, self.screen_hight // 2)
        self.all_sprites = pygame.sprite.Group()
        self.all_sprites.add(self.player)
    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.is_running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.is_running = False

    def _update(self):
        self.all_sprites.update()

    def _draw(self):
        self.screen.fill((40, 44, 52))
        self.all_sprites.draw(self.screen)

        pygame.display.flip()

    def run(self):
        while self.is_running:
            self._check_events()
            self._update()
            self._draw()
            self.clock.tick(self.fps)
        pygame.quit()
        sys.exit()








if __name__ == '__main__':
    Game().run()