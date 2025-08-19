import pygame

class Nave:
    def __init__(self, *args, **kwargs):
        self.rect = kwargs.get('rect', pygame.Rect(0, 0, 50, 50))
        self.cor = kwargs.get('cor', (0, 255, 0))
        self.velocidade = kwargs.get('velocidade', 5)
        self.vidas = kwargs.get('vidas', 3)
        self.invencivel = 0
        self.cooldown_tiro = 0
        self.velocidade_tiro = kwargs.get('velocidade_tiro', 7)  # Adicione esta linha

    def atirar(self):
        
        if self.cooldown_tiro <= 0:
            self.cooldown_tiro = 20  
            return pygame.Rect(self.rect.centerx - 2, self.rect.top, 4, 10)
        return None

    def atualizar(self):
        
        if self.cooldown_tiro > 0:
            self.cooldown_tiro -= 1


    def mover(self, teclas, largura_tela, altura_tela):
        if teclas[pygame.K_LEFT] and self.rect.left > 0:
            self.rect.x -= self.velocidade
        if teclas[pygame.K_RIGHT] and self.rect.right < largura_tela:
            self.rect.x += self.velocidade
        if teclas[pygame.K_UP] and self.rect.top > 0:
            self.rect.y -= self.velocidade
        if teclas[pygame.K_DOWN] and self.rect.bottom < altura_tela:
            self.rect.y += self.velocidade

    def desenhar(self, tela):
        pygame.draw.polygon(tela, self.cor, [
            (self.rect.centerx, self.rect.top),
            (self.rect.left, self.rect.bottom),
            (self.rect.right, self.rect.bottom)
        ])

    def tomar_dano(self):
        if self.invencivel <= 0:
            self.vidas -= 1
            self.invencivel = 60  
            return True
        return False