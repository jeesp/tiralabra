import tkinter as tk
import numpy as np
import time

def turn_array_to_image(image: np.ndarray):
    """
    Metodi muuttaa arrayn kuvaksi.
    """
    height, width = image.shape
    data = f'P5 {width} {height} 255 '.encode() + image.astype(np.uint8).tobytes()
    return tk.PhotoImage(width=width, height=height, data=data, format='PPM')

def display_gui(input_img, neighbors, guess):
    """
    Metodi piirtää grafiikan näytölle.
    """
    root = tk.Tk()
    imgs = []
    array = input_img[0]
    zoom = 3
    input_img_size = 28*zoom
    input_image = turn_array_to_image(array)
    input_image = input_image.zoom(zoom)
    width = 300
    height = 300
    root.geometry('600x300')
    frame = tk.Frame(root)
    frame.grid()
    i = 0
    while i < 7:
        array = neighbors[i][2]
        img = turn_array_to_image(array)
        imgs.append(img)
        i += 1
    canvas = tk.Canvas(root, width=width, height=height)
    canvas.grid(row=0,column=0)
    i = 0
    x = 40
    y = 20
    while i < len(imgs):
        canvas.create_image(x, y, anchor="nw", image=imgs[i])
        add_text(neighbors[i][1], x+10, y+30)
        x += 30
        i += 1
    canvas.create_image(width/2-input_img_size/2, height/2, anchor="nw", image=input_image)
    add_text(input_img[1], width/2-input_img_size/2 + input_img_size/2-5, height/2 
             + input_img_size + 20)
    add_text("Veikkaus: " + str(guess[0]) + ", varmuus: " + str(int(round(guess[1]/7*100, 0))) 
             + "%", 5, height/2 + input_img_size + 40)
    #root.after(5000, lambda:root.destroy())
    root.mainloop()

def add_text(text, x, y):
    """
    Apumetodi tekstin lisäämiseksi ohjelmaan.
    """
    text = tk.Label(text=text)
    text.place(x=x,y=y)