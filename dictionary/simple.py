import json
from difflib import get_close_matches

data = json.load(open("data.json"))


def variations(word):
    matches = get_close_matches(word, data.keys(), 1)
    if matches:
        yn = input( "Did you mean '%s' instead? Y/N: " % matches[0]).lower()
        if yn == "y":
            return data[matches[0]]


def lookup(word):
    word = word.lower()
    if word in data:
        return data[word]

def printDef(definitions):
    for definition in definitions:
        print(" - %s" % definition)

def main():
    word = input("Enter a word: ")

    definitions = lookup(word)
    if definitions:
        printDef(definitions)
        return
    else:
        variation = variations(word)
        if variation:
            printDef(variation)
            return

    print("The word %s was not found." % word)


main()
