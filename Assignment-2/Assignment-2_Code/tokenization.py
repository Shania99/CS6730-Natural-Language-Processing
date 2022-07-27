from util import *
from nltk.tokenize import TreebankWordTokenizer
# Add your import statements here




class Tokenization():

	def naive(self, text):
		"""
		Tokenization using a Naive Approach

		Parameters
		----------
		arg1 : list
			A list of strings where each string is a single sentence

		Returns
		-------
		list
			A list of lists where each sub-list is a sequence of tokens
		"""

		tokenizedText = ['']*len(text)

		#Fill in code here
		for i,sentence in enumerate(text):
			sentence = sentence.replace(',','').replace(';','').replace("-", ' ').replace("/", "")
			tokenizedText[i] = sentence.split(' ')

		return tokenizedText



	def pennTreeBank(self, text):
		"""
		Tokenization using the Penn Tree Bank Tokenizer

		Parameters
		----------
		arg1 : list
			A list of strings where each string is a single sentence

		Returns
		-------
		list
			A list of lists where each sub-list is a sequence of tokens
		"""
		#Fill in code here
		tokenizedText = ['']*len(text)
		treeBank = TreebankWordTokenizer()
		#Fill in code here
		for i,sentence in enumerate(text):
			tokenizedText[i] = [sentence[start:end] for start, end in treeBank.span_tokenize(sentence)]
		return tokenizedText


