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
    for line in poem:
        print(line)


def main():
    # ferdosi = "ferdowsi_train.txt"
    # hafez = "hafez_train.txt"
    # molavi = "molavi_train.txt"
    poets = ["ferdowsi_train.txt", "hafez_train.txt", "molavi_train.txt"]
    print(poets)
    trainFilePath = "./train_set/"
    poems = []
    for file in poets:
        # extractInputFile(file, trainFilePath)
        poems.append(extractInputFile(file, trainFilePath))

    extractUnigram(poems[0])


main()