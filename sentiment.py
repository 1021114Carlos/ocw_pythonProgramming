def search(keyword):
    #implement the function here
    class Entry:
        def __init__(self, word, synonyms):
            self.word = word
            self.synonyms = synonyms
            
    e1 = Entry("dog", ["cheerful", "mad", "delighted"])
    e2 = Entry("nature", ["tiger", "waterfall", "joyful"])

    Thesaurus = [e1, e2]
    
    doc1 = ["this", "is", "a", "single", "document"]
    doc2 = ["here", "is", "another", "document"]
    
    Corpus = [doc1, doc2]
    
    word_list = []
    All_words = [keyword]
    for Entry in Thesaurus:
        if keyword == Entry.word:
            if word in Entry.synonyms:
                All_words.append(word)
            break
    for search_word in All_words:
        count = 0
        for document in Corpus:
            for word in document:
                if search_word == word:
                    count += 1
                    word_list.append(search_word)

    return [search_word, count]

input = "happy"
output = search(input) # invoke the method using a test input
print(output) # prints the output of the function
# do not remove this line!
