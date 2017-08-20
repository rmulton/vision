 import cv2
 
 while True:
        # Get a frame from the webcam
        ret, frame = cam.read()
        
        if ret:
            cv2.imshow('Original image', raw_img)
            if cv2.waitKey(1)&0xFF == ord('q'):
                break

        else:
            print('No frame returned, check that the webcam is connected')
        
cam.release()
cv2.destroyAllWindows()
