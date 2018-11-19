from nltk import IBMModel1,IBMModel2,word_tokenize,AlignedSent
from nltk.translate.phrase_based import phrase_extraction
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

    print(bitext,'\n\n')

    translate_table_1 = model1.translation_table

    alignments_extracted_1 = []
    for temp in bitext:
        alignments_extracted_1.append(temp.alignment)
    print(alignments_extracted_1)

    bitext = []
    for sentence in data1:
        bitext.append(AlignedSent(word_tokenize(sentence['fr'],language='french'),word_tokenize(sentence['en'],language='english')))
    model2 = IBMModel2(bitext,10)
    translate_table_2 = model2.translation_table

    alignments_extracted_2 = []
    for temp in bitext:
        alignments_extracted_2.append(temp.alignment)
    print('\n\n',alignments_extracted_2)


    bitext_test = []
    for sentence in data2:
        bitext_test.append(AlignedSent(word_tokenize(sentence['fr'],language='french'),word_tokenize(sentence['en'],language='english')))
    
    # test model for extracting phrases, MODEL 1:
    test_model = IBMModel1(bitext_test,10)
    alignments_test = bitext_test[0].alignment
    
    # print(bitext_test[0],bitext_test[0].alignment)
    phrases = phrase_extraction(data2[0]['fr'],data2[0]['en'],alignments_test)
    # print(phrases)
    