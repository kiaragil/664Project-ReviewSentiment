with open("aclImdb/test/neg/0_2.txt") as f:
    lines = f.readlines()
    # formatted = lines.split(".")
formatted = lines[0].split(".")
for x in formatted:
    print(x)
f.close()
