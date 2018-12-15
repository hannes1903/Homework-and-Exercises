text = 'Hannes geht nach hause, hannes ist zu hause, ist hannes schlaeft hannes'
words = 'hannes', 'nach', 'ist'

def popular_words(text, words):
    text = text.lower()
    splitted_words = text.split()
    answer = {}
    for word in words:
        answer[word] = splitted_words.count(word)
    return answer

print (popular_words(text, words))


splitted_words = text.split()
answer={}
for word in splitted_words:
    answer[word] = splitted_words.count(word)

print (answer)


# strip() remove unreadable characters
#f inding in a list quite inefficient



ans={}
if word in ans:
    ans[word] += 1
else:
    ans[word] = 1
print(ans)

# import collection

import collections

words =["a", "b", "a", "c", 'b', 'k']

c = collections.Counter(words)

print(c)

c.most_common(2)

print(c)

c['a']

print (c)

##

d={}
for word in words:
    if word in ('a', 'c'):
        if word in d:
            d [word] += 1
        else:
            d[word] = 1

