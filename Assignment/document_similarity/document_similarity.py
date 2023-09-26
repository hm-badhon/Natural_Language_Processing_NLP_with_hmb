# import os
# from gensim import corpora, models, similarities
# from gensim.utils import simple_preprocess
# from pprint import pprint

# # Step 1: Load and preprocess the 20 Newsgroups dataset
# def load_and_preprocess_dataset(dataset_path):
#     documents = []
#     for category in os.listdir(dataset_path):
#         category_path = os.path.join(dataset_path, category)
#         if os.path.isdir(category_path):
#             for document in os.listdir(category_path):
#                 with open(os.path.join(category_path, document), 'r', encoding='latin-1') as file:
#                     content = file.read()
#                     documents.append(content)
    
#     def preprocess(text):
#         return simple_preprocess(text)

#     preprocessed_documents = [preprocess(doc) for doc in documents]
#     return preprocessed_documents

# # Step 2: Create a dictionary and a corpus
# def create_dictionary_and_corpus(documents):
#     dictionary = corpora.Dictionary(documents)
#     corpus = [dictionary.doc2bow(doc) for doc in documents]
#     return dictionary, corpus

# # Step 3: Create a TF-IDF model (optional)
# def create_tfidf_model(corpus):
#     tfidf = models.TfidfModel(corpus)
#     corpus_tfidf = tfidf[corpus]
#     return tfidf, corpus_tfidf

# # Step 4: Create a similarity index
# def create_similarity_index(corpus_tfidf, dictionary):
#     similarity_index = similarities.Similarity('similarity_index', corpus_tfidf, num_features=len(dictionary))
#     return similarity_index

# # Step 5: Query for similarity
# def find_similarity(query, dictionary, tfidf, similarity_index):
#     # Preprocess and transform the query
#     query_bow = dictionary.doc2bow(simple_preprocess(query))
#     query_tfidf = tfidf[query_bow]

#     # Get similarity scores
#     similarity_scores = similarity_index[query_tfidf]
#     return similarity_scores

# if __name__ == "__main__":
#     # Set the path to the 20 Newsgroups dataset
#     dataset_path = 'dataset/20news-19997/20_newsgroups/'
#     # print('Dataset done')

#     # Step 1: Load and preprocess the dataset
#     preprocessed_documents = load_and_preprocess_dataset(dataset_path)
#     # print('Process documnets done')
#     # Step 2: Create a dictionary and a corpus
#     dictionary, corpus = create_dictionary_and_corpus(preprocessed_documents)
#     # print('Dictionary and Corpus done')
#     # Step 3: Create a TF-IDF model (optional)
#     tfidf, corpus_tfidf = create_tfidf_model(corpus)
#     # print('tf idf , corpus Done')
#     # Step 4: Create a similarity index
#     similarity_index = create_similarity_index(corpus_tfidf, dictionary)
#     # print('Similarity done')
#     # Step 5: Query for similarity
#     query = "This is a sample query document."
#     similarity_scores = find_similarity(query, dictionary, tfidf, similarity_index)

#     # Print the similarity scores
#     # pprint(similarity_scores)


#     dictionary.save("gensim_dictionary.dict")
#     tfidf.save("gensim_tfidf.model")

#     # Save the similarity index
#     similarity_index.save("gensim_similarity_index.index")

#     # Step 5: Query for similarity
#     sentence1 = "I am going to school"
#     sentence2 = "I am going to school"

#     # Preprocess and transform the sentences
#     sentence1_bow = dictionary.doc2bow(simple_preprocess(sentence1))
#     sentence1_tfidf = tfidf[sentence1_bow]

#     sentence2_bow = dictionary.doc2bow(simple_preprocess(sentence2))
#     sentence2_tfidf = tfidf[sentence2_bow]

#      # Get cosine similarity between the two sentences
#     similarity = similarities.MatrixSimilarity([sentence1_tfidf], num_features=len(dictionary))
#     similarity_score = similarity[sentence2_tfidf]

#     # Convert the similarity score to a float and format it as a percentage
#     similarity_score_percentage = float(similarity_score) * 100
#     print("sentence 1 : ",sentence1)
#     print("sentence 2 : ",sentence2)


#     # Print the similarity score as a percentage
#     print(f"Similarity between the two sentences: {similarity_score_percentage:.2f}%")
   