# aussiecvcspider
Automatically fetches and stores publicly available Aussie Broadband CVC usage charts for future consumption

## Introduction
[Aussie Broadband](https://www.aussiebroadband.com.au/) publishes [daily charts](https://www.aussiebroadband.com.au/cvc-graphs/) showing per-POI usage of their NBN CVC.

This is to allow their customers to keep them honest about not overprovisioning user connections relative to their available backhaul (resulting in slow connections).

However, Aussie Broadband only publish these charts once a day, and does not publish old data. In an attempt to track CVC usage trends, this script automatically downloads the daily charts for all NBN POIs that Aussie Broadband service.

## Features
- Python 3
- Only relies on `pytz` (but who can help that!?)
- Only downloads charts when there are new ones available (makes use of HTTP `HEAD` and `Last-Modified`)

## Quickstart

1. Download:
    ```
    $ wget https://github.com/KyeRussell/$ cd aussiecvcspider-master
    $ virtualenv .venv --python=python3
    $ source .venv/bin/activate
    $ pip install -r requirements.txt
    ```

2. Extract:
    ```
    $ tar xzvf master.tar.gz
    ```

3. Set up Python virtualenv:
    ```
    $ cd aussiecvcspider-master
    $ virtualenv .venv --python=python3
    $ source .venv/bin/activate
    $ pip install -r requirements.txt
    ```

4. Run:
    ```
    $ python aussiecvcspider.py
    ```

5. Your charts will now be available in `data/POI Name/date.png`.


## Disclaimer
- I am not affiliated with Aussie Broadband.
- I did not ask for permission before writing this.
- If you run this, you are responsible for any reprecussions.
