import re
import pandas as pd

word_dict = {}

with open("./completeWorks.txt", "r", encoding="utf8") as f:
    lines = f.readlines()
    for line in lines:
        line = line.strip()
        line = line.lower()
        line = re.sub(r'[^\w\s]', '', line)
        line = line.split(" ")
        
        line_set = set(line)
        for word in line_set:
            if word != " " or word != "":
                if word in word_dict.keys():
                    word_dict[word] += line.count(word)
                else:
                    word_dict[word] = line.count(word)

pandas_dict = {"words": word_dict.keys(), "count": word_dict.values()}
dataframe = pd.DataFrame.from_dict(pandas_dict)
print(dataframe.sort_values("count", ascending=False)[1:101])
