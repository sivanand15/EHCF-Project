from tkinter import *
from tkinter import ttk
from PIL import ImageTk
from tkinter import filedialog
import cv2
import numpy as np
import time
import os
import tkinter as tk 
import moviepy
from PIL import Image
from moviepy.editor import *
import cv2
import moviepy.editor as mp
import re
import math
from PIL import Image

main = Tk()
main.configure(background='black')
main.title("Video Steganography")
main.geometry('950x700')
global og_path 
og_path = StringVar()
og_path.get()
global video_frames_path
video_frames_path= StringVar()
video_frames_path.get()
def Browse_og_file():
    og_path_a = filedialog.askopenfilename(initialdir="/", title="Select A video")
    og_path.set(og_path_a)
    og_path.get()

def get_frames():
    """Returns all frames in the video object"""
    Browse_og_file()
    video_object = VideoFileClip(og_path.get())
    directory =  og_path.get() + "output\\" +'_frames\\'
    if not os.path.isdir(directory):
        os.makedirs(directory)
    for index, frame in enumerate(video_object.iter_frames()):
        img = Image.fromarray(frame, 'RGB')
        img.save(f'{directory}{index}.png')

def get_audio():
    """Returns the audio track only of a video clip"""
    video_path = filedialog.askopenfilename(initialdir="/", title="Select A video")
    my_clip = mp.VideoFileClip(video_path)

    my_clip.audio.write_audiofile(video_path+"my_result.mp3")
    
def back_3():
    global txt1
    global txt2
    frame_1_back2 = LabelFrame(main, bg='black', fg='#2fa84d')
    frame_1_back2.place(x=0, y=0, height=100, width=1280)

    initial_label =  Label(frame_1_back2,text="Hide data in frames",fg='white', bg="black", font=("Gentona", 40, "bold"))
    initial_label.place(x=230,y=10)
     
    frame_2_back2 = LabelFrame(main,bg='black', fg='#2fa84d')
    frame_2_back2.place(x=0, y=100, height=400, width=1280)

    button_6 = Button(frame_2_back2,text="BROWSE",command=Browse_hide_file)
    button_6.place(x=150,y=150)

    text_name = Label(frame_2_back2,text="Choose a file to hide",font=5)
    text_name.place(x=150,y=100)

    
    text_name = Label(frame_2_back2,text="Choose frames location",font=5)
    text_name.place(x=750,y=100)
    button_6 = Button(frame_2_back2,text="BROWSE",command=Browse_frames_file1)
    button_6.place(x=750,y=150)
    back_button=Button(frame_2_back2,text="back",command=main_page)
    back_button.place(x=1000,y=360)

    text_1 =Label(frame_2_back2,text="Start Frame",font=5)
    text_2 =Label(frame_2_back2,text="End Frame",font=5)
    text_1.place(x=390,y=100)
    text_2.place(x=390,y=150)
    data1 = Text(frame_2_back2,width=20,height=2, bg='black', fg='lime')
    data1.place(x=550,y=100)
    txt1 = data1.get("1.0",'end-1c')
    #txt1=int(txt1a)
    
    data2= Text(frame_2_back2, width=20,height=2, bg='black', fg='lime')
    data2.place(x=550,y=150)
    txt2= data2.get("1.0",'end-1c')
    #txt2=int(txt2a)

    print("txt1 in func:", txt1)
    print("txt2 in func:", txt2)

    button_en = Button(frame_2_back2,text="Hide", command=encode)
    button_en.place(x=650,y=200)

    
    back_button=Button(frame_2_back2,text="back",command=main_page)
    back_button.place(x=800,y=360)

def Browse_hide_file():
    global filename
    filename = filedialog.askopenfilename(initialdir="/", title="Select text file")
    #filename.set(file_to_hidea)
    #filename.get()
    print("file_name:", filename)
    
def Browse_frames_file1():
    global frame_loc
    frame_loc= filedialog.askdirectory(initialdir="/", title="Select frame folder")
    #video_frames_path.set(video_frames_path_a)
    #frame_loc.get()
    print("file_name:", frame_loc)
    
def Browse_frames_file():
    video_frames_path_a = filedialog.askdirectory(initialdir="/", title="Select A video")
    video_frames_path.set(video_frames_path_a)
    video_frames_path.get()

def main_page():
    frame_1 = LabelFrame(main,bg='black',height=100,width=1280)
    frame_1.place(x=0,y=0)

    label1 = Label(frame_1, text="Video Steganography", fg='white', bg="black", font=("Gentona", 40, "bold"))
    label1.place(x=200, y=10)

    frame_2 = LabelFrame(main,bg='black',height=300,width=1280)
    frame_2.place(x=0,y=100)


    footer = Label(frame_2, text="In Video steganography, a message is embedded into frames and audio by altering the ",font=("Helvetica", 15, "bold"), bg='black', fg='lime')
    footer1 = Label(frame_2, text="values of some pixels, which are chosen by an encryption algorithm. The recipient of the",font=("Helvetica", 15, "bold"), bg='black', fg='lime')
    footer2 = Label(frame_2, text="image must be aware of the same algorithm in order to known which pixels he or she",font=("Helvetica",  15,"bold"), bg='black', fg='lime')
    footer3 = Label(frame_2, text="must select to extract the message.", font=("Helvetica", 15, "bold"), bg='black',fg='lime')

    footer.place(x=80, y=10)
    footer1.place(x=100, y=45)
    footer2.place(x=80, y=75)
    footer3.place(x=295, y=105)


    frame_3 = LabelFrame(main,bg='black')
    frame_3.place(x=0,y=300)

    button_1 = Button(frame_3, text='Split Video into frames', bg='#2fa84d', fg='white',padx=2,pady=2, command=get_frames, height=2, width=50,font=2)
    button_1.grid(row = 1, column = 1,  )

    button_2 = Button(frame_3, text='Extract audio', bg='#2fa84d', fg='white', height=2,padx=2,pady=2,command=get_audio, width=50,font=2)
    button_2.grid(row = 2, column = 1,  )

    button_3 = Button(frame_3, text='Hide data in frames', bg='#2fa84d', fg='white', padx=2,pady=2, command=back_3,height=2, width=55,font=2)
    button_3.grid(row = 1, column = 2,  )

    button_6_1 = Button(frame_3, text='Retreive Data from frames', bg='#2fa84d', fg='white',padx=2,pady=2, height=2, width=55,font=2)
    button_6_1.grid(row = 2, column = 2,  )


def generateData(data):
    newdata = []
    for i in data: # list of binary codes of given data
        newdata.append(format(ord(i), '08b'))
    return newdata
 
# Pixels modified according to encoding data in generateData
def modifyPixel(pixel, data):
    datalist = generateData(data)
    lengthofdata = len(datalist)
    imagedata = iter(pixel)
    for i in range(lengthofdata):
        # Extracts 3 pixels at a time
        pixel = [value for value in imagedata.__next__()[:3] + imagedata.__next__()[:3] + imagedata.__next__()[:3]]
        # Pixel value should be made odd for 1 and even for 0
        for j in range(0, 8):
            if (datalist[i][j] == '0' and pixel[j]% 2 != 0):
                pixel[j] -= 1
            elif (datalist[i][j] == '1' and pixel[j] % 2 == 0):
                if(pixel[j] != 0):
                    pixel[j] -= 1
                else:
                    pixel[j] += 1
        # Eighth pixel of every set tells whether to stop ot read further. 0 means keep reading; 1 means thec message is over.
        if (i == lengthofdata - 1):
            if (pixel[-1] % 2 == 0):
                if(pixel[-1] != 0):
                    pixel[-1] -= 1
                else:
                    pixel[-1] += 1
        else:
            if (pixel[-1] % 2 != 0):
                pixel[-1] -= 1
        pixel = tuple(pixel)
        yield pixel[0:3]
        yield pixel[3:6]
        yield pixel[6:9]

def encoder(newimage, data):
    w = newimage.size[0]
    (x, y) = (0, 0)
 
    for pixel in modifyPixel(newimage.getdata(), data):
 
        # Putting modified pixels in the new image
        newimage.putpixel((x, y), pixel)
        if (x == w - 1):
            x = 0
            y += 1
        else:
            x += 1
 
# Improved Encoding Function
# Instead of performing Steganography on all the frames, the function will now instead perform Steganography on selected range of frames
def encode():
    start = 0
    end = 100
    total_frame = end - start + 1
    try:
        with open(filename) as fileinput: # Store Data to be Encoded
            filedata = fileinput.read()
    except FileNotFoundError:
        print("\nFile to hide not found! Exiting...")
        quit()
    datapoints = math.ceil(len(filedata) / total_frame) # Data Distribution per Frame
    counter = start
    print("Performing Steganography...")
    for convnum in range(0, len(filedata), datapoints):
        numbering = frame_loc + "\\" + str(counter) + ".png"
        print(numbering)
        encodetext = filedata[convnum:convnum+datapoints] # Copy Distributed Data into Variable
        try:
            image = Image.open(numbering, 'r') # Parameter has to be r, otherwise ValueError will occur (https://pillow.readthedocs.io/en/stable/reference/Image.html)
        except FileNotFoundError:
            print("\n%d.png not found! Exiting..." % counter)
            quit()
        newimage = image.copy() # New Variable to Store Hiddend Data
        encoder(newimage, encodetext) # Steganography
        new_img_name = numbering # Frame Number
        newimage.save(new_img_name) # Save as New Frame
        counter += 1
    print("Complete!\n")
    
def back_6():
    global txt3
    global txt4
    frame_1_back2 = LabelFrame(main, bg='black', fg='#2fa84d')
    frame_1_back2.place(x=0, y=0, height=100, width=1280)

    initial_label =  Label(frame_1_back2,text="Retreive data from frames",fg='white', bg="black", font=("Gentona", 40, "bold"))
    initial_label.place(x=200,y=10)

    frame_2_back2 = LabelFrame(main,bg='black', fg='#2fa84d')
    frame_2_back2.place(x=0, y=100, height=400, width=1280)

    button_6 = Button(frame_2_back2,text="BROWSE",command=Browse_frames_file)
    button_6.place(x=250,y=150)


    button_6 = Button(frame_2_back2,text="Decode",command=decoder)
    button_6.place(x=850,y=150)

    text_name = Label(frame_2_back2,text="Choose a video frame folder",font=8)
    text_name.place(x=250,y=100)

    text_1 =Label(frame_2_back2,text="Start Frame",font=5)
    text_2 =Label(frame_2_back2,text="End Frame",font=5)
    text_1.place(x=500,y=100)
    text_2.place(x=500,y=150)
    txt3 = Text(frame_2_back2, wrap=WORD,width=20,height=2, bg='black', fg='white')
    txt3.place(x=650,y=100)
    txt4 = Text(frame_2_back2, wrap=WORD, width=20,height=2, bg='black', fg='white')
    txt4.place(x=650,y=150)
    

    back_button=Button(frame_2_back2,text="back",command=main_page)
    back_button.place(x=800,y=360)
    
def Browse_frames_file():
    global video_frames_path
    video_frames_path = filedialog.askdirectory(initialdir="/", title="Select A video")
    #video_frames_path.set(video_frames_path_a)
    print("video_decode_frame:",video_frames_path)

def decoder():
    #txt5=int(txt3)
    #txt6=int(txt4)
    decodedtextfile = open('output\decoded1_frame.txt', 'a')
    decodedtextfile.write('Decoded Text:\n')
    
    #for convnum in range(txt5,txt6):
    for convnum in range(1,200):
        try:
            decodedtextfile.write(decode(convnum))
            print("Data found in Frame %d" % convnum)
        except StopIteration:
            print("No data found in Frame %d" % convnum)
    decodedtextfile.close()

def decode(number):
    data = ''
    numbering = str(number)
    #decoder_numbering = video_frames_path.get() + "/" + number + ".png"
    decoder_numbering = video_frames_path + "\\" + numbering + ".png"
    image = Image.open(decoder_numbering, 'r')
    imagedata = iter(image.getdata())
    while (True):
        pixels = [value for value in imagedata.__next__()[:3] + imagedata.__next__()[:3] + imagedata.__next__()[:3]]
        # string of binary data
        binstr = ''
        for i in pixels[:8]:
            if (i % 2 == 0):
                binstr += '0'
            else:
                binstr += '1'
        if re.match("[ -~]", chr(int(binstr,2))) is not None: # only decode printable data
            data += chr(int(binstr, 2))
        if (pixels[-1] % 2 != 0):
            return data

    
    #button_7 = Button(frame_3,text='combine audio and video', bg='#2fa84d', fg='white',padx=2,pady=2, command=back_7, height=2, width=40,font=2)
    #button_7.grid(row = 2, column = 1,  )

# video_filename = tk.StringVar()

# video_label = tk.Label(main, text="Video File/Frame Path: ")
 
# video_filename_widget = tk.Entry(main, textvariable=video_filename)

# audio_filename = tk.StringVar()

# audio_label = tk.Label(main, text="Audio File: ")
 
# audio_filename_widget = tk.Entry(main, textvariable=audio_filename, state=tk.DISABLED)

# og_filename = tk.StringVar()

# og_label = tk.Label(main, text="Original Video File: ")

 
# og_filename_widget = tk.Entry(main, textvariable=og_filename, state=tk.DISABLED)


# var = tk.IntVar()



frame_1 = LabelFrame(main,bg='black',height=100,width=1280)
frame_1.place(x=0,y=0)

label1 = Label(frame_1, text="Video Steganography", fg='white', bg="black", font=("Gentona", 40, "bold"))
label1.place(x=200, y=10)

frame_2 = LabelFrame(main,bg='black',height=300,width=1280)
frame_2.place(x=0,y=100)


footer = Label(frame_2, text="In Video steganography, a message is embedded into frames and audio by altering the ",font=("Helvetica", 15, "bold"), bg='black', fg='lime')
footer1 = Label(frame_2, text="values of some pixels, which are chosen by an encryption algorithm. The recipient of the",font=("Helvetica", 15, "bold"), bg='black', fg='lime')
footer2 = Label(frame_2, text="image must be aware of the same algorithm in order to known which pixels he or she",font=("Helvetica",  15,"bold"), bg='black', fg='lime')
footer3 = Label(frame_2, text="must select to extract the message.", font=("Helvetica", 15, "bold"), bg='black',fg='lime')

footer.place(x=80, y=10)
footer1.place(x=100, y=45)
footer2.place(x=80, y=75)
footer3.place(x=295, y=105)


frame_3 = LabelFrame(main,bg='black')
frame_3.place(x=0,y=300)

button_1 = Button(frame_3, text='Split Video into frames', bg='#2fa84d', fg='white',padx=2,pady=2, command=get_frames, height=2, width=50,font=2)
button_1.grid(row = 1, column = 1  )

button_2 = Button(frame_3, text='Extract audio', bg='#2fa84d', fg='white', height=2,padx=2,pady=2,command=get_audio, width=50,font=2)
button_2.grid(row = 2, column = 1,  )

button_3 = Button(frame_3, text='Hide data in frames', bg='#2fa84d', fg='white', padx=2,pady=2, command=back_3,height=2, width=55,font=2)
button_3.grid(row = 1, column = 2,  )

'''button_4 = Button(frame_3, text='Hide Data in audio', bg='#2fa84d', fg='white', command=back_4,padx=2,pady=2, height=2, width=40,font=2)
button_4.grid(row = 2, column = 1,  )'''

'''button_5 = Button(frame_3, text='Retreive Data from audio', bg='#2fa84d', fg='white',padx=2,pady=2,command=back_5 ,height=2, width=40,font=2)
button_5.grid(row = 2, column = 1,  )'''


button_6_1 = Button(frame_3, text='Retreive Data from frames', bg='#2fa84d', fg='white',padx=2,pady=2, command=back_6, height=2, width=55,font=2)
button_6_1.grid(row = 2, column = 2,  )



#button_7 = Button(frame_3,text='combine audio and video', bg='#2fa84d', fg='white',padx=2,pady=2, command=back_7, height=2, width=40,font=2)
#button_7.grid(row = 2, column = 1,  )






main.mainloop()