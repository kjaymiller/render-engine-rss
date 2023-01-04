from typing import Type
from .parsers import RSSFeedPageParser
import feedparser
from render_engine.collection import Collection

class RSSCollection(Collection):
    PageParser = RSSFeedPageParser
    content_path = str

    def __init__(self):
        self.content = feedparser.parse(self.content_path)
        super().__init__()

    @property
    def pages(self):
        """Entries for this would be """

        for entry in self.content['entries']:
            yield self.content_type(content=entry, Parser=self.PageParser)
            