from typing import Type
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
        self.raw_content = feedparser.parse(self.content_path)
        super().__init__(plugins=plugins)


    def iter_content_path(self):
        return self.raw_content.entries