from typing import Any
from .parsers import RSSFeedPageParser
import pluggy
import feedparser
from render_engine.collection import Collection


class RSSCollection(Collection):
    PageParser = RSSFeedPageParser
    content_path = str
    sort_by = "published_parsed"
    sort_reverse = True

    def __init__(self, plugins: list = []):
        self.content = feedparser.parse(self.content_path)
        super().__init__(plugins=plugins)

    def get_partial_collection(self):
        for page in self.iter_content_path():
            yield self.get_page(page)

    def iter_content_path(self):
        return self.content.entries
