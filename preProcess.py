import json

def main():
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

    print emails

    return

if __name__ == '__main__':
    main()
