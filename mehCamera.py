import cv2, requests, time
  
# define a video capture object 
vid = cv2.VideoCapture(0)
width = vid.get(cv2.CAP_PROP_FRAME_WIDTH)
height = vid.get(cv2.CAP_PROP_FRAME_HEIGHT)

boxHeight = 500#975
boxWidth = 400#750
start_point = ( int((width/2)-boxWidth/2) , int((height/2)-boxHeight/2))
colour = (255, 0, 0) 
thickness = 2

org = (100, 100) #text location
fontScale = 1
color = (255, 0, 0)
thickness = 2
font = cv2.FONT_HERSHEY_SIMPLEX 


curFrame = 0
frameTaken = -1

while(True):
    curFrame += 1
    ret, frame = vid.read()
    cv2.rectangle(frame, start_point, (start_point[0]+boxWidth, start_point[1]+boxHeight), colour, thickness)

    if frameTaken + 40 > curFrame and frameTaken != -1:
        cv2.putText(frame, 'Picture Taken', org, font,  
            fontScale, color, thickness, cv2.LINE_AA)
    else:
        frameTaken = -1
    cv2.imshow('frame', frame) 


    
    if cv2.waitKey(1) & 0xFF == ord('q'): 
        break

    if cv2.waitKey(1) & 0xFF == ord('p'):
        frameTaken = curFrame
        cropped_image = frame[start_point[1]+2:(start_point[1]+boxHeight)-2, start_point[0]+2:(start_point[0]+boxWidth)-2]
        cv2.imwrite('camera_image.png', cropped_image)
        print('Picture Saved')
            
vid.release()
cv2.destroyAllWindows()
