import os
import json
from pycocotools.coco import COCO

def convert_coco_to_yolo(coco_json_path, output_dir, images_dir):

    coco = COCO(coco_json_path)


    categories = coco.loadCats(coco.getCatIds())
    category_mapping = {cat['id']: i for i, cat in enumerate(categories)}


    os.makedirs(output_dir, exist_ok=True)


    for img_id in coco.getImgIds():
        img_info = coco.loadImgs(img_id)[0]
        img_annotations = coco.loadAnns(coco.getAnnIds(imgIds=img_id))

        yolo_annotations = []
        for ann in img_annotations:
            bbox = ann['bbox']  # COCO bbox: [x_min, y_min, width, height]
            x_center = (bbox[0] + bbox[2] / 2) / img_info['width']
            y_center = (bbox[1] + bbox[3] / 2) / img_info['height']
            width = bbox[2] / img_info['width']
            height = bbox[3] / img_info['height']
            class_id = category_mapping[ann['category_id']]
            yolo_annotations.append(f"{class_id} {x_center} {y_center} {width} {height}")


        label_filename = os.path.splitext(img_info['file_name'])[0] + ".txt"
        with open(os.path.join(output_dir, label_filename), 'w') as label_file:
            label_file.write("\n".join(yolo_annotations))

        print(f"Processed {img_info['file_name']} -> {label_filename}")


train_coco_json =  "Bottle testing.v2i.coco/train/_annotations.coco.json"
valid_coco_json =  "Bottle testing.v2i.coco/valid/_annotations.coco.json"
test_coco_json = "Bottle testing.v2i.coco/test/_annotations.coco.json"

train_images_dir = "Bottle testing.v2i.coco/train"
valid_images_dir = "Bottle testing.v2i.coco/valid"
test_images_dir = "Bottle testing.v2i.coco/test"

test_labels_dir = "Bottle testing.v2i.coco/test/labels"
train_labels_dir = "Bottle testing.v2i.coco/train/labels"
valid_labels_dir = "Bottle testing.v2i.coco/valid/labels"

# Convert annotations to labels
convert_coco_to_yolo(train_coco_json, train_labels_dir, train_images_dir)
convert_coco_to_yolo(valid_coco_json, valid_labels_dir, valid_images_dir)
convert_coco_to_yolo(test_coco_json, test_labels_dir, test_images_dir)

print("Conversion complete!")
