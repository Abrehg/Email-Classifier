import re
import nltk
from nltk.corpus import stopwords
from emoji import UNICODE_EMOJI
import contractions
from nltk.stem import PorterStemmer
from nltk.stem import WordNetLemmatizer
from nltk import pos_tag
from nltk import ne_chunk

def is_emoji(s):
    for emoji in UNICODE_EMOJI["en"]:
        if emoji == s:
            return True
    return False

def normalize_text(input):
    endLoop = False
    count = 0
    emoticon = 0
    # make lowercase (not working, saying input is a list instead of string)
    test = str(input).lower()
    # expanding abbreviations/contractions
    test = contractions.fix(test)
    # removing punctuation
    input = re.sub("[!”#$%&’()*+,-./:;<=>?@[\]^_`{|}~]", "", test)
    # removing white spaces
    test = input.strip()
    # tokenize string
    tagged_input = nltk.word_tokenize(test)
    lemat = [""]
    lemat.pop(0)
    i = 0
    limit = len(tagged_input)
    while count < limit:
      is_stopword = False
      # remove unicode
      if tagged_input[count] == "\u200c":
          tagged_input.pop(count)
          limit = limit - 1
          continue
      #remove empty element
      if tagged_input[count] == "":
          tagged_input.pop(count)
          limit = limit - 1
          continue
      #check for emojis
      stop = stopwords.words("english")
      i = 0
      result = is_emoji(tagged_input[count])
      if result == True:
         limit = limit - 1
         tagged_input.pop(count)
         emoticon = 1
         continue
      #removing stop words
      while i < len(stop):
        if tagged_input[count] == stop[i]:
          tagged_input.pop(count)
          limit = limit - 1
          is_stopword = True
          break
        i = i + 1
      if is_stopword == True:
          continue
      # Lemmatization
      lemmatizer = WordNetLemmatizer()
      lemat.append(lemmatizer.lemmatize(tagged_input[count]))
      #text stemming
      ps = PorterStemmer()
      tagged_input[count] = ps.stem(lemat[count])
      #removing words less than 3 letters long
      if len(tagged_input[count]) < 3:
          tagged_input.pop(count)
          limit = limit - 1
      count = count + 1
    #Part of Speech tagging
    #input = pos_tag(tagged_input)
    #Chunking/Named entity recognition
    #tagged_input = ne_chunk(input)
    #output
    output = tagged_input
    return output, emoticon
