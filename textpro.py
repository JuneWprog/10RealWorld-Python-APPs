inputStrs=[]
def sentence_maker(phrase):
    interrogatives=("how","when","why")
    capitalized=phrase.capitalize()
    if phrase.startswith(interrogatives):
        return "{}? ".format(capitalized)
    else:
        return "{}. ".format(capitalized)
while(True):
    inputStr=input("Say something: ")
    if inputStr!="\end":
        inputStrs.append(inputStr)
    else:
        for sentence in inputStrs:
            sentence=sentence_maker(sentence)
            print (sentence, end=' ')
        break








