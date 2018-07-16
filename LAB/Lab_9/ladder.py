from collections import defaultdict, deque
import sys
def get_word(word1,word2):
    try:
        with open('dictionary.txt') as dictionary:
            length=len(word1)
            words=set()
            temp=defaultdict(list)
            closewords=defaultdict(set)
            for word in dictionary:
                word=word.rstrip()
                if len(word)==length:
                    words.add(word)
                    #print(word)
                    for i in range(length):
                        temp[word[:i],word[i+1:]].append(word)           
            if (word1 not in words) or (word2 not in words):
                words=set()
                return words, closewords
            for item in temp:
                for i in range(len(temp[item])):
                    for j in range(i+1,len(temp[item])):
                        closewords[temp[item][i]].add(temp[item][j])
                        closewords[temp[item][j]].add(temp[item][i])
            return words, closewords
    except FileNotFoundError:
        print('Could not open dictionary.txt. Giving up...')
        sys.exit()
def word_ladder(word1,word2):
    solution=[]
    word1=word1.upper()
    word2=word2.upper()
    if len(word1)==len(word2):
        words,closewords=get_word(word1,word2）
        if len(words)==0:
            return []
    else:
        return []
    if word1==word2:
        return [[word1]]
    queue=deque([[word1]])
    while queue:
        wordlist=queue.pop()
        #print(wordlist)
        lastword=wordlist[-1]        
        for word in closewords[lastword]:
            if word==word2:
                if not solution or len(solution[-1])>len(wordlist):
                    solution.append(wordlist+[word])
            if ((not solution or len(solution[-1])>len(wordlist)+1) and (word not in wordlist)):
                queue.appendleft(wordlist+[word])
    return solution
for x in word_ladder('cold','warm'):
    print(x)       
