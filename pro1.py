board=['1','2','3','4','5','6','7','8','9']
def show():
	global board
	for i in range(3):
		print("\n---------------")
		for j in range(3):
			print("|",board[(3*i)+j],"|",end='')
	print("\n---------------")
outcome=0
print("Enter the no. where you want to fill ur entry at")
show()
reset=1
while reset==1:
	outcome=0
	g=0
	print("New Board:\n")
	board=[' ',' ',' ',' ',' ',' ',' ',' ',' ']
	show()	
	print("Player 1:X\tPlayer 2:O\n")
	while g<9:
		while True:
			x=int(input("Enter player 1:"))
			x-=1;
			if board[x]!=' ':
				print("ALready filled..re-enter:")
			else:
				board[x]='X'
				g+=1
				show()
				break
		if board[0]=='X' or board[0]=='O':
			if board[0]==board[3]==board[6] or board[0]==board[1]==board[2] or board[0]==board[4]==board[8]:
				outcome=1
				break
		if board[4]=='X' or board[4]=='O':
			if board[4]==board[3]==board[5] or board[4]==board[1]==board[7] or board[2]==board[4]==board[6]:
				outcome=2
				break
		if board[8]=='X' or board[8]=='O':
			if board[7]==board[6]==board[8] or board[8]==board[5]==board[2]:
				outcome=3
				break
		if g==9:
			print("DRAW!!!")
			break
		while True:
			x=int(input("Enter player 2:"))
			x-=1;
			if board[x]!=' ':
				print("ALready filled..re-enter:")
			else:
				board[x]='O'
				g+=1
				show()
				break 
		if board[0]=='X' or board[0]=='O':
			if board[0]==board[3]==board[6] or board[0]==board[1]==board[2] or board[0]==board[4]==board[8]:
				outcome=1
				break
		if board[4]=='X' or board[4]=='O':
			if board[4]==board[3]==board[5] or board[4]==board[1]==board[7] or board[2]==board[4]==board[6]:
				outcome=2
				break
		if board[8]=='X' or board[8]=='O':
			if board[7]==board[6]==board[8] or board[8]==board[5]==board[2]:
				outcome=3
				break
		if g==9:
			print("DRAW!!!")
			break
	if outcome==1:
		if board[0]=='X':
			print("Player 1 wins!!!")
		else :
			print("Player 2 wins!!!")
	if outcome==2:
		if board[4]=='X':
			print("Player 1 wins!!!")
		else :
			print("Player 2 wins!!!")
	if outcome==3:
		if board[8]=='X':
			print("Player 1 wins!!!")
		else :
			print("Player 2 wins!!!")
	reset=input("Play again?[1:Yes/Any other:No]:")
	if reset=='1':
		reset=1
	else :
		reset=0
	

		
		
		
	
		



















