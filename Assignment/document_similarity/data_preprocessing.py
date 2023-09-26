import os
from gensim import corpora
from gensim.utils import simple_preprocess
import timeit

# Step 1: Load and preprocess the 20 Newsgroups dataset
def load_and_preprocess_dataset(dataset_path):
    documents = []
    for category in os.listdir(dataset_path):
        category_path = os.path.join(dataset_path, category)
        if os.path.isdir(category_path):
            for document in os.listdir(category_path):
                with open(os.path.join(category_path, document), 'r', encoding='latin-1') as file:
                    content = file.read()
                    documents.append(content)
    
    def preprocess(text):
        return simple_preprocess(text)

    preprocessed_documents = [preprocess(doc) for doc in documents]
    # print('preprocess data', preprocessed_documents)
    return preprocessed_documents

# Step 2: Create a dictionary and a corpus
def create_dictionary_and_corpus(documents):
    dictionary = corpora.Dictionary(documents)
    corpus = [dictionary.doc2bow(doc) for doc in documents]
    # print("Dictionary :", dictionary)
    return dictionary, corpus


if __name__ == "__main__":
    # Set the path to the 20 Newsgroups dataset
    dataset_path = 'dataset/20news-19997/20_newsgroups/'
    # Step 1: Load and preprocess the dataset
    preprocessed_documents = load_and_preprocess_dataset(dataset_path)
    print('Process documnets done')
    # Step 2: Create a dictionary and a corpus
    dictionary, corpus = create_dictionary_and_corpus(preprocessed_documents)
    print('Dictionary and Corpus done')

