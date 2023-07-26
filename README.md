# arXiv-to-Slack Bot

This Python script fetches the latest articles from specified arXiv.org RSS feeds and posts them to a Slack channel. The articles are filtered based on a set of user-provided keywords.

## Getting RSS Feeds from arXiv.org

1. Go to [arXiv.org](http://arxiv.org/).
2. Click on the subject area you're interested in. This will take you to a page with a list of articles in that subject area.
3. Click on the "RSS" button in the top-right corner of the article list. This will take you to the RSS feed for that subject area.
4. Copy the URL of the RSS feed from your browser's address bar.

You can use the URLs of multiple RSS feeds by separating them with spaces when you run the script.

## Setting up a Slack Webhook

1. Go to [https://my.slack.com/services/new/incoming-webhook/](https://my.slack.com/services/new/incoming-webhook/).
2. Select the Slack channel where you want the notifications to be posted and click on "Add Incoming WebHooks Integration".
3. You'll be taken to a page with a Webhook URL. This is what you'll use to post messages to your Slack channel. Copy this URL and keep it safe.
4. Customize the name and icon of the bot, if you want, and click on "Save Settings".

## Running the Script

1. Open a terminal.
2. Run the script as follows:

```bash
python script.py -k keyword1 keyword2 -u http://arxiv.org/rss/cs http://arxiv.org/rss/cs.AI
