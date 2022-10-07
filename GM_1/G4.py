
words = {"Ball":"ბურთი", "Door":"კარი", "Fence":"ღობე"}

print(words["Ball"])
print("---------------------------")

for word in words:
    print(word, words[word])

print("---------------------------")

for word in words.keys():
    print(word, words[word])

print("---------------------------")

for word in words.values():
    print(word)

print("---------------------------")
for key,value in words.items():
    print(key,value)


print("---------------------------")

odd= [i for i in range(1,10)   if i % 2 == 0]
even= [i for i in range(1,10) if i % 2 !=0]
print(even)
print(odd)

print("---------------------------")

odd= [i for i in range(1,900000)   if i % 2 == 0]
odd2= (i for i in range(1,900000)   if i % 2 == 0 )

print(odd.__sizeof__())
print(odd2.__sizeof__())

