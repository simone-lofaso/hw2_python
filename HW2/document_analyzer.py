from collections import Counter
file_name = "document.txt" #fix file directory

words = []

#Check for bad input. Maybe surround w/ try except (except is catch in python)
with open("document.txt", "r", errors = "ignore") as f:
    for word in f:
         words.append(word.lower().split())
f.close
    

count = Counter(words)   
top5 = count.most_common(5) 
print(top5)




