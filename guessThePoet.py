import io


def extractInputFile(file, path):

    location = path + file
    print(location)
    txt = []
    with io.open(location, 'r', encoding='utf-8') as f:
       for line in f:
            txt.append(line)

    print(type(txt))
    return txt


def pruningNotImportantWord(dictionary):
    for key in list(dictionary.keys()):
        if dictionary[key] <= 2:
            del dictionary[key]
    return dictionary


def unigram(poem, pruningNedded):
    unigramDict = dict()
    for line in poem:
        line = line.strip()
        words = line.split()
        for word in words:
            if word in unigramDict:
                unigramDict[word] += 1
            else:
                unigramDict[word] = 1
    if pruningNedded:
        print("dict length before pruning: ", len(unigramDict))
        return pruningNotImportantWord(unigramDict)
    else:
        print("dict length without pruning: ", len(unigramDict))
        return unigramDict


def bigram(poem):
    bigramDict = dict()
    for line in poem:
        # print(line)
        words = line.split()
        # print(words)
        for i in range(len(words)):
            if words[i] not in bigramDict:
                bigramDict[words[i]] = dict()
                bigramDict.setdefault(words[i], {})['s'] = 0
                bigramDict.setdefault(words[i], {})['e'] = 0
            if i == 0:
                # start of the poem
                bigramDict[words[i]]['s'] += 1
            else:
                if i == len(words) - 1:
                    # end of the poem
                    bigramDict[words[i]]['e'] += 1
                if words[i-1] not in bigramDict[words[i]]:
                    bigramDict.setdefault(words[i], {})[words[i-1]] = 1
                else:
                    bigramDict[words[i]][words[i-1]] += 1

    # print(len(bigramDict))
    # for key, value in bigramDict.items():
    #     print(key)
    #     print(value)
    #     print("********")
    return bigramDict

def train():
    poets = ["ferdowsi_train.txt", "hafez_train.txt", "molavi_train.txt"]
    print(poets)
    trainFilePath = "./train_set/"
    poems = []
    for file in poets:
        # extractInputFile(file, trainFilePath)
        poems.append(extractInputFile(file, trainFilePath))

    unigramDictForEachPoem = list()
    for poem in poems:
        unigramDictForEachPoem.append(unigram(poem, False))
    # for unigramDict in unigramDictForEachPoem:
    #     print(len(unigramDict))

    bigramDictForEachPoem = list()
    bigram(poems[0])
    for poem in poems:
        bigramDictForEachPoem.append(bigram(poem))
    return unigramDictForEachPoem, bigramDictForEachPoem

# return the list: unigram value of the input word in all of the poets files
def unigramCalculator(unigramDictForEachPoem, word):
    numberOfWords = list()
    numberOfRepetation = [0,0,0]
    for i in range(len(unigramDictForEachPoem)):
        numberOfWords.append(len(unigramDictForEachPoem[i]))
        # print("fuck: ", numberOfWords)
        try:
            # print(unigramDictForEachPoem[i][word])
            # print(numberOfWords[i])
            numberOfRepetation[i] = unigramDictForEachPoem[i][word] / numberOfWords[i]
        except:
            numberOfRepetation[i] = 0
    # print(numberOfRepetation)
    return numberOfRepetation


def bigramCalculator(bigramDictForEachPoem,unigramDictForEachPoem, word, pastWord, position):
    numberOfLinesOfEachPoem = [9000, 7700, 8000]
    numberOfRepetation = [0, 0, 0]
    for i in range(len(bigramDictForEachPoem)):
        # print("i: ", i)
        try:
            if position is 's':
                numberOfRepetation[i] = bigramDictForEachPoem[i][word]['s'] / numberOfLinesOfEachPoem[i]
            elif position is 'e':
                numberOfRepetation[i] = bigramDictForEachPoem[i][word]['e'] / numberOfLinesOfEachPoem[i]
            else:
                # print("sorat: ", bigramDictForEachPoem[i][word][pastWord])
                # print("makhraj: ", unigramDictForEachPoem[i][pastWord])
                numberOfRepetation[i] = bigramDictForEachPoem[i][word][pastWord] / unigramDictForEachPoem[i][pastWord]
        except:
            numberOfRepetation[i] = 0

    # print(numberOfRepetation)
    return numberOfRepetation


def test(unigramDictForEachPoem, bigramDictForEachPoem):
    l1 = 0.3333
    l2 = 0.3333
    l3 = 0.3333
    e = 0.0000001
    path = "./test_set/"
    file = "test_file.txt"
    poems = extractInputFile(file, path)
    ferdowsiSize = 9000
    hafezSize = 7700
    molaviSize = 8000
    i = 0
    for line in poems:
        print(line)
        words = line.split()
        poetOfThisPoem = words[0]
        backOff = [1.0, 1.0, 1.0]
        for i in range(len(words)):
            if not i == 0:
                unigramValueOfThisWordForEachPoet = unigramCalculator(unigramDictForEachPoem, words[i])
                # print("word[i]: ", words[i])
                # if i == 1:
                #     print("word[i-1]: ", "f")
                # else:
                #     print("word[i-1]: ", words[i - 1])
                if i == 1:
                    bigramValueOfThisWordForEachPoet = bigramCalculator(bigramDictForEachPoem, unigramDictForEachPoem, words[i], "f", 's')
                elif i == len(words) - 1:
                    bigramValueOfThisWordForEachPoet = bigramCalculator(bigramDictForEachPoem, unigramDictForEachPoem, words[i], words[i-1], 'e')
                else:
                    bigramValueOfThisWordForEachPoet = bigramCalculator(bigramDictForEachPoem, unigramDictForEachPoem, words[i], words[i-1], 'm')
                # print(unigramValueOfThisWordForEachPoet)
                # print(bigramValueOfThisWordForEachPoet)
                for i in range(len(backOff)):
                    backOff[i] *= ((l3 * bigramValueOfThisWordForEachPoet[i]) + (l2 * unigramValueOfThisWordForEachPoet[i]) + (l1 * e))
        print("each poet probability: ", backOff)



        i += 1
        if i == 10:
            return



def main():
    unigramDictForEachPoem, bigramDictForEachPoem = train()
    test(unigramDictForEachPoem, bigramDictForEachPoem)





main()


# for bigramDict in bigramDictForEachPoem:
    #         i = 0
    #         print("i: ", i)
    #         for key, value in bigramDict.items():
    #             print(key)
    #             print(value)
    #             print("********")
    #             i += 1
    #             if i == 10:
    #                 break
    #         print(len(bigramDict))