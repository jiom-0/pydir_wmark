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
    horiz=int(image.shape[1]*horiz/100)
    vert=int(image.shape[0]*vert/100)
    ovr[oH - lH - vert:oH - vert, oW - lW - horiz:oW - horiz] = lgo
    final = image.copy()
    final = cv2.addWeighted(ovr,0.4,final,1.0,0,final)
    cv2.imwrite(directory+path, final)


directory=os.getcwd()+'/wm/'
if os.path.exists(directory)==False:
    os.mkdir(os.getcwd()+'/wm')

list_dir=os.listdir()
logo_path='teste.png'
scl=10
horiz=50
vert=50

for x in list_dir:
    if logo_path!=x:
        if '.jpg' in x:
            wMark(directory,x,logo_path,horiz,vert,scl)
        elif '.jpeg' in x:
            wMark(directory,x,logo_path,horiz,vert,scl)
        elif '.png' in x:
            wMark(directory,x,logo_path,horiz,vert,scl)
