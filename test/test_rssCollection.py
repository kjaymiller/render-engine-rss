import pytest
from render_engine_rss.collection import RSSCollection, feedparser
from datetime import time


@pytest.fixture
def mock_parser(monkeypatch):


    def mock_parse(*args, **kwargs):
        feed_items = [
                {
                    'link': 'https://example.com/1',
                    'published_parsed': "b",
                    'summary': "This is Example 1",
                    'title': "Test Title 1",
                },
                {
                    'link': 'https://example.com/2',
                    'published_parsed': "a",
                    'summary': "This is Example 2",
                    'title': "Test Title 2",
                },
        ]

        return {"entries": feed_items}

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

    assert len(list(collection.pages)) == 2 
    for entry  in map(lambda x: x.title, collection.pages):
        assert entry in ["Test Title 1", "Test Title 2"]


def test_collection_includes_template(mock_parser):
    """Test that the collection can parse a feed into pages with templates"""

    class SimpleRSSCollection(RSSCollection):
        content_path = "https://example.com/rss"
        template = "test.html"

    collection = SimpleRSSCollection()

    next(collection.pages).template == "test.html"


def test_collection_sorts_by_published_parsed(mock_parser):
    """Test that the collection can parse a feed into pages with templates"""

    class SimpleRSSCollection(RSSCollection):
        content_path = "https://example.com/rss"

    collection = SimpleRSSCollection()

    assert collection.sorted_pages[0].title == "Test Title 2"