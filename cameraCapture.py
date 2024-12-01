import cv2
import os
import re

# Specify the directory to save images
output_dir = r"C:\UNF\Systems Programming\Pi Project\images\bottles"           
os.makedirs(output_dir, exist_ok=True)

# Function to find the highest number in existing filenames
def get_next_image_index(directory, prefix="bottle_", extension=".png"):
    max_index = -1
    pattern = re.compile(f"{prefix}(\\d+)\\{extension}") 
    for filename in os.listdir(directory):
        match = pattern.match(filename)
        if match:
            max_index = max(max_index, int(match.group(1)))
    return max_index + 1

# Get the next image index
img_count = get_next_image_index(output_dir)

# Initialize the webcam
cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print("Error: Could not access the webcam.")
    exit()

print("Press SPACE to capture an image. Press ESC to exit.")

while True:
    # Read a frame from the webcam
    ret, frame = cap.read()
    if not ret:
        print("Error: Failed to capture image.")
        break
    
    # Display the frame in a window
    cv2.imshow("Webcam - Press SPACE to capture", frame)

    # Check for key press
    key = cv2.waitKey(1)
    if key == 27:  # ESC key to exit
        break
    elif key == 32:  # SPACE key to capture
        # Save the captured image
        img_path = os.path.join(output_dir, f"bottle_{img_count:04d}.png")
        cv2.imwrite(img_path, frame)
        print(f"Image saved: {img_path}")
        img_count += 1

# Release the webcam and close all OpenCV windows
cap.release()
cv2.destroyAllWindows()
