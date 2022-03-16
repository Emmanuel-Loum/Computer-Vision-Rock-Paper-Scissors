import time
import random
import cv2
from keras.models import load_model
import numpy as np

def gamer():
    model = load_model('keras_model.h5')
    cap = cv2.VideoCapture(0)
    data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)
    

    messenger3=' '
    messenger2=' '
    messenger='Press T to start'
    f=False
    m=False
    
    while True: 
          
        ret, frame = cap.read()
        resized_frame = cv2.resize(frame, (224, 224), interpolation = cv2.INTER_AREA)
        image_np = np.array(resized_frame)
        normalized_image = (image_np.astype(np.float32) / 127.0) - 1 # Normalize the image
        data[0] = normalized_image
        prediction = model.predict(data)
        cv2.imshow('frame', frame)
        # Press q to close the window
        font=cv2.FONT_HERSHEY_SIMPLEX
        cv2.putText(frame,messenger,(50,70),font,1,(255,153,51),2,cv2.LINE_4)
        cv2.putText(frame,messenger2,(90,440),font,1,(0,255,255),2,cv2.LINE_4)
        cv2.putText(frame,messenger3,(50,200),font,1,(0,255,0),2,cv2.LINE_4)
        cv2.imshow('frame', frame)
        

        rules=['rock','paper','scissors'] 
        rules=random.choice(rules)
           

        #Start command
        if cv2.waitKey(1) & 0xFF == ord('t'):
            m=True
            win=0
            lose=0
            tie=0
            t=3
        
        if m==True:
            
            mins,secs=divmod(t,60)
            timer='{:02d}:{:02d}'.format(mins,secs)
            time.sleep(1)
            t-=1
                
            messenger=timer
            if t==-1:

                m=False
                f=True
         
         #continue command                       
        if cv2.waitKey(1) & 0xFF == ord('c'):
            f=True
        
        
        if f==True:               
            messenger='show your hand'  
            messenger2=' '
            messenger3=' '
            
            if prediction[0][0]>0.9:
                
                word="rock"
                
                
                    
                if word=='rock' and rules=='scissors':
                    win=win+1
                    messenger=f'P1: {word} Comp: {rules} You win!'
                    
                    f=False                    
                    messenger2='Long Press c to continue'

                    if win==3:
                        messenger3=f"wins={win} lose={lose} tie={tie} You win"
                        messenger2='Press T to play again q to quit'
                        
                        m=False
                    
                    
                
                elif word==rules:
                    tie=tie+1
                    messenger=f'P1: {word} Comp: {rules} Its a tie!'
                    f=False
        
                    messenger2='Long Press c to continue'

                    if tie==3:

                        messenger3=f"wins={win} lose={lose} tie={tie} Its a Draw"
                        messenger2='Press T to play again q to quit'
                        
                        m=False
                    
                    
                    
                else:
                    lose=lose+1
                    messenger=f'P1:{word} Comp:{rules} You Lose!'
                    f=False
                                        
                    messenger2='Long Press c to continue'

                    if lose==3:
                        messenger3=f"wins={win} lose={lose} tie={tie} Comp wins"
                        messenger2='Press T to play again q to quit'
                        
                        m=False
                    
                    
                                    
            elif prediction[0][1]>0.9:
                #print("paper")
                word="paper"
                

                if word=='paper' and rules=='rock':
                    win=win+1
                    messenger=f'P1:{word} Comp:{rules} You win!'
                    
                    f=False
                    messenger2='Long press c to continue'

                    if win==3:
                        messenger3=f"wins={win} lose={lose} tie={tie} You win"
                        messenger2='Press T to play again q to quit'
                       
                        m=False
                    
                    
                

                elif word==rules:
                    tie=tie+1
                    messenger=f'P1:{word} Comp:{rules} Its a tie!' 
                
                    f=False
                    messenger2='Long press c to continue'
                    if tie==3:
                        messenger3=f"wins={win} lose={lose} tie={tie} Its a tie"
                        messenger2='Press T to play again q to quit'
                       
                        m=False
                        
                    
                
                else:
                    lose=lose+1
                    messenger=f'P1:{word} Comp: {rules} You Lose!'
                    
                    f=False
                    messenger2='Long press c to continue'

                    if lose==3:

                        messenger3=f"wins={win} lose={lose} tie={tie} Comp win"
                        messenger2='Press T to play again q to quit'
                       
                        m=False
                    
                    
                
                    
               
            elif prediction[0][2]>0.9:
                #print("scissors")
                word="scissors"
                

                if word=='scissors' and rules=='paper':
                    win=win+1
                    messenger=f'P1: {word} Comp:{rules} You Win!'
                    
                    f=False
                    messenger2='Long press c to continue' 
                    if win==3:
                        messenger3=f"wins={win} lose={lose} tie={tie} You win"
                        messenger2='Press T to play again q to quit' 
                                            
                        m=False
                    
                    

                elif word==rules:
                    tie=tie+1
                    messenger=f'P1:{word} Comp:{rules} A tie!' 
                
                    f=False
                    messenger2='Long press c to continue'
                    if tie==3:
                        messenger3=f"wins={win} lose={lose} tie={tie} Its a Draw"
                        messenger2='Press T to play again q to quit'
                      
                        m=False
                    
                    
                else:
                    lose=lose+1
                    messenger=f'P1: {word} Comp: {rules} You lose!'
                    
                    f=False
                    messenger2='Long press c to continue'
                    if lose==3:
                        messenger3=f"wins={win} lose={lose} tie={tie} Comp wins"
                        messenger2='Press T to play again q to quit'
                        
                        m=False
                    
                
              
                
            elif prediction[0][3]>0.9:
                
               
                word="nothing"


        #quit command       
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # After the loop release the cap object
    #cap.release()
    # Destroy all the windows
    #cv2.destroyAllWindows()
gamer()
