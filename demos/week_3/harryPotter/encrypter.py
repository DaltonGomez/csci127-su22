class Encrypter:

    def __init__(self):
        self.bookNums = [1, 2, 3, 4, 5, 6, 7]

    def encryptText(self) -> None:
        with open("cipher.txt", "r", encoding="utf-8") as cipherFile:
            cipherLines = cipherFile.readlines()
        encryptionDict = {}
        for lineIdx in range(len(cipherLines)):
            cipherLines[lineIdx] = cipherLines[lineIdx].replace("\n", "")
            if cipherLines[lineIdx][0] != "#":
                encryptionList = cipherLines[lineIdx].split("->")
                encryptionDict[encryptionList[0]] = encryptionList[1]
                encryptionDict[encryptionList[0].upper()] = encryptionList[1].upper()
        print(encryptionDict)
        # FOR EACH BOOK
        for bookNum in self.bookNums:
            with open("Book" + str(bookNum) + "_Plaintext.txt", "r", encoding="utf-8") as book:
                bookString = book.read()
            encryptionMap = bookString.maketrans(encryptionDict)
            encryptedString = bookString.translate(encryptionMap)
            with open("Book" + str(bookNum) + "_Encrypted.txt", "w", encoding="utf-8") as encryptedBook:
                encryptedBook.write(encryptedString)


if __name__ == "__main__":
    encrypter = Encrypter()
    encrypter.encryptText()
