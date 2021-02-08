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


def extractUnigram(poem, pruningNedded):
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
        unigramDictForEachPoem.append(extractUnigram(poem, True))
    for unigramDict in unigramDictForEachPoem:
        print(len(unigramDict))



main()