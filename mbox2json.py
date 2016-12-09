import json, mailbox


# CODE Reference: http://stackoverflow.com/questions/7166922/extracting-the-body-of-an-email-from-mbox-file-decoding-it-to-plain-text-regard

def getcharsets(msg):
    charsets = set({})
    for c in msg.get_charsets():
        if c is not None:
            charsets.update([c])
    return charsets

def handleerror(errmsg, emailmsg,cs):
    print()
    print(errmsg)
    print("This error occurred while decoding with ",cs," charset.")
    print("These charsets were found in the one email.",getcharsets(emailmsg))
    print("This is the subject:",emailmsg['subject'])
    print("This is the sender:",emailmsg['From'])

def getbodyfromemail(msg):
    body = None
    if msg.is_multipart():
        for part in msg.walk():
            if part.is_multipart():
                for subpart in part.walk():
                    if subpart.get_content_type() == 'text/plain':
                        body = subpart.get_payload(decode=True)
            elif part.get_content_type() == 'text/plain':
                body = part.get_payload(decode=True)
    elif msg.get_content_type() == 'text/plain':
        body = msg.get_payload(decode=True)
    """for charset in getcharsets(msg):
        try:
            body = body.decode(charset)
        except UnicodeDecodeError:
            handleerror("UnicodeDecodeError: encountered.",msg,charset)
            pass
        except AttributeError:
            handleerror("AttributeError: encountered" ,msg,charset)
            pass"""
    return body


if __name__ == '__main__':
    ## E.mails with desired metadata
    emails = []

#    c = 0  ##counter for testing

    for thisemail in mailbox.mbox('UMSI-Open.mbox'):
        ## E.mail text and metadata
        email = {}

        body = getbodyfromemail(thisemail)
        #print '******************************************'
        #print thisemail['subject']
        email['subject'] = unicode(thisemail['subject'], errors='ignore')
        #print thisemail['Date']
        email['date'] = unicode(thisemail['Date'], errors='ignore')
        if thisemail['To']:
        #    print "TO: " + thisemail['To']
            email['to'] = unicode(thisemail['To'], errors='ignore')
        if thisemail['From']:
        #    print "FROM: " + thisemail['From']
            email['from'] = unicode(thisemail['From'], errors='ignore')
        #print
        #print body
        try:
            email['body'] = unicode(body, errors='ignore')
        except:
            email['body'] = "NONE"
        emails.append(email)
#        c += 1
#        if c > 10:
#            break
    #final_emails = []
    #for email in emails:
    #    final_emails.append(unicode(email, errors='ignore'))
    print json.dumps(emails)
    ## JSON file for output
    JSONoutput = open('email.json', 'w')

    JSONoutput.write(json.dumps(emails))

