class TextAnalyzer:

    def __init__(self):
        self.bookNums = [1, 2, 3, 4, 5, 6, 7]

    def decryptTexts(self) -> None:
        """Decrypts all books using the cipher.txt file"""
        # Open cipher file
        with open("cipher.txt", "r", encoding="utf-8") as f:
            txtLines = f.readlines()
        # Build decryption dictionary
        decryptionDict = {}
        for lineIndex in range(len(txtLines)):
            txtLines[lineIndex] = txtLines[lineIndex].replace("\n", "")
            if txtLines[lineIndex][0] != "#":
                charSubstitution = txtLines[lineIndex].split("->")
                decryptionDict[charSubstitution[1]] = charSubstitution[0]
                decryptionDict[charSubstitution[1].upper()] = charSubstitution[0].upper()
        # For all books
        for bookNum in self.bookNums:
            # Read in book
            with open("Book" + str(bookNum) + "_encrypted.txt", "r", encoding="utf-8") as f:
                bookString = f.read()
            decryptionTable = bookString.maketrans(decryptionDict)
            decryptedBook = bookString.translate(decryptionTable)
            # Save book output
            with open("Book" + str(bookNum) + "_plain.txt", "w", encoding="utf-8") as f:
                f.write(decryptedBook)

    def replaceWord(self, stringToFind: str, replacementString: str) -> None:
        """Finds all occurrences of one string and replaces them with another"""
        # For all books
        for bookNum in self.bookNums:
            # Read in book
            with open("Book" + str(bookNum) + "_plain.txt", "r", encoding="utf-8") as f:
                bookString = f.read()
            replacedBook = bookString.replace(stringToFind, replacementString)
            # Save book output
            with open("Book" + str(bookNum) + "_replaced.txt", "w", encoding="utf-8") as f:
                f.write(replacedBook)

    def countOccurrences(self, stringToCount: str) -> int:
        """Counts the number of times the string appears in the text"""
        # For all books
        count = 0
        for bookNum in self.bookNums:
            # Read in book
            with open("Book" + str(bookNum) + "_plain.txt", "r", encoding="utf-8") as f:
                bookString = f.read()
            # Count occurrences
            count += bookString.count(stringToCount)
        print(stringToCount + " Occurrences: " + str(count))
        return count

    def countSameSentenceOccurrences(self, firstString: str, secondString: str) -> int:
        """Counts the number of times two strings appear in the same sentence"""
        # For all books
        count = 0
        for bookNum in self.bookNums:
            # Read in book
            with open("Book" + str(bookNum) + "_plain.txt", "r", encoding="utf-8") as f:
                bookString = f.read()
            # Split on sentences
            sentences = bookString.split(".")
            # TODO - Update to split on '?' and '!' as well
            for sentence in sentences:
                # Count if and only if both strings in sentence
                if sentence.count(firstString) > 0 and sentence.count(secondString) > 0:
                    count += 1
        return count
