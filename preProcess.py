import json

## Loads email data from JSON file
def load():
    ## Open JSON file
    inFile = open('email.json', 'rU')

    for line in inFile:
        ## E.mails from JSON
        jsonEmails = json.loads(line)
        break

    ## To store e.mail bodies as documents
    emails = {}

    for email in jsonEmails:
        emails[email['subject']] = email['body']

    return emails
