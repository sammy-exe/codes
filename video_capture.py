import cv2


vid = cv2.VideoCapture(0)
vid.isOpened()
while(True):
  
  ret, frame = vid.read()

  # Display
  cv2.imshow('frame', frame)
  
  # 'q' button is quitting button
  if cv2.waitKey(1) & 0xFF == ord('q'):
    break

# After the loop release the cap object
vid.release()
# Destroy all the windows
cv2.destroyAllWindows()
