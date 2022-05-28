a = str(input())
b = str(input())

def find_anagram(word,anagram):
    
    word = word.lower()
    anagram = anagram.lower()
    
    sortedWord = sorted(word) 
    sortedAnagram = sorted(anagram)   
    
    if sortedAnagram == sortedWord:
       return True
    return False

x=find_anagram(a,b)
print(x)