import pytest
from render_engine_rss.collection import RSSCollection, feedparser


@pytest.fixture
def mock_parser(monkeypatch):


    def mock_parse(*args, **kwargs):
        feed_item = {
                    'link': 'https://kjaymiller.com/blog/the-pit-show-it-s-easy-when-you-re-customer-number-one.html',
                    'published': 'Mon, 11 Feb 2019 08:00:00 +0000',
                    'summary': "<p>My guest this week is Justin Duke. </p><p>Just is a developer</p>",
                    'title': "Test Title",
        }

        return {
                "entries": [feed_item]
        }

    monkeypatch.setattr(
            feedparser,
            "parse",
            mock_parse, 
    )

def test_collection_parses_pages_string(mock_parser):
    """Test that the collection can parse a feed into pages"""
    
    class SimpleRSSCollection(RSSCollection):
        content_path = "https://example.com/rss"

    collection = SimpleRSSCollection()

    assert len(list(collection.pages)) == 1 
    assert next(collection.pages).title == "Test Title"
