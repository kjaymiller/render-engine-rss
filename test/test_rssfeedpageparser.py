import copy
import pytest
from render_engine import page
from render_engine_rss.parsers import RSSFeedPageParser

def test_parse():

    feed_item = {
        'link': 'https://kjaymiller.com/blog/the-pit-show-it-s-easy-when-you-re-customer-number-one.html',
        'published': 'Mon, 11 Feb 2019 08:00:00 +0000',
        'summary': "<p>My guest this week is Justin Duke. </p><p>Just is a developer</p>",
    }

    class TestPage(page.Page):
        Parser = RSSFeedPageParser
        content = copy.copy(feed_item) # copy the dict so we don't modify the original

    test_page = TestPage()
    assert test_page.link == feed_item['link']
    assert test_page.content == feed_item['summary']

