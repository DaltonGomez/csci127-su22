# Import Google's Text To Speech
from gtts import gTTS

# MY CODE
bookName = "alice_in_wonderland"
with open(bookName + ".txt", encoding="utf8") as f:
    bookAsString = f.read()

# Language in which you want to convert
language = "en"

# Passing the text and language to the engine,
audioBook = gTTS(text=bookAsString, lang=language, slow=False)

# Saving the converted audio in a mp3 file
audioBook.save("AiW.mp3")
