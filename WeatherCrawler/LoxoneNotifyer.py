#!usr/bin/env python
# -*-coding:utf-8 -*-

import socket
import datetime

class LoxoneNotifyer:
    """description of class"""

    def __init__(self, ip, port):
        self.ip = ip
        self.port = port
        self.date2009 = datetime.datetime(2009,1,1)

    def _toLoxDate(date):
        return int((date-datetime.datetime(1970,1,1)).total_seconds())

    def _buildDataEntry(weatherData, dataName, data):
        return weatherData.stationId + '.' + dataName + '=' + str(data) + ' '

    def pushNewData(self, weatherData):
        message = LoxoneNotifyer._buildDataEntry(weatherData, 'dataTime', LoxoneNotifyer._toLoxDate(weatherData.dataTime))
        message += LoxoneNotifyer._buildDataEntry(weatherData, 'temperature', weatherData.temp2m)
        message += LoxoneNotifyer._buildDataEntry(weatherData, 'temp2mMin',   weatherData.temp2mMin)
        message += LoxoneNotifyer._buildDataEntry(weatherData, 'temp2mMinTime', LoxoneNotifyer._toLoxDate(weatherData.temp2mMinTime))
        message += LoxoneNotifyer._buildDataEntry(weatherData, 'temp2mMax', weatherData.temp2mMax)
        message += LoxoneNotifyer._buildDataEntry(weatherData, 'temp2mMaxTime', LoxoneNotifyer._toLoxDate(weatherData.temp2mMaxTime))
        message += LoxoneNotifyer._buildDataEntry(weatherData, 'humidity', weatherData.humidity)
        message += LoxoneNotifyer._buildDataEntry(weatherData, 'dewPoint', weatherData.dewPoint)
        message += LoxoneNotifyer._buildDataEntry(weatherData, 'pressure', weatherData.pressure)
        message += LoxoneNotifyer._buildDataEntry(weatherData, 'pressure3hTrend', weatherData.pressure3hTrend)
        message += LoxoneNotifyer._buildDataEntry(weatherData, 'snowLine', weatherData.snowLine)
        message += LoxoneNotifyer._buildDataEntry(weatherData, 'cloudBase', weatherData.cloudBase)
        message += LoxoneNotifyer._buildDataEntry(weatherData, 'uvIndex', weatherData.uvIndex)
        message += LoxoneNotifyer._buildDataEntry(weatherData, 'solarRadiation', weatherData.solarRadiation)
        message += LoxoneNotifyer._buildDataEntry(weatherData, 'evapotranspiration', weatherData.evapotranspiration)
        message += LoxoneNotifyer._buildDataEntry(weatherData, 'windchill', weatherData.windchill)
        message += LoxoneNotifyer._buildDataEntry(weatherData, 'windSpeed', weatherData.windSpeed)
        message += LoxoneNotifyer._buildDataEntry(weatherData, 'windDirection', weatherData.windDirection)
        message += LoxoneNotifyer._buildDataEntry(weatherData, 'windDominatingDirection', weatherData.windDominatingDirection)
        message += LoxoneNotifyer._buildDataEntry(weatherData, 'gust', weatherData.gust)
        message += LoxoneNotifyer._buildDataEntry(weatherData, 'gustDirection', weatherData.gustDirection)
        message += LoxoneNotifyer._buildDataEntry(weatherData, 'lastFrost', LoxoneNotifyer._toLoxDate(weatherData.lastFrost))
        message += LoxoneNotifyer._buildDataEntry(weatherData, 'rainLastHour', weatherData.rainLastHour)
        message += LoxoneNotifyer._buildDataEntry(weatherData, 'rainDay', weatherData.rainDay)
        message += LoxoneNotifyer._buildDataEntry(weatherData, 'rainLast', LoxoneNotifyer._toLoxDate(weatherData.rainLast))
        message += LoxoneNotifyer._buildDataEntry(weatherData, 'sunrise', LoxoneNotifyer._toLoxDate(weatherData.sunrise))
        message += LoxoneNotifyer._buildDataEntry(weatherData, 'sunZenith', LoxoneNotifyer._toLoxDate(weatherData.sunZenith))
        message += LoxoneNotifyer._buildDataEntry(weatherData, 'sunset', LoxoneNotifyer._toLoxDate(weatherData.sunset))
        message += LoxoneNotifyer._buildDataEntry(weatherData, 'cloudiness', weatherData.cloudiness)

        with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as sock:
            sock.sendto(bytes(message, "utf-8"), (self.ip, self.port))
            sock.close()
