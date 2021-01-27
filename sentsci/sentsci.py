import re
from sentsci.train import train_nb_segmenter, punct_features

prefixes = "(Fig|Dr|Mr|Mrs)"
floating = "[.]([0-9])"
websites = "[.](com|net|org|io|gov)"

nb_segmenter = train_nb_segmenter()


def split(text):
    text = re.sub(prefixes, r"\\1<prd>", text)
    text = re.sub(websites, r"\\1", text)
    text = re.sub("<prd>", ".", text)

    text = re.sub(r"\.\s", r".<splitter>", text)
    text = re.sub(r"\?\s", r"?<splitter>", text)
    text = re.sub(r"\!\s", r"!<splitter>", text)

    return text.split("<splitter>")


def nb_split(text):
    start = 0
    sents = []
    for i, word in enumerate(text):
        if word in '.?!' and nb_segmenter.classify(punct_features(text, i)) is True:
            sents.append(text[start:i+1])
            start = i+1
    if start < len(text):
        sents.append(text[start:])
    return sents
