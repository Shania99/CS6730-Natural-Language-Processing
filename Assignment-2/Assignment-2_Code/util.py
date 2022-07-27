# Add your import statements here






# Add any utility functions here
def get_ground_truth(query_id, qrels, relevance=False):
    rel_docs = {
        int(dic['id']): int(dic['position'])
        for dic in qrels
        if int(dic['query_num']) == int(query_id)
    }
    rel_docs_1 = sorted(rel_docs.items(), key=lambda item: item[1])
    if not relevance:
        return [(x[0]) for x in rel_docs_1]
    else:
        return rel_docs