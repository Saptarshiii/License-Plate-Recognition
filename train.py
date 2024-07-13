from ultralytics import YOLO
import cv2
import matplotlib.pyplot as plt
import numpy as np

if __name__ == '__main__':
    # Initialize the model
    model = YOLO('yolov8s.yaml')

    # Train the model
    results = model.train(data='data.yaml', epochs=50, device='0',resume=True)

    # Assuming the results contain a confusion matrix or similar statistics
    # Extract the confusion matrix values
    tp = results.metrics.confusion_matrix.tp
    tn = results.metrics.confusion_matrix.tn
    fp = results.metrics.confusion_matrix.fp
    fn = results.metrics.confusion_matrix.fn

    # Calculate accuracy for each epoch
    accuracies = (tp + tn) / (tp + tn + fp + fn)

    # Plot accuracy over epochs
    epochs = range(1, len(accuracies) + 1)
    plt.figure(figsize=(10, 5))
    plt.plot(epochs, accuracies, label='Accuracy')
    plt.xlabel('Epoch')
    plt.ylabel('Accuracy')
    plt.title('Accuracy over Epochs')
    plt.legend()
    plt.show()

    # Plot confusion matrix values over epochs
    plt.figure(figsize=(10, 5))
    plt.plot(epochs, tp, label='True Positives')
    plt.plot(epochs, tn, label='True Negatives')
    plt.plot(epochs, fp, label='False Positives')
    plt.plot(epochs, fn, label='False Negatives')
    plt.xlabel('Epoch')
    plt.ylabel('Count')
    plt.title('Confusion Matrix Values over Epochs')
    plt.legend()
    plt.show()
