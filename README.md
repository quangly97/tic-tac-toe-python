# Tic-Tac-Toe Game
![tictactoe](https://user-images.githubusercontent.com/62526327/88591576-8c57f580-d02a-11ea-9bfb-75eb7e821eac.PNG)

## Brief
A Tic-Tac-Toe game implemented with python and its pygame library.

## Methods Used
* create_board()
* draw_board(screen, board)
* spot_available(board, position):
* insert_piece(board, piece, position):
* tic_tac_toe(board, piece):
* board_full(board):

## Technologies Used
* Python
* Git
* Github
* pygame
* numpy
* math

## Sample Code
```
while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

        if event.type == pygame.MOUSEBUTTONDOWN:

            if turn == 0:
                position = (math.floor(event.pos[0]//PXLSIZE) , math.floor(event.pos[1]//PXLSIZE))
                if spot_available(board, position):
                    insert_piece(board, 1, position)
                
                if tic_tac_toe(board, 1):
                    game_over = True
            else:
                position = (math.floor(event.pos[0]//PXLSIZE) , math.floor(event.pos[1]//PXLSIZE))
                if spot_available(board, position):
                    insert_piece(board, 2, position)
                
                if tic_tac_toe(board, 2):
                    game_over = True

            if board_full(board):
                game_over = True

            draw_board(screen, board)
            pygame.display.update()

            turn += 1
            turn = turn % 2

            if(game_over):
                pygame.time.delay(5000)
```
