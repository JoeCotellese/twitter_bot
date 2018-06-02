from twitter_bot.automation import TwitterBot
import config

def main():
    tb = TwitterBot(config.USERNAME, config.PASSWORD)
    tb.login()
    #tb.follow_suggested_followers(100)
    tb.follow_search(2, "#macos #productivity")
    #tb.follow_who_to_follow()
    tb.logout()

if __name__ == '__main__':
    main()