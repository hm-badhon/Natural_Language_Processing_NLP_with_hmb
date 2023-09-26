from gensim import models
from data_preprocessing import dictionary, corpus

# Step 3: Create a TF-IDF model (optional)
def create_tfidf_model(corpus):
    tfidf = models.TfidfModel(corpus)
    corpus_tfidf = tfidf[corpus]
    return tfidf, corpus_tfidf

if __name__ == "__main__":
    # Step 3: Create a TF-IDF model (optional)
    tfidf, corpus_tfidf = create_tfidf_model(corpus)
    print('TF-IDF and corpus_tfidf processing done.')

    model_save_path = "models/gensim_tfidf.model"
    tfidf.save(model_save_path)
    print("TF-IDF model saved")

    dictionary_save_path = "models/gensim_dictionary.dict"
    dictionary.save(dictionary_save_path)
    print("Dictionary saved")
