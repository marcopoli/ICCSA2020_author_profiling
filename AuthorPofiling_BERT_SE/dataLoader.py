import ndjson
import json

#sentFile = open("sentences_0.txt","w+")
#sentFileID = open("id_and_sentences_0.tsv","w+")
#sentFileLabels =  open("labels_0.tsv","w+")

labe = []
with open('/Users/kram/Desktop/pan19-celebrity-profiling-training-dataset-2019-01-31/labels.ndjson') as l:
    for line in l:
        labe.append(line);
print(len(labe))

j = 0;
with open('/Users/kram/Desktop/pan19-celebrity-profiling-training-dataset-2019-01-31/feeds.ndjson') as f:


        for line in f:

            num = j / 5000
            if (j % 5000 == 0):
                try:
                    sentFileID.close()
                except:
                    pass
                sentFileID = open("id_and_sentences_" + str(num) + ".tsv", "w+")


            j_content = json.loads(line)
            id = j_content['id']
            text = j_content['text']
            i = 1
            if len(text)>100 :


                for s in text[:150]:
                    s = str(s).replace("\n"," ").replace("\r"," ").replace("\t", " ").replace("  "," ")

                    sentFileID.write(str(id)+"_"+str(i)+"\t"+s+"\n")


                    i = i+1

            j = j+1;

print(j)
sentFileID.close()