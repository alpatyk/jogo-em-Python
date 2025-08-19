import sys
import os
import pygame
import random

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from entidades.nave import Nave
from entidades.asteroide import Asteroide
from entidades.nave_inimiga import NaveInimiga
from utils.funcoes import * 

def inicializar_jogo():
    pygame.init()
    LARGURA, ALTURA = 800, 600
    tela = pygame.display.set_mode((LARGURA, ALTURA))
    pygame.display.set_caption("Jogo de Nave Espacial")
    clock = pygame.time.Clock()
    FPS = 60
    fonte = pygame.font.SysFont(None, 36)
    
    nave = Nave(
        rect=pygame.Rect(LARGURA//2 - 25, ALTURA - 50, 50, 50),
        vidas=3
    )
    
    return {
        'tela': tela,
        'clock': clock,
        'fps': FPS,
        'fonte': fonte,
        'nave': nave,
        'inimigos': [],
        'tiros_inimigos': [],
        'tiros_jogador': [],
        'pontos': 0,
        'game_over': False,
        'spawn_timer': 0,
        'dificuldade': 1,
        'LARGURA': LARGURA,
        'ALTURA': ALTURA,
        'cooldown_tiro': 0
    }

def atualizar_jogo(estado):
    if estado['game_over']:
        return estado
    
    estado['nave'].atualizar()
    
    teclas = pygame.key.get_pressed()
    estado['nave'].mover(teclas, estado['LARGURA'], estado['ALTURA'])
    
    if teclas[pygame.K_SPACE]:
        tiro = estado['nave'].atirar()
        if tiro:  
            estado['tiros_jogador'].append(tiro)
    
    if estado['cooldown_tiro'] > 0:
        estado['cooldown_tiro'] -= 1
    
    estado['spawn_timer'] += 1
    if estado['spawn_timer'] >= 60 // estado['dificuldade']:
        estado['spawn_timer'] = 0
        if random.random() < 0.7:
            estado['inimigos'].append(
                criar_inimigo('asteroide', estado['LARGURA'], estado['ALTURA'])
            )
        else:
            estado['inimigos'].append(
                criar_inimigo('nave_inimiga', estado['LARGURA'], estado['ALTURA'])
            )
    
    for tiro in estado['tiros_jogador'][:]:
        tiro.y -= estado['nave'].velocidade_tiro
        if tiro.bottom < 0:
            estado['tiros_jogador'].remove(tiro)
            continue
        
        for inimigo in estado['inimigos'][:]:
            if tiro.colliderect(inimigo.rect):
                estado['pontos'] += inimigo.pontos
                estado['tiros_jogador'].remove(tiro)
                estado['inimigos'].remove(inimigo)
                break
    
    for inimigo in estado['inimigos'][:]:
        inimigo.mover()
        
        tiro = inimigo.atirar()
        if tiro:
            estado['tiros_inimigos'].append(tiro)
        
        if estado['nave'].rect.colliderect(inimigo.rect):
            estado['nave'].vidas -= 1
            estado['inimigos'].remove(inimigo)
            
            if estado['nave'].vidas <= 0:
                estado['game_over'] = True
    
    for tiro in estado['tiros_inimigos'][:]:
        tiro.y += 5 
        if tiro.top > estado['ALTURA']:
            estado['tiros_inimigos'].remove(tiro)
        elif tiro.colliderect(estado['nave'].rect):
            estado['nave'].vidas -= 1
            estado['tiros_inimigos'].remove(tiro)
            if estado['nave'].vidas <= 0:
                estado['game_over'] = True
    
    return estado

def main():
    estado = inicializar_jogo()
    
    rodando = True
    while rodando:
        resultado = processar_eventos(estado['nave'], estado['game_over'])
        if resultado == 'reiniciar':
            estado = inicializar_jogo()
        elif not resultado:
            rodando = False
        
        estado = atualizar_jogo(estado)
        
        desenhar_tela(
            estado['tela'], estado['nave'], estado['inimigos'],
            estado['tiros_inimigos'], estado['tiros_jogador'],
            estado['game_over'], estado['pontos'], estado['fonte']
        )
        
        estado['clock'].tick(estado['fps'])
    
    pygame.quit()

if __name__ == "__main__":
    main()