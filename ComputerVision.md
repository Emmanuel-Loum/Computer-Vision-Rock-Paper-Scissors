# A rock,paper,scissors game that interacts with a laptop user using the camera while playing.

## MILESTONE 1



Keras models offer a simple,user-friendly way to define a neural networkthat will then be built for 
you by TensorFlow which provides a collection of workflows to develop and train models using Python.
Model is downloaded from TensorFlow tab in Teachable Machine.


## MILESTONE 2

```python
    import cv2
    from keras.models import load_model
    import numpy as np
    model = load_model('KERAS_MODEL.h5')
    cap = cv2.VideoCapture(0)
    data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)

    while True: 
        ret, frame = cap.read()
        resized_frame = cv2.resize(frame, (224, 224), interpolation = cv2.INTER_AREA)
        image_np = np.array(resized_frame)
        normalized_image = (image_np.astype(np.float32) / 127.0) - 1 # Normalize the image
        data[0] = normalized_image
        prediction = model.predict(data)
        cv2.imshow('frame', frame)
        # Press q to close the window
        print(prediction)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
                
    # After the loop release the cap object
    cap.release()
    # Destroy all the windows
    cv2.destroyAllWindows()
```
The above code is used to run the model downloaded from teachable machine in your computer and to check whether the camera is working.


## MILESTONE 3

Creation of rock,paper,scissors game using Python with if-else statements inorder to figure out a win,lose and tie.
 ```python
            if word.lower()=='scissors' and rules[num]=='paper':
                win=win+1
                print('Player: '+ word +'\n' + 'Computer: '
                +rules[num] + ' \nYou won! \nPress q to quit')
                print('win: '+str(win))
                print('lose: '+str(lose))
                print('tie '+str(tie))
                if win ==3:
                    print('Game Over! \n You won')
                    break

   ```         
 


## MILESTONE 4

Merging the keras model with the python coded game so that the user input may be from the camera.Using prediction from the model,the game will be able to predict the outcome of the user input which can be translated to either rock,paper,scissors or nothing.
    
Before the game starts,a countdown timer is set to count from 3 to 0 as shown in the code below.

```python    
        if cv2.waitKey(1) & 0xFF == ord('t'):
            m=True
            t=3
        
        if m==True:
            
            mins,secs=divmod(t,60)
            timer='{:02d}:{:02d}'.format(mins,secs)
            time.sleep(1)
            t-=1
                
            messenger=timer
            if t==-1:

                m=False
```
using the if-else statement, the game repeats 3 times to finalise who the winner is.

Display text message on an OpenCV window by using the function putText()
```python
cv2.putText(frame,messenger2,(90,440),font,1,(0,255,255),2,cv2.LINE_4)
``` 
Displayed text on the camera screen inclusive of commands for the start,continue or quit options.
``` python             
        #quit command       
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

        #continue command                       
        if cv2.waitKey(1) & 0xFF == ord('c'):
            f=True
```
<!--Blockquote-->
> ## CONCLUSION

    To conclude, using Keras models makes it easy for user interaction with an application.However,
    the game would have a better user experience if the OpenCV dispayed the computer's choice by a picture of either paper,rock or scissors 
    and show a relevant animation after the win,lose or tie.
