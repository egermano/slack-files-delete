# -*- encoding: utf-8 -*-

import httplib2
import json
import calendar
import urllib
from datetime import datetime, timedelta

TOKEN = "YOURTOKEN"
DAYS = 30

date = str(calendar.timegm((datetime.now() + timedelta(- DAYS)).utctimetuple()))

params = {"token": TOKEN, "ts_to": date}
data = urllib.urlencode(params)

h = httplib2.Http()

(response, content) = h.request(
    'https://slack.com/api/files.list',
    "POST",
    body=data,
    headers={'Content-type': 'application/x-www-form-urlencoded'})

files = json.loads(content)["files"]
paging = json.loads(content)["paging"]

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

    files.append(json.loads(content)["files"])
    paging = json.loads(content)["paging"]

if len(files) < 1:
    print "No files to delete."
else:
    print "Total Files to delete: " + str(len(files)) + "\n Start deleting files."

for f in files:
    try:
        print "Deleting file " + str(f["id"]) + ": " + str(f["name"]) + "..."

        timestamp = str(calendar.timegm(datetime.now().utctimetuple()))
        url = "https://slack.com/api/files.delete?t=" + timestamp

        params = {
            "token": TOKEN,
            "file": f["id"],
            "set_active": "true",
            "_attempts": "1"};

        data = urllib.urlencode(params)

        h = httplib2.Http()

        (resp, content)  = h.request(url,
            "POST",
            body=data,
            headers={'Content-type': 'application/x-www-form-urlencoded'})

    except Exception as e:
        print e
