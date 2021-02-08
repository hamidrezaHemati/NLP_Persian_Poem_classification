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


def extractUnigram(poem):
    unigramDict = dict()
    for line in poem:
        line = line.strip()
        words = line.split()
        for word in words:
            if word in unigramDict:
                unigramDict[word] += 1
            else:
                unigramDict[word] = 1

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
        unigramDictForEachPoem.append(extractUnigram(poem))
    for unigramDict in unigramDictForEachPoem:
        print(len(unigramDict))
        # for key in list(unigramDict.keys()):
        #     print(key, ":", unigramDict[key])


main()