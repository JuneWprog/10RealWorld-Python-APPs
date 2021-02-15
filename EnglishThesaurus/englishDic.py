
# |************************************************|
# | //    A Simple English Dictionary  //          |
# |        using json as data source.              |
# |
#  ************************************************|

#json is a standard python library
import json

#SequenceMatcher compare the similarity between 2 words
from difflib import SequenceMatcher
# Example: SequenceMatcher(None, "rain","rainn").ratio()

#read json file into dataset
data = json.load(open("data.json"))
# put all keys into a list
dataKeys=list(data.keys())

#If can't find a perfect match.Look for similar word
#Define satisfying matching rate
rate=0.8

def calculatMatch(word):
    for key in dataKeys:
        matchRateUpper=SequenceMatcher(None, word.capitalize(),key).ratio()
        if (matchRateUpper==1.0):
            return(key)
        else:
            matchRate=SequenceMatcher(None, word,key).ratio() 
            if (matchRate>rate):
                return(key)
    return(word)
def translate(word):
    if word in data:
        print(f"   -- {word} -- \n ")
        return(data[word])
    else:
        matchStr=calculatMatch(word)
        if matchStr!=word:
            print(f"Found the Best Match for you: {matchStr}  \n ")
            print(f"   -- {matchStr} -- \n ")
            return(data[matchStr])
        else:
            return(["The word doesn't exist. Please double check it."])
def printResult(result):
        length=len(result)
        for i in range(length):
            if (length>1):
                if (i==length-1):
                    print(f"{i+1}.    {result[i]} \n ")
                else:
                    print(f"{i+1}.    {result[i]}")
            else:
                print(f"    {result[i]} \n")

def main():               
    print("            How to Use:") 
    print("1. input any word you wanna translate")
    print("2. quit the program, input :quit")
    print(f"     ------Good Luck------- \n ")
    while True:
        word=input("Enter a word: ")
        print("")
        if word == ":quit":
            break
        else:
            word=word.lower()
            result=translate(word)
            printResult(result)

main()