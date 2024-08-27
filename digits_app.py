#importing libraries 
from keras.models import load_model
from tkinter import *
import tkinter as tk
import win32gui
from PIL import ImageGrab, Image
import numpy as np

# Load the pre-trained model
model = load_model("CNN_model_pretrained.h5")

def predict_digit(img):
    # Resize image to 28x28 pixels
    img = img.resize((28, 28))
    # Convert RGB to grayscale
    img = img.convert('L')
    img = np.array(img)
    # Reshaping for model normalization
    img = img.reshape(1, 28, 28, 1)
    img = img / 255
    
    # Predicting the class
    res = model.predict([img])[0]
    return np.argmax(res)

class App(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.x = self.y = None
        # Creating elements
        self.canvas = tk.Canvas(self, width=280, height=280, bg="black", cursor="cross")
        self.label = tk.Label(self, text="Analyzing..", font=("Helvetica", 18), bg="white")
        self.classify_btn = tk.Button(self, text="Search", command=self.classify_handwriting)
        self.button_clear = tk.Button(self, text="Clear", command=self.clear_all)
        # Grid structure
        self.canvas.grid(row=0, column=0, pady=2, sticky=W)
        self.label.grid(row=0, column=1, pady=2, padx=2)
        self.classify_btn.grid(row=1, column=1, pady=2, padx=2)
        self.button_clear.grid(row=1, column=0, pady=2)
        # Bind events
        self.canvas.bind("<B1-Motion>", self.draw_lines)
        self.canvas.bind("<ButtonPress-1>", self.start_draw)
        self.canvas.bind("<ButtonRelease-1>", self.end_draw)
        
    def clear_all(self):
        self.canvas.delete("all")
        self.label.configure(text="Analyzing...")
        
    def classify_handwriting(self):
        self.canvas.update()
        # Correct the region capture to match the canvas coordinates
        x = self.canvas.winfo_rootx()
        y = self.canvas.winfo_rooty()
        x1 = x + self.canvas.winfo_width()
        y1 = y + self.canvas.winfo_height()
        im = ImageGrab.grab(bbox=(x, y, x1, y1))

        # Predict the digit
        digit = predict_digit(im)
        
        self.label.configure(text=str(digit))
        
    def start_draw(self, event):
        self.x = event.x
        self.y = event.y
        
    def draw_lines(self, event):
        if self.x and self.y:
            self.canvas.create_line(self.x, self.y, event.x, event.y, fill='white', width=8)
        self.x = event.x
        self.y = event.y
        
    def end_draw(self, event):
        self.x = None
        self.y = None

# Run the application
app = App()
mainloop()
