text = input("Enter a string:")
vowels =0
consonants=0
text = text.lower()
b1=['a','e','i','o','u']

def result(text,vowels,consonants):
    for i in range(len(text)):
         if text[i] in b1:
                vowels = vowels+1
         else:
            consonants = consonants+1
    d= {"vowels":vowels,"consonants":consonants} 
    return d               
print(result(text,vowels,consonants))