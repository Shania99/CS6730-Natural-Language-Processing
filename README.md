# CS6730: Natural Language Processing

Information retrieval (IR) is the process of obtaining information system resources that are relevant to an
information need from a collection of those resources. Searches can be based on full-text or other content-based
indexing. It is the science of searching for information in a document, searching for documents themselves, and
also searching for the metadata that describes data, and for databases of texts, images or sounds.
The cranfield dataset contains 225 queries and 1400 documents and ground truth with relevant documents
for each query, with positions of importance, ranging from 1 to 4, 1 being the most important.
The aim of this project is to build an information retrieval system to retrieve the relevant documents from the
cranfield dataset for all queries in the dataset and evaluate its performance on 225 queries and 1400 documents
using the following metrics: Precision@k, Recall@k, F-score@k, Mean Average Precision@k and nDCG@k, to
see how the system fares against ground truth relevances.
