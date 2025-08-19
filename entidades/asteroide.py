import pygame
from entidades.inimigo import Inimigo
import random

class Asteroide(Inimigo):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.raio = kwargs.get('raio', 20)
        self.rect = pygame.Rect(0, 0, self.raio*2, self.raio*2)
        self.rect.x = random.randrange(0, kwargs.get('largura_tela', 800) - self.raio*2)
        self.rect.y = -random.randrange(1, 100)
        self.velocidade = random.randrange(1, 5)

    def mover(self):
        self.rect.y += self.velocidade

    def desenhar(self, tela):
        pygame.draw.circle(tela, self.cor, self.rect.center, self.raio)