"""just prototyping right now"""

from typing import DefaultDict, OrderedDict

from flask import Flask

import pygal

app = Flask(__name__)


test_data = {
    "error_code":0,
    "response":[
        [22.75,0,"cats_room","Tue, 10 Aug 2021 10:00:05 GMT"],
        [24.0772,0,"office","Tue, 10 Aug 2021 10:00:05 GMT"],
        [31.125,0,"server_room","Tue, 10 Aug 2021 10:00:05 GMT"],
        [30.25,0,"server_room","Tue, 10 Aug 2021 09:00:05 GMT"],
        [24.0017,0,"office","Tue, 10 Aug 2021 09:00:05 GMT"],
        [22.5,0,"cats_room","Tue, 10 Aug 2021 09:00:05 GMT"],
        [22.5,0,"cats_room","Tue, 10 Aug 2021 08:00:05 GMT"],
        [23.9828,0,"office","Tue, 10 Aug 2021 08:00:05 GMT"],
        [30.25,0,"server_room","Tue, 10 Aug 2021 08:00:05 GMT"],
        [22.5,0,"cats_room","Tue, 10 Aug 2021 07:00:05 GMT"],
        [24.2283,0,"office","Tue, 10 Aug 2021 07:00:05 GMT"],
        [30.0,0,"server_room","Tue, 10 Aug 2021 07:00:05 GMT"],
        [30.125,0,"server_room","Tue, 10 Aug 2021 06:00:06 GMT"],
        [22.625,0,"cats_room","Tue, 10 Aug 2021 06:00:06 GMT"],
        [24.4928,0,"office","Tue, 10 Aug 2021 06:00:06 GMT"],
        [24.4739,0,"office","Tue, 10 Aug 2021 05:00:05 GMT"],
        [22.75,0,"cats_room","Tue, 10 Aug 2021 05:00:05 GMT"],
        [30.25,0,"server_room","Tue, 10 Aug 2021 05:00:05 GMT"],
        [30.375,0,"server_room","Tue, 10 Aug 2021 04:00:05 GMT"],
        [22.75,0,"cats_room","Tue, 10 Aug 2021 04:00:05 GMT"]
    ]
}

# MOVE TO CONFIG
expected_keys = ['server_room', 'cats_room', 'office']

def validate(data: dict) -> list:
    """Validates the returned DB data

    :param dict data: The output dict from the DB interface

    :returns: list

    """
    error = False
    try:

        if data["error_code"] == 0:
            data = data["response"]
        else:
            error = True
            error_text = f"DB data returned error code: {data['error_code']}"

    except KeyError as err:
        error = True
        error_text = str(err)

    if error:
        raise ValueError(error_text)

    return data


def sort_data(data: list) -> dict:
    """Sorts the DB output into plottable data

    :param dict list: The 'response' data from the DB interface call

    :returns: dict

    """
    return_dict = DefaultDict(OrderedDict)
    for values in data:
        return_dict[values[3]].update({values[2]: values[0]})

    return return_dict


def plot_data(data: dict) -> tuple:
    """Later"""
    x_labels = reversed(data.keys())
    return_dict = DefaultDict(list)
    for values in reversed(data.values()):
        for expected_key in expected_keys:
            update_val = None
            if expected_key in values.keys():
                update_val = values[expected_key]

            return_dict[expected_key].append(update_val)

    return x_labels, return_dict


@app.route("/")
def home():
    """Testing"""
    validated_data = validate(test_data)
    chart_labels, chart_data = plot_data(sort_data(validated_data))
    chart = pygal.Line(interpolate='cubic', style=pygal.style.DarkColorizedStyle)
    chart.x_labels = chart_labels
    chart.add('server room', chart_data['server_room'])
    chart.add('cats', chart_data['cats_room'])
    chart.add('office', chart_data['office'])
    return chart.render_response()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=False)
