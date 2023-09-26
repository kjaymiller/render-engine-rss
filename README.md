# render-engine-rss

Render-Engine-RSS is a [render-engine custom parser](https://render-engine.readthedocs.io/en/latest/parsers/) that enables you to create a collection based on the contents of an RSS Feed.

This is especially good when you're working with a podcast or newsletter service.

> **NOTE**
> This custom collection is read-only and does not create local copies of the parsed feeds

## Parsers

Render Engine RSS Comes with 1 CustomCollection Collection Object and 2 PageParsers

### RSSCollection and RSSFeedPageParser

The RSSCollection object is the most frequent way to fetch your feed. 

The default parser for this collection is the RSSFeedPageParser which parses individual entries into Page objects based on their RSS Metadata.

Set your `content_path` to a **url** or **local file path**. 

```python
from render_engine.site import Site
from render_engine_rss.collection import RSSCollection

app = Site()

@app.collection
class Newsletter(RSSCollection):
    routes = ['newsletter']
    content_path = "https://buttondown.email/kjaymiller/rss"
```

### The PodcastPageParser

> **NOTE**
> You can also use the PodcastPageParser to index videos from a YouTube channel. This usage is experimental and may not be maintained in the long term.

This extension was originally designed to create a local collection for a few podcasts. The PodcastPageParser is designed to process feeds designed for podcasts.

To use, pass in the PodcastPageParser to your collection.

```python
from render_engine_rss.collection import RSSCollection
from render_engine_rss.parsers import PodcastPageParser

@app.collection
class Conduit(RSSCollection):
    PageParser = PodcastPageParser
    routes = ['conduit']
    content_path = "https://www.relay.fm/conduit/feed"
```

