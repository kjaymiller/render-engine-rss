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

        attrs = content

        if image:=attrs.get('image', None):
            if isinstance(image, dict):
                attrs['image'] = image.get("href", attrs["image"])


        if _content:=attrs.get('content', None):
            if isinstance(attrs['content'], list):
                for item in attrs['content']:
                    if item['type'] == 'text/html':
                        attrs['content'] = content = item['value']
                        return attrs, content
        else:
            return attrs, ''

        return attrs, content