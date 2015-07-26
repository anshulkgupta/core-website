# CORE Website

The website for the Columbia Organization of Rising Entrepreneurs.

## Setup on localhost

Run the following commands:

```
#! /bin/bash
virtualenv --no-site-packages .
source bin/activate
pip install -r requirements.txt
```

## Material Design vs. Bootstrap

We're experimenting with Google's [Material Design] (http://www.getmdl.io/index.html) library. 

This website uses a differnet global font scheme and color scheme from the default files in the Material Design Lite library. These changes are made to the `src/_variables.scss` file in the Material Design lite [source code] (https://github.com/google/material-design-lite). The source code is then compiled into the `material.css` file that is used in this repository.

The following steps were performed to achieve this:
```
# Clone/copy the Material Design lite source code.
git clone https://github.com/google/material-design-lite.git
# Go into the newly created folder containing the source code.
cd material-design-lite
# Install necessary dependencies.
npm install && npm install -g gulp
# Make the changes to the src/_variables.scss file
<see below>
# Build a production version of the components.
gulp
# Use the dist/material.css file as a stylesheet
```

### Changes to _variables.scss of MDL v1.0.1
```
--- a/src/_variables.scss
+++ b/src/_variables.scss
@@ -55,8 +55,8 @@
    We should be able to improve on this once CSS Font Loading L3 becomes more
    widely available.
 */
-$preferred_font: 'Roboto', 'Helvetica', 'Arial', sans-serif !default;
-$performance_font: 'Helvetica', 'Arial', sans-serif !default;
+$preferred_font: 'Montserrat', 'Roboto', 'Helvetica', 'Arial', sans-serif !default;
+$performance_font: 'Montserrat', 'Helvetica', 'Arial', sans-serif !default;

 /* ==========  COLORS  ========== */

@@ -82,9 +82,9 @@ $trim-color-classes: false !default;

 // Use color primarily for emphasis. Choose colors that fit with
 // your brand and provide good contrast between visual components.
-$color-primary: $palette-indigo-500 !default;
-$color-primary-dark: $palette-indigo-700 !default;
-$color-accent: $palette-pink-A200 !default;
+$color-primary: 84,161,255 !default; // CORE Blue in RGB
+$color-primary-dark: 33,133,255 !default; // Two shades darker than the $color-primary
+$color-accent: $palette-indigo-A200 !default;
```
