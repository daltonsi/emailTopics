from sklearn.feature_extraction.text import CountVectorizer
from sklearn.decomposition import LatentDirichletAllocation

import csv, preProcess


def main():
    ## Maximum number of features for term frequency vectorizer
    maxFeats = 1000

    ## E.mails for which to find topics
    emails = preProcess.load()

    ## Term frequency vectorizer
    tfVectorizer = CountVectorizer(max_df = 0.95, min_df = 2,
                                   max_features = maxFeats,
                                   stop_words = 'english')

    ## Term frequency of emails
    tf = tfVectorizer.fit_transform(emails.values())

    ## Range of numbers of topics to seach through
    topicNums = range(1, 51)

    ## To store perplexity at diferent number of topics
    perplexities = [('No. Topics', 'Perplexity')]

    for i in topicNums:
        ## Latent Dirichlet Allocation model
        lda = LatentDirichletAllocation(n_topics = i, max_iter = 5,
                                        learning_method = 'online',
                                        learning_offset = 50.0,
                                        random_state = 0)

        lda.fit(tf)

        ## Perplexity of the model
        perplexity = lda.perplexity(tf)

        perplexities.append((i, perplexity))

        print 'No. Topics: ', i
        print 'Perplexity: ', perplexity

    ## File to write perplexities
    plxCSV = csv.writer(open('topicsVSperplexity.csv', 'wb', buffering = 0))

    plxCSV.writerows(perplexities)

    return

if __name__ == '__main__':
    main()
