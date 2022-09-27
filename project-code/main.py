with open("/Users/hemantathapa/Desktop/Fall 2022/CSC 664-02/Project/aclImdb/train/unsup/1_0.txt") as f:
    lines = f.readlines()
    # formatted = lines.split(".")
formatted = lines[0].split(".")
for x in formatted:
    print(x)
f.close()
