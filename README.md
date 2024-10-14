# Logo Addition to Media Files

This repository contains Python scripts that add logos to image and video files. The scripts support both portrait and landscape orientations, ensuring that logos are placed appropriately.

## Features

- Add logos to JPG images.
- Add logos to video files (MP4, MOV, AVI, MKV).
- Automatically adjust logo placement based on image/video orientation (portrait or landscape).

## Prerequisites

Before running the scripts, ensure you have the following installed on your machine:

- Python 3.x
- `pip` (Python package installer)

### Required Libraries

You need the following Python libraries:
- Pillow (PIL)
- MoviePy
- CairoSVG (if using SVG logos)

You can install these libraries using the following command:

```bash
pip install Pillow moviepy cairosvg
