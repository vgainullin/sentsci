import nltk
from data import load_nltk_sentences


def train_nb_model(sents):
    print(len(sents))
    tokens = []
    boundaries = set()
    offset = 0
    for sent in sents:
        tokens.extend(sent)
        offset += len(sent)
        boundaries.add(offset-1)

    featuresets = [(punct_features(tokens, i), (i in boundaries)) for i in range(1, len(tokens)-1) if tokens[i] in '.?!']

    size = int(len(featuresets) * 0.1)
    train_set, test_set = featuresets[size:], featuresets[:size]
    classifier = nltk.NaiveBayesClassifier.train(train_set)
    acc = nltk.classify.accuracy(classifier, test_set)
    print(acc)
    return classifier


def punct_features(tokens, i):
    return {'next-word-capitalized': tokens[i+1][0].isupper(),
            'prev-word': tokens[i-1].lower(),
            'punct': tokens[i],
            'prev-word-is-one-char': len(tokens[i-1]) == 1}


def train_nb_segmenter():
    sents = load_nltk_sentences()
    try:
        model = train_nb_model(sents)
    except LookupError:
        nltk.download('punkt')
        model = train_nb_model(sents)
    return model


if __name__ == '__main__':
    train_nb_segmenter()
