import os
from gensim import corpora

from gensim import models
# from gensim.utils import simple_preprocess
from data_preprocessing import dictionary, corpus


# Step 3: Create a TF-IDF model (optional)
def create_tfidf_model(corpus):
    tfidf = models.TfidfModel(corpus)
    corpus_tfidf = tfidf[corpus]
    return tfidf, corpus_tfidf


if __name__=="__main__":
    # Step 3: Create a TF-IDF model (optional)
    tfidf, corpus_tfidf = create_tfidf_model(corpus)
    print('tf idf , corpus_tfidf process done.')

    model_save_path = "models/gensim_tfidf.model"
    model_save = tfidf.save(model_save_path)
    print("Model saved")
    

    dictionary_save_path = "logs/gensim_dictionary.dict"
    dictionary_save = dictionary.save(dictionary_save_path)
    print("Dictionary saved")
  



