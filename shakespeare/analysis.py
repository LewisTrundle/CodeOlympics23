

word_dict = {}

with open("./completeWorks.txt") as f:
    for line in f:
        try:

            print(line)
        except:
            continue