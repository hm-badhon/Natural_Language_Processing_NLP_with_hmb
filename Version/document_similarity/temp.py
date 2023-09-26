
import os
from gensim.similarities import Similarity
from gensim.utils import simple_preprocess
from data_preprocessing import dictionary
from gensim.models import TfidfModel

# Step 4: Create a similarity index
def create_similarity_index(corpus_tfidf, dictionary):
    similarity_index = Similarity('similarity_index', corpus_tfidf, num_features=len(dictionary))
    return similarity_index

# Step 5: Query for similarity
def find_similarity(query, dictionary, tfidf, similarity_index):
    # Preprocess and transform the query
    query_bow = dictionary.doc2bow(simple_preprocess(query))
    query_tfidf = tfidf[query_bow]

    # Get similarity scores
    similarity_scores = similarity_index[query_tfidf]
    return similarity_scores
    

if __name__ == "__main__":

    # Step 4: Create a similarity index
    similarity_index = create_similarity_index(corpus_tfidf, dictionary)
    # print('Similarity done')
    # Step 5: Query for similarity
    query = "This is a sample query document."
    similarity_scores = find_similarity(query, dictionary, tfidf, similarity_index)



    # Save the similarity index
    similarity_index_path = "logs/gensim_similarity_index.index"
    similarity_index_save=similarity_index.save(similarity_index_path)
    # Print the similarity scores
    # pprint(similarity_scores)


    # Step 5: Query for similarity
    sentence1 = "I am going to school"
    sentence2 = "I am going to school"

    # Preprocess and transform the sentences
    sentence1_bow = dictionary.doc2bow(simple_preprocess(sentence1))
    sentence1_tfidf = tfidf[sentence1_bow]

    sentence2_bow = dictionary.doc2bow(simple_preprocess(sentence2))
    sentence2_tfidf = tfidf[sentence2_bow]

     # Get cosine similarity between the two sentences
    similarity = similarities.MatrixSimilarity([sentence1_tfidf], num_features=len(dictionary))
    similarity_score = similarity[sentence2_tfidf]

    # Convert the similarity score to a float and format it as a percentage
    similarity_score_percentage = float(similarity_score) * 100
    print("sentence 1 : ",sentence1)
    print("sentence 2 : ",sentence2)


    # Print the similarity score as a percentage
    print(f"Similarity between the two sentences: {similarity_score_percentage:.2f}%")