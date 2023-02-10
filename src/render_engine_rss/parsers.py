import pathlib
import feedparser
from typing import Any

from render_engine.parsers.base_parsers import BasePageParser

class RSSFeedPageParser(BasePageParser):
    @staticmethod
    def parse_content_path(content: dict) -> tuple[dict[str, Any], str]:
        """Fething content and atttributes from a content_path"""
        return content

    @staticmethod
    def parse_content(content: dict) -> tuple[dict[str, Any], str]:
        attrs = content 
        content = attrs.pop("summary", None)

        return attrs, content


class PodcastPageParser(RSSFeedPageParser):
    @staticmethod
    def parse_content_path(content: dict):
        return content

    @staticmethod
    def parse_content(content: dict) -> tuple[dict[str, Any], str]:
        """Fething content and atttributes from a content_path"""

        attrs = content

        if image:=attrs.get('image', None):
            if isinstance(image, dict):
                attrs['image'] = image.get("href", attrs["image"])

        if _content:=attrs.get('content', None):
            if isinstance(_content, list):
                for item in _content:
                    if item['type'] == 'text/html':
                        return attrs, item['value'] 
            elif isinstance(_content, str):
                    return attrs, _content

        return attrs, ""