import nltk


def load_nltk_sentences():
    try:
        return nltk.corpus.treebank_raw.sents()
    except LookupError:
        nltk.download('treebank')
        return nltk.corpus.treebank_raw.sents()
