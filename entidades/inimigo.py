import pygame

class Inimigo:
    def __init__(self, *args, **kwargs):
        self.rect = kwargs.get('rect', pygame.Rect(0, 0, 50, 50))
        self.cor = kwargs.get('cor', (255, 0, 0))
        self.velocidade = kwargs.get('velocidade', 3)
        self.dano = kwargs.get('dano', 1)
        self.vida = kwargs.get('vida', 1)
        self.pontos = kwargs.get('pontos', 10)

    def mover(self):
        raise NotImplementedError("Método mover deve ser implementado")

    def desenhar(self, tela):
        raise NotImplementedError("Método desenhar deve ser implementado")

    def atirar(self):
        return None  

    def colidir(self, outro_rect):
        return self.rect.colliderect(outro_rect)