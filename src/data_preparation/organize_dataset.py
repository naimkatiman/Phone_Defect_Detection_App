import os
import shutil

def organize_dataset(source_dir, target_dir):
    # Create target directories
    categories = ['Oil', 'Screen', 'Stain']
    for category in categories:
        os.makedirs(os.path.join(target_dir, category), exist_ok=True)

    # Move and rename files
    for filename in os.listdir(source_dir):
        if filename.startswith('Oil'):
            shutil.move(os.path.join(source_dir, filename), 
                        os.path.join(target_dir, 'Oil', filename))
        elif filename.startswith('Scr'):
            shutil.move(os.path.join(source_dir, filename), 
                        os.path.join(target_dir, 'Screen', filename))
        elif filename.startswith('Stn'):
            shutil.move(os.path.join(source_dir, filename), 
                        os.path.join(target_dir, 'Stain', filename))

if __name__ == "__main__":
    source_directory = '../../data/raw'
    target_directory = '../../data/processed'
    organize_dataset(source_directory, target_directory)