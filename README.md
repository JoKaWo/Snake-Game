# 🐍 Snake Game

Um jogo da cobrinha clássico desenvolvido em **Python** com a biblioteca **Pygame**, com menu inicial, sistema de pontuação, níveis de velocidade, tela de vitória/derrota e placar de líderes (leaderboard) persistente.

## 👥 Autores

- [Josué Kaufmann Wolfgramm](https://github.com/JoKaWo)
- [Guilherme Moreira Pagano](https://github.com/Guilherme-Pagano)

## 🎮 Sobre o jogo

O objetivo é controlar a cobrinha, comer as maçãs que aparecem no mapa e crescer sem colidir com as bordas do mapa ou com o próprio corpo. Maçãs vermelhas valem 1 ponto e maçãs roxas (mais raras) valem 3 pontos. A cada 10 pontos a cobra sobe de nível e aumenta sua velocidade. Ao final de cada partida, a pontuação é salva em um placar de líderes local (`leaderboard.txt`).

### Funcionalidades

- Menu inicial com navegação por mouse ou teclado
- Cadastro de nome do jogador
- Placar de líderes (top 10) com destaque para 1º, 2º e 3º lugares
- Sistema de níveis com aumento progressivo de velocidade
- Dois tipos de comida com pontuações diferentes
- Telas de vitória e de derrota
- Efeitos sonoros e música de fundo

## 🕹️ Controles

| Tecla | Ação |
|---|---|
| `W` / `↑` | Mover para cima |
| `S` / `↓` | Mover para baixo |
| `A` / `←` | Mover para esquerda |
| `D` / `→` | Mover para direita |
| `1`, `2`, `3` | Navegar pelos menus (também é possível clicar com o mouse) |

## 📦 Pré-requisitos

- [Python 3.10+](https://www.python.org/downloads/) instalado
- `pip` (gerenciador de pacotes do Python)

## ⚙️ Como clonar e executar

1. **Clone o repositório**

   ```bash
   git clone https://github.com/JoKaWo/Snake-Game.git
   ```

2. **Acesse a pasta do projeto**

   ```bash
   cd Snake-Game
   ```

3. **(Recomendado) Crie um ambiente virtual**

   ```bash
   python -m venv venv
   ```

   Ative o ambiente virtual:

   - Windows:
     ```bash
     venv\Scripts\activate
     ```
   - Linux/macOS:
     ```bash
     source venv/bin/activate
     ```

4. **Instale as dependências**

   ```bash
   pip install -r requirements.txt
   ```

5. **Execute o jogo**

   ```bash
   python main.py
   ```

## 🗂️ Estrutura do projeto

```
Snake-Game/
├── main.py                  # Código principal do jogo
├── requirements.txt         # Dependências do projeto
├── leaderboard.txt          # Placar de líderes (gerado/atualizado automaticamente)
├── PressStart2P.ttf         # Fonte usada nos textos e menus
├── map.png                  # Imagem de fundo do mapa
├── main_menu.png            # Tela do menu inicial
├── enter_name.png           # Tela de cadastro de nome
├── leaderboard.png          # Tela do placar de líderes
├── you_win.png               # Tela de vitória
├── tela_morte.png           # Tela de derrota
├── head.png / body.png      # Sprites da cobra
├── spr_red_apple.png        # Sprite da maçã vermelha
├── spr_purple_apple.png     # Sprite da maçã roxa
├── bg_music.mp3              # Música de fundo
├── eat_apple_sound.mp3       # Som ao comer a maçã
├── level_up.mp3               # Som ao subir de nível
├── game_over.mp3              # Som de game over
└── you_win.mp3                 # Som de vitória
```

## 🎨 Créditos e licenças dos assets

- **Fonte:** [Press Start 2P](https://fonts.google.com/specimen/Press+Start+2P), criada por Cody "CodeMan38" Boisclair, distribuída sob a [SIL Open Font License 1.1](https://openfontlicense.org/).
- **Sprites e imagens** (cobra, maçãs, telas de menu, nome, leaderboard, vitória e derrota): criados originalmente pelos autores deste projeto.
- **Efeitos sonoros e música de fundo** (`bg_music.mp3`, `eat_apple_sound.mp3`, `level_up.mp3`, `game_over.mp3`, `you_win.mp3`): obtidos em plataformas de áudio gratuito e livre de direitos autorais, como [Pixabay](https://pixabay.com/sound-effects/) e a [Biblioteca de Áudio do YouTube](https://www.youtube.com/audiolibrary), utilizados sob licença royalty-free / sem necessidade de atribuição.

## 📄 Licença do código

Este projeto foi desenvolvido para fins acadêmicos.

## 🔗 Repositório

[https://github.com/JoKaWo/Snake-Game](https://github.com/JoKaWo/Snake-Game)
