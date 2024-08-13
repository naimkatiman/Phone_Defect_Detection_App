import unittest
import tensorflow as tf
from src.model.train_model import create_model

class TestTrainModel(unittest.TestCase):
    def test_create_model(self):
        model = create_model()
        
        # Check if the model has the correct number of layers
        self.assertEqual(len(model.layers), 8)
        
        # Check if the output shape is correct (3 classes)
        self.assertEqual(model.output_shape, (None, 3))

    def test_model_compile(self):
        model = create_model()
        model.compile(optimizer='adam',
                      loss='categorical_crossentropy',
                      metrics=['accuracy'])
        
        # Check if the model is compiled
        self.assertTrue(model.optimizer)
        self.assertTrue(model.loss)
        self.assertTrue(model.metrics)

if __name__ == '__main__':
    unittest.main()