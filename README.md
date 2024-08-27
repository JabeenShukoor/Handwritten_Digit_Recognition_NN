# Handwritten Digit Recognition Using CNN

This project is a Python-based application that uses a Convolutional Neural Network(CNN) to recognize handwritten digits. 
The model is trained on the MNIST dataset and can predict digits drawn by the user in a simple GUI application.

## Project Structure

The project consists of the following main files:

1. **`CNN_model.py`**: This file contains the code for building, training, and saving the CNN model using the MNIST dataset.
2. **`CNN_model_pretrained.h5`**: This is the saved pre-trained CNN model file.
3. **`digits_app.py`**: This is the application file that provides a GUI for users to draw digits, which are then recognized by the CNN model.

## Getting Started

### Prerequisites

To run this project, you need to have the following libraries installed:

- `keras`
- `tensorflow`
- `numpy`
- `Pillow`
- `tkinter`
- `pywin32` (for Windows users, to use `ImageGrab`)

You can install the necessary packages using pip:

\`\`\`bash
pip install keras tensorflow numpy pillow pywin32
\`\`\`

### Running the Project

1. **Training the Model**: 

   The model is trained on the MNIST dataset using the `CNN_model.py` script. If you wish to retrain the model, you can run this script:

   \`\`\`bash
   python CNN_model.py
   \`\`\`

   This will save a new model as `CNN_model_pretrained.h5`.

2. **Running the GUI Application**:

   The `digits_app.py` script launches a simple GUI where you can draw digits and get predictions. To run the application, use:

   \`\`\`bash
   python digits_app.py
   \`\`\`

   The application will open a window where you can draw a digit using your mouse and it will display the recognized digit.

## How It Works

1. **Model Architecture**:

   The CNN model is built using Keras and consists of the following layers:
   - Convolutional layers with ReLU activation
   - MaxPooling layer
   - Dropout layers for regularization
   - Dense (Fully Connected) layers
   - Softmax layer for output

2. **Training**:

   The model is trained on the MNIST dataset, which includes 60,000 training images and 10,000 testing images of handwritten digits (0-9). The dataset is preprocessed by normalizing the pixel values and converting the labels to one-hot encoded format.

3. **Prediction**:

   In the application, the user can draw a digit on the canvas. The drawn image is captured, resized, and converted to grayscale before being fed into the model. The model then predicts the digit and displays the result.

## Screenshots 
![Drawing and Prediction Example](![Screenshot (375)](https://github.com/user-attachments/assets/2a8491e6-700e-453e-acb7-a6085b3a996b)
)


## Future Enhancements

- Add more advanced pre-processing techniques to improve prediction accuracy.
- Extend the application to recognize digits in various languages
- Improve the GUI for a better user experience.




