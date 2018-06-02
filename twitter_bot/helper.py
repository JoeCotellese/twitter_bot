from bs4 import BeautifulSoup
import arrow

class StreamList():
    def __init__(self, html):
        self.html=html
    
    @property
    def profile_links(self):
        soup = BeautifulSoup(self.html, 'html.parser')
        stream = soup.find(class_='stream-container')
        #links = stream.find_all(class_='js-user-profile-link')
        links = []
        for link in stream.find_all(class_='js-user-profile-link'):
            links.append('https://www.twitter.com{}'.format(link.get('href')))
        return links
    
    def follow_buttons(self):
        return 0

def days_since_follow(now, follow_date):
    today = arrow.get(now)
    follow_day = arrow.get(follow_date)
    diff = today - follow_day
    return diff.days 