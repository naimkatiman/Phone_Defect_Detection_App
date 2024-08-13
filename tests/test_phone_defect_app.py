import unittest
import os
import tensorflow as tf
from src.app.phone_defect_app import PhoneDefectApp

class MockTk:
    def __init__(self):
        self.title_text = ""
        self.geometry_text = ""

    def title(self, text):
        self.title_text = text

    def geometry(self, text):
        self.geometry_text = text

class TestPhoneDefectApp(unittest.TestCase):
    def setUp(self):
        self.mock_tk = MockTk()
        self.app = PhoneDefectApp(self.mock_tk)

    def test_app_initialization(self):
        self.assertEqual(self.mock_tk.title_text, "Phone Defect Detection")
        self.assertEqual(self.mock_tk.geometry_text, "600x400")

    def test_model_loading(self):
        self.assertIsInstance(self.app.model, tf.keras.Model)

    def test_class_names(self):
        expected_classes = ['Oil', 'Screen', 'Stain']
        self.assertEqual(self.app.class_names, expected_classes)

if __name__ == '__main__':
    unittest.main()