import pygame
import random

# ==================================================
# CONFIGURAÇÃO INICIAL
# ==================================================

pygame.init()
pygame.mixer.init()
pygame.display.set_caption("Snake Game")

largura = 640
altura = 576

tela = pygame.display.set_mode((largura, altura))
relogio = pygame.time.Clock()


# ==================================================
# CORES (RGB)
# ==================================================

preto    = (0, 0, 0)
branco   = (255, 255, 255)
vermelho = (255, 0, 0)
verde    = (0, 255, 0)
ouro     = (255, 215, 0)
prata    = (192, 192, 192)
bronze   = (205, 127, 50)


# ==================================================
# CONFIGURAÇÕES DO JOGO
# ==================================================

tamanho_quadrado = 32
vel_jogo = 5
nome_jogador_atual = ""

# ==================================================
# IMAGENS
# ==================================================

imagens = {
    "imagem_comida_vermelha": pygame.image.load("spr_red_apple.png"),
    "imagem_comida_roxa":     pygame.image.load("spr_purple_apple.png"),
    "imagem_head":            pygame.image.load("head.png"),
    "imagem_body":            pygame.image.load("body.png"),
    "imagem_menu":            pygame.image.load("main_menu.png"),
    "imagem_nome":            pygame.image.load("enter_name.png"),
    "imagem_leaderboard":     pygame.image.load("leaderboard.png"),
    "imagem_vitoria":         pygame.image.load("you_win.png"),
    "imagem_tela_morte":      pygame.image.load("tela_morte.png"),
    "imagem_fundo":           pygame.image.load("map.png")
}


# ==================================================
# SONS
# ==================================================

sons = {
    "bg_music":  pygame.mixer.Sound("bg_music.mp3"),
    "snd_comer": pygame.mixer.Sound("eat_apple_sound.mp3"),
    "level_up":  pygame.mixer.Sound("level_up.mp3"),
    "game_over": pygame.mixer.Sound("game_over.mp3"),
    "you_win":   pygame.mixer.Sound("you_win.mp3")
}

sons["bg_music"].set_volume(0.01)
sons["snd_comer"].set_volume(1)


# ==================================================
# FUNÇÕES DE DESENHO
# ==================================================

def desenhar_comida(x_comida, y_comida, tipo_comida):

    if tipo_comida == 0:
        imagem_comida = imagens["imagem_comida_vermelha"]
        tela.blit(imagem_comida, (x_comida, y_comida))
    else:
        imagem_comida = imagens["imagem_comida_roxa"]
        tela.blit(imagem_comida, (x_comida, y_comida))


def desenhar_cobra(tamanho, corpo_cobra, velocidade_x, velocidade_y):

    imagem_head = imagens["imagem_head"]
    imagem_body = imagens["imagem_body"]

    angulo = 0

    if velocidade_x > 0:
        angulo = 0
    elif velocidade_x < 0:
        angulo = 180
    elif velocidade_y < 0:
        angulo = 90
    elif velocidade_y > 0:
        angulo = 270

    imagem_head = pygame.transform.rotate(imagem_head, angulo)

    for i, parte in enumerate(corpo_cobra):

        x = parte[0]
        y = parte[1]

        if i == len(corpo_cobra) - 1:
            tela.blit(imagem_head, (x, y))
        else:
            tela.blit(imagem_body, (x, y))


def desenhar_pontos(pontuacao):
    fonte = pygame.font.Font("PressStart2P.ttf", 20)
    texto = fonte.render(f"{pontuacao}", True, branco)
    tela.blit(texto, [tamanho_quadrado * 4, tamanho_quadrado * 1.75])


def desenhar_fundo(fundo):
    tela.blit(imagens["imagem_fundo"], (0, 0))


def desenhar_recorde(recorde):
    fonte = pygame.font.Font("PressStart2P.ttf", 20)
    texto = fonte.render(f"{recorde}", True, branco)
    tela.blit(texto, [tamanho_quadrado * 13, tamanho_quadrado * 1.75])


# ==================================================
# TELA INICIAL
# ==================================================

def tela_menu():

    # --------------------------
    # POSIÇÕES DOS TEXTOS
    # --------------------------

    x_play = 210
    y_play = 400

    x_leaderboard = 210
    y_leaderboard = 448

    x_quit = 210
    y_quit = 495

    # --------------------------
    # TAMANHOS DAS ÁREAS CLICÁVEIS (largura, altura)
    # --------------------------

    w_play        = 248
    h_play        = 40

    w_leaderboard = 248
    h_leaderboard = 40

    w_quit        = 248
    h_quit        = 40

    # --------------------------
    # RETÂNGULOS CLICÁVEIS
    # --------------------------

    rect_play        = pygame.Rect(x_play - 13,        y_play - 13,        w_play,        h_play)
    rect_leaderboard = pygame.Rect(x_leaderboard - 13, y_leaderboard - 13, w_leaderboard, h_leaderboard)
    rect_quit        = pygame.Rect(x_quit - 13,        y_quit - 13,        w_quit,        h_quit)

    fonte = pygame.font.Font("PressStart2P.ttf", 15)

    texto_play        = fonte.render("1 - Play",        True, preto)
    texto_leaderboard = fonte.render("2 - Leaderboard", True, preto)
    texto_quit        = fonte.render("3 - Quit",        True, preto)

    while True:

        tela.fill(preto)
        tela.blit(imagens["imagem_menu"], (0, 0))
        tela.blit(texto_play,        (x_play,        y_play))
        tela.blit(texto_leaderboard, (x_leaderboard, y_leaderboard))
        tela.blit(texto_quit,        (x_quit,        y_quit))

        # Mudando ícone do mouse
        mouse_pos = pygame.mouse.get_pos()

        if rect_play.collidepoint(mouse_pos) or \
        rect_leaderboard.collidepoint(mouse_pos) or \
        rect_quit.collidepoint(mouse_pos):
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
        else:
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)

        pygame.display.update()

        for evento in pygame.event.get():

            if evento.type == pygame.QUIT:
                pygame.quit()
                quit()

            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_1:
                    return "nome"
                if evento.key == pygame.K_2:
                    return "leaderboard"
                if evento.key == pygame.K_3:
                    return "quit"

            if evento.type == pygame.MOUSEBUTTONDOWN:
                if rect_play.collidepoint(evento.pos):
                    return "nome"
                if rect_leaderboard.collidepoint(evento.pos):
                    return "leaderboard"
                if rect_quit.collidepoint(evento.pos):
                    return "quit"


# ==================================================
# TELA NOME
# ==================================================

def tela_nome():

    nome_digitado = ""

    # --------------------------
    # POSIÇÕES DOS TEXTOS
    # --------------------------

    x_nome     = 170
    y_nome     = 325

    x_menu     = 50
    y_menu     = 518

    x_continue = 190
    y_continue = 432

    # --------------------------
    # TAMANHOS DAS ÁREAS CLICÁVEIS (largura, altura)
    # --------------------------

    w_menu     = 202
    h_menu     = 43

    w_continue = 300
    h_continue = 55

    # --------------------------
    # RETÂNGULOS CLICÁVEIS
    # --------------------------

    rect_menu     = pygame.Rect(x_menu - 16,     y_menu - 14,     w_menu,     h_menu)
    rect_continue = pygame.Rect(x_continue - 20, y_continue - 20, w_continue, h_continue)

    fonte = pygame.font.Font("PressStart2P.ttf", 15)

    texto_menu     = fonte.render("1 - Back",     True, branco)
    texto_continue = fonte.render("2 - Continue", True, branco)

    while True:

        tela.fill(preto)
        tela.blit(imagens["imagem_nome"], (0, 0))

        texto_nome = fonte.render(nome_digitado, True, branco)
        tela.blit(texto_nome,     (x_nome,     y_nome))
        tela.blit(texto_menu,     (x_menu,     y_menu))
        tela.blit(texto_continue, (x_continue, y_continue))

        # Mudando ícone do mouse
        mouse_pos = pygame.mouse.get_pos()

        if rect_menu.collidepoint(mouse_pos) or \
        rect_continue.collidepoint(mouse_pos):
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
        else:
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)

        pygame.display.update()

        for evento in pygame.event.get():

            if evento.type == pygame.QUIT:
                pygame.quit()
                quit()

            if evento.type == pygame.KEYDOWN:

                if evento.key == pygame.K_1:
                    return None

                if evento.key == pygame.K_2:
                    if nome_digitado != "":
                        return nome_digitado

                if evento.key == pygame.K_BACKSPACE:
                    nome_digitado = nome_digitado[:-1]

                elif len(nome_digitado) < 10:
                    caractere = evento.unicode.upper()
                    if caractere.isalnum():
                        nome_digitado += caractere

            if evento.type == pygame.MOUSEBUTTONDOWN:

                if rect_menu.collidepoint(evento.pos):
                    return None

                if rect_continue.collidepoint(evento.pos):
                    if nome_digitado != "":
                        return nome_digitado


# ==================================================
# TELA LEADERBOARD
# ==================================================

def tela_leaderboard():

    leaderboard = carregar_leaderboard()

    # --------------------------
    # POSIÇÕES DOS TEXTOS
    # --------------------------

    x_nome      = 160
    x_pontos    = 470
    y_inicial   = 215
    espacamento = 26.5
    x_menu      = 53
    y_menu      = 518

    # --------------------------
    # TAMANHO DA ÁREA CLICÁVEL DO BOTÃO BACK (largura, altura)
    # Ajuste esses valores se o clique não estiver pegando direito
    # --------------------------

    w_menu = 190
    h_menu = 40

    # --------------------------
    # RETÂNGULO CLICÁVEL
    # --------------------------

    rect_menu = pygame.Rect(x_menu - 16, y_menu - 13, w_menu, h_menu)

    fonte = pygame.font.Font("PressStart2P.ttf", 15)

    while True:

        tela.fill(preto)
        tela.blit(imagens["imagem_leaderboard"], (0, 0))

        for i, jogador in enumerate(leaderboard):

            y = y_inicial + (i * espacamento)

            cor = branco
            if i == 0:
                cor = ouro
            elif i == 1:
                cor = prata
            elif i == 2:
                cor = bronze

            texto_nome   = fonte.render(jogador["nome"],        True, cor)
            texto_pontos = fonte.render(str(jogador["pontos"]), True, cor)

            tela.blit(texto_nome,   (x_nome,   y))
            tela.blit(texto_pontos, (x_pontos, y))

        texto_menu = fonte.render("1 - Back", True, branco)
        tela.blit(texto_menu, (x_menu, y_menu))

        # Mudar ícone do mouse
        mouse_pos = pygame.mouse.get_pos()

        if rect_menu.collidepoint(mouse_pos):
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
        else:
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)

        pygame.display.update()

        for evento in pygame.event.get():

            if evento.type == pygame.QUIT:
                pygame.quit()
                quit()

            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_1:
                    return

            if evento.type == pygame.MOUSEBUTTONDOWN:
                if rect_menu.collidepoint(evento.pos):
                    return


# ==================================================
# TELA DE VITÓRIA
# ==================================================

def tela_vitoria():

    # --------------------------
    # POSIÇÕES DOS TEXTOS
    # --------------------------

    x_tela_vitoria = tamanho_quadrado * 4.57
    y_tela_vitoria = tamanho_quadrado * 5

    x_play_again = 210
    y_play_again = 315

    x_main_menu = 210
    y_main_menu = 365

    # --------------------------
    # TAMANHOS DAS ÁREAS CLICÁVEIS (largura, altura)
    # --------------------------

    w_play_again = 248
    h_play_again = 39

    w_main_menu  = 248
    h_main_menu  = 39

    # --------------------------
    # RETÂNGULOS CLICÁVEIS
    # --------------------------

    rect_play_again = pygame.Rect(x_play_again - 13, y_play_again - 10, w_play_again, h_play_again)
    rect_main_menu  = pygame.Rect(x_main_menu - 13,  y_main_menu - 10,  w_main_menu,  h_main_menu)

    fonte = pygame.font.Font("PressStart2P.ttf", 15)

    texto_play_again = fonte.render("1 - Play Again", True, preto)
    texto_main_menu  = fonte.render("2 - Main Menu",  True, branco)

    while True:

        tela.blit(imagens["imagem_vitoria"], (x_tela_vitoria, y_tela_vitoria))
        tela.blit(texto_play_again, (x_play_again, y_play_again))
        tela.blit(texto_main_menu,  (x_main_menu,  y_main_menu))

        mouse_pos = pygame.mouse.get_pos()

        if rect_play_again.collidepoint(mouse_pos) or \
           rect_main_menu.collidepoint(mouse_pos):
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
        else:
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)

        pygame.display.update()

        for evento in pygame.event.get():

            if evento.type == pygame.QUIT:
                pygame.quit()
                quit()

            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_1:
                    return "play"
                if evento.key == pygame.K_2:
                    return "menu"

            if evento.type == pygame.MOUSEBUTTONDOWN:
                if rect_play_again.collidepoint(evento.pos):
                    return "play"
                if rect_main_menu.collidepoint(evento.pos):
                    return "menu"

# ==================================================
# TELA DE MORTE
# ==================================================

def tela_morte():

    # --------------------------
    # POSIÇÕES DOS TEXTOS
    # --------------------------

    x_tela_morte = tamanho_quadrado * 4.57
    y_tela_morte = tamanho_quadrado * 5

    x_play_again = 210
    y_play_again = 315

    x_main_menu = 210
    y_main_menu = 365

    # --------------------------
    # TAMANHOS DAS ÁREAS CLICÁVEIS (largura, altura)
    # --------------------------

    w_play_again = 248
    h_play_again = 40

    w_main_menu  = 248
    h_main_menu  = 40

    # --------------------------
    # RETÂNGULOS CLICÁVEIS
    # --------------------------

    rect_play_again = pygame.Rect(x_play_again - 13, y_play_again - 13, w_play_again, h_play_again)
    rect_main_menu  = pygame.Rect(x_main_menu - 13,  y_main_menu - 13,  w_main_menu,  h_main_menu)

    fonte = pygame.font.Font("PressStart2P.ttf", 15)

    texto_play_again = fonte.render("1 - Play Again", True, preto)
    texto_main_menu  = fonte.render("2 - Main Menu",  True, branco)

    while True:

        tela.blit(imagens["imagem_tela_morte"], (x_tela_morte, y_tela_morte))
        tela.blit(texto_play_again, (x_play_again, y_play_again))
        tela.blit(texto_main_menu,  (x_main_menu,  y_main_menu))

        mouse_pos = pygame.mouse.get_pos()

        if rect_play_again.collidepoint(mouse_pos) or \
           rect_main_menu.collidepoint(mouse_pos):
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
        else:
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)

        pygame.display.update()

        for evento in pygame.event.get():

            if evento.type == pygame.QUIT:
                pygame.quit()
                quit()

            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_1:
                    return "play"
                if evento.key == pygame.K_2:
                    return "menu"

            if evento.type == pygame.MOUSEBUTTONDOWN:
                if rect_play_again.collidepoint(evento.pos):
                    return "play"
                if rect_main_menu.collidepoint(evento.pos):
                    return "menu"

# ==================================================
# MECÂNICAS AUXILIARES
# ==================================================

def gerar_comida(corpo_cobra):

    while True:

        x_comida = (
            round(
                random.randrange(
                    tamanho_quadrado,
                    largura - (tamanho_quadrado * 2)
                ) / float(tamanho_quadrado)
            ) * float(tamanho_quadrado)
        )

        y_comida = (
            round(
                random.randrange(
                    (tamanho_quadrado * 4),
                    altura - (tamanho_quadrado * 2)
                ) / float(tamanho_quadrado)
            ) * float(tamanho_quadrado)
        )

        if [x_comida, y_comida] not in corpo_cobra:

            if random.randint(1, 10) == 1:
                tipo_comida = 1      # roxa (10%)
            else:
                tipo_comida = 0      # vermelha (90%)

            return x_comida, y_comida, tipo_comida


def selecionar_velocidade(tecla, velocidade_x, velocidade_y):

    if (tecla == pygame.K_DOWN or tecla == pygame.K_s) and (velocidade_y == 0):
        velocidade_x = 0
        velocidade_y = tamanho_quadrado

    elif (tecla == pygame.K_UP or tecla == pygame.K_w) and (velocidade_y == 0):
        velocidade_x = 0
        velocidade_y = -tamanho_quadrado

    elif (tecla == pygame.K_LEFT or tecla == pygame.K_a) and (velocidade_x == 0):
        velocidade_x = -tamanho_quadrado
        velocidade_y = 0

    elif (tecla == pygame.K_RIGHT or tecla == pygame.K_d) and (velocidade_x == 0):
        velocidade_x = tamanho_quadrado
        velocidade_y = 0

    return velocidade_x, velocidade_y


def carregar_recorde():

    leaderboard = carregar_leaderboard()

    if len(leaderboard) > 0:
        return leaderboard[0]["pontos"]

    return 0


def carregar_leaderboard():

    leaderboard = []

    try:

        with open("leaderboard.txt", "r") as arquivo:

            for linha in arquivo:

                linha = linha.strip()

                if linha != "":

                    nome, pontos = linha.split(";")

                    leaderboard.append(
                        {
                            "nome": nome,
                            "pontos": int(pontos)
                        }
                    )

    except:
        pass

    return leaderboard


def salvar_leaderboard(leaderboard):

    with open("leaderboard.txt", "w") as arquivo:

        for jogador in leaderboard:

            arquivo.write(
                f"{jogador['nome']};{jogador['pontos']}\n"
            )


def atualizar_leaderboard(nome, pontos):

    leaderboard = carregar_leaderboard()

    jogador_encontrado = False

    for jogador in leaderboard:

        if jogador["nome"] == nome:

            jogador_encontrado = True

            if pontos > jogador["pontos"]:
                jogador["pontos"] = pontos

            break

    if not jogador_encontrado:

        leaderboard.append(
            {
                "nome": nome,
                "pontos": pontos
            }
        )

    leaderboard.sort(
        key=lambda jogador: jogador["pontos"],
        reverse=True
    )

    leaderboard = leaderboard[:10]

    salvar_leaderboard(leaderboard)


def tocar_som(nome):
    sons[nome].play()


def tocar_musica(nome, loop):

    pygame.mixer.music.load(nome)

    if loop:
        pygame.mixer.music.play(-1)
    else:
        pygame.mixer.music.play()


def parar_musica():
    pygame.mixer.music.stop()


# ==================================================
# LOOP PRINCIPAL
# ==================================================

def rodar_jogo():

    global nome_jogador_atual

    rodando = True

    velocidade_atual = vel_jogo
    nivel_atual = 1

    recorde = carregar_recorde()

    x = largura // 2
    y = altura // 2

    velocidade_x = 0
    velocidade_y = 0

    proxima_velocidade_x = 0
    proxima_velocidade_y = 0

    tamanho_cobra = 1
    corpo_cobra = []
    pontuacao = 0
    max_casas = 234

    x_comida, y_comida, tipo_comida = gerar_comida(corpo_cobra)

    while rodando:

        # --------------------------
        # Entrada do jogador
        # --------------------------

        mudou_direcao = False

        for evento in pygame.event.get():

            if evento.type == pygame.QUIT:
                pygame.quit()
                quit()

            elif evento.type == pygame.KEYDOWN and not mudou_direcao:
                proxima_velocidade_x, proxima_velocidade_y = (
                    selecionar_velocidade(
                        evento.key,
                        proxima_velocidade_x,
                        proxima_velocidade_y
                    )
                )
                mudou_direcao = True

        # --------------------------
        # Atualização de posição
        # --------------------------

        velocidade_x = proxima_velocidade_x
        velocidade_y = proxima_velocidade_y

        x += velocidade_x
        y += velocidade_y

        if (x < tamanho_quadrado or x >= largura - tamanho_quadrado or
                y < (tamanho_quadrado * 4) or y >= altura - tamanho_quadrado):

            atualizar_leaderboard(nome_jogador_atual, pontuacao)
            tocar_som("game_over")

            resultado = tela_morte()

            if resultado == "play":
                return "play"
            if resultado == "menu":
                return "menu"

        # --------------------------
        # Controle do corpo da cobra
        # --------------------------

        corpo_cobra.append([x, y])

        if len(corpo_cobra) > tamanho_cobra:
            del corpo_cobra[0]

        # colisão consigo mesma
        for parte in corpo_cobra[:-1]:

            if parte == [x, y]:

                atualizar_leaderboard(nome_jogador_atual, pontuacao)
                tocar_som("game_over")

                resultado = tela_morte()

                if resultado == "play":
                    return "play"
                if resultado == "menu":
                    return "menu"

        # --------------------------
        # Renderização
        # --------------------------

        tela.fill(preto)

        desenhar_fundo("map.png")
        desenhar_comida(x_comida, y_comida, tipo_comida)
        desenhar_cobra(tamanho_quadrado, corpo_cobra, velocidade_x, velocidade_y)
        desenhar_pontos(pontuacao)
        desenhar_recorde(carregar_recorde())

        pygame.display.update()

        # --------------------------
        # Sistema de comida
        # --------------------------

        if x == x_comida and y == y_comida:

            tamanho_cobra += 1
            tocar_som("snd_comer")

            if tipo_comida == 0:
                pontuacao += 1
            else:
                pontuacao += 3

            novo_nivel = (pontuacao // 10) + 1

            if novo_nivel > nivel_atual:
                nivel_atual = novo_nivel
                velocidade_atual += 1
                tocar_som("level_up")

            x_comida, y_comida, tipo_comida = gerar_comida(corpo_cobra)

        if tamanho_cobra >= max_casas:

            atualizar_leaderboard(nome_jogador_atual, pontuacao)
            tocar_som("you_win")

            resultado = tela_vitoria()

            if resultado == "play":
                return "play"
            if resultado == "menu":
                return "menu"

        relogio.tick(velocidade_atual)


# ==================================================
# EXECUÇÃO
# ==================================================

tocar_musica("bg_music.mp3", True)

while True:

    opcao = tela_menu()

    if opcao == "quit":
        break

    if opcao == "leaderboard":
        tela_leaderboard()
        continue

    if opcao == "nome":

        nome = tela_nome()

        if nome is None:
            continue

        nome_jogador_atual = nome

        while True:

            resultado = rodar_jogo()

            if resultado == "play":
                continue

            if resultado == "menu":
                break

pygame.quit()
