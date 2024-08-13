import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk
import numpy as np
import tensorflow as tf
import os

class PhoneDefectApp:
    def __init__(self, master):
        self.master = master
        master.title("Phone Defect Detection")
        master.geometry("600x400")

        model_path = os.path.join(os.path.dirname(__file__), '..', '..', 'models', 'phone_defect_model.h5')
        self.model = tf.keras.models.load_model(model_path)
        self.class_names = ['Oil', 'Screen', 'Stain']

        self.create_widgets()

    def create_widgets(self):
        self.canvas = tk.Canvas(self.master, width=300, height=300)
        self.canvas.pack()

        self.select_button = tk.Button(self.master, text="Select Image", command=self.select_image)
        self.select_button.pack()

        self.detect_button = tk.Button(self.master, text="Detect Defect", command=self.detect_defect)
        self.detect_button.pack()

        self.result_label = tk.Label(self.master, text="")
        self.result_label.pack()

    def select_image(self):
        file_path = filedialog.askopenfilename()
        if file_path:
            self.image = Image.open(file_path)
            self.image = self.image.resize((300, 300))
            self.photo = ImageTk.PhotoImage(self.image)
            self.canvas.create_image(0, 0, anchor=tk.NW, image=self.photo)
            self.result_label.config(text="")

    def detect_defect(self):
        if not hasattr(self, 'image'):
            messagebox.showerror("Error", "Please select an image first.")
            return

        img_array = tf.keras.preprocessing.image.img_to_array(self.image)
        img_array = tf.image.resize(img_array, (224, 224))
        img_array = tf.expand_dims(img_array, 0)  # Create batch axis

        predictions = self.model.predict(img_array)
        score = tf.nn.softmax(predictions[0])
        predicted_class = self.class_names[np.argmax(score)]
        confidence = 100 * np.max(score)

        result_text = f"Detected defect: {predicted_class} with {confidence:.2f}% confidence"
        self.result_label.config(text=result_text)

if __name__ == "__main__":
    root = tk.Tk()
    app = PhoneDefectApp(root)
    root.mainloop()