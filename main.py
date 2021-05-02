from myLibrary import *


if __name__ == '__main__':
    my_board = chess_board('input_image.png')
    dimension = int(input("Enter the new dimension of square board: "))
    my_board.resizing(dimension)
    code = input("Enter the code for shell you are interested in: ")
    my_board.drawing(code)
    my_board.displaying()