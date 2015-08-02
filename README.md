# CORE Website

The website for the Columbia Organization of Rising Entrepreneurs.

## Local Setup

Run the following commands:

```
#! /bin/bash
virtualenv --no-site-packages .
source bin/activate
pip install -r requirements.txt
```

## Material Design vs. Bootstrap

We're experimenting with Google's [Material Design](http://www.getmdl.io/index.html) library. This website uses a different global font scheme and color scheme from the default files in the Material Design Lite library. These changes are made to the `src/_variables.scss` file in the Material Design Lite [source code](https://github.com/google/material-design-lite).