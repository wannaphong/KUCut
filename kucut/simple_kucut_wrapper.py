#-*- coding:utf-8 -*-

from .wordcut import *
import os.path

class SimpleKucutWrapper:
    def __init__(self):
        HOME = os.path.dirname(__file__)
        lexicon_file = os.path.join(HOME,'dict/lexicon.txt')
        syllable_file = os.path.join(HOME,'dict/syllable.txt')
        database_file = os.path.join(HOME,'corpus.db')
        lexiconDict = Dictionary(lexicon_file)
        syllableDict = Dictionary(syllable_file)
        self.seg = Segmentation(syllable = syllableDict,
            lexicon = lexiconDict,
            quiet = True,
            database = database_file,
            blank = '_',
            home = HOME)
        prohibit_file = os.path.join(HOME,'dict/prohibit.txt')
        self.seg.loadProhibitPattern(prohibit_file)

    def tokenize(self, text_list):
        results, ambiguous_list = \
            self.seg.tokenize(text_list, style='Normal', space=True)
        return list(map(treat_result, results))

def treat_word(w):
    if isinstance(w, bytes):
        return w.decode("iso8859_11")
    return w

def treat_t(t):
    return list(map(treat_word, t[0]))

def treat_result(result):
    return list(map(treat_t, result[1]))
