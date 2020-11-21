word_list = []
n = int(input())
for i in range(n):
    word = str(input())
    word_len = len(word)
    word_list.append((word,word_len))
    
word_list = list(set(word_list))
word_list.sort(key = lambda word:(word[1],word[0]))

for word in word_list:
    print(word[0])

# lambda의 활용법을 숙지할것
