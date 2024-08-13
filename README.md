# Phone Defect Detection App

This application uses computer vision to detect defects on phone surfaces such as oil smudges, screen scratches, and stains.

## Setup

1. Clone this repository
2. Install dependencies:
   ```
   pip install -r requirements.txt
   ```
3. Organize your dataset:
   ```
   python src/data_preparation/organize_dataset.py
   ```
4. Train the model:
   ```
   python src/model/train_model.py
   ```
5. Run the application:
   ```
   python src/app/phone_defect_app.py
   ```

## Project Structure

- `data/`: Contains raw and processed datasets
- `models/`: Stores trained model files
- `src/`: Source code for data preparation, model training, and the main application
- `docs/`: Project documentation
- `tests/`: Unit tests and integration tests

## Usage

1. Launch the application
2. Click "Select Image" to choose a phone image
3. Click "Detect Defect" to analyze the image

The application will display the detected defect type and confidence level.