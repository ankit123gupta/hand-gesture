import cv2
import numpy as np
import myfunctions as my

angle =0
pin=""
text="Please raise your hand..."


instructions=np.zeros((500,500))
cap = cv2.VideoCapture(0)

while cap.isOpened():
    ret , frame = cap.read()
    frame=cv2.flip(frame,1)
    w,h,_=frame.shape
    img_timer=my.timer(frame,angle)
    angle=(angle+9)%360
    thres= my.thresold(img_timer)
    # img_timer=my.timer(thres,angle)
    if angle>=350:
        # condition ture the call for ML
        detected_number=my.test(thres)      #detect the no.
        #print(detected_number)
        if detected_number<=9:
            pin+=str(detected_number)
        else:
            print("addon_function")
        # 274001
        if len(pin)==6:
            # call for output function
            my.show_result(cap,pin)
            # print(pin)
            pin=""
    cv2.putText(frame,text,(int(w*0.1),int(h*0.1)),cv2.FONT_HERSHEY_SIMPLEX,0.8,(255,255,255))
    cv2.putText(frame,pin,(int(w*0.1),int(h*0.16)),cv2.FONT_HERSHEY_SIMPLEX,0.8,(255,255,255))
    cv2.imshow("img",frame)
    cv2.imshow("thres",thres)
    if cv2.waitKey(1)==27:
        break;




cap.release()
cv2.destroyAllWindows()