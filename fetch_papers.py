import argparse
import feedparser
import requests
import json
from datetime import datetime
import hashlib

# Set Slack webhook URL
slack_webhook_url = 'https://hooks.slack.com/services/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'

# Create a set to store the hash values of all the titles posted before
posted_titles_hash = set()

# Function to post message to Slack
def post_to_slack(message):
    headers = {'Content-type': 'application/json'}
    response = requests.post(slack_webhook_url, headers=headers, data=json.dumps({"text": message}))
    if response.status_code != 200:
        raise ValueError(f'Request to slack returned an error {response.status_code}, the response is:\n{response.text}')

# Function to filter feed entries by keywords
def filter_feed_by_keywords(feed, keywords):
    for keyword in keywords:
        keyword_header_posted = False
        for entry in feed.entries:
            # If the keyword is in the title, post the title and link to Slack
            if keyword.lower() in entry.title.lower():
                # Create a hash of the title
                title_hash = hashlib.md5(entry.title.encode('utf-8')).hexdigest()

                # If the title was not posted before, post it
                if title_hash not in posted_titles_hash:
                    # Post the keyword as a header if not already posted
                    if not keyword_header_posted:
                        post_to_slack(f"\n{'=' * 30} \nKeyword: {keyword}\n{'=' * 30}")
                        keyword_header_posted = True

                    post_to_slack(f"{entry.title}\n{entry.link}\n")
                    posted_titles_hash.add(title_hash)

def main():
    parser = argparse.ArgumentParser(description='Fetch and filter arXiv feed.')
    parser.add_argument('-k', '--keywords', nargs='+', help='keywords to filter by', required=True)
    parser.add_argument('-u', '--urls', nargs='+', help='URLs to fetch the feed from', required=True)
    args = parser.parse_args()

    # Parse date and post it
    post_to_slack(f" \n *{'=' * 60}* \n Today's Post: {datetime.now().date()} \n *{'=' * 60}* ")

    # Fetch and filter feed from each URL
    for url in args.urls:
        feed = feedparser.parse(url)
        filter_feed_by_keywords(feed, args.keywords)

if __name__ == "__main__":
    main()

