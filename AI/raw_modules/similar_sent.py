# Updated 23/1/24

from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np 

def cosine_sent(t_sentence: str,sentences: list):
    '''sentence similarity'''
    model = SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2')
    target_sent=model.encode([t_sentence])
    check_sent=model.encode(sentences)
    similarity_scores = cosine_similarity(target_sent, check_sent)
    best_category_index = np.argmax(similarity_scores)
    best_category = sentences[best_category_index]
    match_per=round((list(similarity_scores)[0][best_category_index])*100,2)
    return best_category,match_per