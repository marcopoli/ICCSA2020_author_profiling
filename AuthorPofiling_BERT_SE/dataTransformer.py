from sentence_transformers import SentenceTransformer
import emoji
import joblib
from ekphrasis.classes.preprocessor import TextPreProcessor
from ekphrasis.classes.tokenizer import SocialTokenizer
from ekphrasis.dicts.emoticons import emoticons
import pandas as pd
import numpy as np
model = SentenceTransformer('bert-large-nli-stsb-mean-tokens')

text_processor = TextPreProcessor(
    # terms that will be normalized
    normalize=['url', 'email', 'user', 'percent', 'money', 'phone', 'time', 'date', 'number'],
    # terms that will be annotated
    annotate={"hashtag"},
    fix_html=True,  # fix HTML tokens

    unpack_hashtags=True,  # perform word segmentation on hashtags

    # select a tokenizer. You can use SocialTokenizer, or pass your own
    # the tokenizer, should take as input a string and return a list of tokens
    tokenizer=SocialTokenizer(lowercase=True).tokenize,
    dicts=[emoticons]
)


for j in range(2,3):
  dt = pd.read_csv('id_and_sentences_'+str(float(j))+'.tsv', sep='\t', encoding='utf8', header=None, names=["id", "message"],
                  error_bad_lines=False)
  id = dt.iloc[:, 0]
  sentences = dt.iloc[:, 1]

  examples = []
  import re

  i = 0
  for s in sentences:
      s = s.lower()
      s = str(" ".join(text_processor.pre_process_doc(s)))
      s = re.sub(r"[^a-zA-ZÀ-ú</>!?♥♡\s\U00010000-\U0010ffff]", ' ', s)
      s = re.sub(r"\s+", ' ', s)
      s = re.sub(r'(\w)\1{2,}', r'\1\1', s)
      s = re.sub(r'^\s', '', s)
      s = re.sub(r'\s$', '', s)
      s = emoji.demojize(s).replace(":", "").replace("_", " ").replace("<", " ").replace(">", " ").replace("/", "")
      s = re.sub(r"\s+", ' ', s).lstrip()
      # print(s)
      examples.append(s)
      i = i + 1

  sentence_embeddings = model.encode(examples)
  print(sentence_embeddings[0])
  print(sentence_embeddings[0].shape)

  b = open("embeddings_"+str(j)+".txt","w+")
  k = 0
  for emb in sentence_embeddings:
    b.write(str(id[k])+"\t")
    for t in emb:
      b.write(str(t)+"\t")
    b.write("\n")
    k = k+1

  b.close()

