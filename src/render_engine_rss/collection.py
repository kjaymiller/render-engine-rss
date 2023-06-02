from .parsers import RSSFeedPageParser
import feedparser
from render_engine.blog import Blog


class RSSCollection(Blog):
    PageParser = RSSFeedPageParser
    content_path = str
    sort_by = "published_parsed"

    def __init__(self):
        self.content = feedparser.parse(self.content_path)
        super().__init__()

    def get_partial_collection(self):
        for page in self.iter_content_path():
            yield self.get_page(page)

    def iter_content_path(self):
        return self.content.entries
