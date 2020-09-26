import cv2
import numpy as np
import random
import pandas as pd


text="Please raise your hand..."


### PREPARE BINARY IMAGE
def thresold(img):
    img=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
    # img=cv2.GaussianBlur(img,(3,3),0)
    img=cv2.inRange(img,np.array([4,80,0]),np.array([70,255,255]))
    # img=cv2.morphologyEx(img,cv2.MORPH_CLOSE,np.ones((3,3)),iterations=1)
    # img=cv2.GaussianBlur(img,(3,3),0)
    # _,img=cv2.threshold(img,100,255,cv2.THRESH_BINARY)
    return img

def timer(img,i):
    radius = 8
    axes = (radius, radius)
    angle = 0;
    try:
        h,w=img.shape   #for binary image
    except:
        h,w,_=img.shape     # for colored imgae
    center = (w-20, 20)
    color = (255,0,0)
    cv2.ellipse(img, center, axes, angle, 0, i, color, 2)
    return img

def test(img):
    n = random.random()
    return int(n*10)

def show_result(cap,pin):
    # print(pin)
    r,d_name,s_name=data(pin)
    # r,d_name,s_name=data("274001")
    while cap.isOpened():
        _,frame=cap.read()
        frame = cv2.flip(frame, 1)
        w, h, _ = frame.shape
        cv2.putText(frame, text, (int(w * 0.1), int(h * 0.1)), cv2.FONT_HERSHEY_SIMPLEX, 0.8,(255, 255, 255))
        cv2.putText(frame, pin, (int(w * 0.1), int(h * 0.16)), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 255, 255))
        if r==1:
            dd_name="District name : "+d_name
            ss_name="State name : "+s_name
            cv2.putText(frame, "Right pincode", (int(w * 0.1), int(h * 0.22)), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0))
            cv2.putText(frame, dd_name, (int(w * 0.1), int(h * 0.28)), cv2.FONT_HERSHEY_SIMPLEX, 0.8,(255, 255, 255))
            cv2.putText(frame, ss_name, (int(w * 0.1), int(h * 0.34)), cv2.FONT_HERSHEY_SIMPLEX, 0.8,(255, 255, 255))
        else:
            cv2.putText(frame, "Wrong Pincode.", (int(w * 0.1), int(h * 0.22)), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 0,255))
            cv2.putText(frame, "try again...", (int(w * 0.1), int(h * 0.28)), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 0,255))
            # cv2.waitKey(1000)

        # cv2.imshow("thres",frame)
        cv2.destroyWindow("thres")
        cv2.imshow("img",frame)
        if cv2.waitKey(1)== ord("q"):
            break


def data(pin):
    p=int(pin)
    df = pd.read_csv('pin_code_list.csv')
    h = df[df.pincode == p].reset_index()
    p = h[h.index == 0]
    try:
        d_name = p['Districtname'][0]
        s_name = p['statename'][0]
        return 1,d_name,s_name
    except:
        return 0,"no","no"
