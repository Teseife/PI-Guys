=# YOLO (You Only Look Once) - Real-Time Object Detection

## Objective

The objective of this project is to deploy a YOLOv5 model on a compact and resource-constrained device like a Raspberry Pi. This project involves training a custom YOLOv5 model on a dataset tailored for specific object detection tasks, integrating the model into the YOLOv5 framework, and optimizing it for inference on the Raspberry Pi. By leveraging custom data and fine-tuning the model, the goal is to achieve efficient and accurate real-time object detection on a portable, small-scale device.

## Overview

YOLO is a state-of-the-art (SOTA) system for real-time object detection. It is implemented on the **Darknet framework in C** ([YOLO on Darknet](https://pjreddie.com/darknet/yolo/)), which is designed for computer vision tasks. Unlike traditional detection systems that classify regions and perform detection separately, YOLO processes the entire image in one go, leveraging global context to make its predictions.

## Key Features

- **Single Network Evaluation**: YOLO predicts bounding boxes and class probabilities with a single network evaluation, making it highly efficient.
- **Global Context Awareness**: By analyzing the entire image during inference, YOLO incorporates the spatial relationships between objects and their surroundings to make accurate predictions.

## How YOLO Works

1. **Image Grid Division**:
   - The input image is divided into an  `S * S` grid.
   - Each grid cell predicts:
     - *B* bounding boxes.
     - Confidence scores for those boxes.
     - *C* class probabilities.

   
![yolo](https://github.com/user-attachments/assets/df3b3c3f-4e76-44bf-8ce9-9ebe6009443e)

   *Figure: The YOLO model processes the input image by dividing it into a grid. Each grid cell predicts bounding boxes, confidence scores, and class probabilities. Post-processing techniques refine these into accurate final detections.*

2. **Confidence Thresholding**:
   - Most bounding boxes have very low probabilities.
   - YOLO eliminates boxes below a certain confidence threshold.

3. **Non-Max Suppression**:
   - Removes duplicate detections by keeping only the most confident predictions for each object.

### YOLO Model Output

YOLO outputs a tensor representing predictions for bounding boxes, class probabilities, and confidence scores. Post-processing techniques like thresholding and non-max suppression refine these predictions into accurate detections.

## Comparison of Classifiers and Localizers

### Classifiers
- Assign a label or category to an input image or video frame.
- Classify the entire image or a region into predefined classes.
- **Purpose**: To categorize an image or a specific region of an image.

### Localizers
- Determine the position of objects within an image.
- Use bounding boxes or pixel-level segmentation masks to indicate object locations.
- **Purpose**: To localize objects and identify their exact positions in the image.

## Test Time and Global Context

- **Test Time**: This is the phase where a trained model makes predictions on new, unseen data.
- **Global Context**:
  - YOLO utilizes the comprehensive information from the entire image, such as spatial relationships and object surroundings.
  - This holistic approach improves the accuracy of predictions by considering the overall scene composition.

## Why YOLO?

YOLO’s ability to process the entire image at once and incorporate global context sets it apart from traditional methods. It’s fast, accurate, and efficient, making it ideal for real-time applications like video surveillance, autonomous vehicles, and robotics.

---

## Links

- **YOLO Explanation Article**: [YOLO Family Explanation](https://medium.com/@lokwa780/yolo-family-explanation-690515934a6a)
- **Darknet Framework**: [YOLO on Darknet](https://pjreddie.com/darknet/yolo/)
- **Source of Image**: [Image Credit](https://medium.com/@lokwa780/yolo-family-explanation-690515934a6a)

---

## This project was done in collaboration with:

| Name    |
|---------|
| Ian     |        
| Alex    |       
| Thomas  |          
| Eduardo |            
