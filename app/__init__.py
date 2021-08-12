"""Constants and imports"""

import sys
import os

sys.path.append(os.path.abspath(os.path.join(__file__, "../app/")))
sys.path.append(os.path.abspath(os.path.join(__file__, "../app/common/")))

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