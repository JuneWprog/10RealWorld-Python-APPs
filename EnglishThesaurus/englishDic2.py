
# |************************************************|
# | //    A Simple English Dictionary  //          |
# |        using json as data source.              |
# |                                                |
#  ************************************************|

#json is a standard python library
import json

#SequenceMatcher compare the similarity between 2 words
from difflib import get_close_matches
# Example: SequenceMatcher(None, "rain","rainn").ratio()

#read json file into dataset
data = json.load(open("data.json"))
# put all keys into a list
dataKeys=data.keys()




def translate(word):
    if word in dataKeys:
        print(f"   -- {word} -- \n ")
        return(data[word])
    elif word.lower() in dataKeys:
        print(f"   --{word.lower()} -- \n ") 
        return(data[word.lower()])
    elif word.lower().title() in dataKeys:
        print(f"   --{word.lower().title()} -- \n ") 
        return(data[word.lower().title()])
    else:
        matchStrs=get_close_matches(word,dataKeys)
        if len(matchStrs)>0:
            matchStr=matchStrs[0]
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
    print("2. quit the program, input :")
    print(f"     ------Good Luck------- \n ")
    while True:
        word=input("Enter a word: ")
        print("")
        if word == ":q":
            break
        else:
            result=translate(word)
            printResult(result)

main()