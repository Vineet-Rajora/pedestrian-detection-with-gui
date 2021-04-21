from __future__ import print_function
from tkinter import *
import tkinter as tk 
from tkinter import Message, Text
from imutils.object_detection import non_max_suppression
from imutils import paths
import numpy as np
import argparse
import imutils
import cv2

def testing_images():
      images=(txt.get())
      if images:
            ap = argparse.ArgumentParser()
            ap.add_argument("-i", "--images", type=str,default=txt.get(),
            help="path to images directory")
            args = vars(ap.parse_args())
            
            # initialize the HOG descriptor/person detector
            hog = cv2.HOGDescriptor()
            hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())
            
            # loop over the image paths

            for imagePath in paths.list_images(args["images"]):
                    
                    # load the image and resize it to (1) reduce detection time
                    # and (2) improve detection accuracy
                    
                    image = cv2.imread(imagePath)
                    image = imutils.resize(image, width=min(400, image.shape[1]))
                    orig = image.copy()
                    
                    # detect people in the image
                    
                    (rects, weights) = hog.detectMultiScale(image, winStride=(4, 4),
                            padding=(8, 8), scale=1.05)
                    
                    # draw the original bounding boxes
                    
                    for (x, y, w, h) in rects:
                            cv2.rectangle(orig, (x, y), (x + w, y + h), (0, 0, 255), 2)
                            
                    # apply non-maxima suppression to the bounding boxes using a
                    # fairly large overlap threshold to try to maintain overlapping
                    # boxes that are still people
                    
                    rects = np.array([[x, y, x + w, y + h] for (x, y, w, h) in rects])
                    pick = non_max_suppression(rects, probs=None, overlapThresh=0.65)
                    
                    # draw the final bounding boxes
                    
                    for (xA, yA, xB, yB) in pick:
                            cv2.rectangle(image, (xA, yA), (xB, yB), (0, 255, 0), 2)
                            
                    # show some information on the number of bounding boxes
                    
                    filename = imagePath[imagePath.rfind("/") + 1:]
                    print("[INFO] {}: {} original boxes, {} after suppression".format(
                            filename, len(rects), len(pick)))
                    
                    # show the output images
                    cv2.imshow("After NMS", image)
                    cv2.waitKey(0)

      else:
            print("Provide the correct path for input images")

def VCR_TECHDOT():
        print("IF YOU LIKE THE CONTENT THEN LIKE THE VIDEO")
        print("IF YOU'RE NOT SUBSCRIBED MY CHANNEL THEN WHY ARE YOU WAITING FOR?? \n JUST HIT THAT SUBSCRIBE BUTTON")
        print("IF YOU THINK THIS IS GOING TO BE HELPFUL TO ANYONE THEN SHARE WITH THEM.\n\n")

window = tk.Tk()
photo=PhotoImage(file="vcr_techdot.png")
canvas = tk.Canvas(window, height=500, width=700,bg='black')
canvas.pack()  
window.title("Pedestrian Detection Project Window") 
window.configure(background ='black') 
window.grid_rowconfigure(1, weight = 1) 
window.grid_columnconfigure(1, weight = 1)

message = tk.Label( window, text ="PEDESTRIAN-DETECTION\n(Using OpenCV & Python)",
                    bg ="black", fg = "red", width = 20,  height = 1, font = ('arial', 30, 'bold'))        
message.place(relx = 0.5, rely = 0,relwidth=.9,relheight=.3, anchor='n')

frame = tk.Frame(window, bg='yellow', bd=10)
frame.place(relx=0.5, rely=0.32, relwidth=0.85, relheight=0.1, anchor='n')

message2 = tk.Label( frame, text ="Created by VCR TECHDOT",
                    bg='black', fg = "yellow", font = ('arial', 20, 'bold'))        
message2.place(relx = 0.5, rely = 0,relwidth=1,relheight=1, anchor='n')

lbl = tk.Label(window, text = "Input image folder",  
width = 20, height = 2, fg ="blue",  
bg = "yellow", font = ('Arial', 15, ' bold ') )  
lbl.place(relx=.15, rely = .5) 
  
txt = tk.Entry(window,  
width = 20, bg ="yellow",  
fg ="red", font = ('Arial', 15, ' bold ')) 
txt.place(relx=.57, rely=.52)

testImg = tk.Button(window, text ="DETECT\nPEDESTRIAN",  
command = testing_images, fg ="Red", bg ="blue",  
width = 15, height = 4, activebackground = "Red",  
font =('fixedsys', 16, ' bold ')) 
testImg.place(relx=.25, rely=.7)

TECHDOT = tk.Button(window,  command = VCR_TECHDOT, bg ="blue",  
image=photo,width=60,height=70, activebackground = "Red",) 
TECHDOT.place(relx=.88, rely=.83)

quitWindow = tk.Button(window, text ="QUIT",  
command = window.destroy, fg ="red", bg ="blue",  
width = 15, height = 4, activebackground = "Red",  
font =('fixedsys', 16, ' bold ')) 
quitWindow.place(relx=.6, rely=.7)
  
