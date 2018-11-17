from nltk import IBMModel1,IBMModel2,word_tokenize,AlignedSent
import json 
from os import getcwd

if __name__ == '__main__':

    cwd = getcwd()

    with open(cwd+'\\data1.json') as f:
        json_data1 = f.read()
    with open(cwd+'\\data2.json') as f:
        json_data2 = f.read()

    data1 = json.loads(json_data1)
    data2 = json.loads(json_data2)

    bitext = []
    for sentence in data1:
        bitext.append(AlignedSent(word_tokenize(sentence['fr'],language='french'),word_tokenize(sentence['en'],language='english')))

    model1 = IBMModel1(bitext,10)
    model2 = IBMModel2(bitext,10)