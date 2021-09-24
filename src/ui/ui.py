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

def display_gui(input_img, neighbors):
    """
    Metodi piirtää grafiikan näytölle.
    """
    root = tk.Tk()
    imgs = []
    array = input_img[0]
    input_image = turn_array_to_image(array)
    width = 300
    height = 300
    i = 0
    while i < 7:
        array = neighbors[i][2]
        img = turn_array_to_image(array)
        imgs.append(img)
        i += 1
    canvas = tk.Canvas(root, width=width, height=height)
    canvas.pack()
    i = 0
    x = 40
    y = 20
    while i < len(imgs):
        canvas.create_image(x, y, anchor="nw", image=imgs[i])
        text = tk.Label(text=neighbors[i][1])
        text.place(x=x+10,y=y+30)
        x += 30
        i += 1
    canvas.create_image(width/2-28/2, height/2-28/2, anchor="nw", image=input_image)
    root.after(3000, lambda:root.destroy())
    root.mainloop()
    