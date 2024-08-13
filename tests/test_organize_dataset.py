import unittest
import os
import shutil
from src.data_preparation.organize_dataset import organize_dataset

class TestOrganizeDataset(unittest.TestCase):
    def setUp(self):
        self.test_dir = 'test_data'
        self.source_dir = os.path.join(self.test_dir, 'raw')
        self.target_dir = os.path.join(self.test_dir, 'processed')
        
        # Create test directory structure
        os.makedirs(self.source_dir, exist_ok=True)
        
        # Create dummy files
        open(os.path.join(self.source_dir, 'Oil_001.jpg'), 'w').close()
        open(os.path.join(self.source_dir, 'Scr_001.jpg'), 'w').close()
        open(os.path.join(self.source_dir, 'Stn_001.jpg'), 'w').close()

    def test_organize_dataset(self):
        organize_dataset(self.source_dir, self.target_dir)
        
        # Check if target directories are created
        self.assertTrue(os.path.exists(os.path.join(self.target_dir, 'Oil')))
        self.assertTrue(os.path.exists(os.path.join(self.target_dir, 'Screen')))
        self.assertTrue(os.path.exists(os.path.join(self.target_dir, 'Stain')))
        
        # Check if files are moved to correct directories
        self.assertTrue(os.path.exists(os.path.join(self.target_dir, 'Oil', 'Oil_001.jpg')))
        self.assertTrue(os.path.exists(os.path.join(self.target_dir, 'Screen', 'Scr_001.jpg')))
        self.assertTrue(os.path.exists(os.path.join(self.target_dir, 'Stain', 'Stn_001.jpg')))

    def tearDown(self):
        # Clean up test directory
        shutil.rmtree(self.test_dir)

if __name__ == '__main__':
    unittest.main()