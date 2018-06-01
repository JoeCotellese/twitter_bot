import pytest
import context
from datetime import datetime
from twitter_bot.helper import StreamList
from test_data import STREAM_CONTAINER

def test_twitterlist():
    stream_list = StreamList(STREAM_CONTAINER)
    assert len(stream_list.profile_links) == 40

def test_twitterlisturls():
    stream_list = StreamList(STREAM_CONTAINER)
    assert stream_list.profile_links[0] == 'https://www.twitter.com/ScaleByTheBay'
    
