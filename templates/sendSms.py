#!/usr/bin/python3
################################################################################
#                                                                              #
#                                 {o,o}                                        #
#                                 |)__)                                        #
#                                 -"-"-                                        #
#                                                                              #
################################################################################

###############################---IMPORTS---####################################

import sys
import yaml
import os
import time
from twilio.rest import TwilioRestClient
import random

################################################################################

##############################---VARIABLES---###################################

locks_file = "lock.yml"
account_sid = "{{ monit_twilio_account }}"
auth_token  = "{{ monit_twilio_auh_token }}"
number_to = "{{ monit_twilio_number_to }}"
number_from = "{{ monit_twilio_number_from }}"
if len(sys.argv) < 2:
    print("usage ./sendSms <action> <event>")
    sys.exit
action = sys.argv[1]
event = sys.argv[2]
fileData = { 'locks': [] }

################################################################################

##############################---FUNCTIONS---###################################

def sendSMS(message):
    """
    Send an sms with twilio api.
    """
    client = TwilioRestClient(account_sid, auth_token)
    client.messages.create(
        body  = message,
        to    = number_to,
        from_ = number_from
    )

def writeLockFile(lock_file, content):
    """
    Write new locks list to the file
    """

    f = open(lock_file, "w")
    yaml.dump(content, f, default_flow_style=False)
    f.close()

def getLocks(lock_file):
    """
    Get lock list form the file.
    """

    if os.path.exists(lock_file):
        f = open(lock_file, "r")
        with f as stream:
            content = yaml.load(stream)
        f.close()
    else:
        content = { 'locks': [] }

    if content == None:
        content = { 'locks': [] }
    return content

def newAlert():
    if not event in fileData['locks']:
        sendSMS(event + " is down!")
        fileData['locks'].append(event)
        writeLockFile(locks_file, fileData)

def removeAlert():
    if event in fileData['locks']:
        sendSMS(event + " is back up.")
        fileData['locks'].remove(event)
        writeLockFile(locks_file, fileData)


################################################################################

###############################---EXECUTION---##################################

time.sleep(random.randrange(0,100,2)/10 )
fileData = getLocks(locks_file)

if action == "alert":
    newAlert()
elif action == "succeeded":
    removeAlert()
else:
    print("ERROR: unknown action")

################################################################################
