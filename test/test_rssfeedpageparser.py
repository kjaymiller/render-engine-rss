import copy
from render_engine import page
from render_engine_rss.parsers import RSSFeedPageParser, PodcastPageParser

def test_rss_feed_page_parse():

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


def test_podcast_page_parser():
    feed_item = [
        {
            'type': 'text/html',
            'value': 'some html text',
        },
        {
            'type': 'text/plain',
            'value': 'some other text',
        },

    ]


    class TestPage(page.Page):
        Parser = PodcastPageParser
        content = {
                'content': feed_item,
                'image': {"href": "https://example.com/image.jpg"}
                }

    test_page = TestPage()
    assert test_page.image == "https://example.com/image.jpg"
    assert test_page.content== "some html text"


