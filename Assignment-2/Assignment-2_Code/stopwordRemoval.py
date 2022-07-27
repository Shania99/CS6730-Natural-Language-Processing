from util import *

# Add your import statements here
from nltk.corpus import stopwords




class StopwordRemoval():

	def fromList(self, text):
		"""
		Sentence Segmentation using the Punkt Tokenizer

		Parameters
		----------
		arg1 : list
			A list of lists where each sub-list is a sequence of tokens
			representing a sentence

		Returns
		-------
		list
			A list of lists where each sub-list is a sequence of tokens
			representing a sentence with stopwords removed
		"""

		stopwordRemovedText = ['']*len(text)

		#Fill in code here
		stopWords = stopwords.words('english')
		#Fill in code here
		for i, word_list in enumerate(text):
			stopwordRemovedText[i] = [word for word in word_list if word not in stopWords ]
	
		
		return stopwordRemovedText



