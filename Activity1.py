import numpy as np
import cv2

def apply_filter(image,filter_type):
    fimg=image.copy()
    if filter_type=="red":
        fimg[:,:,1]=0 #Green channel to zero
        fimg[:,:,0]=0 #Blue channel to zero
    elif filter_type=="blue":
        fimg[:,:,1]=0 #Green channel to zero
        fimg[:,:,2]=0 #Red channel to zero
    elif filter_type=="green":
        fimg[:,:,0]=0 #Blue channel to zero
        fimg[:,:,2]=0 #Red channel to zero
    elif filter_type=="sobel":
        grayimage=cv2.cvtColor(image , cv2.COLOR_BGR2GRAY)
        sobelx=cv2.Sobel(grayimage, cv2.CV_64F , 1 , 0 , ksize=3)
        sobely=cv2.Sobel(grayimage, cv2.CV_64F , 0 , 1 , ksize=3)
        combine_sobel=cv2.bitwise_or(sobelx.astype("uint8") , sobely.astype("uint8"))
        fimg=cv2.cvtColor(combine_sobel , cv2.COLOR_GRAY2BGR)
    elif filter_type=="canny":
        grayimage=cv2.cvtColor(image , cv2.COLOR_BGR2GRAY)
        edges=cv2.Canny(grayimage , 100, 200)
        fimg=cv2.cvtColor(edges , cv2.COLOR_GRAY2BGR)
    return fimg

    

image_path="example.jpg"
image=cv2.imread(image_path)
if image is None:
    print("Image not found")
else:
    filter_type="orignal"
    print("Press following keys to apply filter")
    print("r for red tint")
    print("b for blue tint")
    print("g for green tint")
    print("s for sobel")
    print("c for canny")
    print("press q for quit")
    while True:
        fimg=apply_filter(image,filter_type)
        cv2.imshow("filtered_image ", fimg )
        key=cv2.waitKey(0)
        if key==ord("r"):
            filter_type="red"   
        elif key==ord("b"):
            filter_type="blue"   
        elif key==ord("g"):
            filter_type="green"  
        elif key==ord("s"):
            filter_type="sobel"
        elif key==ord("c"):
            filter_type="canny"    
        elif key==ord("q"):
            print("Exiting...")
            break
        else:
            print("Invalid key!! , press valid key")
    cv2.destroyAllWindows()
          
    
