import gameboard
import player

print("Welcome to the game!")
print("Instructions: ")
print("To move up: w")
print("To move down: s")
print("To move left: a")
print("To move right: d")

print("Try to get to the end! Good Luck!")
print("-----------------------------")

# TODO
# Create a new GameBoard called board
board = gameboard.GameBoard()
# Create a new Player called player starting at position 3,2
player = player.Player(intitalRow = 3, initialColumn = 2)

while True:
    board.printBoard(player.rowPosition, player.columnPosition)
    selection = input("Make a move: ")
    # TODO
    # Move the player through the board
    if selection == "w":
        board.checkMove(player.rowPosition -1, player.columnPosition)
        player.moveUp()
    elif selection == "s":
        board.checkMove(player.rowPosition +1, player.columnPosition)
        player.moveDown()
    elif selection == "a":
        board.checkMove(player.rowPosition, player.columnPosition -1)        
        player.moveLeft()
    elif selection == "d":
        board.checkMove(player.rowPosition, player.columnPosition +1)
        player.moveRight()
        break
    # Check if the player has won, if so print a message and break the loop!
