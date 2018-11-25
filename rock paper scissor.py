import random
play=True
while(play):
	print('--\nSelect rock(r) , paper (p), scissor (s)  ')
	choice=input('enter your choice  (r|p|s):  ' )
	if choice=='r':
		print('you have selected rock(r)')
	elif choice =='p':
		print('you have selected paper(p)')
	elif choice=='s':
		print('you have selected scissor(s)')
	else:
		print('wrong option')
		continue
	print('lets play')
	print('you vs machine')
	machine = random.choice(['r', 'p', 's'])
	if choice=='r':
		if machine =='s':
		    print(choice+' v '+machine+ '\tYou won ')
		elif machine == 'p':
		    print(choice+' v '+machine +'\tMachine won ')
		else:
			print(choice+' v '+machine +'\tDraw ')
	elif choice=='s':
		if machine =='r':
		    print(choice+' v '+machine + '\tMachine won ')
		elif machine == 'p':
		    print(choice+' v '+machine + '\tYou wone ')
		else:
		    print(choice+' v '+machine +'\tDraw ')
	elif choice=='p':
		if machine =='s':
		    print(choice+' v '+machine + '\tMachine won')
		elif machine == 'r':
		    print(choice+' v '+machine +'\tYou won ')
		else:
		    print(choice+' v '+machine +'\tDraw ')
	print("**************Game over**************")

	yes=input('do you want to play again ([YES]/NO)')
	if yes.lower()=='no':
		play=False
