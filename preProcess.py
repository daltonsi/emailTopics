import json
import re
import EFZP as zp

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

        # Removes Whitespace
        emails[email['subject']] = email['subject'].strip() + "\n" + email['body'].strip()


        # Filters out signatures
        # WARNING: will remove all text below a forwarded email
        emails[email['subject']] = emails[email['subject']].split('--')[0]
        emails[email['subject']] = emails[email['subject']].split('Best,')[0]
        #emails[email['subject']] = emails[email['subject']].split('Thanks!')[0]

        # Removes all lines starting with one or more '>' characters
        # NOTE: This is meant to filter out forwarded text
        emails[email['subject']] = re.sub(r'(?m)^\>.*\n?', '', emails[email['subject']])

        # Remove forwarded time tag
        # EXAMPLE:On Thu, Sep 29, 2016 at 11:53 AM, Karen Stover <s10.kstover@gmail.com> wrote:
        emails[email['subject']] = re.sub(r'(?m)^\On.*\n?', '', emails[email['subject']])
        emails[email['subject']] = re.sub(r'(?m)^\wrote.*\n?', '', emails[email['subject']])




        # Remove URLs
        emails[email['subject']] = re.sub(r'^https?:\/\/.*[\r\n]*', '', emails[email['subject']], flags=re.MULTILINE)
        emails[email['subject']] = re.sub(r'^http?:\/\/.*[\r\n]*', '', emails[email['subject']], flags=re.MULTILINE)
        emails[email['subject']] = re.sub(r'<http?:\/\/.*[\r\n]*', '', emails[email['subject']], flags=re.MULTILINE)


        # Remove File Links
        #emails[email['subject']] = re.sub(r'<file?:\/\/.*[\r\n]*', '', emails[email['subject']], flags=re.MULTILINE)
        #emails[email['subject']] = zp.parse(emails[email['subject']])

    return emails


if __name__ == '__main__':
    loaded = load()
    #print loaded[loaded.keys()[9]]
    print loaded[loaded.keys()[16]]
    print
