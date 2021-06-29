<head>
  <meta charset="utf-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  {%- seo -%}
  <link rel="stylesheet" href="{{ "/assets/css/style.css" | relative_url }}">
  {%- feed_meta -%}
  {%- if jekyll.environment == 'production' and site.google_analytics -%}
    {%- include google-analytics.html -%}
  {%- endif -%}
  <meta name="google-site-verification" content="2yFYZWwMInNYqVGarzS4imN1ASlVCGiR2IBy-c17q2g" />
</head>
# yellow-pages-scraper
Python Selenium based scraper which scrapes the details of businesses and outputs a csv in the same folder.
Gets Name, Category, Phone Number, Address and locality.

**REQUIREMENTS**

`pip3 install selenium`


**INSTALLATION**

simply run

`git clone https://github.com/abhishekrai43/yellow-pages-scraper`

`cd yellow-pages-scraper`


**RUN**

`python3 yellow-pages.py`

