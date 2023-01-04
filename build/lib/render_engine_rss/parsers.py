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
