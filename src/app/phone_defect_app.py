import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk
import numpy as np
import tensorflow as tf
import os

class PhoneDefectApp:
    def __init__(self, master, model_path=None):
        self.master = master
        master.title("Phone Defect Detection")
        master.geometry("600x400")

        if model_path is None:
            model_path = os.path.join(os.path.dirname(__file__), '..', '..', 'models', 'phone_defect_model.h5')

        if os.path.exists(model_path):
            self.model = tf.keras.models.load_model(model_path)
        else:
            print(f"Warning: Model file not found at {model_path}. Functionality will be limited.")
            self.model = None

        self.class_names = ['Oil', 'Screen', 'Stain']

        self.create_widgets()

    # ... rest of the class implementation ...

if __name__ == "__main__":
    root = tk.Tk()
    app = PhoneDefectApp(root)
    root.mainloop()