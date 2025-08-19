import pygame

from entidades.asteroide import Asteroide
from entidades.nave_inimiga import NaveInimiga

def processar_eventos(nave, game_over):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return False
        if game_over and event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                return 'reiniciar'
    return True

def desenhar_tela(tela, nave, inimigos, tiros_inimigos, tiros_jogador, game_over, pontos, fonte):
    tela.fill((0, 0, 0))
    
    nave.desenhar(tela)
    for inimigo in inimigos:
        inimigo.desenhar(tela)
    for tiro in tiros_inimigos + tiros_jogador:
        pygame.draw.rect(tela, (255, 255, 255), tiro)
    
    texto_pontos = fonte.render(f"Pontos: {pontos}", True, (255, 255, 255))
    texto_vidas = fonte.render(f"Vidas: {nave.vidas}", True, (255, 255, 255))
    tela.blit(texto_pontos, (10, 10))
    tela.blit(texto_vidas, (10, 40))
    
    if game_over:
        texto = pygame.font.SysFont(None, 72).render("GAME OVER", True, (255, 0, 0))
        tela.blit(texto, (tela.get_width()//2 - texto.get_width()//2, tela.get_height()//2 - 50))
        instrucao = fonte.render("Pressione R para reiniciar", True, (255, 255, 255))
        tela.blit(instrucao, (tela.get_width()//2 - instrucao.get_width()//2, tela.get_height()//2 + 20))
    
    pygame.display.flip()

def criar_inimigo(tipo, largura_tela, altura_tela, **kwargs):
    if tipo == 'asteroide':
        return Asteroide(largura_tela=largura_tela, altura_tela=altura_tela, **kwargs)
    elif tipo == 'nave_inimiga':
        return NaveInimiga(largura_tela=largura_tela, altura_tela=altura_tela, **kwargs)
    return None