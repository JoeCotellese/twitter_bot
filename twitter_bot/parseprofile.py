from bs4 import BeautifulSoup
import dateparser

class ParseProfile():
    def __init__(self, html):
        self.html = html
    
    @property
    def join_date(self):
        soup = BeautifulSoup(self.html, 'html.parser')
        join_date_html = soup.find(class_='ProfileHeaderCard-joinDateText')
        date_string = join_date_html['title']
        date = dateparser.parse(date_string)
        return date
    
    @property
    def follower_count(self):
        soup = BeautifulSoup(self.html, 'html.parser')
        data_nav = soup.find(attrs={"data-nav":"followers"})
        count = data_nav.find(class_='ProfileNav-value')['data-count']
        return int(count)
    
    @property
    def following_count(self):
        soup = BeautifulSoup(self.html, 'html.parser')
        data_nav = soup.find(attrs={"data-nav":"following"})
        count = data_nav.find(class_='ProfileNav-value')['data-count']
        return int(count)
    
    @property
    def following(self):
        #you must be logged in
        soup = BeautifulSoup(self.html, 'html.parser')
        user_actions = soup.find(class_='user-actions')
        if 'not-following' in user_actions['class']:
            return False
        else:
            return True        

    @property
    def follows_back(self):
        soup = BeautifulSoup(self.html, 'html.parser')
        follows_back = soup.find(class_='FollowStatus')
        if follows_back == None:
            return False
        else:
            return True
    @property
    def muted(self):
        pass

    @property
    def location(self):
        pass

    @property
    def twitter_handle(self):
        soup = BeautifulSoup(self.html, 'html.parser')
        profile_card = soup.find(class_='ProfileHeaderCard-screenname')
        username = '@{}'.format(profile_card.find(class_='u-linkComplex-target').string)
        return username
    
    