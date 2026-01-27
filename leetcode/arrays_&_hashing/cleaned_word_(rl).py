def CleanedWord(paragraph):
   split1 = paragraph.split(" ")
   cleaned = []

   for word in split1: 
      new_word = ""

      for char in word: 
         if char.isalnum(): 
            new_word += char

      new_word = new_word.lower()

      if new_word != "": 
         cleaned.append(new_word)
    

print(CleanedWord("Bob hit a ball, the hit BALL flew far after it was hit."))