import twitterBot

PROMISED_DOWN = 150
PROMISED_UP = 10
CHROME_DRIVER_PATH = "/Users/manchunko/Downloads/Development/chromedriver"
TWITTER_EMAIL = "dmc.dante.zzzz@gmail.com"
TWITTER_PW = "Kochun1!"

bot = twitterBot.InternetSpeedTwitterBot(PROMISED_DOWN, PROMISED_UP)
speed = bot.get_internet_speed()
print(speed)
bot.tweet_at_provider(TWITTER_EMAIL, TWITTER_PW)
