import time
import snscrape.modules.twitter as sntwitter
import requests

WEBHOOK_URL = 'https://discord.com/api/webhooks/...'  # замени на свой

def get_latest_tweet(username):
    try:
        scraper = sntwitter.TwitterUserScraper(username)
        tweet = next(scraper.get_items())
        return tweet.content
    except Exception as e:
        print(f"[ERROR] Не удалось получить твит: {e}")
        return None

def send_to_discord(message):
    try:
        data = {"content": message}
        response = requests.post(WEBHOOK_URL, json=data)
        print(f"[INFO] Отправлено в Discord: {response.status_code}")
    except Exception as e:
        print(f"[ERROR] Ошибка отправки в Discord: {e}")

def main_loop():
    last_tweet = None
    while True:
        tweet = get_latest_tweet("UPvestorChain")
        if tweet and tweet != last_tweet:
            send_to_discord(tweet)
            last_tweet = tweet
        time.sleep(60)  # проверка раз в минуту

if __name__ == "__main__":
    print("[INFO] Скрипт запущен")
    main_loop()
