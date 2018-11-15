import json
import nltk
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
            t[(e_word, f_word)] = 1.0

iterations  = int(input("Enter iterations: "))

for i in range(0, iterations):
    count = {}
    total_f = {}
    total_e = {}
    for bitext in json_data:
        f_sentence = bitext[languages[0]]
        e_sentence = bitext[languages[1]]
        for e_word in e_sentence.split(" "):
            total_e[e_word] = 0.0
            for f_word in f_sentence.split(" "):
                total_e[e_word] = total_e[e_word] + t[(e_word, f_word)]
        for e_word in e_sentence.split(" "):
            for f_word in f_sentence.split(" "):
                count[(e_word, f_word)] = 0.0
                total_f[f_word] = 0.0
                count[(e_word, f_word)] = count[(e_word, f_word)] + (t[(e_word, f_word)] / total_e[e_word])
                total_f[f_word] = total_f[f_word] + (t[(e_word, f_word)] / total_e[e_word])
    word_pairs = list(t.keys())
    for e_word in set(total_e):
        for f_word in set(total_f):
            if (e_word, f_word) in word_pairs:
                t[(e_word, f_word)] = count[(e_word, f_word)] / total_f[f_word]

pprint(t)
