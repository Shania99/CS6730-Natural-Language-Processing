from util import *

import numpy as np

class InformationRetrieval():

    def __init__(self):
        self.index = None

    def buildIndex(self, docs, docIDs):
        """
        Builds the document index in terms of the document
        IDs and stores it in the 'index' class variable

        Parameters
        ----------
        arg1 : list
            A list of lists of lists where each sub-list is
            a document and each sub-sub-list is a sentence of the document
        arg2 : list
            A list of integers denoting IDs of the documents
        Returns
        -------
        None
        """
   
        
        index = None
        N = len(docs) #finding the total number of documents
        
        DF = {} #Dictionary which will contain keys: terms, values: corresponding documents it is present in (Note: These are not the document IDs as we are interested in number of docs and not the specific docs)
        for i in range(len(docs)):
            for j in range(len(docs[i])):
                for k in docs[i][j]:
            
                    try:
                        DF[k].add(i)
                    except:
                        DF[k] = {i}
        
        #Finding the document frequency of each unique term
        for i in DF:
            DF[i] = len(DF[i])
        self.DF = DF #Now, DF is a dictionary with key = unique terms, value = document frequency
        
        #list of unique terms in considering all the docs
        term_list = list(DF.keys())
        self.term_list = term_list
        
        #list of documnent frequencies of the terms
        df = list()
        for i in range(len(DF)):
            df.append(DF[self.term_list[i]])
        self.df = df
        
        #Finding the inverse document frequencies
        idf = np.log((np.array(N))/(np.array(self.df)))
        self.idf = idf
   

        #Computing the term-document matrix   
        TermDoc_matrix = np.zeros((len(DF),len(docs))) 
        for i in range(len(docs)):       
            for j in range(len(docs[i])):  
                for word in docs[i][j]:
                    try:
                        TermDoc_matrix[self.term_list.index(word),i] += 1
                    except:
                        dummy_var = 0
        
        self.TermDoc_matrix = TermDoc_matrix
        
                
        #Computing the document vectors
        self.doc_vectors = np.zeros((len(self.term_list),len(docs)))
        for i in range(len(self.term_list)):
            self.doc_vectors[i,:] = self.idf[i]*TermDoc_matrix[i,:] 
            
        # Dictionary with keys:doc_IDs
        index = {key: None for key in docIDs}  
        for i in range(len(docs)):
            index[docIDs[i]] = self.doc_vectors[:,i] # updating values with document vectors                
        
        self.index = index
    
    

    def rank(self, queries):

        """
		Rank the documents according to relevance for each query

		Parameters
		----------
		arg1 : list
			A list of lists of lists where each sub-list is a query and
			each sub-sub-list is a sentence of the query
		

		Returns
		-------
		list
			A list of lists of integers where the ith sub-list is a list of IDs
			of documents in their predicted order of relevance to the ith query
		"""
        doc_IDs_ordered = []

        #Fill in code here
        

        #Computing the term-queries matrix
        term_queries_matrix = np.zeros((len(self.term_list), len(queries)))
        for i in range(len(queries)):
            for j in range(len(queries[i])):
                for word in queries[i][j]:
                    try:
                        term_queries_matrix[self.term_list.index(word), i] +=1
                    except:
                        dummy_var = 0
        
        self.term_queries_matrix = term_queries_matrix
        # TF-IDF representation of the queries 
        term_queries_tfidf_matrix = np.zeros((len(self.term_list),len(queries)))
        for i in range(len(self.term_list)):
            term_queries_tfidf_matrix[i,:] = self.idf[i]*term_queries_matrix[i,:]
                        
        self.term_queries_tfidf_matrix = term_queries_tfidf_matrix
        document_IDs = list(self.index.keys()) #list of docIDs
        doc_IDs_ordered  = list(range(len(queries)))
    
        for i in range(len(queries)):#iterating over the queries
            cosine_similarities = {key: None for key in document_IDs} #dictionary with key: doc_IDs
            for j in range(len(self.index)):
                x = self.index[document_IDs[j]]
                y = self.term_queries_tfidf_matrix[:,i]
                cosine_similarities[document_IDs[j]] = np.dot(x,y)/(np.linalg.norm(x)*np.linalg.norm(y)) #computing the cosine similarities between query and all the document vectors

            rank_cosine_similarities = sorted(cosine_similarities.items(), key = lambda kv: kv[1],reverse = True) #sorting the docs based on predicted order of relevance
            doc_IDs_ordered[i] = [k[0] for k in rank_cosine_similarities] #adding the list of docs in the predicted order of relevance for the ith query
            
        return doc_IDs_ordered

            