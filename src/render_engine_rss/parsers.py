import pathlib
import feedparser
from typing import Any

from render_engine.parsers.base_parsers import BasePageParser

class RSSFeedPageParser(BasePageParser):
    @staticmethod
    def parse_content(content: dict) -> tuple[dict[str, Any], str]:
        """Fething content and atttributes from a content_path"""

        attrs = content 
        content = attrs.pop("summary", None)

        return attrs, content


    @staticmethod
    def markup(page: type["Page"], content: str) -> str:
        """Markup the content with the page's template"""

        return content


class PodcastPageParser(RSSFeedPageParser):
    @staticmethod
    def parse_content(content: dict) -> tuple[dict[str, Any], str]:
        """Fething content and atttributes from a content_path"""

        attrs, _content = RSSFeedPageParser.parse_content(content)

        if 'image' in attrs:
            attrs['image'] = attrs["image"].get("href", attrs["image"])

        for item in _content:
            if item.get("type", None) == "text/html":
                content = item['value']

        return attrs, content
        