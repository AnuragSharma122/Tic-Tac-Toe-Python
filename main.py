import numpy
import pygame, sys
import numpy as np

pygame.init()

Height = 600
Width = 600
Bg_color = (24,184,168)
line_color = (12,164,148)
screen = pygame.display.set_mode((Height, Width))
board_rows = 3
board_col = 3
player = 1
circle_color = (250,250,250)
black = (84,84,84)
game_over = False

board = numpy.zeros((board_rows, board_col))
print(board)

pygame.display.set_caption('Tic Tac Toe')
screen.fill(Bg_color)


def mark_squares(row, col, player):
    board[row][col] = player

def available_squares(row, col):
    if board[row][col] == 0:
        return True
    else:
        return False

def is_board_full():
    for row in range(board_rows):
        for col in range(board_col):
            if board[row][col] == 0:
                return  False

    return True


def draw_shapes():
    for row in range(board_rows):
        for col in range(board_col):
            if board[row][col] == 1:
                pygame.draw.circle(screen, circle_color, (int(col*(Height/3) + Height/6), int(row*(Width/3) + Width/6)), Width/10, int((Width/30)))
            elif board[row][col] == 2:
                pygame.draw.line(screen, black, (col*Height/3 + Height/10, row*(Width/3) + (Width/3)-Width/10), (col*Height/3+Height/3-Height/10, row*(Width/3)+Width/10), int((Width/30)))
                pygame.draw.line(screen, black,
                                 (col * (Height/3) + Height/10, row * (Width/3) + Width/10), (col * (Height/3) + (Height/3) -Height/10, row * (Width/3) + (Width/3) - Width/10), int((Width/30)))


def draw_vertical_line(col,player):
    if(player == 1):
        color = circle_color
    elif(player == 2):
        color = black

    posX = Height/6 + (Height/3)*col

    pygame.draw.line(screen, color, (posX, 20), (posX, Height-20), int((Width/30)))


def draw_horzontal_line(row,player):
    if (player == 1):
        color = circle_color
    elif (player == 2):
        color = black

    posY = Width/6 + (Width/3)*row

    pygame.draw.line(screen, color, (20,posY), (Width-20, posY), int((Width/30)))

def draw_diagonal_from_top(player):
    if (player == 1):
        color = circle_color
    elif (player == 2):
        color = black

    pygame.draw.line(screen, color, (20,20), (Width-20, Height-20),int((Width/30)))

def draw_diagonal_from_bottom(player):
    if (player == 1):
        color = circle_color
    elif (player == 2):
        color = black

    pygame.draw.line(screen, color, (20,Height-20), (Width-20, 20),int((Width/30)))


def check_win(player):
    #check row condition
    for row in range(board_rows):
        if board[row][0] == player and board[row][1] == player and board[row][2] == player:
            draw_horzontal_line(row,player)
            return True

    #check column
    for col in range(board_col):
        if board[0][col] == player and board[1][col] == player and board[2][col] == player:
            draw_vertical_line(col,player)
            return True

    #check diagonal from top
    if board[0][0] == player and board[1][1] == player and board[2][2] == player:
        draw_diagonal_from_top(player)
        return True

    if board[2][0] == player and board[1][1] == player and board[0][2] == player:
        draw_diagonal_from_bottom(player)
        return True

def draw_lines():
    #Vertical Lines
    pygame.draw.line(screen, line_color, ((Width/3) ,0), ((Width/3) ,Height), 15)
    pygame.draw.line(screen, line_color, ((2*Width/3) , 0), ((2*Width/3) , Height), 15)

    # Horizontal Lines
    pygame.draw.line(screen, line_color, (0, (Height/3)), (Width, (Height/3)), 15)
    pygame.draw.line(screen, line_color, (0, (2*Height/3)), (Width, (2*Height/3)), 15)

draw_lines()

def restart():
    for row in range(board_rows):
        for col in range(board_col):
            board[row][col] = 0

    player = 1
    screen.fill(Bg_color)
    draw_lines()




while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN and not game_over:
            mouseX = event.pos[0]
            mouseY = event.pos[1]

            row_clicked = int(mouseY/(Height/3))
            col_clicked = int(mouseX/(Height/3))

            if available_squares(row_clicked, col_clicked):
                if player == 1:
                    mark_squares(row_clicked,col_clicked,1)
                    if check_win(player):
                        game_over = True
                    player = 2
                elif player == 2:
                    mark_squares(row_clicked, col_clicked, 2)
                    if check_win(player):
                        game_over = True
                    player = 1
            draw_shapes()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                restart()
                game_over = False

    pygame.display.update()