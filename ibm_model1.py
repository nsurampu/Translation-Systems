import json
import nltk
from collections import defaultdict
from pprint import pprint

json_data_file = open("data1.json", 'r')
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

pprint(t)
