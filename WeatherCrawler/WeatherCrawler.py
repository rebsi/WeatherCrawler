#!usr/bin/env python
# -*-coding:utf-8 -*-

from HausruckWatherProvider import HausruckWatherProvider
from ZamgWatherProvider import ZamgWatherProvider
from LoxoneNotifyer import LoxoneNotifyer

data = HausruckWatherProvider().getWatherData()
#data = ZamgWatherProvider().getWatherData()
dataObservers = [LoxoneNotifyer("127.0.0.1", 5005)]

# TODO: station filter

if data.saveToMsSql():
    for dataObserver in dataObservers:
        dataObserver.pushNewData(data)

print(data)

