def search(keyword) :
    # implement the function here
   class Entry:
      def __init__(self, word, synonyms):
         self.word = word
         self.synonyms = synonyms
   #e1 = Entry("dog", ["doggie", "puppy"])
   #e2 = Entry("cat", ["kitty"])

   #Thesaurus = [e1, e2]

   #doc1 = ["this", "is", "a", "single", "document"]
   #doc2 = ["here", "is", "another", "document"]

   #Corpus = [doc1, doc2]

   All_words = [keyword]
   for Entry in Thesaurus:
      if keyword == Entry.word:
         for word in Entry.synonyms:
            All_words.append(word)
         break
   for search_word in All_words:
      count = 0
      for document in Corpus:
         for word in document:
            if search_word == word:
               count += 1
      #return search_word, count

   return search_word, count

input = "happy"
output = search(input) # invoke the method using a test input
print(output) # prints the output of the function
# do not remove this line!
