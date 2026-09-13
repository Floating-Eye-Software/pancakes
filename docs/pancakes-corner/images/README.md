# Pancakes Corner Images

This directory contains local display copies of freely licensed images linked
from Pancakes Corner articles. Each article keeps its image wrapped in a link
to the corresponding Wikimedia Commons file page so readers can inspect the
source, creator, and license.

Downloads are intentionally gradual because Wikimedia applies long cooldowns
after throttling. From the repository root:

```sh
make corner-images-status
make corner-images
```

`make corner-images` attempts at most three missing files, waits 15 seconds
between attempts, stops immediately on HTTP 429, and changes an article to its
local image path only after that file exists. Run it occasionally until
`make corner-images-status` reports that every referenced image is local.
