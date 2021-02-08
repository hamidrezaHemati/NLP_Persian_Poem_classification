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

    print(len(bigramDict))
    for key, value in bigramDict.items():
        print(key)
        print(value)
        print("********")




def main():
    poets = ["ferdowsi_train.txt", "hafez_train.txt", "molavi_train.txt"]
    print(poets)
    trainFilePath = "./train_set/"

    poems = []
    for file in poets:
        # extractInputFile(file, trainFilePath)
        poems.append(extractInputFile(file, trainFilePath))

    unigramDictForEachPoem = list()
    for poem in poems:
        unigramDictForEachPoem.append(unigram(poem, True))
    for unigramDict in unigramDictForEachPoem:
        print(len(unigramDict))

    bigramForEachPoem = list()
    bigram(poems[0])
    # for poem in poems:
    #     bigram(poem)




main()