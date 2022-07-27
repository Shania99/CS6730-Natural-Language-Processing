from util import *
# Add your import statements here
import math



class Evaluation():

	def queryPrecision(self, query_doc_IDs_ordered, query_id, true_doc_IDs, k):
		
		# sourcery skip
		"""
		Computation of precision of the Information Retrieval System
		at a given value of k for a single query

		Parameters
		----------
		arg1 : list
			A list of integers denoting the IDs of documents in
			their predicted order of relevance to a query
		arg2 : int
			The ID of the query in question
		arg3 : list
			The list of IDs of documents relevant to the query (ground truth)
		arg4 : int
			The k value

		Returns
		-------
		float
			The precision value as a number between 0 and 1
		"""
		# print("query_doc_IDs_ordered[:k]", query_doc_IDs_ordered[:k])
		# print("true_doc_IDs", true_doc_IDs)
		# print("set", set(query_doc_IDs_ordered[:k]).intersection(set(true_doc_IDs)))
		num_returned_relevant = len(set(query_doc_IDs_ordered[:k]).intersection(set(true_doc_IDs)))
		precision = num_returned_relevant / len(query_doc_IDs_ordered[:k])
		# print("in query precision", precision)
		return precision


	def meanPrecision(self, doc_IDs_ordered, query_ids, qrels, k):
		# sourcery skip
		"""
		Computation of precision of the Information Retrieval System
		at a given value of k, averaged over all the queries

		Parameters
		----------
		arg1 : list
			A list of lists of integers where the ith sub-list is a list of IDs
			of documents in their predicted order of relevance to the ith query
		arg2 : list
			A list of IDs of the queries for which the documents are ordered
		arg3 : list
			A list of dictionaries containing document-relevance
			judgements - Refer cran_qrels.json for the structure of each
			dictionary
		arg4 : int
			The k value

		Returns
		-------
		float
			The mean precision value as a number between 0 and 1
		"""
		precision_list = []
		
		for i, query_id in enumerate(query_ids):
			predicted = doc_IDs_ordered[i]
			ground_truth = get_ground_truth(query_id, qrels)
			# print("ground truth is", ground_truth)
			precision = self.queryPrecision(predicted, query_id, ground_truth, k)
			precision_list.append(precision)
		
		meanPrecision = sum(precision_list)/len(precision_list)
		# print(meanPrecision)
		return meanPrecision

	
	def queryRecall(self, query_doc_IDs_ordered, query_id, true_doc_IDs, k):
		# sourcery skip
		"""
		Computation of recall of the Information Retrieval System
		at a given value of k for a single query

		Parameters
		----------
		arg1 : list
			A list of integers denoting the IDs of documents in
			their predicted order of relevance to a query
		arg2 : int
			The ID of the query in question
		arg3 : list
			The list of IDs of documents relevant to the query (ground truth)
		arg4 : int
			The k value

		Returns
		-------
		float
			The recall value as a number between 0 and 1
		"""

		

		#Fill in code here
		num_returned_relevant = len(set(query_doc_IDs_ordered[:k]).intersection(set(true_doc_IDs)))
		recall = num_returned_relevant/len(true_doc_IDs)
		# print(recall)
		return recall


	def meanRecall(self, doc_IDs_ordered, query_ids, qrels, k):
		# sourcery skip
		"""
		Computation of recall of the Information Retrieval System
		at a given value of k, averaged over all the queries

		Parameters
		----------
		arg1 : list
			A list of lists of integers where the ith sub-list is a list of IDs
			of documents in their predicted order of relevance to the ith query
		arg2 : list
			A list of IDs of the queries for which the documents are ordered
		arg3 : list
			A list of dictionaries containing document-relevance
			judgements - Refer cran_qrels.json for the structure of each
			dictionary
		arg4 : int
			The k value

		Returns
		-------
		float
			The mean recall value as a number between 0 and 1
		"""
		recall_list = []
		for i, query_id in enumerate(query_ids):
			predicted = doc_IDs_ordered[i]
			ground_truth = get_ground_truth(query_id, qrels)
			recall = self.queryRecall(predicted, query_id, ground_truth, k)
			recall_list.append(recall)
		
		meanRecall = sum(recall_list)/len(recall_list)
		
		# print(meanRecall)
		#Fill in code here

		return meanRecall


	def queryFscore(self, query_doc_IDs_ordered, query_id, true_doc_IDs, k):
		# sourcery skip
		"""
		Computation of fscore of the Information Retrieval System
		at a given value of k for a single query

		Parameters
		----------
		arg1 : list
			A list of integers denoting the IDs of documents in
			their predicted order of relevance to a query
		arg2 : int
			The ID of the query in question
		arg3 : list
			The list of IDs of documents relevant to the query (ground truth)
		arg4 : int
			The k value

		Returns
		-------
		float
			The fscore value as a number between 0 and 1
		"""

		precision = self.queryPrecision(query_doc_IDs_ordered, query_id, true_doc_IDs, k)
		recall = self.queryRecall(query_doc_IDs_ordered, query_id, true_doc_IDs, k)
		# print("fscore precision", precision)
		# print("fscore recall", recall)
		if precision == 0 or recall == 0:
			fscore = 0
		else:
			fscore = 2*precision*recall/(precision + recall)

		#Fill in code here

		return fscore


	def meanFscore(self, doc_IDs_ordered, query_ids, qrels, k):
		# sourcery skip
		"""
		Computation of fscore of the Information Retrieval System
		at a given value of k, averaged over all the queries

		Parameters
		----------
		arg1 : list
			A list of lists of integers where the ith sub-list is a list of IDs
			of documents in their predicted order of relevance to the ith query
		arg2 : list
			A list of IDs of the queries for which the documents are ordered
		arg3 : list
			A list of dictionaries containing document-relevance
			judgements - Refer cran_qrels.json for the structure of each
			dictionary
		arg4 : int
			The k value
		
		Returns
		-------
		float
			The mean fscore value as a number between 0 and 1
		"""
		fscore_list = []
		for i, query_id in enumerate(query_ids):
			predicted = doc_IDs_ordered[i]
			ground_truth = get_ground_truth(query_id, qrels)
			fscore = self.queryFscore(predicted, query_id, ground_truth, k)
			fscore_list.append(fscore)
		
		meanFscore = sum(fscore_list)/len(fscore_list)
		

		#Fill in code here

		return meanFscore
	

	def queryNDCG(self, query_doc_IDs_ordered, query_id, true_doc_IDs, k):
		"""
		Computation of nDCG of the Information Retrieval System
		at given value of k for a single query

		Parameters
		----------
		arg1 : list
			A list of integers denoting the IDs of documents in
			their predicted order of relevance to a query
		arg2 : int
			The ID of the query in question
		arg3 : list
			The list of IDs of documents relevant to the query (ground truth)
		arg4 : int
			The k value

		Returns
		-------
		float
			The nDCG value as a number between 0 and 1
		"""
		relevance_dic = get_ground_truth(query_id, self.qrels, relevance=True)
		pred_relevance_list = []
		
		for doc_id in query_doc_IDs_ordered:
			if doc_id in relevance_dic:
				pred_relevance_list.append(relevance_dic[doc_id])
			else:
				pred_relevance_list.append(0)
		
		# print("pred_relevance_list", pred_relevance_list)

		dcg = 0
		###calculating dcg
		for i, rel_i in enumerate(pred_relevance_list[:k], start=1):
			dcg += rel_i / math.log((i + 1), 2)
		
		### calculating idcg
		relevance_list = list(relevance_dic.items())
		sorted_relevance_list = sorted(relevance_list, key=lambda x: x[1], reverse=True)
		ranked_true_docs = [i[1] for i in sorted_relevance_list]
		true_relevance_list = ranked_true_docs[:k]
		idcg = 0
		for i, rel_i in enumerate(true_relevance_list, start=1):
			idcg += rel_i / math.log((i + 1), 2)

		if idcg==0 or dcg==0:
			nDCG = 0
		else:
			nDCG = dcg / idcg

		return nDCG


	def meanNDCG(self, doc_IDs_ordered, query_ids, qrels, k):
		# sourcery skip
		"""
		Computation of nDCG of the Information Retrieval System
		at a given value of k, averaged over all the queries

		Parameters
		----------
		arg1 : list
			A list of lists of integers where the ith sub-list is a list of IDs
			of documents in their predicted order of relevance to the ith query
		arg2 : list
			A list of IDs of the queries for which the documents are ordered
		arg3 : list
			A list of dictionaries containing document-relevance
			judgements - Refer cran_qrels.json for the structure of each
			dictionary
		arg4 : int
			The k value

		Returns
		-------
		float
			The mean nDCG value as a number between 0 and 1
		"""
		self.qrels = qrels
		ndcg_list = []
		for i, query_id in enumerate(query_ids):
			true_doc_IDs = get_ground_truth(query_id,qrels)
			ndcg = self.queryNDCG(doc_IDs_ordered[i], query_id, true_doc_IDs, k)
			ndcg_list.append(ndcg)

		meanNDCG = sum(ndcg_list) / len(ndcg_list)
		return meanNDCG


	def queryAveragePrecision(self, query_doc_IDs_ordered, query_id, true_doc_IDs, k):
		# sourcery skip
		"""
		Computation of average precision of the Information Retrieval System
		at a given value of k for a single query (the average of precision@i
		values for i such that the ith document is truly relevant)

		Parameters
		----------
		arg1 : list
			A list of integers denoting the IDs of documents in
			their predicted order of relevance to a query
		arg2 : int
			The ID of the query in question
		arg3 : list
			The list of documents relevant to the query (ground truth)
		arg4 : int
			The k value

		Returns
		-------
		float
			The average precision value as a number between 0 and 1
		"""
		# precision_at_i =[]
		# for i, doc_id in enumerate(query_doc_IDs_ordered, start=1):
		# 	if doc_id in true_doc_IDs:
		# 		precision = self.queryPrecision(query_doc_IDs_ordered, query_id, true_doc_IDs, i)
		# 		precision_at_i.append(precision)
		# print("precision_at_i",precision_at_i)
		# avgPrecision = sum(precision_at_i)/len(precision_at_i)
		# print("avgPrecision", avgPrecision)
		
		# return avgPrecision
		num_relevant = 0
		precision_at_i = []
		
		for i,docID in enumerate(query_doc_IDs_ordered[:k],start=1):
			if docID in true_doc_IDs:
				num_relevant += 1
				precision_at_i.append(num_relevant / i)
				
		if num_relevant == 0:
			avgPrecision = 0
		else:    
			avgPrecision = sum(precision_at_i)/num_relevant     
		
		return avgPrecision


	def meanAveragePrecision(self, doc_IDs_ordered, query_ids, q_rels, k):
		# sourcery skip
		"""
		Computation of MAP of the Information Retrieval System
		at given value of k, averaged over all the queries

		Parameters
		----------
		arg1 : list
			A list of lists of integers where the ith sub-list is a list of IDs
			of documents in their predicted order of relevance to the ith query
		arg2 : list
			A list of IDs of the queries
		arg3 : list
			A list of dictionaries containing document-relevance
			judgements - Refer cran_qrels.json for the structure of each
			dictionary
		arg4 : int
			The k value

		Returns
		-------
		float
			The MAP value as a number between 0 and 1
		"""
		average_precision_list = []
		for i, query_id in enumerate(query_ids, start=1):
			predicted = doc_IDs_ordered[i-1]
			ground_truth = get_ground_truth(query_id, q_rels)
			avg_precision = self.queryAveragePrecision(predicted, query_id, ground_truth, k)
			average_precision_list.append(avg_precision)
		
		# print("precision_list",average_precision_list)
		meanAveragePrecision = sum(average_precision_list)/len(average_precision_list)
		
		

		return meanAveragePrecision

