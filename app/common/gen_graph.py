"""Fetches the sensor data from DB api and draws the chart"""

from typing import DefaultDict, OrderedDict

import pygal

from common import SENSOR_NAMES

from db import DBInterface


class Graph:
    """Generates the chart"""

    def __init__(self, records: int = 76) -> None:
        """init for Chart"""
        self.records = records

    def _get(self) -> list:
        """Gets and validates the returned DB data

        :param dict data: The output dict from the DB interface

        :returns: list

        """
        error, data = DBInterface().request(path=DBInterface.call, args={"proc": "get_temp", "args": [self.records]})
        if error:
            raise ValueError(f"Error receiving data from DB. Response: {data}")

        return data["response"]

    def _sort(self) -> tuple:
        """Sorts the raw data from the DB

        :returns tuple: x axis labels, data to plot
        """
        raw_data = self._get()
        sorted_dict = DefaultDict(OrderedDict)
        for values in raw_data:
            sorted_dict[values[3]].update({values[2]: values[0]})

        x_labels = reversed(sorted_dict.keys())
        plot_data = DefaultDict(list)
        for values in reversed(sorted_dict.values()):
            for expected_key in SENSOR_NAMES:
                update_val = None
                if expected_key in values.keys():
                    update_val = values[expected_key]

                plot_data[expected_key].append(update_val)

        return x_labels, plot_data

    @property
    def plot_data(self) -> dict:
        """This will return the sorted DB data so it can be plotted"""
        labels, data = self._sort()
        return {"labels": labels, "data": data}

    def generate(self):
        """Generates the pygal line graph"""
        chart = pygal.Line(interpolate='cubic', style=pygal.style.DarkColorizedStyle)
        chart.x_labels = self.plot_data["labels"]
        for sensor in SENSOR_NAMES:
            chart.add(sensor, self.plot_data["data"][sensor])

        return chart.render_response()
