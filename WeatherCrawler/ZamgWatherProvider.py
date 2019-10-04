from bs4 import BeautifulSoup
from html.parser import HTMLParser
import urllib.request
import re
import datetime
from WeatherData import WeatherData

class ZamgWatherProvider(object):
    """description of class"""

    def getWatherData(self):
        req = urllib.request.Request(
            "https://www.zamg.ac.at/cms/de/wetter/wetterwerte-analysen/oberoesterreich", 
            data=None, 
            headers={
                'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'
            }
        )

        fp = urllib.request.urlopen(req)
        mybytes = fp.read()
        mystr = mybytes.decode("utf8")
        fp.close()

        location = 'Wolfsegg'

        soup = BeautifulSoup(mystr, "html.parser")
        locationLinks = soup.findAll("a", text = location)
        if (len(locationLinks) != 1):
            raise Exception('Failed to find location link for [{}]. count: {}'.format(location, locationLinks.count))

        values = locationLinks[0].parent.parent.findChildren(recursive=False)

        h2 = soup.findAll("h2", text = re.compile("Aktuelle Messwerte der Wetterstationen von "))

        dataFromHour = int(re.search("(\d+)", h2[0].text)[1])
        dataDateTime = datetime.datetime.now().replace(hour=dataFromHour, minute=0, second=0, microsecond=0)

        try:
            temperature = float(values[2].text[:-1])
            humidity = float(values[3].text[:-1])
            windRe = re.search("(.+), (\d+) km/h", values[4].text)
            windDirection = windRe[1]
            windSpeed = int(windRe[2])
            gust = int(re.search("(\d+) km/h", values[5].text)[1])
            rainLastHour = float(re.search("(\d+\.\d+) mm", values[6].text)[1])
            sun = int(values[7].text[:-1])
            pressure = float(re.search("(\d+\.\d+) hPa", values[8].text)[1])
            elevation = int(re.search("(\d+)", values[1].text)[1])
        except:
            raise Exception('Failed to parse data: {}'.format(sys.exc_info()[0]))

        return WeatherData(dataDateTime, temperature, humidity, windDirection, windSpeed, gust, rainLastHour, sun, pressure, elevation)
