import json
import pandas as pd

dict = {'000000':[]}
#Training
#(7500, 150, 1024)
#Test
#(2248, 150, 1024)

labe = []
with open('/Users/kram/Desktop/pan19-celebrity-profiling-training-dataset-2019-01-31/labels.ndjson') as l:
    for line in l:
        data = []
        prof = json.loads(line)
        id = prof["id"]
        occ = prof["occupation"]
        gender = prof["gender"]
        fame = prof["fame"]
        age = (2020-int(prof["birthyear"]))
        print(age)
        data.append(occ)
        data.append(gender)
        data.append(fame)
        data.append(age)
        dict[str(id)] = data

print(dict)

b = open("y_values_2_3_test.txt", "w+")
ids_train = []
ids_test = []

index2 = 0
prevId = 0
index = 0
ids = []
ids2 = []
for j in range(3,4):
    dt = pd.read_csv('id_and_sentences_'+str(j)+'.0.tsv', sep='\t', encoding='utf8', header=None, names=["id", "message"], error_bad_lines=False)
    id = dt.iloc[:, 0]

    for idd in id:
        f_id = idd.split('_')[0]
        if len(ids) < 2612:
            if index == 0:
                 prevId = f_id
                 ids.append(f_id)
                 index = index + 1

            if f_id != prevId and index != 0:
                prevId = f_id
                ids.append(f_id)
                index = index + 1
        else:
            if index == 0:
                prevId = f_id
                ids2.append(f_id)
                index = index + 1

            if f_id != prevId and index != 0:
                prevId = f_id
                ids2.append(f_id)
                index = index + 1

    print(len(ids))
    print(len(ids2))


for id in ids2:
        ids_train.append(id)
        results = dict[str(id)]
        b.write(id+"\t")
        for r in results:
            b.write(str(r) + "\t")
        b.write("\n")
        index2 = index2 +1
b.close()

import numpy as np
print(np.array(ids_train).shape)