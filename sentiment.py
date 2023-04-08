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

   final = []
   All_words = [keyword]
   for Entry in Thesaurus:
      if keyword == Entry.word:
         for word in Entry.synonyms:
            All_words.append(word)
   for keyword in All_words:
      count = 0
      for document in Corpus:
         for word in document:
               if keyword == word:
                  count += 1
                  result = (keyword, count)
      final.append(result)
   return final

input = "happy"
output = search(input) # invoke the method using a test input
print(output) # prints the output of the function
# do not remove this line!
