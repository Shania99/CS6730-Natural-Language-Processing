from util import *

# Add your import statements here
import nltk.data



class SentenceSegmentation():

	def naive(self, text):
		"""
		Sentence Segmentation using a Naive Approach

		Parameters
		----------
		arg1 : str
			A string (a bunch of sentences)

		Returns
		-------
		list
			A list of strings where each string is a single sentence
		"""
		# punctuations = ['.','!','?']
		newText = text.replace('!','.').replace('?','.')
		segmentedText = newText.split('.')
		if segmentedText[-1]=='':
			segmentedText.pop()
		return segmentedText



	# def augmented_tokenization(self, segmentedText):
	# 	"""
	# 	Takes text segmented using punkt and removed hyphens and slashes and extra spaces

	# 	Args:
	# 		segmentedText ([type]): [description]
	# 	"""


	def punkt(self, text):
		"""
		Sentence Segmentation using the Punkt Tokenizer

		Parameters
		----------
		arg1 : str
			A string (a bunch of sentences)

		Returns
		-------
		list
			A list of strings where each strin is a single sentence
		"""
		tokenizer = nltk.data.load('tokenizers/punkt/english.pickle')
		segmentedText = tokenizer.tokenize(text)
		return segmentedText


