import cv2
import os
import json

# Paths for input and output directories
input_dir = r"C:\UNF\Systems Programming\Pi Project\images\bottles"
output_dir = r"C:\UNF\Systems Programming\Pi Project\images\bottles_with_boxes"
coco_json_path = r"C:\UNF\Systems Programming\Pi Project\images\coco\annotations.json"

os.makedirs(output_dir, exist_ok=True)  # Create the output directory if it doesn't exist

# Get all image files in the input folder
image_files = [f for f in os.listdir(input_dir) if f.lower().endswith(('.png', '.jpg', '.jpeg'))]

if not image_files:
    print("No image files found in the input directory.")
    exit()

# Get a list of already processed files in the output folder
processed_files = {f for f in os.listdir(output_dir)}

# Initialize COCO-style dictionary
coco_data = {
    "images": [],
    "annotations": [],
    "categories": [{"id": 1, "name": "bottle"}]  # Assuming only 'bottle' as category
}

image_id = 1
annotation_id = 1

print("Press ENTER after drawing a bounding box to proceed to the next image.")
print("Press ESC to skip an image without drawing a box.")
print("Resuming from where you left off...")

for img_file in image_files:
    output_path = os.path.join(output_dir, img_file)

    # Skip if this image has already been processed
    if img_file in processed_files:
        print(f"Skipping {img_file} (already processed).")
        image_id += 1  # Increment the image_id even if the image is skipped
        continue

    img_path = os.path.join(input_dir, img_file)
    image = cv2.imread(img_path)
    if image is None:
        print(f"Error loading image: {img_file}. Skipping...")
        image_id += 1  # Increment the image_id even if the image is invalid
        continue

    # Add image info to coco_data
    coco_data["images"].append({
        "id": image_id,
        "file_name": img_file,
        "width": image.shape[1],
        "height": image.shape[0]
    })

    # Show the image and allow the user to draw a bounding box
    print(f"Processing {img_file}...")
    bbox = cv2.selectROI("Draw Bounding Box", image, fromCenter=False, showCrosshair=True)

    if bbox == (0, 0, 0, 0):  # User pressed ESC or did not draw a box
        print(f"Skipped {img_file}")
        cv2.destroyWindow("Draw Bounding Box")
        image_id += 1  # Increment the image_id to avoid ID collision
        continue

    # Create annotation (category_id = 1 for 'bottle')
    x, y, w, h = map(int, bbox)
    annotation = {
        "id": annotation_id,
        "image_id": image_id,
        "category_id": 1,  # 'bottle' category
        "bbox": [x, y, w, h],
        "area": w * h,
        "iscrowd": 0
    }

    # Add the annotation to the coco_data
    coco_data["annotations"].append(annotation)

    # Draw the bounding box on the image
    cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)

    # Save the image with the bounding box
    cv2.imwrite(output_path, image)
    print(f"Saved with bounding box: {output_path}")

    # Close the ROI window
    cv2.destroyWindow("Draw Bounding Box")

    # Increment IDs for next image/annotation
    image_id += 1
    annotation_id += 1

# Write the final COCO JSON to file
with open(coco_json_path, 'w') as json_file:
    json.dump(coco_data, json_file, indent=4)

print("Processing complete. Check the output folder and annotations.json for results.")
