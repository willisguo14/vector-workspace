import os

from PIL import Image
import numpy as np 

def write_data(f_path, img_ids):

    n = len(img_ids)

    img_path = "/scratch/ssd002/datasets/celeba/Img/img_align_celeba"

    with open(f_path, "w") as f:

        for i, img_id in enumerate(img_ids):
            if i != n - 1:
                f.write(f"{os.path.join(img_path, img_id)}\n")
            else:
                f.write(f"{os.path.join(img_path, img_id)}")   

# test preprocess_image() in taming/data/base.py
def preprocess_image(image_path):
    image = Image.open(image_path)
    if not image.mode == "RGB":
        image = image.convert("RGB")
    image = np.array(image).astype(np.uint8)
    # image = preprocessor(image=image)["image"]
    image = (image/127.5 - 1.0).astype(np.float32)
    return image

def main():

    data_splits_f = "/scratch/ssd002/datasets/celeba/Eval/list_eval_partition.txt"

    train_img_ids = []
    val_img_ids = []
    test_img_ids = []

    with open(data_splits_f, "r") as f:
        lines = f.read().splitlines()

        for line in lines:
            img_id, split = line.split()
            
            if split == '0':
                train_img_ids.append(img_id)
            elif split == '1':
                val_img_ids.append(img_id)
            elif split == '2':
                test_img_ids.append(img_id)
    
    train_f = "train.txt"
    val_f = "val.txt"
    test_f = "test.txt"

    write_data(train_f, train_img_ids)
    write_data(val_f, val_img_ids)
    write_data(test_f, test_img_ids)

    ### 

    # img = preprocess_image("/scratch/ssd002/datasets/celeba/Img/img_align_celeba/000001.jpg")
    # print(img.shape)
    # print(img)

if __name__ == "__main__":
    main()