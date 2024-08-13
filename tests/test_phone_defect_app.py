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
        # Create a dummy model file for testing
        model = tf.keras.Sequential([tf.keras.layers.Dense(1, input_shape=(1,))])
        model.save('dummy_model.keras', save_format='keras')
        self.app = PhoneDefectApp(self.mock_tk, model_path='dummy_model.keras', test_mode=True)

    def tearDown(self):
        # Remove the dummy model file after tests
        if os.path.exists('dummy_model.keras'):
            os.remove('dummy_model.keras')

    def test_app_initialization(self):
        self.assertIsInstance(self.app, PhoneDefectApp)

    def test_model_loading(self):
        self.assertIsInstance(self.app.model, tf.keras.Model)

    def test_class_names(self):
        expected_classes = ['Oil', 'Screen', 'Stain']
        self.assertEqual(self.app.class_names, expected_classes)

if __name__ == '__main__':
    unittest.main()