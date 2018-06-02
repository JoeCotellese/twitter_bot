import pytest
import context
from twitter_bot.storage import Storage

def test_storage():
    storage = Storage('test.db')
    storage.save_user('@joecotellese')
    results = storage.get_user('@joecotellese')
    storage.remove_user('@joecotellese')
    assert results[0] == '@joecotellese'

