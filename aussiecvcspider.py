# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

import json
import os
import urllib.request
from datetime import datetime, timedelta
from pathlib import Path
from time import sleep

import pytz
from pytz import timezone

POI_LIST_URL = 'https://www.aussiebroadband.com.au/__process.php?mode=CVCDropdown'  # NOQA: E501


def main():
    # Set up the data directory.
    cwd = Path(os.getcwd())
    data_dir = cwd / 'data'
    if not data_dir.is_dir():
        data_dir.mkdir()

    # Get POI information.
    poi_list = json.loads(urllib.request.urlopen(POI_LIST_URL).read())

    # Pull and save POI chart
    for poi in poi_list:
        print(poi['name'])
        # Ensure that POI directory has been created.
        poi_dir = data_dir / poi['name']
        if not poi_dir.is_dir():
            poi_dir.mkdir()

        # Try to determine what date the current chart image represents based
        # on the HTTP 'Last-Modified' date.
        request = urllib.request.Request(poi['url'], method='HEAD')
        response = urllib.request.urlopen(request)
        # Some date massaging...
        modified_at = response.getheader('Last-Modified')
        modified_at = datetime.strptime(modified_at,
                                        '%a, %d %b %Y %H:%M:%S %Z')
        modified_at = modified_at.replace(tzinfo=pytz.utc)
        modified_at = modified_at.astimezone(timezone('Australia/Perth'))
        chart_date = (modified_at - timedelta(days=1)).date()

        # Check for an existing chart for this date.
        chart_path = poi_dir / '{}.png'.format(chart_date.isoformat())
        if not chart_path.exists():
            chart = chart_path.open('wb')
            chart.write(urllib.request.urlopen(poi['url']).read())
            print('\tChart saved!')
        else:
            print('\tWe already have today\'s chart.')


if __name__ == '__main__':
    main()
