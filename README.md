# Slack Files Delete

> Script for bulk delete files in slack.

I love Slack, but I don’t have money enough to pay for all users in my company.

The first problem is the 10k messages history limit, it’s ok, I can deal with that. The second is the storage limit for files.

That second problem you need to delete old files to free space to still able to upload and share files. To do this, you need to open Slack, find files and delete each one, there’s no way to bulk delete. And s so, can deal with that to, with my super power.

So, I wrote this script to do that for me.

## Using

In order to delete files the script needs your so called **legacy token**. You can create and mange yours here:  
[https://api.slack.com/custom-integrations/legacy-tokens](https://api.slack.com/custom-integrations/legacy-tokens)

The script takes arguments to configure your token and the days you want to keep files for.

```bash
-t TOKEN      Your slack legacy token. (required)
-d DAYS       The amount of days you want to keep. (default: 30)
              Everything older will be deleted.
```

So you can just execute it in your terminal like this:

```bash
python main.py -t xoxp-... -d 90
```
