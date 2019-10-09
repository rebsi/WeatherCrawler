#!usr/bin/env python
# -*-coding:utf-8 -*-

import pyodbc
import datetime

class MsSqlWeatherDataMixin:
    """description of class"""

    def _insertIntoTable(self, cursor):
        cursor.execute('INSERT INTO [dbo].[WeatherData] ([StationId],[DataTime],[Elevation],[Temperature],[Temp2mMin],[Temp2mMinTime],[Temp2mMax],[Temp2mMaxTime],[Humidity],[HumidityMin],[HumidityMinTime],[HumidityMax],[HumidityMaxTime],[DewPoint],[DewPointMin],[DewPointMinTime],[DewPointMax],[DewPointMaxTime],[Pressure],[Pressure3hTrend],[Wellness],[ForecastShort],[ForecastLong],[SnowLine],[CloudBase],[UvIndex],[SolarRadiation],[SolarRadiationMax],[SolarRadiationMaxTime],[Evapotranspiration],[Windchill],[WindchillMin],[WindchillMinTime],[WindchillMax],[WindchillMaxTime],[WindSpeed],[WindDirection],[WindDominatingDirection],[WindMaxTime],[WindMax],[WindMaxDirection],[Gust],[GustDirection],[GustMaxTime],[GustMax],[GustMaxDirection],[LastFrost],[LastFrostDuration],[RainLastHour],[RainDay],[RainLast],[Sunrise],[SunZenith],[Sunset],[Cloudiness],[MoonPhase],[MoonNextFull]) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)',
            self.stationId,
            self.dataTime,
            self.elevation,
            self.temperature,
            self.temp2mMin,
            self.temp2mMinTime,
            self.temp2mMax,
            self.temp2mMaxTime,
            self.humidity,
            self.humidityMin,
            self.humidityMinTime,
            self.humidityMax,
            self.humidityMaxTime,
            self.dewPoint,
            self.dewPointMin,
            self.dewPointMinTime,
            self.dewPointMax,
            self.dewPointMaxTime,
            self.pressure,
            self.pressure3hTrend,
            self.wellness,
            self.forecastShort,
            self.forecastLong,
            self.snowLine,
            self.cloudBase,
            self.uvIndex,
            self.solarRadiation,
            self.solarRadiationMax,
            self.solarRadiationMaxTime,
            self.evapotranspiration,
            self.windchill,
            self.windchillMin,
            self.windchillMinTime,
            self.windchillMax,
            self.windchillMaxTime,
            self.windSpeed,
            self.windDirection,
            self.windDominatingDirection,
            self.windMaxTime,
            self.windMax,
            self.windMaxDirection,
            self.gust,
            self.gustDirection,
            self.gustMaxTime,
            self.gustMax,
            self.gustMaxDirection,
            self.lastFrost,
            self.lastFrostDuration,
            self.rainLastHour,
            self.rainDay,
            self.rainLast,
            self.sunrise,
            self.sunZenith,
            self.sunset,
            self.cloudiness,
            self.moonPhase,
            self.moonNextFull)

    def saveToMsSql(self):
        conn = pyodbc.connect('Driver={SQL Server};'
                              'Server=localhost;'
                              'Database=eberTest;'
                              'Trusted_Connection=yes;')

        with conn:
            cursor = conn.cursor()
            cursor.execute('SELECT TOP (1) dataTime FROM [dbo].[WeatherData] WITH (UPDLOCK) ORDER BY dataTime DESC')
            row = cursor.fetchone()

            lastDataTime = None
            if row != None:
                lastDataTime = datetime.datetime.strptime(row[0], '%Y-%m-%d %H:%M:%S.%f0')

            if lastDataTime == None or lastDataTime < self.dataTime:
                self._insertIntoTable(cursor)

            conn.commit()


#CREATE TABLE [WeatherData] (
#	Id INT IDENTITY(1, 1) NOT NULL
#	,EntryTime DATETIME2 NOT NULL DEFAULT(GETDATE())
#	,StationId NVARCHAR(60) NOT NULL
#	,DataTime DATETIME2 NOT NULL
#	,Elevation DECIMAL(4, 0) NULL
#	,Temperature DECIMAL(5, 2) NULL
#	,Temp2mMin DECIMAL(5, 2) NULL
#	,Temp2mMinTime DATETIME2 NULL
#	,Temp2mMax DECIMAL(5, 2) NULL
#	,Temp2mMaxTime DATETIME2 NULL
#	,Humidity DECIMAL(5, 2) NULL
#	,HumidityMin DECIMAL(5, 2) NULL
#	,HumidityMinTime DATETIME2 NULL
#	,HumidityMax DECIMAL(5, 2) NULL
#	,HumidityMaxTime DATETIME2 NULL
#	,DewPoint DECIMAL(5, 2) NULL
#	,DewPointMin DECIMAL(5, 2) NULL
#	,DewPointMinTime DATETIME2 NULL
#	,DewPointMax DECIMAL(5, 2) NULL
#	,DewPointMaxTime DATETIME2 NULL
#	,Pressure DECIMAL(6, 2) NULL
#	,Pressure3hTrend DECIMAL(5, 2) NULL
#	,Wellness NVARCHAR(100) NULL
#	,ForecastShort NVARCHAR(100) NULL
#	,ForecastLong NVARCHAR(1000) NULL
#	,SnowLine DECIMAL(4, 0) NULL
#	,CloudBase DECIMAL(5, 0) NULL
#	,UvIndex DECIMAL(5, 2) NULL
#	,SolarRadiation DECIMAL(8, 2) NULL
#	,SolarRadiationMax DECIMAL(8, 2) NULL
#	,SolarRadiationMaxTime DATETIME2 NULL
#	,Evapotranspiration DECIMAL(6, 3) NULL
#	,Windchill DECIMAL(5, 2) NULL
#	,WindchillMin DECIMAL(5, 2) NULL
#	,WindchillMinTime DATETIME2 NULL
#	,WindchillMax DECIMAL(5, 2) NULL
#	,WindchillMaxTime DATETIME2 NULL
#	,WindSpeed DECIMAL(5, 2) NULL
#	,WindDirection NVARCHAR(7) NULL
#	,WindDominatingDirection NVARCHAR(7) NULL
#	,WindMaxTime DATETIME2 NULL
#	,WindMax DECIMAL(5, 2) NULL
#	,WindMaxDirection NVARCHAR(7) NULL
#	,Gust DECIMAL(5, 2) NULL
#	,GustDirection NVARCHAR(7) NULL
#	,GustMaxTime DATETIME2 NULL
#	,GustMax DECIMAL(5, 2) NULL
#	,GustMaxDirection NVARCHAR(7) NULL
#	,LastFrost DATETIME2 NULL
#	,LastFrostDuration NVARCHAR(100) NULL
#	,RainLastHour DECIMAL(5, 2) NULL
#	,RainDay DECIMAL(5, 2) NULL
#	,RainLast DATETIME2 NULL
#	,Sunrise DATETIME2 NULL
#	,SunZenith DATETIME2 NULL
#	,Sunset DATETIME2 NULL
#	,Cloudiness DECIMAL(5, 2) NULL
#	,MoonPhase DECIMAL(5, 2) NULL
#	,MoonNextFull DATETIME2 NULL
#   ,PRIMARY KEY (Id)
#	)

