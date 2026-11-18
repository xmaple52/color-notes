# color-notes

Inspect HEX colors and calculate WCAG contrast ratios for text.

Python 3.10+ · standard library only.

## Quick start

```sh
python color_notes.py 99e97a --background 080d0b
```

Accepts opaque sRGB HEX colors only, with or without `#`. Uses WCAG relative luminance and contrast formula. Reports text thresholds: AA normal 4.5:1, AA large 3:1, AAA normal 7:1. Large text means at least 18 pt, or 14 pt bold. Contrast alone is not a complete accessibility audit. No browser, network, or dependencies required.

## Tests

```sh
python -m unittest discover -s tests -v
```
