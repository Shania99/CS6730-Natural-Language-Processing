from util import *

# Add your import statements here

from nltk.stem import WordNetLemmatizer

class InflectionReduction:

	def reduce(self, text):
		"""
		Stemming/Lemmatization

		Parameters
		----------
		arg1 : list
			A list of lists where each sub-list a sequence of tokens
			representing a sentence

		Returns
		-------
		list
			A list of lists where each sub-list is a sequence of
			stemmed/lemmatized tokens representing a sentence
		"""

		reducedText = ['']*len(text)

		#Fill in code here
		
		lemma = WordNetLemmatizer()
		for i, word_list in enumerate(text):
			reducedText[i] = [lemma.lemmatize(word) for word in word_list]

		return reducedText


