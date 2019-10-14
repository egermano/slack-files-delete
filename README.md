# Slack Files Delete

> Script for bulk delete files in slack.

I love Slack, but I don’t have money enough to pay for all users in my company.

The first problem is the 10k messages history limit, it’s ok, I can deal with that. The second is the storage limit for files.

That second problem you need to delete old files to free space to still able to upload and share files. To do this, you need to open Slack, find files and delete each one, there’s no way to bulk delete. And s so, can deal with that to, with my super power.

So, I wrote this script to do that for me.

## Using

In order to delete files the script needs your so called **legacy token**. You can create and mange yours here:  
[https://api.slack.com/custom-integrations/legacy-tokens](https://api.slack.com/custom-integrations/legacy-tokens)

Once you cloned or downloaded this repo you need to edit the file `main.py`.

```python
# Create and manage yours at https://api.slack.com/custom-integrations/legacy-tokens
TOKEN = "YOURTOKEN"

# The timespan you want to keep files. Everything older then that will be deleted.
DAYS = 30
```

Now you can just execute it in your terminal like this:

```bash
python main.py
```
