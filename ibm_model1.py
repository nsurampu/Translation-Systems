import json
import nltk
from collections import defaultdict
from pprint import pprint

def IBM_Model_1(test_file):
    '''

    Takes a json file as argument and returns the predicted alignment of the phrases
    withing the passed json documentself.

    @type test_file: A json file

    '''

    json_data_file = open(test_file, 'r')
    json_data = json.load(json_data_file)
    languages = list(json_data[0].keys())

    t = {}

    for bitext in json_data:
        f_sentence = bitext[languages[0]]
        e_sentence = bitext[languages[1]]
        for e_word in e_sentence.split(" "):
            for f_word in f_sentence.split(" "):
                t[(e_word, f_word)] = 1/(len(languages[0]))

    iterations  = int(input("Enter iterations: "))

    for i in range(0, iterations):
        count = defaultdict(float)
        total_f = defaultdict(float)
        total_e = defaultdict(float)
        for bitext in json_data:
            f_sentence = bitext[languages[0]]
            e_sentence = bitext[languages[1]]
            for e_word in e_sentence.split(" "):
                #total_e[e_word] = 0.0
                for f_word in f_sentence.split(" "):
                    total_e[e_word] = total_e[e_word] + t[(e_word, f_word)]
            for e_word in e_sentence.split(" "):
                for f_word in f_sentence.split(" "):
                    #count[(e_word, f_word)] = 0.0
                    #total_f[f_word] = 0.0
                    count[(e_word, f_word)] = count[(e_word, f_word)] + (t[(e_word, f_word)] / total_e[e_word])
                    total_f[f_word] = total_f[f_word] + (t[(e_word, f_word)] / total_e[e_word])
        word_pairs = list(t.keys())
        for f_word in set(total_f):
            for e_word in set(total_e):
                if (e_word, f_word) in word_pairs:
                    if total_f[f_word] != 0:
                        t[(e_word, f_word)] = count[(e_word, f_word)] / total_f[f_word]

    # pprint(t)
    bitext_alignment = {}
    bitext_num = 1
    for bitext in json_data:
        alignment = []
        f_sentence = bitext[languages[0]]
        e_sentence = bitext[languages[1]]
        f_words = f_sentence.split(" ")
        e_words = e_sentence.split(" ")
        for f_word in f_words:
            temp = 0
            for e_word in e_words:
                if t[(e_word, f_word)] > temp:
                    final_e = e_word
                    temp = t[(e_word, f_word)]
            alignment.append((f_words.index(f_word) + 1, e_words.index(final_e) + 1))
        bitext_alignment[languages[0] +": " + f_sentence + ", " + languages[1] +": " + e_sentence] = alignment
        bitext_num = bitext_num + 1

    pprint(bitext_alignment)

# IBM_Model_1("data1.json")
