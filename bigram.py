sentence = """
Have free hours and love children? 
Drive kids to school, soccer practice 
and other activities.
"""

words = sentence.split()

bigrams = []

for i in range(len(words)-1):
    bigrams.append((words[i],words[i+1]))
    

print(bigrams)
