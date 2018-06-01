from bs4 import BeautifulSoup
class ParseCard():
    def __init__(self, html):
        self.html = html

    @property
    def name(self):
        soup = BeautifulSoup(self.html, 'html.parser')
        name = soup.find(class_="fullname").string
        name = name.strip()
        return name

    @property
    def twitter_handle(self):
        soup = BeautifulSoup(self.html, 'html.parser')
        profile_card = soup.find(class_='ProfileCard-screenname')
        username = '@{}'.format(profile_card.find(class_='u-linkComplex-target').string)
        return username
    
    @property
    def muted(self):
        soup = BeautifulSoup(self.html, 'html.parser')
        muting = soup.find(class_="muting")
        if muting == None:
            return False
        else:
            return True
        