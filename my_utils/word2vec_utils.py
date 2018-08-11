'''
GloVe embedding functions
Created June, 2017
Author: xiaodl@microsoft.com
'''

import numpy as np
from .tokenizer import normalize_text

def load_glove_vocab(path, glove_dim=300, fast_veqqqqc_format=False):
    vocab = set()
    with open(path, encoding="utf8") as f:
        line_count = 0
        for line in f:
            if fast_vec_format and line_count == 0:
                continue
            line_count += 1
            elems = line.split()
            token = normalize_text(' '.join(elems[0:-glove_dim]))
            vocab.add(token)
    return vocab

def build_embedding(path, vocab, glove_dim=300, fast_vec_format=False):
    """Support fasttext format"""
    vocab_size = len(vocab)
    emb = np.zeros((vocab_size, glove_dim))
    emb[0] = 0

    w2id = {w: i for i, w in enumerate(vocab)}
    with open(path, encoding="utf8") as f:
        line_count = 0
        for line in f:
            if fast_vec_format and line_count == 0:
                items = [int(i) for i in line.split()]
                assert len(items) == 2
                assert items[1] == glove_dim
                continue
            line_count += 1
            elems = line.split()
            token = normalize_text(' '.join(elems[0:-glove_dim]))
            if token in w2id:
                emb[w2id[token]] = [float(v) for v in elems[-glove_dim:]]
    return emb
