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
                print("TRAIN")
                train_img_ids.append(img_id)
            elif split == '1':
                print("VAL")
                val_img_ids.append(img_id)
            elif split == '2':
                print("TEST")
                test_img_ids.append(img_id)
            else:
                print("ERROR")

    pass 

if __name__ == "__main__":
    main()