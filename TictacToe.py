
print("---------------- WELCOME TO TIC TAC TOE ----------------")
def instructions():
    print("******* INSTRUCTIONS *******")
    print("-> Potisions are like :-")
    print("  1 |  2 | 3  ")
    print("--------------")
    print("  4 | 5  | 6  ")
    print("--------------")
    print("  7 | 8  | 9  ")
    print("-> The first player will be using 'X' and the second player using 'O'....So enter the names carefully...... ")
    print("The game is start from FIRST player(X's turn) ")
    
instructions()

# Game board
board = ["-", "-", "-",
         "-", "-", "-",
         "-", "-", "-"]

# If game is still going
game_still_going = True


# Who won? Or tie?
winner = None

ready = input("Are you ready to play the game Y/N...").lower()



if ready == 'y':
        print("LETS START THE GAME")
        while ready == 'y':
            
# Who's turn is it?
            p1 = input("Enter the name of first player :")
            p2 = input("Enter the name of second player :")
            print(p1," you will be using 'X' ")
            print(p2," you will using 'O' ")

            player1 = "X"      



            # --------- Functions -----------


            def display_board():
                print(board[0] + " | " + board[1] + " | " + board[2])
                print(board[3] + " | " + board[4] + " | " + board[5])
                print(board[6] + " | " + board[7] + " | " + board[8])
                
                
                
            # Play a game of tic tac toe
            def play_game():
                    display_board()

                    # While the game is still going
                    while game_still_going:

                        # Handle a single turn of an arbitrary player
                        handle_turn(player1)

                        # Check if the game has ended
                        check_if_game_over()

                        # Flip to the other player
                        flip_player()

                    # The game has ended
                    if winner == "X":
                        print("Hurray !!",p1 ," you won.")
                    if   winner == "O":
                        print("Hurray !!",p2 ," you won.")
                    elif winner == None:
                        print("Tie.")


            def handle_turn(player):

                print(player + "'s turn.")
                position = input("Choose a position from 1-9 : ")
                
                
                valid = False
                while not valid:

                    while position not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
                        position = input("Choose a position from 1-9: ")    

                    position = int(position) - 1

                    if board[position] == "-":
                        
                        valid = True
                    else:
                        print("This position already filled. Go again.")

                board[position] = player

                display_board()
                
                     


            def check_if_game_over():
                check_for_winner()
                check_if_tie()


            def check_for_winner():
                # Set up global variables
                global winner
                # check rows
                row_winner = check_rows()
                # check columns
                column_winner = check_columns()
                # check diagonals
                diagonal_winner = check_diagonals()
                if row_winner:
                    # there was a win
                    winner = row_winner

                elif column_winner:
                    # there was a win
                    winner = column_winner
                elif diagonal_winner:
                    # there was a win
                    winner = diagonal_winner
                else:
                    # ther was no win
                    winner = None
                return


            def check_rows():
                # Set up global variables
                global game_still_going
                # check if any of the rows have all the same values (and is not empty)
                row_1 = board[0] == board[1] == board[2] != "-"
                row_2 = board[3] == board[4] == board[5] != "-"
                row_3 = board[6] == board[7] == board[8] != "-"
                # If any row does have a match, flag that there is a win
                if row_1 or row_2 or row_3:
                    game_still_going = False
                # Return the winner (X or O)
                if row_1:
                    return board[0]
                elif row_2:
                    return board[3]
                elif row_3:
                    return board[6]
                return


            def check_columns():
                # Set up global variables
                global game_still_going
                # check if any of the columns have all the same values (and is not empty)
                column_1 = board[0] == board[3] == board[6] != "-"
                column_2 = board[1] == board[4] == board[7] != "-"
                column_3 = board[2] == board[5] == board[8] != "-"
                # If any column does have a match, flag that there is a win
                if column_1 or column_2 or column_3:
                    game_still_going = False
                # Return the winner (X or O)
                if column_1:
                    return board[0]
                elif column_2:
                    return board[1]
                elif column_3:
                    return board[2]
                return


            def check_diagonals():
                # Set up global variables
                global game_still_going
                # check if any of the diagonals have all the same values (and is not empty)
                diagonal_1 = board[0] == board[4] == board[8] != "-"
                diagonal_2 = board[2] == board[4] == board[6] != "-"
                # If any diagonal does have a match, flag that there is a win
                if diagonal_1 or diagonal_2:
                    game_still_going = False
                # Return the winner (X or O)
                if diagonal_1:
                    return board[0]
                elif diagonal_2:
                    return board[2]
                return


            def check_if_tie():
                global game_still_going
                if "-" not in board:
                    game_still_going = False
                return


            def flip_player():
                # global variables we need
                global player1
                # if the current player was X, then change it to O
                if player1 == "X":
                    player1 = "O"
                # if the current player was O, then change it to X
                elif player1 == "O":
                    player1 = "X"
                return
                


            play_game()
            ready = input("Press 'y' to play again or any other key to quit: ").lower()
        print("Thank you for playing game")
            
else:
    print("You are not ready to play the game,WE ARE SORRY")

