import cv2

#path for video 
cap = cv2.VideoCapture(r"C:\Users\NHI658\Desktop\Brane\sample2.mp4")

width = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
print("Dimensions of the video --- width: {} height: {}".format(width,height))

aspect_ratio = 2/3

count = 0
num_frames = 10

while cap.isOpened():
    ret, frame = cap.read()
    if ret is not True:
        print(count)
    frame_width = int(width*aspect_ratio)
    frame_height = int(height*aspect_ratio)
    #frame = cv2.resize(frame,(frame_width,frame_height))
    print("Size: {} {}".format(frame_width,frame_height))
    cv2.imshow("frame", frame)
    if count % num_frames == 0:
        
        #folder should already be created in the specified path
        cv2.imwrite(r"images5\\frame"+str(count)+".jpg",frame)
    
    if cv2.waitKey(1) & 0xFF==ord('q'):
        break
    
    count += 1
    

cap.release()
cv2.destroyAllWindows()
