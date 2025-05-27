import subprocess
import time
import requests

DISCORD_WEBHOOK_URL = "https://discord.com/api/webhooks/..."  # ← вставь сюда свой URL
TWITTER_USERNAME = "UPvestorChain"

def get_latest_tweet():
    result = subprocess.run(
        ["snscrape", f"twitter-user {TWITTER_USERNAME}"],
        capture_output=True,
        text=True
    )
    lines = result.stdout.strip().split('\n')
    if lines:
        return lines[0]
    return None

def send_to_discord(message):
    data = {"content": message}
    response = requests.post(DISCORD_WEBHOOK_URL, json=data)
    return response.status_code == 204

def main():
    last_tweet = None
    while True:
        tweet = get_latest_tweet()
        if tweet and tweet != last_tweet:
            send_to_discord(tweet)
            last_tweet = tweet
        time.sleep(60)  # проверка каждую минуту

if __name__ == "__main__":
    main()
