import random


def rpsgame():
     
     win=0
     lose=0
     tie=0
     while True:
        word=input('Choose between rock,paper,scissors ')
        word=word.lower()
        
        rules=['rock','paper','scissors']
        num=random.randint(0,2)
        if word=='q':
            print('win: '+str(win))
            print('lose: '+str(lose))
            print('tie '+str(tie))
            break
      
            
        elif word.lower()=='scissors' and rules[num]=='paper':
            win=win+1
            print('Player: '+ word +'\n' + 'Computer: '
            +rules[num] + ' \nYou won! \nPress q to quit')
            print('win: '+str(win))
            print('lose: '+str(lose))
            print('tie '+str(tie))
            if win ==3:
                print('Game Over! \n You won')
                break

        elif word.lower()=='paper' and rules[num]=='rock':
            win=win+1
            print('Player: '+ word +'\n' + 'Computer: '
            +rules[num] + ' \n You won! \nPress q to quit')
            print('win: '+str(win))
            print('lose: '+str(lose))
            print('tie '+str(tie))
            if win ==3:
                print('Game Over! \n You won')
                break

        elif word.lower()=='rock' and rules[num]=='scissors':
            win=win+1
            print('Player: '+ word +'\n' + 'Computer: '
            +rules[num] + ' \n You won! \nPress q to quit')
            print('win: '+str(win))
            print('lose: '+str(lose))
            print('tie '+str(tie))
            if win == 3:
                print('Game Over! \n You won')
                break

        elif word.lower()==rules[num]:
            tie=tie+1
            print('Player: '+ word +'\n' + 'Computer: '
            +rules[num] + ' \nIts a draw. \nPress q to quit')
            print('win: '+str(win))
            print('lose: '+str(lose))
            print('tie '+str(tie))
            if tie == 3:
                print('Game Over! \nIt was a Draw')
                break
        else:
            lose=lose+1
            
            
            print( 'Player: '+ word +'\n' + 'Computer: '
            + rules[num] + ' \nComputer won.  \nPress q to quit')
            print('win: '+str(win))
            print('lose: '+str(lose))
            print('tie '+str(tie))
            if  lose == 3:
                print('Game Over \nYou lose')
                break
      

    
rpsg=(rpsgame())