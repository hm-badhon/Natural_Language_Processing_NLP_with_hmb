
import os
from gensim.models import TfidfModel
from gensim.corpora import Dictionary
from gensim.utils import simple_preprocess
from gensim.similarities import MatrixSimilarity


def generate_tfidf_from_sentence(sentence):
    sentence_bow = loaded_tfidf_dictionary.doc2bow(simple_preprocess(sentence))
    sentence_tfidf = loaded_tfidf_model[sentence_bow]
    return sentence_tfidf


def calculate_similarity(sentence1_tfidf,sentence2_tfidf,tfidf_model,tfidf_dictionary):
    # Get cosine similarity between the two sentences
    similarity = MatrixSimilarity([sentence1_tfidf], num_features=len(tfidf_dictionary))
    similarity_score = similarity[sentence2_tfidf]

    # Print the similarity score as a percentage
    # print(f"Similarity between the two sentences: {similarity_score_percentage:.2f}%")
    return similarity_score
    

if __name__ == "__main__":

    # Step 4: Create a similarity index
    sentence1 = "I am going to school"
    sentence2 = "I am going to school"
    saved_model_path='models/gensim_tfidf.model'
    saved_dictionary_path='logs/gensim_dictionary.dict'

    print("sentence 1 : ",sentence1)
    print("sentence 2 : ",sentence2)

    loaded_tfidf_model = TfidfModel.load(saved_model_path)
    loaded_tfidf_dictionary=Dictionary.load(saved_dictionary_path)

    
    sentence1_tfidf=generate_tfidf_from_sentence(sentence1)
    sentence2_tfidf=generate_tfidf_from_sentence(sentence2)

    similarity_score=calculate_similarity(sentence1_tfidf,sentence2_tfidf,loaded_tfidf_model,loaded_tfidf_dictionary)
    print('similarity score: ',similarity_score)



   