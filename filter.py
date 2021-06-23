from utils import CFEVideoConf, image_resize
import glob
import math

cap=cv2.VideoCapture(0)

frames_per_second =20
save_path ='saved-media/filter.mp4'
config = CFEVideoConf(cap, filepath=save_path, res='480p')

def apply_invert(frame):
    return cv2.bitwise_not(frame)

while(True):
    ret, frame = cap.read()
    invert = apply_invert(frame)
    cv2.imshow('invert', frame)
    if cv2.waitKey(20) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()