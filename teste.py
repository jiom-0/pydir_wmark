import cv2
import numpy as np
import os
def wMark(directory,path,path_logo,horiz,vert,scl):
    image = cv2.imread(path)
    oH,oW = image.shape[:2]
    image = np.dstack([image, np.ones((oH,oW), dtype="uint8") * 255])
    lgo_img = cv2.imread(path_logo,cv2.IMREAD_UNCHANGED)
    w = int(lgo_img.shape[1] * scl / 100)
    h = int(lgo_img.shape[0] * scl / 100)
    dim = (w,h)
    lgo = cv2.resize(lgo_img, dim, interpolation = cv2.INTER_AREA)
    lH,lW = lgo.shape[:2]
    ovr = np.zeros((oH,oW,4), dtype="uint8")
    horiz=int(image.shape[0]*horiz/100)
    vert=int(image.shape[0]*vert/100)
    ovr[oH - lH - vert:oH - vert, oW - lW - horiz:oW - horiz] = lgo
    final = image.copy()
    final = cv2.addWeighted(ovr,0.3,final,1.0,0,final)
    cv2.imwrite(directory+'teste.jpg', final)

os.mkdir(os.getcwd()+'/wm')
directory=os.getcwd()+'/wm/'
list_dir=os.listdir()
for x in list_dir:
    wMark(directory,x,'teste.png',50,50,10)