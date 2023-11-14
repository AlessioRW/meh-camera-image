import cv2, requests, discord
  
# define a video capture object 
vid = cv2.VideoCapture(0)
width = vid.get(cv2.CAP_PROP_FRAME_WIDTH)
height = vid.get(cv2.CAP_PROP_FRAME_HEIGHT)

client = discord.Client()

while(True): 
    ret, frame = vid.read()

    boxHeight = 975
    boxWidth = 750
    start_point = ( int((width/2)-boxWidth/2) , int((height/2)-boxHeight/2))
    colour = (255, 0, 0) 
    thickness = 2

    fin_img = cv2.rectangle(frame, start_point, (start_point[0]+boxWidth, start_point[1]+boxHeight), colour, thickness) 

    cv2.imshow('frame', frame) 
      
    if cv2.waitKey(1) & 0xFF == ord('q'): 
        break
    if cv2.waitKey(1) & 0xFF == ord('p'):
        cropped_image = frame[start_point[1]+2:(start_point[1]+boxHeight)-2, start_point[0]+2:(start_point[0]+boxWidth)-2]
        cv2.imwrite('camera_image.png', cropped_image)
        print('Picture Saved')

        

        response = requests.post(
            'https://api.remove.bg/v1.0/removebg',
            files={'image_file': open('./camera_image.png', 'rb')},
            data={'size': 'auto'},
            headers={'X-Api-Key': 'ZujcDVvQxtcd6wL6E5RVKd3D'},
        )
        if response.status_code == requests.codes.ok:
            with open('no-bg.png', 'wb') as out:
                out.write(response.content)
        else:
            print("Error:", response.status_code, response.text)

# After the loop release the cap object 
vid.release()
# Destroy all the windows
cv2.destroyAllWindows()

@bot.event
async def uploadImage():
    

client.run('MTE3NDAzODI1NjQ2ODM2OTQ4OQ.GZeNap.AakMHXPeNNAA-Jgyt8zwIcL23iymUoFG1eyQiE')