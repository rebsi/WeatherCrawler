#!usr/bin/env python
# -*-coding:utf-8 -*-

from HausruckWatherProvider import HausruckWatherProvider
from ZamgWatherProvider import ZamgWatherProvider

data = HausruckWatherProvider().getWatherData()
#data = ZamgWatherProvider().getWatherData()

data.saveToMsSql()

print(data)

