import string
import random
from tabulate import tabulate

def calculate_probability(word1, word2, unigram, bigram):
    if((word1, word2) not in bigram):
        return 0
    else:
        prob = bigram[ (word1, word2) ] / unigram[word1]
        return prob

corpus = "<s> The sun slowly dipped below </s>. <s> the horizon, casting a warm golden glow across the tranquil meadow </s>. <s> Birds chirped their evening melodies as a gentle breeze rustled the leaves on the trees </s>. <s> In the distance, the sound of childrens laughter echoed through the air, filling the atmosphere with joy </s>. <s> The scent of freshly bloomed flowers wafted through the garden, creating a symphony of colors and fragrances </s>. <s> As nightfall approached, the stars emerged, painting the sky with their shimmering brilliance, a breathtaking sight that whispered of endless possibilities. </s>"

corpus = corpus.lower()
words_array = corpus.split()
words_array =  [word.replace('.', '').replace(',', '') for word in words_array]
print(words_array)

unigram = {}
for word in words_array:
    if word in unigram:
        unigram[word] = unigram[word] + 1
    else:
        unigram[word] = 1

print('unigram')
table_data = [[key, value] for key, value in unigram.items()]
print(tabulate(table_data, headers=["Word", "Count"], tablefmt="grid"))

bigram = {}
for i in range(len(words_array) - 1):
    input = (words_array[i],words_array[i+1])
    if( input in bigram):
        bigram[input] = bigram[input] + 1
    else:
        bigram[input] = 1    

print("bigram")
table_data = [[key, value] for key, value in bigram.items()]
print(tabulate(table_data, headers=["Word", "Count"], tablefmt="grid"))

random_sentences = random.sample(words_array, 5)
input = ['<s>',random_sentences[0], random_sentences[1], random_sentences[2],random_sentences[3],random_sentences[4], '</s>']
# input = ['<s>','the','sun','slowly','dipped','below', '</s>']
prob = 1
for i in range(len(input) - 1):
    prob = prob * calculate_probability(input[i], input[i+1], unigram, bigram)

print(prob)