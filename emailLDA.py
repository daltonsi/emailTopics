from sklearn.feature_extraction.text import CountVectorizer
from sklearn.decomposition import LatentDirichletAllocation

import preProcess


def print_top_words(model, feature_names, n_top_words):
    ## function code credit:  http://scikit-learn.org/stable/auto_examples/
    #  applications/topics_extraction_with_nmf_lda.html
    for topic_idx, topic in enumerate(model.components_):
        print("Topic #%d:" % topic_idx)
        print(" ".join([feature_names[i]
                        for i in topic.argsort()[:-n_top_words - 1:-1]]))
    print()


def main():
    ## Number of topics
    n_topics = 10

    n_top_words = 20

    n_features = 1000

    ## E.mails to find topics for
    emails = preProcess.load()

    ## Term frequency vectorizer
    tf_vectorizer = CountVectorizer(max_df = 0.95, min_df = 2,
                                    max_features = n_features,
                                    stop_words = 'english')

    ## Term frequency of emails
    tf = tf_vectorizer.fit_transform(emails.values())

    ## Latent Dirichlet Allocation model
    lda = LatentDirichletAllocation(n_topics = n_topics, max_iter = 5,
                                    learning_method = 'online',
                                    learning_offset = 50.0, random_state = 0)

    lda.fit(tf)

    tf_feature_names = tf_vectorizer.get_feature_names()
    print_top_words(lda, tf_feature_names, n_top_words)

    return

if __name__ == '__main__':
    main()
