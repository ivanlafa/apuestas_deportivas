import pygame
import sys
import random

pygame.init()

# Tamaño de la ventana del juego
WINDOW_WIDTH, WINDOW_HEIGHT = 800, 600

# Colores
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)

# Tamaño del bloque de serpiente
BLOCK_SIZE = 20

# Velocidad de movimiento de la serpiente
SNAKE_SPEED = 15

# Crear la ventana del juego
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption('Snake Game')

# Fuente para mostrar el puntaje y el mensaje de fin de juego
font = pygame.font.SysFont(None, 35)

# Función para dibujar la serpiente
def draw_snake(snake):
    for block in snake:
        pygame.draw.rect(window, GREEN, pygame.Rect(block[0], block[1], BLOCK_SIZE, BLOCK_SIZE))

# Función para mostrar el mensaje de fin de juego
def show_message(message, color):
    text = font.render(message, True, color)
    rect = text.get_rect(center=(WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2))
    window.blit(text, rect)
    pygame.display.update()
    pygame.time.delay(3000)

# Función principal del juego
def main():
    snake = [[100, 100]] # Lista de bloques que representan la serpiente
    direction = 'RIGHT' # Dirección inicial de la serpiente
    clock = pygame.time.Clock()
    score = 0

    # Comida inicial en una posición aleatoria
    food_x, food_y = random.randrange(0, WINDOW_WIDTH - BLOCK_SIZE, BLOCK_SIZE), random.randrange(0, WINDOW_HEIGHT - BLOCK_SIZE, BLOCK_SIZE)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and direction != 'DOWN':
                    direction = 'UP'
                elif event.key == pygame.K_DOWN and direction != 'UP':
                    direction = 'DOWN'
                elif event.key == pygame.K_LEFT and direction != 'RIGHT':
                    direction = 'LEFT'
                elif event.key == pygame.K_RIGHT and direction != 'LEFT':
                    direction = 'RIGHT'

        # Mover la serpiente en la dirección actual
        if direction == 'UP':
            head = [snake[0][0], snake[0][1] - BLOCK_SIZE]
        elif direction == 'DOWN':
            head = [snake[0][0], snake[0][1] + BLOCK_SIZE]
        elif direction == 'LEFT':
            head = [snake[0][0] - BLOCK_SIZE, snake[0][1]]
        elif direction == 'RIGHT':
            head = [snake[0][0] + BLOCK_SIZE, snake[0][1]]

        # Añadir la nueva posición de la cabeza de la serpiente
        snake.insert(0, head)

        # Comprobar colisiones con los bordes de la pantalla
        if head[0] < 0 or head[0] >= WINDOW_WIDTH or head[1] < 0 or head[1] >= WINDOW_HEIGHT:
            show_message(f"El juego ha terminado. Perdiste. Puntaje: {score}", RED)
            pygame.quit()
            sys.exit()

        # Comprobar colisiones con la comida
        if snake[0][0] == food_x and snake[0][1] == food_y:
            # La serpiente ha comido la comida, así que la comida se coloca en una nueva posición aleatoria
            food_x, food_y = random.randrange(0, WINDOW_WIDTH - BLOCK_SIZE, BLOCK_SIZE), random.randrange(0, WINDOW_HEIGHT - BLOCK_SIZE, BLOCK_SIZE)
            score += 1
        else:
            # Si no se ha comido la comida, eliminar el último bloque de la serpiente
            snake.pop()

        # Dibujar todo en la ventana
        window.fill(BLACK)
        pygame.draw.rect(window, RED, pygame.Rect(food_x, food_y, BLOCK_SIZE, BLOCK_SIZE))
        draw_snake(snake)

        # Mostrar el puntaje en la pantalla
        score_text = font.render(f"Puntaje: {score}", True, WHITE)
        window.blit(score_text, [0, 0])

        # Actualizar la ventana
        pygame.display.update()
        clock.tick(SNAKE_SPEED)

if __name__ == "__main__":
    main()
