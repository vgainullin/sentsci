import re
from sentsci.trainer import train_nb_segmenter, punct_features
import nltk
from nltk.tokenize.treebank import TreebankWordDetokenizer
from sacremoses import MosesTokenizer, MosesDetokenizer

tk = MosesTokenizer()
dtk = MosesDetokenizer()
prefixes = "(Fig|Dr|Mr|Mrs)[.]"
floating = "[.]([0-9])"
websites = "[.](com|net|org|io|gov)"

nb_segmenter = train_nb_segmenter()


def split(text):
    text = re.sub(prefixes,"\\1<prd>",text)
    text = re.sub(websites,"<prd>\\1",text)

    text = text.replace(".",".<splitter>")
    text = text.replace("?","?<splitter>")
    text = text.replace("!","!<splitter>")
    text = text.replace("<prd>",".")
    sentences = [x.lstrip() for x in text.split("<splitter>")]
    return sentences[:-1]


def nb_split(text):
    text = tk.tokenize(text)
    start = 0
    sents = []
    for i, word in enumerate(text):
        if word in '.?!':
            if nb_segmenter.classify(punct_features(text, i)):
                sents.append(dtk.detokenize(text[start:i+1]))
                start = i+1
    if start < len(text):
        sents.append(dtk.detokenize(text[start:]))
    return sents
