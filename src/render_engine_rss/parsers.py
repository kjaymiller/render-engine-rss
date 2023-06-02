from typing import Any

from render_engine.parsers.base_parsers import BasePageParser


def parse_rss_feed_entry(entry: dict) -> dict[str, Any]:
    if image := entry.get("image", None):
        if isinstance(image, dict):
            entry["image"] = image.get("href", entry["image"])

    if content := entry.pop("content", None):
        if isinstance(content, list):
            for item in content:
                if item["type"] == "text/html":
                    return entry, item["value"]
        elif isinstance(content, str):
            return entry, content

    elif content := entry.pop("summary", None):
        if isinstance(content, str):
            return entry, content

        elif isinstance(content, dict):
            return entry, content["summary"]

    return entry, ""


class RSSFeedPageParser(BasePageParser):
    @staticmethod
    def parse_content_path(content: dict) -> tuple[dict[str, Any], str]:
        """Fetching content and atttributes from a content_path"""
        return parse_rss_feed_entry(content)

    @staticmethod
    def parse_content(content: str) -> tuple[dict[str, Any], str]:
        return parse_rss_feed_entry(content)


class PodcastPageParser(RSSFeedPageParser):
    pass
