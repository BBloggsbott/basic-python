import random
play=True
while(play):
    print('select rock(r) , paper (p), scissor (s)  ')
    choice=input('enter your choice  (r),(p),(s):  ' )
    if choice=='r':
        print('you have selected rock(r)')
    elif choice =='p':
        print('you have selected paper(p)')
    elif choice=='s':
        print('you have selected scissor(s)')
    else:
        print('wrong option')
    print('lets play')
    print('you vs machine')
    if choice=='r':
        machine=random.choice(['s','p'])
        if machine =='s':
            print(choice+' v '+machine+ '      you won ')
        else:
            print(choice+' v '+machine +'      machine won ')
    elif choice=='s':
        machine=random.choice(['r','p'])
        if machine =='r':
            print(choice+' v '+machine + '     machine won ')
        else:
            print(choice+' v '+machine + '     you wone ')
    elif choice=='p':
        machine=random.choice(['s','r'])
        if machine =='s':
            print(choice+' v '+machine + '     machine won')
        else:
            print(choice+' v '+machine +'      you won ')
    
    print("**************Game over**************")

    yes=input('do you want to play again ( YES /NO )')
    if yes=='no':
        play=False


    
    

