from bs4 import BeautifulSoup

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