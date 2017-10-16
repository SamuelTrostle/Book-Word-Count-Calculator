
with open('book.txt') as myFile:
    # Set a variable to the contents, use .read() extension to read contents
    contents = myFile.read()
    #print(contents)
def word_count(book):
    novel_text = book.lower().split()
    words = {}
    for x in novel_text:
        if x in words:
            words[x] += 1
        else:
            words[x] = 1
    print(words)
word_count(contents)