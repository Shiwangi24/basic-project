from itertools import cycle
from PIL import Image, ImageTk
import time
import tkinter as tk

root=tk.Tk()
root.title("Image slideshow viewer")

#list of image paths (only image files)

image_paths = [
    r'c:\Users\pc\Pictures\Saved Pictures\download (1).jpg',
    r'c:\Users\pc\Pictures\Saved Pictures\butterfly.jpg',
    r'c:\Users\pc\Pictures\Saved Pictures\dream.jpg',
    r'c:\Users\pc\Pictures\Saved Pictures\dream2.jpg',
    r'c:\Users\pc\Pictures\Saved Pictures\ganesha.jpg',
    r'c:\Users\pc\Pictures\Saved Pictures\images (1).jpg',
    r'c:\Users\pc\Pictures\Saved Pictures\images (2).jpg',
    r'c:\Users\pc\Pictures\Saved Pictures\love.jpg',
    r'c:\Users\pc\Pictures\Saved Pictures\images.jpg',
    
]

#resize the image to 1080x1080
image_size=(720, 720)
images=[Image.open(path). resize(image_size) for path in image_paths]
photo_images=[ImageTk.PhotoImage(image) for image in images]

label = tk.Label(root)
label.pack()

def update_image():
    photo_image = next(slideshow)
    label.config(image = photo_image)
    label.update()
    root.after(3000, update_image)

slideshow = cycle(photo_images)

def start_slideshow():
     update_image()

play_button = tk.Button(root, text= "play slideshow", command=start_slideshow)
play_button.pack()

root.mainloop()





