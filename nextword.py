"""
    Next-word predictor without using ML libraries.
    This algorithm illustrates generative AI basics transparently.
    It doesn't enforce matching of brackets, parenthesis, or quotes.
    It doesn't properly handle abbreviations like Mrs. or Mr.
    It assumes single apostrophes are contractions.
    Christopher Burke, 2/7/24
"""
import io
import string
import random
from collections import Counter
from multiset import *

def isPunct(char):
    # True if the character is punctuation
    otherPunctuation = '—“”‘’'
    return char in string.punctuation or char in otherPunctuation

def isEndOfSentence(token):
    # True if the token marks the end of a sentence
    if token is None:
        return True
    terminators = ['.', '!', '?']
    return token in terminators

def tokenize(text):
    # In this tokenization we:
    #   - Treat words and punctuation marks as tokens
    #   - Treat hyphenated words as one word
    #   - Ignore white space
    #   - Ignore capitalization
    # To accomplish this we go character-by-character
    tokens: list[str] = []
    otherPunctuation = '—“”‘’'
    contractions = '-’\'_'
    currentWord = ''
    inWord = False
    for char in text:
        if isPunct(char):
            # Punctuation
            if inWord and char in contractions:
                # Special case - hyphenated word or contraction
                currentWord += char
            else:
                # Save current word first
                if inWord:
                    tokens.append(currentWord.lower())
                    currentWord = ''
                    inWord = False
                # Punctuation gets its own token
                tokens.append(''+char)
        elif char not in string.whitespace:
            # Collect characters into words
            # This also collects hyphens in hyphenated words
            inWord = True
            currentWord += char
        else:
            # White space; if in a word, save it
            if inWord:
                tokens.append(currentWord.lower())
                currentWord = ''
                inWord = False
    # Handle the last word
    if inWord:
        tokens.append(currentWord.lower())
    return tokens

#
# First-order model (looks only at preceding word)
#
def makeFirstOrderModel(tokens: list[str]):
    # First-order model
    # A dictionary of (word, successors), where successors is a multiset; digraphs
    # We can determine probability of next word by its frequency in the multiset
    firstOrderModel = {}
    tokenCount = len(sourceTokens)
    for tokenIndex in range(0, tokenCount):
        token = sourceTokens[tokenIndex]
        nextToken = sourceTokens[tokenIndex+1] if tokenIndex+1 < tokenCount else ''
        if token not in firstOrderModel:
            firstOrderModel[token] = Multiset()
        firstOrderModel[token].add(nextToken)
    return firstOrderModel

def predictNextWordFirstOrder(model, currentWord, predecessor):
    # Using a first order model, predict the next word by
    # selecting from the known successors based on frequency.
    # predecessor is ignored
    nextWord = None
    if currentWord in model.keys():
        nextWord = random.choice(list(model[currentWord]))
    return nextWord

def generateSentenceFirstOrder(model, starter):
    # Using a first order model and starting from the given
    # word, generate until end of sentence
    sentence = ''
    currentWord = starter
    while not isEndOfSentence(currentWord):
        sentence += (' ' + currentWord)
        currentWord = predictNextWordFirstOrder(model, currentWord, '')
    sentence += currentWord if currentWord else '.'  # Trailing period, question mark, or exclamation
    return sentence

#
# Second-order model (looks at preceding two words)
#
def makeSecondOrderModel(tokens: list[str]):
    # Second-order model
    # A dictionary of (word, (predecessor, successors)), where successors is a multiset; trigraphs
    # We can determine probability of next word by its frequency in the multiset
    secondOrderModel = {}
    predecessor = ''
    tokenCount = len(sourceTokens)
    for tokenIndex in range(0, tokenCount):
        token = sourceTokens[tokenIndex]
        nextToken = sourceTokens[tokenIndex+1] if tokenIndex+1 < tokenCount else ''
        if token not in secondOrderModel:
            secondOrderModel[token] = {}
        if predecessor not in secondOrderModel[token]:
            (secondOrderModel[token])[predecessor] = Multiset()
        (secondOrderModel[token])[predecessor].add(nextToken)
        predecessor = token
    return secondOrderModel

def predictNextWordSecondOrder(model, currentWord, predecessor):
    # Using a second order model, predict the next word by
    # selecting from the known successors based on frequency
    nextWord = None
    if currentWord in model.keys():
        nextWord = random.choice(list((model[currentWord])[predecessor]))
    return nextWord

def getRandomPredecessorSecondOrder(model, currentWord):
    predecessor = None
    if currentWord in model.keys():
        predecessor = random.choice(list(model[currentWord].keys()))
    return predecessor

def generateSentenceSecondOrder(model, starter):
    # Using a second order model and starting from the given
    # word, generate until end of sentence
    sentence = ''
    currentWord = starter
    predecessor = getRandomPredecessorSecondOrder(model, currentWord)
    while not isEndOfSentence(currentWord):
        sentence += (' ' + currentWord)
        newPredecessor = currentWord
        currentWord = predictNextWordSecondOrder(model, currentWord, predecessor)
        predecessor = newPredecessor
    sentence += currentWord if currentWord else '.'  # Trailing period, question mark, or exclamation
    return sentence

# Main line
if __name__ == '__main__':
    # Get some training text
    sourceText = ''
    sourceTextFileNames = input('Enter comma-separated source text file names: ')
    for filename in sourceTextFileNames.split(','):
        file = io.open(filename.strip(), mode="r", encoding="utf-8")
        sourceText += file.read()
        sourceText += '\n'
        file.close()

    # Tokenize it into words and punctuation
    sourceTokens = tokenize(sourceText)

    # Test stub: word counts
    counts = Counter(sourceTokens)
    print(counts)

    # First-order model (looks only at previous token)
    # This model is a dictionary of multisets
    firstOrderModel = makeFirstOrderModel(sourceTokens)

    # Second-order model (looks at previous two tokens)
    # This model is a dictionary of dictionaries of multisets
    secondOrderModel = makeSecondOrderModel(sourceTokens)

    """
        Test cases, based on starter words from "Wuthering Heights"
    
        In the "Wuthering Heights" source text, the starter words
        occur the following numbers of times. 

            this:       294
            precincts:  1
            truth:      20
            once:       76
            heathcliff: 54

        Obviously a word that occurs only once in the training data
        will always be followed by the same word when generating
    """
    testWords = ['this', 'precincts', 'truth', 'once', 'heathcliff', 'conversation', 'bolkónski']
    print()
    for testWord in testWords:
        print(f'\nFirst-order variations on \'{testWord}\':')
        for i in range(10):
            result = generateSentenceFirstOrder(firstOrderModel, testWord)
            print(result)
        print(f'\nSecond-order variations on \'{testWord}\':')
        for i in range(10):
            result = generateSentenceSecondOrder(secondOrderModel, testWord)
            print(result)
