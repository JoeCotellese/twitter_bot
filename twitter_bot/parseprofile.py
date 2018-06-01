from bs4 import BeautifulSoup
import dateparser

class ParseProfile():
    def __init__(self, html):
        self.html = html

    @property
    def following(self):
        pass        
    
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
    def muted(self):
        pass

    @property
    def location(self):
        pass

    @property
    def screenname(self):
        pass
