import pytest
import context
from datetime import datetime
from twitter_bot.parseprofile import ParseProfile
from test_data import PROFILE_FOLLOWING_ME, PROFILE_NOTFOLLOWING_ME, PROFILE_ME


def test_following_count():
    profile = ParseProfile(PROFILE_NOTFOLLOWING_ME)
    assert profile.following_count == 1479

def test_followers_count():
    profile = ParseProfile(PROFILE_NOTFOLLOWING_ME)
    assert profile.follower_count == 12598791
    
def test_join_date():
    profile = ParseProfile(PROFILE_NOTFOLLOWING_ME)
    assert profile.join_date == datetime(2007, 3, 27, 7, 19)

def test_twitter_handle():
    profile = ParseProfile(PROFILE_NOTFOLLOWING_ME)
    assert profile.twitter_handle == '@washingtonpost'

def test_notfollowing():
    profile = ParseProfile(PROFILE_NOTFOLLOWING_ME)
    assert profile.following == False

def test_notfollowing_itsme():
    profile = ParseProfile(PROFILE_ME)
    assert profile.following == False

def test_following():
    profile = ParseProfile(PROFILE_FOLLOWING_ME)
    assert profile.following == True
    
def test_follows_back():
    profile = ParseProfile(PROFILE_FOLLOWING_ME)
    assert profile.follows_back == True

def test_doesnt_follow_back():
    profile = ParseProfile(PROFILE_NOTFOLLOWING_ME)
    assert profile.follows_back == False
    