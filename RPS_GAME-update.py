import cv2
import random
from keras.models import load_model
import numpy as np


def rpsgame():
    model = load_model('keras_model_f.h5')
    cap = cv2.VideoCapture(0)
    data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)

    rock=0
    paper=0
    scissors=0

    win=0
    lose=0
    tie=0
   
    

    while True:
        rules=['rock','paper','scissors'] 
        rules=random.choice(rules)
        #num=random.randint(0,5)
        

        ret, frame = cap.read()
        resized_frame = cv2.resize(frame, (224, 224), interpolation = cv2.INTER_AREA)
        image_np = np.array(resized_frame)
        normalized_image = (image_np.astype(np.float32) / 127.0) - 1 # Normalize the image
        data[0] = normalized_image
        prediction = model.predict(data)
        cv2.imshow('frame', frame)
        # Press q to close the window
        #print(prediction[0])

        if prediction[0][0]>0.9:
            print("rock")
            word="rock"
            
            num=random.randint(0,5)
            while True:
                if word=='rock' and rules=='scissors':
                    win=win+1
                    print('Player: '+ word +'\n' + 'Computer: '
                    +rules + ' \n You won! \nPress q to quit')
                    print('win: '+str(win))
                    print('lose: '+str(lose))
                    print('tie '+str(tie))
                    break
                
                elif word==rules:
                    tie=tie+1
                    print('Player: '+ word +'\n' + 'Computer: '
                    +rules + ' \nIts a draw. \nPress q to quit')
                    print('win: '+str(win))
                    print('lose: '+str(lose))
                    print('tie '+str(tie))
                    
                    break
                    
                else:
                    lose=lose+1
                    print( 'Player: '+ word +'\n' + 'Computer: '
                    + rules + ' \nComputer won.  \nPress q to quit')
                    print('win: '+str(win))
                    print('lose: '+str(lose))
                    print('tie '+str(tie))
                    break
                    
            
            if win==3:
                print("You win")
                break

            elif lose==3:
                print("Computer wins")
                break
            
            elif tie==3:
                print("Its a Draw")

                break

            
                
                
        elif prediction[0][1]>0.9:
            print("paper")
            word="paper"
            while True:

                if word=='paper' and rules=='rock':
                    win=win+1
                    print('Player: '+ word +'\n' + 'Computer: '
                    +rules + ' \n You won! \nPress q to quit')
                    print('win: '+str(win))
                    print('lose: '+str(lose))
                    print('tie '+str(tie))
                    break

                elif word==rules:
                    tie=tie+1
                    print('Player: '+ word +'\n' + 'Computer: '
                    +rules + ' \nIts a draw. \nPress q to quit')
                    print('win: '+str(win))
                    print('lose: '+str(lose))
                    print('tie '+str(tie))
                    
                    break

                else:
                    lose=lose+1
                    print( 'Player: '+ word +'\n' + 'Computer: '
                    + rules + ' \nComputer won.  \nPress q to quit')
                    print('win: '+str(win))
                    print('lose: '+str(lose))
                    print('tie '+str(tie))
                    break

            if win==3:
                print("You win")
                break

            elif lose==3:
                print("Computer wins")

                break
            elif tie==3:
                print("Its a Draw")
                break
            
        elif prediction[0][2]>0.9:
            print("scissors")
            word="scissors"
            while True:

                if word=='scissors' and rules=='paper':
                    win=win+1
                    print('Player: '+ word +'\n' + 'Computer: '
                    +rules + ' \nYou won! \nPress q to quit')
                    print('win: '+str(win))
                    print('lose: '+str(lose))
                    print('tie '+str(tie))
                    break


                elif word==rules:
                    tie=tie+1
                    print('Player: '+ word +'\n' + 'Computer: '
                    +rules + ' \nIts a draw. \nPress q to quit')
                    print('win: '+str(win))
                    print('lose: '+str(lose))
                    print('tie '+str(tie))
                    
                    break

                else:
                    lose=lose+1
                    print( 'Player: '+ word +'\n' + 'Computer: '
                    + rules + ' \nComputer won.  \nPress q to quit')
                    print('win: '+str(win))
                    print('lose: '+str(lose))
                    print('tie '+str(tie))
                    break
                
            if win==3:
                print("You win")
                break
            

            elif lose==3:
                print("Computer wins")
                break

            elif tie==3:
                print("Its a draw")
                break

            
        elif prediction[0][3]>0.9:
            print("nothing")
            word="nothing"
            
            
            

        
                
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

        
        
        
        
       




        
    # After the loop release the cap object
    #cap.release()
    # Destroy all the windows
    #cv2.destroyAllWindows()

rpsg=(rpsgame())
