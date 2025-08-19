import pygame
from entidades.inimigo import Inimigo
import random

class NaveInimiga(Inimigo):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.frequencia_tiro = kwargs.get('frequencia_tiro', 120)  
        self.contador_tiro = 0
        self.dano = kwargs.get('dano', 10) 
    def mover(self):
        self.rect.y += self.velocidade
        
        self.rect.x += random.choice([-1, 0, 1]) * 2

    def desenhar(self, tela):
        pygame.draw.polygon(tela, self.cor, [
            (self.rect.centerx, self.rect.bottom),
            (self.rect.left, self.rect.top),
            (self.rect.right, self.rect.top)
        ])

    def atirar(self):
        self.contador_tiro += 1
        if self.contador_tiro >= self.frequencia_tiro:
            self.contador_tiro = 0
            return pygame.Rect(self.rect.centerx-2, self.rect.bottom, 4, 10)
        return None