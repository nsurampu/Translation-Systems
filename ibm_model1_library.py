from nltk import IBMModel1, IBMModel2, word_tokenize, AlignedSent
from nltk.translate.phrase_based import phrase_extraction
import json
from collections import OrderedDict
from collections import defaultdict
from os import getcwd


'''
This script uses NLTK's IBMModel1 and IBMModel2 for creating translation alignments and finally uses 
nltk.translate.phrase_based.phrase_extraction() for identifying and ranking possible phrase translations on 
our custom dataset.

'''
def main():

    '''
        This is the core logic of our program.
    '''
    test_corpus = True
    custom_corpus = False

    cwd = getcwd()
    # read data from the given dataset
    with open(cwd+'\\data1.json') as f:
        json_data1 = f.read()
    with open(cwd+'\\data2.json') as f:
        json_data2 = f.read()
    with open(cwd+'\\Alternative Corpus\\parallel.json') as f:
        json_data3 = f.read()
    # data is in JSON format and hence needs to be parsed
    data1 = json.loads(json_data1)
    data2 = json.loads(json_data2)
    data3 = json.loads(json_data3)
    # create an aligned corpus for phrase extraction
    bitext = []
    for sentence in data1:
        bitext.append(AlignedSent(word_tokenize(
            sentence['fr'], language='french'), word_tokenize(sentence['en'], language='english')))
    
    # run the model (model 1)  for 10 iterations
    model1 = IBMModel1(bitext, 10)

    # print(bitext, '\n\n')
    
    # get the word translation table
    translate_table_1 = model1.translation_table
    
    # extract alignments and show them
    alignments_extracted_1 = []
    for temp in bitext:
        alignments_extracted_1.append(temp.alignment)
    print(alignments_extracted_1)

    # Similarly run the model2 and print the results
    bitext = []
    for sentence in data1:
        bitext.append(AlignedSent(word_tokenize(
            sentence['fr'], language='french'), word_tokenize(sentence['en'], language='english')))
    model2 = IBMModel2(bitext, 10)
    translate_table_2 = model2.translation_table

    alignments_extracted_2 = []
    for temp in bitext:
        alignments_extracted_2.append(temp.alignment)
    # print('\n\n',alignments_extracted_2,'\n\n')
    print('finished\n')

    
    # if this is true, run the phrase translation model for data2.json

    ''''''
    if test_corpus:
        bitext_test = []
        # get the parallel sentences here
        for sentence in data2:
            bitext_test.append(AlignedSent(word_tokenize(sentence['fr'], language='french'), word_tokenize(sentence['en'], language='english')))

        # test model for extracting phrases, MODEL 1, used to extract phrases:
        test_model = IBMModel1(bitext_test, 10)
        alignments_test = bitext_test[0].alignment

        # print(bitext_test[0], bitext_test[0].alignment)
        phrases = phrase_extraction(
            data2[0]['fr'], data2[0]['en'], alignments_test)
        for i in phrases:
            print(i, '\n\n')


        '''
        
        CHANDRAHAS ADD DESCRIPTION HERE. OPTIONALLY, SAVE THE TRANSLATIONS
        
        '''

        countef = defaultdict()
        countf = defaultdict()

        for sent in range(len(data3)):
            phrases = phrase_extraction(
                data2[sent]['fr'], data2[sent]['en'], alignments_test)
            for phrase in phrases:
                pair = (phrase[2], phrase[3])
                print(pair)
                if pair not in countef:
                    countef[pair] = 1
                else:
                    countef[pair] = countef[pair] + 1

        for word in countef:
            fword = word[0]
            if fword not in countf:
                countf[fword] = countef[word]
            else:
                countf[fword] = countf[fword] + countef[word]
        print('ranks: \n\n')

        final = defaultdict(dict)

        for word in countef:
            val = countef[word] / countf[word[0]]
            # print(word,"    ", val)
            final[word[0]][word[1]] = val

        # print(final)

        for entity in final:
            # print(entity)
            current = final[entity]
            print(entity)
            # print(current)
            d_descending = sorted(
                current.items(), key=lambda kv: kv[1], reverse=True)
            for i in d_descending:
                print(i)
            print("\n")

        # print(final)


    # print("final")
    # for word in countef:
        # print(word,"    ",countef[word])
        
    # if this is set as true, do the same for the dataset that we generated.
    if custom_corpus:
        bitext_test = []
        for sentence in data3:
            bitext_test.append(AlignedSent(word_tokenize(sentence['gr'], language='german'), word_tokenize(sentence['en'], language='english')))

        # test model for extracting phrases, MODEL 1:
        test_model = IBMModel1(bitext_test, 10)
        alignments_test = bitext_test[0].alignment

        '''
        
        CHANDRAHAS ADD DESCRIPTION HERE
        
        '''
        countef = defaultdict()
        countf = defaultdict()
        
        for sent in range(len(data3)):
            phrases = phrase_extraction(
                data3[sent]['gr'], data3[sent]['en'], alignments_test)
            for phrase in phrases:
                pair = (phrase[2], phrase[3])
                # print(pair)
                if pair not in countef:
                    countef[pair] = 1
                else:
                    countef[pair] = countef[pair] + 1

        for word in countef:
            fword = word[0]
            if fword not in countf:
                countf[fword] = countef[word]
            else:
                countf[fword] = countf[fword] + countef[word]
        print('ranks: \n\n')

        final = defaultdict(dict)

        for word in countef:
            val = countef[word] / countf[word[0]]
            # print(word,"    ", val)
            final[word[0]][word[1]] = val

        # print(final)

        for entity in final:
            # print(entity)
            current = final[entity]
            print(entity)
            # print(current)
            d_descending = sorted(
                current.items(), key=lambda kv: kv[1], reverse=True)
            for i in d_descending:
                print(i)
            print("\n")

        # print(final)


    print("final")
    for word in countef:
        # print(word, "    ", countef[word])

        # for i in phrases:
        #     for j in phrases:
        #         for word in i:
        for sent in range(len(data3)):
            phrases = phrase_extraction(
                data3[sent]['gr'], data3[sent]['en'], alignments_test)
            for phrase in phrases:
                pair = (phrase[2], phrase[3])
                # print(pair)
                if pair not in countef:
                    countef[pair] = 1
                else:
                    countef[pair] = countef[pair] + 1

        for word in countef:
            fword = word[0]
            if fword not in countf:
                countf[fword] = countef[word]
            else:
                countf[fword] = countf[fword] + countef[word]
        print('ranks: \n\n')

        final = defaultdict(dict)

        for word in countef:
            val = countef[word] / countf[word[0]]
            # print(word,"    ", val)
            final[word[0]][word[1]] = val

    print(final)

    for entity in final:
        # print(entity)
        current = final[entity]
        print(entity)
        # print(current)
        d_descending = sorted(current.items(), key=lambda kv: kv[1], reverse=True)
        for i in d_descending:
            print(i)
        print("\n")


if __name__ == "__main__":
    main()