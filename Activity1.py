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
    elif filter_type=="increase red":
        fimg[:,:,2]=cv2.add(fimg[:,:,2] , 50)
    elif filter_type=="decrease blue":
        fimg[:,:,0]=cv2.subtract(fimg[:,:,0] , 50)
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
    print("i for increase red intensity")
    print("d for decrease blue intensity")
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
        elif key==ord("i"):
            filter_type="increase red"
        elif key==ord("d"):
            filter_type="decrease blue"    
        elif key==ord("q"):
            print("Exiting...")
            break
        else:
            print("Invalid key!! , press valid key")
    cv2.destroyAllWindows()
          
    
