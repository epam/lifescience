---
kind: example
shows: [image]
---

# Image

A blue square as an SVG image, two units wide, with its top-left corner at (0, 2).

```json
{
  "ket_version": "2.0.0",
  "root": {
    "nodes": [
      {
        "type": "image",
        "format": "image/svg+xml",
        "boundingBox": {"x": 0, "y": 2, "z": 0, "width": 2, "height": 2},
        "data": "PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIzMiIgaGVpZ2h0PSIzMiIgdmlld0JveD0iMCAwIDMyIDMyIj48cmVjdCB4PSIwIiB5PSIwIiB3aWR0aD0iMzIiIGhlaWdodD0iMzIiIGZpbGw9IiMzMzY2Y2MiLz48L3N2Zz4="
      }
    ]
  }
}
```
