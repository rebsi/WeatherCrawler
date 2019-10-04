import datetime
from MsSqlWeatherDataMixin import MsSqlWeatherDataMixin

class WeatherData(MsSqlWeatherDataMixin):
    """description of class"""
    def __init__(self, stationId, dataTime, temperature, humidity, windDirection, windSpeed, gust, rainLastHour, sun, pressure, elevation):
        self.stationId = stationId
        self.dataTime = dataTime
        self.temperature = temperature
        self.humidity = humidity
        self.windDirection = windDirection
        self.windSpeed = windSpeed
        self.gust = gust
        self.rainLastHour = rainLastHour
        self.cloudiness = 100 - sun
        self.pressure = pressure
        self.elevation = elevation

    def __init__(
        self, stationId,
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
    ):
        self.stationId = stationId
        self.dataTime = dataTime

        self.elevation = elevation

        self.temperature = self.temp2m = temp2m
        self.temp2mMin = temp2mMin
        self.temp2mMinTime = temp2mMinTime
        self.temp2mMax = temp2mMax
        self.temp2mMaxTime = temp2mMaxTime

        self.humidity = humidity
        self.humidityMin = humidityMin
        self.humidityMinTime = humidityMinTime
        self.humidityMax = humidityMax
        self.humidityMaxTime = humidityMaxTime

        self.dewPoint = dewPoint
        self.dewPointMin = dewPointMin
        self.dewPointMinTime = dewPointMinTime
        self.dewPointMax = dewPointMax
        self.dewPointMaxTime = dewPointMaxTime

        self.pressure = pressure
        self.pressure3hTrend = pressure3hTrend

        self.wellness = wellness
        self.forecastShort = forecastShort
        self.forecastLong = forecastLong
        self.snowLine = snowLine
        self.cloudBase = cloudBase
        self.uvIndex = uvIndex

        self.solarRadiation = solarRadiation
        self.solarRadiationMax = solarRadiationMax
        self.solarRadiationMaxTime = solarRadiationMaxTime

        self.evapotranspiration = evapotranspiration

        self.windchill = windchill
        self.windchillMin = windchillMin
        self.windchillMinTime = windchillMinTime
        self.windchillMax = windchillMax
        self.windchillMaxTime = windchillMaxTime

        self.windSpeed = windSpeed
        self.windDirection = windDirection
        self.windDominatingDirection = windDominatingDirection
        self.windMaxTime = windMaxTime
        self.windMaxGrp = windMaxGrp
        self.windMax = windMax
        self.windMaxDirection = windMaxDirection

        self.gust = gust
        self.gustDirection = gustDirection
        self.gustMaxTime = gustMaxTime
        self.gustMaxGrp = gustMaxGrp
        self.gustMax = gustMax
        self.gustMaxDirection = gustMaxDirection

        self.lastFrost = lastFrost
        self.lastFrostDuration = lastFrostDuration

        self.rainLastHour = rainLastHour
        self.rainDay = rainDay
        self.rainLast = rainLast

        self.sunrise = sunrise
        self.sunZenith = sunZenith
        self.sunset = sunset
        self.cloudiness = cloudiness

        self.moonPhase = moonPhase
        self.moonNextFullGrp = moonNextFullGrp
        self.moonNextFull = moonNextFull

    def __str__(self):
        return 'temperature: {}°\nhumidity: {}%\nwindDirection: {}\nwindSpeed: {}km/h\ngust: {}km/h\nrain: {}mm\ncloudiness: {}%\npressure: {}hPa\nElevation: {}'.format(self.temperature, self.humidity, self.windDirection, self.windSpeed, self.gust, self.rainLastHour, self.cloudiness, self.pressure, self.elevation)
    def __unicode__(self):
        return self.__str__();
    def __repr__(self):
        return self.__str__();
