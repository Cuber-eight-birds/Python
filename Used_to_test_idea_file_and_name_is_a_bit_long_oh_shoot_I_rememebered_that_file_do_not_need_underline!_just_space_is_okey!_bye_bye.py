import pygame
import random
 
# 游戏界面大小
GRID_SIZE = 4
CELL_SIZE = 100
GRID_WIDTH = GRID_SIZE * CELL_SIZE
GRID_HEIGHT = GRID_SIZE * CELL_SIZE
 
# 颜色定义
BACKGROUND_COLOR = (187, 173, 160)
CELL_COLOR = (205, 193, 180)
TEXT_COLOR = (255, 255, 255)
 
# 初始化Pygame
pygame.init()
 
# 创建游戏窗口
window = pygame.display.set_mode((GRID_WIDTH, GRID_HEIGHT + 50))
pygame.display.set_caption("2048")
 
# 加载字体
font = pygame.font.Font(None, 48)
 
# 积分变量
score = 0
 
 
def draw_grid():
    # 绘制游戏界面网格
    window.fill(BACKGROUND_COLOR)
    for row in range(GRID_SIZE):
        for col in range(GRID_SIZE):
            cell_value = grid[row][col]
            cell_color = get_cell_color(cell_value)
            cell_rect = pygame.Rect(col * CELL_SIZE, row * CELL_SIZE, CELL_SIZE, CELL_SIZE)
            pygame.draw.rect(window, cell_color, cell_rect)
            if cell_value != 0:
                draw_text(cell_value, cell_rect)
 
    # 绘制积分
    score_text = font.render("Score: " + str(score), True, TEXT_COLOR)
    window.blit(score_text, (10, GRID_HEIGHT + 10))
 
 
def draw_text(value, rect):
    # 绘制方块中的数字
    text_surface = font.render(str(value), True, TEXT_COLOR)
    text_rect = text_surface.get_rect()
    text_rect.center = rect.center
    window.blit(text_surface, text_rect)
 
 
def get_cell_color(value):
    # 根据方块的值获取对应的颜色
    colors = {
        0: (205, 193, 180),
        2: (238, 228, 218),
        4: (237, 224, 200),
        8: (242, 177, 121),
        16: (245, 149, 99),
        32: (246, 124, 95),
        64: (246, 94, 59),
        128: (237, 207, 114),
        256: (237, 204, 97),
        512: (237, 200, 80),
        1024: (237, 197, 63),
        2048: (237, 194, 46),
    }
    return colors.get(value, (0, 0, 0))
 
 
def add_new_tile():
    # 在随机空位置生成一个新数字（2或4）
    empty_cells = [(i, j) for i in range(GRID_SIZE) for j in range(GRID_SIZE) if grid[i][j] == 0]
    if empty_cells:
        row, col = random.choice(empty_cells)
        grid[row][col] = random.choice([2, 4])
 
 
def move_tiles_left():
    # 向左移动所有数字块
    global score
    for row in range(GRID_SIZE):
        merged = [False] * GRID_SIZE
        for col in range(1, GRID_SIZE):
            if grid[row][col] != 0:
                k = col
                while k > 0 and grid[row][k - 1] == 0:
                    grid[row][k - 1] = grid[row][k]
                    grid[row][k] = 0
                    k -= 1
                if k > 0 and not merged[k - 1] and grid[row][k - 1] == grid[row][k]:
                    grid[row][k - 1] *= 2
                    grid[row][k] = 0
                    merged[k - 1] = True
                    score += grid[row][k - 1]  # 更新积分
 
 
def move_tiles_up():
    # 向上移动所有数字块
    global score
    for col in range(GRID_SIZE):
        merged = [False] * GRID_SIZE
        for row in range(1, GRID_SIZE):
            if grid[row][col] != 0:
                k = row
                while k > 0 and grid[k - 1][col] == 0:
                    grid[k - 1][col] = grid[k][col]
                    grid[k][col] = 0
                    k -= 1
                if k > 0 and not merged[k - 1] and grid[k - 1][col] == grid[k][col]:
                    grid[k - 1][col] *= 2
                    grid[k][col] = 0
                    merged[k - 1] = True
                    score += grid[k - 1][col]  # 更新积分
 
 
def move_tiles_right():
    # 向右移动所有数字块
    global score
    for row in range(GRID_SIZE):
        merged = [False] * GRID_SIZE
        for col in range(GRID_SIZE - 2, -1, -1):
            if grid[row][col] != 0:
                k = col
                while k < GRID_SIZE - 1 and grid[row][k + 1] == 0:
                    grid[row][k + 1] = grid[row][k]
                    grid[row][k] = 0
                    k += 1
                if k < GRID_SIZE - 1 and not merged[k + 1] and grid[row][k + 1] == grid[row][k]:
                    grid[row][k + 1] *= 2
                    grid[row][k] = 0
                    merged[k + 1] = True
                    score += grid[row][k + 1]  # 更新积分
 
 
def move_tiles_down():
    # 向下移动所有数字块
    global score
    for col in range(GRID_SIZE):
        merged = [False] * GRID_SIZE
        for row in range(GRID_SIZE - 2, -1, -1):
            if grid[row][col] != 0:
                k = row
                while k < GRID_SIZE - 1 and grid[k + 1][col] == 0:
                    grid[k + 1][col] = grid[k][col]
                    grid[k][col] = 0
                    k += 1
                if k < GRID_SIZE - 1 and not merged[k + 1] and grid[k + 1][col] == grid[k][col]:
                    grid[k + 1][col] *= 2
                    grid[k][col] = 0
                    merged[k + 1] = True
                    score += grid[k + 1][col]  # 更新积分
 
 
def is_game_over():
    # 检查游戏是否结束（无法再移动数字块）
    for row in range(GRID_SIZE):
        for col in range(GRID_SIZE):
            if grid[row][col] == 0:
                return False
            if col < GRID_SIZE - 1 and grid[row][col] == grid[row][col + 1]:
                return False
            if row < GRID_SIZE - 1 and grid[row][col] == grid[row + 1][col]:
                return False
    return True
 
 
def draw_grid():
    # 绘制游戏界面网格
    window.fill(BACKGROUND_COLOR)
    for row in range(GRID_SIZE):
        for col in range(GRID_SIZE):
            cell_value = grid[row][col]
            cell_color = get_cell_color(cell_value)
            cell_rect = pygame.Rect(col * CELL_SIZE, row * CELL_SIZE, CELL_SIZE, CELL_SIZE)
            pygame.draw.rect(window, cell_color, cell_rect)
            if cell_value != 0:
                draw_text(cell_value, cell_rect)
 
    # 绘制积分
    score_text = font.render("Score: " + str(score), True, TEXT_COLOR)
    window.blit(score_text, (10, GRID_HEIGHT + 10))
 
 
def update_score(points):
    # 更新积分
    global score
    score += points
 
 
# 初始化游戏界面
grid = [[0] * GRID_SIZE for _ in range(GRID_SIZE)]
add_new_tile()
add_new_tile()
 
# 游戏循环
running = True
while running:
    # 处理事件
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if not is_game_over():
                if event.key == pygame.K_a or event.key == pygame.K_LEFT:
                    move_tiles_left()
                    add_new_tile()
                elif event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                    move_tiles_right()
                    add_new_tile()
                elif event.key == pygame.K_w or event.key == pygame.K_UP:
                    move_tiles_up()
                    add_new_tile()
                elif event.key == pygame.K_s or event.key == pygame.K_DOWN:
                    move_tiles_down()
                    add_new_tile()  # 在移动后生成新数字块
 
    # 绘制界面
    draw_grid()
    pygame.display.update()
 
    if is_game_over():
        print("Game over!")
        print("Final Score: ", score)
 
# 退出游戏
pygame.quit()