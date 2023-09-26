import os
from gensim.models import TfidfModel
# from gensim.utils import simple_preprocess
from data_preprocessing import load_and_preprocess_dataset,create_dictionary_and_corpus


# Step 3: Create a TF-IDF model (optional)
def create_tfidf_model(corpus,model_save_path):
    tfidf_model = TfidfModel(corpus)
    corpus_tfidf = tfidf_model[corpus]
    tfidf_model.save(model_save_path)
    
    print("Model saved successfully")

    return tfidf_model, corpus_tfidf


if __name__=="__main__":
    model_save_path = "models/gensim_tfidf.model"
    dictionary_save_path = "logs/gensim_dictionary.dict"
    dataset_path = 'dataset/20news-19997/20_newsgroups/'

    preprocessed_documents = load_and_preprocess_dataset(dataset_path)
    dictionary,corpus = create_dictionary_and_corpus(preprocessed_documents)

       # Step 3: Create a TF-IDF model (optional)
    tfidf, corpus_tfidf = create_tfidf_model(corpus,model_save_path)
    print('tf idf , corpus_tfidf process done.')


    dictionary_save = dictionary.save(dictionary_save_path)
    print("Dictionary saved")
  



