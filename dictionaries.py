def merge_dictionaries(dic1,dic2): 
    print(dic1)
    print(dic2)
    dic1_sort = dict(sorted(dic1.items()))
    dic2_sort = dict(sorted(dic2.items()))
    dic1_sort.update(dic2_sort) 
    print(dic1_sort)
dict1 = {"c": 6, "a": 2, "b": 3}
dict2 = {"b": 10, "d": 4}
merge_dictionaries(dict1 , dict2)

sentence = input("Enter a sentence : ")
words = sentence.split() 
print(words)
repeat = 0 
dictionaries = {}
for i in range(len(words)):
    if words[i] not in dictionaries:
        repeat = 0  
        for j in range(len(words)):
            if(words[i] == words[j]) : 
                repeat += 1 
        dictionaries.update({words[i] : repeat})

print(dictionaries)
