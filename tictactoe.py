i = 0

board_inputs = [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ']


def player_input():
    player1 = input("Player1 choose X or O: ")
    player1 = player1.upper()
    if player1 == 'X':
        player2 = 'O'
    else:
        player2 = 'X'

    print("Player1 goes first!\n")

    def decision(p1):
        x = 0

        if(board_inputs[1] == board_inputs[5] == board_inputs[9]):
            if board_inputs[1] == ' ':
                pass
            else:
                if board_inputs[1] == p1:
                    print("Player1 is the winner!")
                else:
                    print("Player2 is the winner!")
                x+=1
                return x
        if(board_inputs[3] == board_inputs[5] == board_inputs[7]):
            if board_inputs[3] == ' ':
                pass
            else:
                if board_inputs[1] == p1:
                    print("Player1 is the winner!")
                else:
                    print("Player2 is the winner!")
                x+=1
                return x


        for j in range(0,7,3):
            if(board_inputs[j+1] == board_inputs[j+2] == board_inputs[j+3]):
                if board_inputs[j+1] == ' ':
                    continue
                if board_inputs[j+1] == p1:
                    print("Player1 is the winner!")
                    x+=1
                    return x
                else:
                    print("Player2 is the winner!")
                    x+=1
                    return x

        for k in range(0,3):
            if board_inputs[k+1] == board_inputs[k+4] == board_inputs[k+7]:
                if board_inputs[k+1] == ' ':
                    continue
                if board_inputs[k+1] == p1:
                    print("Player1 is the winner!")
                    x+=1
                    return x
                else:
                    print("Player2 is the winner!")
                    x+=1
                    return x
        return x

    for i in range(9):
        boards(player1,player2,i)
        n = decision(player1)
        if n > 0:
            break
    if n == 0:
        print("It's a tie!!")






def boards(p1,p2,i):

    print(board_inputs[9],'|',board_inputs[8],'|',board_inputs[7])
    print('-','|','-','|','-')
    print(board_inputs[6],'|',board_inputs[5],'|',board_inputs[4])
    print('-','|','-','|','-')
    print(board_inputs[3],'|',board_inputs[2],'|',board_inputs[1])

    if i % 2 == 0:
        pos = int(input("Player1 enter position: "))
        board_inputs[pos] = p1
    else:
        pos = int(input("Player2 enter position: "))
        board_inputs[pos] = p2

    print("\n"*100)






while True:
    board_inputs = [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ']
    player_input()
    print("Enter Y to play again: ")
    again = input()

    if again.upper() == 'Y':
        continue
    else:
        break

