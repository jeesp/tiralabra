from tkinter import *
import numpy as np
import time

width = 300
height = 300
zoom = 3
input_img_size = 28*zoom
photos = []

def turn_array_to_image(image: np.ndarray):
    """
    Metodi muuttaa arrayn kuvaksi.
    """
    image_height, image_width = image.shape
    data = f'P5 {image_width} {image_height} 255 '.encode() + image.astype(np.uint8).tobytes()
    return PhotoImage(width=image_width, height=image_height, data=data, format='PPM')

def display_gui(app):
    """
    Metodi piirtää grafiikan näytölle.
    """
    root = Tk()
    root.geometry('600x300')
    frame = Frame(root)
    frame.grid()
    canvas_left = Canvas(root, width=width, height=height)
    canvas_left.grid(row=0,column=0)
    
    #root.after(5000, lambda:root.destroy())
    canvas_right = Canvas(root, width=width, height=height, background='green')
    canvas_right.grid(row=0,column=1)
    sample_imgs = create_images(app.test_samples)
    i = 0
    j = 0
    while j < 3:
        k = 0
        while k < 3:
            Button(canvas_right, anchor="nw", image=sample_imgs[i], command=lambda i=i: process_clicked_image(app, root, canvas_left, i)).grid(row=j, column = k)
            k += 1
            i += 1
        j += 1
    root.mainloop()
def create_left_side(app, root, canvas_left, imgs, input_image):

    i = 0
    x = 40
    y = 20
    while i < len(imgs):
        label = Label(image=imgs[i])
        canvas_left.create_image(x, y, anchor="nw", image=imgs[i])
        add_text(app.nearest_neighbors[i][1], x+10, y+30)
        x += 30
        i += 1
    canvas_left.create_image(width/2-input_img_size/2, height/2, anchor="nw", image=input_image)
    add_text(app.input_image[1], width/2-input_img_size/2 + input_img_size/2-5, height/2 
             + input_img_size + 20)
    if app.input_image[1] == app.guess[0]:
        add_text("Veikkaus: " + str(app.guess[0]) + ", varmuus: " + str(int(round(app.guess[1]/7*100, 0)))
                 + "%", 5, height/2 + input_img_size + 40)
    else:
        add_text("Veikkaus: " + str(app.guess[0]), 5, height/2 + input_img_size + 40)
    canvas_left.update()
def process_clicked_image(app, root, canvas_left, i):
    print(i)
    app.input_image = app.test_samples[i]
    app.process_image()
    array = app.test_samples[i][0]
    input_image = turn_array_to_image(array)
    input_image = input_image.zoom(zoom)
    photos.append(input_image)
    imgs = create_images(app.nearest_neighbors)
    create_left_side(app, root, canvas_left, imgs, input_image)
def create_images(arrays):
    images = []
    i = 0
    while i < len(arrays):
        array = arrays[i][0]
        img = turn_array_to_image(array)
        photos.append(img)
        images.append(img)
        i += 1
    return images

def add_text(text, x, y):
    """
    Apumetodi tekstin lisäämiseksi ohjelmaan.
    """
    text = Label(text=text)
    text.place(x=x,y=y)