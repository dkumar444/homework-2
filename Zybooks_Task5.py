import csv

input1 = input()

with open(input1, 'r') as wordsfile:
    words_reader = csv.reader(wordsfile)
    for row in words_reader:
        list_of_words = row

freq_in_list = list(dict.fromkeys(list_of_words))
listSize = len(freq_in_list)

for i in range(listSize):
    print(freq_in_list[i], list_of_words.count(freq_in_list[i]))