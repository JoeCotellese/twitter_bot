import pytest
import context
from datetime import datetime
from twitter_bot.helper import StreamList, days_since_follow
from test_data import STREAM_CONTAINER

def test_twitterlist():
    stream_list = StreamList(STREAM_CONTAINER)
    assert len(stream_list.profile_links) == 40

def test_twitterlisturls():
    stream_list = StreamList(STREAM_CONTAINER)
    assert stream_list.profile_links[0] == 'https://www.twitter.com/ScaleByTheBay'
    

def test_dayssincefollow():
    result = ('@joecotellese', 1519776000)
    now = 1520640000
    days = days_since_follow(now, result[1])
    assert days == 10