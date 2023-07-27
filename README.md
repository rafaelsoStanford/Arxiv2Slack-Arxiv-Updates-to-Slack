# arXiv-to-Slack Bot

This Python script fetches the latest articles from specified arXiv.org RSS feeds and posts them to a Slack channel. The articles are filtered based on a set of user-provided keywords and specified RSS feeds. 



## Requirements:
Run the following line in your environement
```
pip install argparse feedparser requests jsonlib
```

## Getting RSS Feeds from arXiv.org

1. Go to [arXiv.org](http://arxiv.org/).
2. Click on the subject area you're interested in. This will take you to a page with a list of articles in that subject area.
3. Click on the "RSS" button in the top-right corner of the article list. This will take you to the RSS feed for that subject area.
4. Copy the URL of the RSS feed from your browser's address bar.

You can use the URLs of multiple RSS feeds by separating them with spaces when you run the script.

## Setting up a Slack Webhook

1. Go to [Create new slack app](https://api.slack.com/apps?new_app=1).
2. Create a new App from scratch and select your workspace. 
3. Press on "Incoming Webhooks". Enable Webhooks and add a new Webhook to Workspace. 
4. Choose your preferred channel on where you want the messages to be sent to. You can create a custom private channel on slack if you haven't done so already.
5. Copy the Webhook URL and modify the following line inside of **fetch_papers.py**

```
slack_webhook_url = 'YourWebhookURL'
```
## Running the Script

1. Open a terminal.
2. Run the script as follows:

```bash
python script.py -k keyword1 keyword2 -u http://arxiv.org/rss/cs http://arxiv.org/rss/cs.AI
```

Replace keyword1 keyword2 with your space-separated keywords, and replace http://arxiv.org/rss/cs http://arxiv.org/rss/cs.AI with your space-separated RSS feed URLs.

## Setting up a Daily Task

You can use the built-in task scheduling feature of your operating system to run the script daily.
On Unix-like Systems (Linux, macOS)

You can use cron to schedule tasks:
1. Open a terminal.
2. Run crontab -e to edit the cron table.
3. Add a line like this:
```bash
0 8 * * * /usr/bin/python /path/to/script.py -k keyword1 keyword2 -u http://arxiv.org/rss/cs http://arxiv.org/rss/cs.AI
```
Replace /usr/bin/python with the path to your Python interpreter, and replace /path/to/script.py with the path to the script. This line will run the script every day at 8 AM.

## RSS Endings in Arxiv
The RSS feeds are sorted by different categories and subjects. Some endings are listed here:
  1. General arXiv Feed: /rss
  2. Mathematics: /math
  3. Computer Science: /cs
  4. Physics: /physics
  5. Electrical Engineering and Systems Science: /eess

### Browse context
Further subcategories can be accessed by combining the endings with a . and the subcategory: i.e. cs.AI (Artificial Inteligence) or cs.RO (Robotics). Check the papers you are reading on Arxiv on the current context and add the links to the arguments being passed to the script. 

* This code was meant for personal use. I had some fun setting it up and its what it is. There might have been a better or cleaner way of doing this, possibly not involving a seperate script or a slack app. * 


