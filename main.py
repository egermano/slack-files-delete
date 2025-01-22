# -*- encoding: utf-8 -*-
#!/usr/bin/env python

""" Script for bulk delete files in slack. """

import httplib2
import json
import calendar
import urllib
import sys
import argparse
from datetime import datetime, timedelta

DAYS = 30 

parser = argparse.ArgumentParser(
    description="Delete old files from Slack."
)

# Create and manage yours at https://api.slack.com/custom-integrations/legacy-tokens
parser.add_argument(
    "-t",
    "--token",
    help='The slack legacy token. Manage yours at https://api.slack.com/custom-integrations/legacy-tokens',
    required=True
)

# The timespan you want to keep files. Everything older then that will be deleted.
parser.add_argument(
    "-d",
    "--days",
    help='Amount of days that should stay. Everything that is older will be deleted.', 
    type=int,
    default=DAYS
)

args = parser.parse_args()
TOKEN = args.token
DAYS = args.days

date = str(calendar.timegm((datetime.now() + timedelta(- DAYS)).utctimetuple()))

params = {"token": TOKEN, "ts_to": date}
data = urllib.urlencode(params)

h = httplib2.Http()

(response, content) = h.request(
    'https://slack.com/api/files.list',
    "POST",
    body=data,
    headers={'Content-type': 'application/x-www-form-urlencoded'})

def check_error(error_message, answer, error_code = 1):
    if not answer["ok"]:
        print >> sys.stderr, '%s : %s' % (error_message, answer['error'])
        sys.exit(error_code)

answer = json.loads(content)
check_error('Could not get file list', answer)
files = answer["files"]
paging = answer["paging"]

while paging["page"] < paging["pages"]:
    newPage = paging["page"] + 1

    params["page"] = newPage
    data = urllib.urlencode(params)

    h = httplib2.Http()

    (response, content) = h.request(
        'https://slack.com/api/files.list',
        "POST",
        body=data,
        headers={'Content-type': 'application/x-www-form-urlencoded'})

    answer = json.loads(content)
    check_error('Could not get page of file', answer)
    files = files + answer["files"]
    paging = answer["paging"]

if len(files) < 1:
    print "No files to delete."
else:
    print "Total Files to delete: " + str(len(files)) + "\n Start deleting files."

for f in files:
    try:
        print "Deleting file " + str(f["id"]) + ": " + f["name"].encode('utf-8') + "...",

        timestamp = str(calendar.timegm(datetime.now().utctimetuple()))
        url = "https://slack.com/api/files.delete?t=" + timestamp

        params = {
            "token": TOKEN,
            "file": f["id"],
            "set_active": "true",
            "_attempts": "1"}

        data = urllib.urlencode(params)

        h = httplib2.Http()

        (resp, content) = h.request(url,
            "POST",
            body=data,
            headers={'Content-type': 'application/x-www-form-urlencoded'})

        print "[{}]".format("\033[92m {}\033[00m" .format(json.loads(content)["OK"]))

    except Exception as e:
        print e
