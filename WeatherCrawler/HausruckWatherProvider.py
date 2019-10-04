from bs4 import BeautifulSoup
from html.parser import HTMLParser
import urllib3
import re
import time
import datetime
import locale
from WeatherData import WeatherData

import subprocess

class HausruckWatherProvider(object):
    """description of class"""

    def _getTextFromTr(tableRows, idx, subIdx = 1, tag = 'font'):
        return tableRows[idx].findChildren(tag)[subIdx].text

    def _parseInt(self, str):
        return int(re.search("(\d+)", str)[1])

    def _parseFloat(self, str):
        return float(re.search("(\d+,\d+)", str)[1].replace(',','.'))

    def _parseTime(self, str):
        timePart = datetime.datetime.strptime(re.search("(\d+:\d+)", str)[1], '%H:%M')
        return datetime.datetime.now().replace(hour=timePart.hour, minute=timePart.minute, second=0, microsecond=0)

    def _parseDirection(self, str):
        return re.search(".+ / (.+)", str)[1]

    def _parseDirectionAndString(self, str):
        return re.search("(.+) (\d+.+)", str)

    def _monthTextToNr(self, str):
        if (str.startswith('J')):
            return '1'
        if (str.startswith('F')):
            return '2'
        if (str.startswith('Mä')):
            return '3'
        if (str.startswith('Ap')):
            return '4'
        if (str.startswith('Ma')):
            return '5'
        if (str.startswith('Jun')):
            return '6'
        if (str.startswith('Jul')):
            return '7'
        if (str.startswith('Au')):
            return '8'
        if (str.startswith('S')):
            return '9'
        if (str.startswith('O')):
            return '10'
        if (str.startswith('N')):
            return '11'
        if (str.startswith('D')):
            return '12'
        raise Exception('Failed to parse month: ' + str)

    def getWatherData(self):
        #header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36'}
        #http = urllib3.PoolManager(1, header)
        #response = http.request('GET', 'http://wetter-hausruckviertel.at/wetter_wolfsegg/current.html')
        #soup = BeautifulSoup(response.data.decode('utf-8'))

        output = subprocess.Popen(['FetchPageWorkaround.exe', 'http://wetter-hausruckviertel.at/wetter_wolfsegg/current.html'], stdout=subprocess.PIPE).communicate()[0]
        soup = BeautifulSoup(output)
        
        tableRows = soup.findAll("tr")

        dataDateGrp = re.search("(\d{1,2}\.) (.+)( \d{4})", HausruckWatherProvider._getTextFromTr(tableRows, 2))
        dataTime = datetime.datetime.strptime(HausruckWatherProvider._getTextFromTr(tableRows, 3) + ' ' + dataDateGrp[1] + self._monthTextToNr(dataDateGrp[2]) + dataDateGrp[3], '%H:%M %d.%m %Y')
        
        elevation = int(re.search("(\d+) m", tableRows[0].findChildren('b')[0].text)[1])

        temp2m = self._parseFloat(HausruckWatherProvider._getTextFromTr(tableRows, 4, 2))
        temp2mMin = self._parseFloat(HausruckWatherProvider._getTextFromTr(tableRows, 4, 4))
        temp2mMinTime = self._parseTime(HausruckWatherProvider._getTextFromTr(tableRows, 4, 3))
        temp2mMax = self._parseFloat(HausruckWatherProvider._getTextFromTr(tableRows, 4, 6))
        temp2mMaxTime = self._parseTime(HausruckWatherProvider._getTextFromTr(tableRows, 4, 5))
        
        humidity = self._parseInt(HausruckWatherProvider._getTextFromTr(tableRows, 6, 2))
        humidityMin = self._parseInt(HausruckWatherProvider._getTextFromTr(tableRows, 6, 4))
        humidityMinTime = self._parseTime(HausruckWatherProvider._getTextFromTr(tableRows, 6, 3))
        humidityMax = self._parseInt(HausruckWatherProvider._getTextFromTr(tableRows, 6, 6))
        humidityMaxTime = self._parseTime(HausruckWatherProvider._getTextFromTr(tableRows, 6, 5))

        dewPoint = self._parseFloat(HausruckWatherProvider._getTextFromTr(tableRows, 7, 2))
        dewPointMin = self._parseFloat(HausruckWatherProvider._getTextFromTr(tableRows, 7, 4))
        dewPointMinTime = self._parseTime(HausruckWatherProvider._getTextFromTr(tableRows, 7, 3))
        dewPointMax = self._parseFloat(HausruckWatherProvider._getTextFromTr(tableRows, 7, 6))
        dewPointMaxTime = self._parseTime(HausruckWatherProvider._getTextFromTr(tableRows, 7, 5))

        pressure = self._parseFloat(HausruckWatherProvider._getTextFromTr(tableRows, 8, 2))
        pressure3hTrend = self._parseFloat(HausruckWatherProvider._getTextFromTr(tableRows, 8, 3))

        wellness = HausruckWatherProvider._getTextFromTr(tableRows, 9)
        forecastShort = HausruckWatherProvider._getTextFromTr(tableRows, 10)
        forecastLong = HausruckWatherProvider._getTextFromTr(tableRows, 11).strip()
        snowLine = self._parseInt(HausruckWatherProvider._getTextFromTr(tableRows, 12))
        cloudBase = self._parseInt(HausruckWatherProvider._getTextFromTr(tableRows, 13))
        uvIndex = self._parseFloat(HausruckWatherProvider._getTextFromTr(tableRows, 14, 2))

        solarRadiation = self._parseInt(HausruckWatherProvider._getTextFromTr(tableRows, 15, 2))
        solarRadiationMax = self._parseInt(HausruckWatherProvider._getTextFromTr(tableRows, 15, 4))
        solarRadiationMaxTime = self._parseTime(HausruckWatherProvider._getTextFromTr(tableRows, 15, 3))

        evapotranspiration = self._parseFloat(HausruckWatherProvider._getTextFromTr(tableRows, 16))

        windchill = self._parseFloat(HausruckWatherProvider._getTextFromTr(tableRows, 17, 2))
        windchillMin = self._parseFloat(HausruckWatherProvider._getTextFromTr(tableRows, 17, 4))
        windchillMinTime = self._parseTime(HausruckWatherProvider._getTextFromTr(tableRows, 17, 3))
        windchillMax = self._parseFloat(HausruckWatherProvider._getTextFromTr(tableRows, 17, 6))
        windchillMaxTime = self._parseTime(HausruckWatherProvider._getTextFromTr(tableRows, 17, 5))

        windSpeed = self._parseFloat(HausruckWatherProvider._getTextFromTr(tableRows, 19, 2))
        windDirection = self._parseDirection(HausruckWatherProvider._getTextFromTr(tableRows, 20))
        windDominatingDirection = HausruckWatherProvider._getTextFromTr(tableRows, 20, 3)
        windMaxTime = self._parseTime(HausruckWatherProvider._getTextFromTr(tableRows, 19, 3))
        windMaxGrp = self._parseDirectionAndString(HausruckWatherProvider._getTextFromTr(tableRows, 19, 4))
        windMax = self._parseFloat(windMaxGrp[2])
        windMaxDirection = windMaxGrp[1]

        gust = self._parseFloat(HausruckWatherProvider._getTextFromTr(tableRows, 18, 2))
        gustDirection = self._parseDirection(HausruckWatherProvider._getTextFromTr(tableRows, 21))
        gustMaxTime = self._parseTime(HausruckWatherProvider._getTextFromTr(tableRows, 18, 3))
        gustMaxGrp = self._parseDirectionAndString(HausruckWatherProvider._getTextFromTr(tableRows, 18, 4))
        gustMax = self._parseFloat(gustMaxGrp[2])
        gustMaxDirection = gustMaxGrp[1]

        lastFrost = datetime.datetime.strptime(HausruckWatherProvider._getTextFromTr(tableRows, 22, 3), '(%H:%M\xa0\xa0%d.%m.%Y)')
        lastFrostDuration = HausruckWatherProvider._getTextFromTr(tableRows, 22, 2)[7:]

        rainLastHour = self._parseFloat(HausruckWatherProvider._getTextFromTr(tableRows, 23, 1))
        rainDay = self._parseFloat(HausruckWatherProvider._getTextFromTr(tableRows, 23, 2))
        rainLast = datetime.datetime.strptime(tableRows[26].findChildren('b')[0].contents[0], '%H:%M\xa0\xa0%d.%m.%Y')
        
        sunrise = self._parseTime(HausruckWatherProvider._getTextFromTr(tableRows, 33, 0, 'b'))
        sunZenith = self._parseTime(HausruckWatherProvider._getTextFromTr(tableRows, 34, 0, 'b'))
        sunset = self._parseTime(HausruckWatherProvider._getTextFromTr(tableRows, 35, 0, 'b'))
        cloudiness = 100 - self._parseInt(HausruckWatherProvider._getTextFromTr(tableRows, 37, 0, 'b'))

        moonPhase = self._parseInt(HausruckWatherProvider._getTextFromTr(tableRows, 41, 0, 'b'))
        moonNextFullGrp = re.search("(.+\.) (.+)( \d{4})", HausruckWatherProvider._getTextFromTr(tableRows, 42, 0, 'b').replace('\xa0', ''))
        moonNextFull = datetime.datetime.strptime(moonNextFullGrp[1] + self._monthTextToNr(dataDateGrp[2]) + moonNextFullGrp[3], '%H:%M %d.%m %Y')

        return WeatherData('Wolfsegg',
            dataTime, elevation, temp2m, temp2mMin, temp2mMinTime, temp2mMax, temp2mMaxTime, 
            humidity, humidityMin, humidityMinTime, humidityMax, humidityMaxTime, 
            dewPoint, dewPointMin, dewPointMinTime, dewPointMax, dewPointMaxTime, 
            pressure, pressure3hTrend, 
            wellness, forecastShort, forecastLong, snowLine, cloudBase, uvIndex, 
            solarRadiation, solarRadiationMax, solarRadiationMaxTime, 
            evapotranspiration, 
            windchill, windchillMin, windchillMinTime, windchillMax, windchillMaxTime, 
            windSpeed, windDirection, windDominatingDirection, windMaxTime, windMaxGrp, windMax, windMaxDirection, 
            gust, gustDirection, gustMaxTime, gustMaxGrp, gustMax, gustMaxDirection, 
            lastFrost, lastFrostDuration, 
            rainLastHour, rainDay, rainLast, 
            sunrise, sunZenith, sunset, cloudiness, 
            moonPhase, moonNextFullGrp, moonNextFull
            )
