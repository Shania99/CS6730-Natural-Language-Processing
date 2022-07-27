README:

The code cannot be run on the command line and should be run on a python notebook only.

path = ‘specify the path to cranfield dataset folder here’
cran_queries.json, cran_qrels.json, cran_docs.json must be in the same directory as the code and the remaining files.
Remaining files can be found at: https://drive.google.com/drive/folders/1rtTtwV0trUdkjWXjym6thTOd5OIIB7T5?usp=sharing

When  do_bigram = False (default)  in PennTreeBank Function, it tokenizes the sentences into 
If a ‘StopIteration’ error is raised while calling pipeline function to compute CleanDocs and CleanDocs_bigram, please run it again after a minute.

For the LSA Experiments block, ‘reduced_docs.txt’ and ‘reduced_queries.txt’ have been provided in the same folder. These are from Assignment-2 (Punkt Segmenter and PennTree Bank Tokenizer)

For ESA,  ‘ESA_articles_500_depth-1.csv’ and ‘ESA_articles_3343_depth-3.csv have been provided in the same folder.

Do not run the block Finding Optimal Value of K and Optimal Pre-Processing unless you want to regenerate the plots again. 
words and if do_bigram = True, it tokenizes the sentences into words and phrases.

NOTE: In the PDF Report, the figures and tables mentioned in the explanation are linked to the corresponding Figures and Tables, and can be seen by clicking on the figure/table number appearing in the explanation.
