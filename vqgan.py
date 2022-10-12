def main():

    data_splits_f = "/scratch/ssd002/datasets/celeba/Eval/list_eval_partition.txt"

    with open(data_splits_f, "r") as f:
        lines = f.read().splitlines()

        for line in lines:
            img_id, split = line.split()
            print(f"{img_id} // {split}")

    pass 

if __name__ == "__main__":
    main()