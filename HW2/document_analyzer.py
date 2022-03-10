import string

limit = 0
OUTPUT_LIMIT = 5

file = open('document.txt', encoding='utf8')
data = file.read().strip(string.punctuation)
file.close()
words = data.split()

dict = {i:words.count(i) for i in words}
for k,v in sorted(dict.items(), key=lambda x:x[1], reverse=True):
    print(k, ":", v)
    limit += 1
    if limit == OUTPUT_LIMIT:
        break



