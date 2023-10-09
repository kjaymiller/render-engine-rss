import pytest
from render_engine_rss.collection import RSSCollection

class SimpleRSSCollection(RSSCollection):
    content_path = "./test/test_output.rss"
    template = "test.html"

class TestRSSCollection:

    collection = SimpleRSSCollection()

    def test_collection_parses_url(self):
        """
        Test the collection can parse a feed url into pages
        17 Mar 2023 - With feedparser having a 'cgi deprecation warning'
        this test is to ensure we can still parse a url
        
        # TODO: Figure out test for url parsing.
        """
        assert len([p for p in self.collection.__iter__()]) == 2 


    @pytest.mark.parametrize(
            "index, title",
            [
                (0, "Test Title 1"),
                (1, "Test Title 2")
            ],
    )
    def test_collection_parses_pages_string(self, index, title):
        """Test that the collection can parse a feed into pages
        17 Mar 2023 - With feedparser having a 'cgi deprecation warning'
        this test is to ensure we can still parse a filepath
        """
        assert [x.title for x in self.collection][index] == title


    def test_collection_includes_template(self):
        """Test that the collection can parse a feed into pages with templates"""
        for x in self.collection:
            assert x.template == "test.html"


    def test_collection_sorts_by_published_parsed(self):
        """Test that the collection can parse a feed into pages with templates"""

        assert self.collection.sorted_pages[0].title == "Test Title 2"