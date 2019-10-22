from nltk.tokenize import sent_tokenize, word_tokenize
from sumy.parsers.plaintext import PlaintextParser 
from sumy.nlp.tokenizers import Tokenizer 
from sumy.summarizers.lex_rank import LexRankSummarizer 

import time

start_time = time.clock()
file = "inputtext.txt"
parser = PlaintextParser.from_file(file, Tokenizer("english"))
summarizer = LexRankSummarizer()

summary = summarizer(parser.document, 5)

for sentence in summary:
    print (sentence)


print (time.clock() - start_time, "seconds")
