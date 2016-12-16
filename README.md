# emailTopics
Semester project for Fall 2016 data mining course

There are two programs ready to run that use email.json:

    1. optimalTopics.py
       This calculates the perplexity of LDA models for 1 to 50 topics.
       Run with the following command in folder of the repository:
           python optimalTopics.py

    2. emailLDA.py
       This outputs the top 20 words for 10 topics.
       Run with the following command in folder of the repository:
           python emailLDA.py

optimalTopics.py and emailLDA.py depend on preProcess.py to perform preprocessing on the data collected in email.json.

To produce email.json, an MBOX file is extracted for its e.mail subject and body via mbox2json.py.
