# Translation System

This project implements the IBM Model 1, EM algorithm, IBM Model 2 and phrase based translation using Python3.

### Description

This project implements three types of translation systems:
IBM Model 1 using EM algorithm.
IBM Model 2
Phrase based Translation

### Prerequisites

Python3 along with nltk library is required to run this set of programs.

### Structure of project

data1.json : A json dataset consisting of simple French-English phrase translations.

data2.json : A json dataset consisting of longer French-English phrase translations.

ibm_model1.py : This script implements the IBM Model 1 along with the EM algorithm from scratch. The script takes as arguments the file path of a json file structured in the same manner as the preloaded data1.json and data2.json files.

ibm_model1_library.py : This script uses NLTK's IBMModel1 and IBMModel2 for creating translation alignments and finally uses
nltk.translate.phrase_based.phrase_extraction() for identifying and ranking possible phrase translations on
our custom dataset.

### Results during runs

ibm_model1.py : This scratch implementations of IBM Model 1 + EM has given good results for the preloaded datasets, which can be seen by comparing the output- an alignment matrix, with the true alignments in the corresponding json datasets.

ibm_model1_library.py : This implementations of IBM Model 1 & 2 has given good results for the preloaded datasets, which can be seen by comparing the output- an alignment matrix, with the true alignments in the corresponding json datasets.

### Built with

Python3 </br>
NLTK </br>
OS </br>
Collections </br>
JSON </br>
Pprint

### Authors

Chandrahas Aroori [https://github.com/Exorust] </br>
Naren Surampudi [https://github.com/nsurampu] </br>
Aditya Srikanth [https://github.com/aditya-srikanth]

### Acknowledgments

We'd like to thank our Information Retrieval instructor to give us this opportunity to make such a project.
