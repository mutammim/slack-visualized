import csv
from operator import itemgetter

import matplotlib.pyplot as plot
import squarify

# ---------------------------------------------------------------------------- #
#                                   Constants                                  #
# ---------------------------------------------------------------------------- #

# Have any channels you'd like to exclude? Add their names here.
# This is good for botspam channels.

BLOCKED_CHANNELS = []

# Adjust the DPI.
# The text size changing is a notable consequence.

DPI = 75

# Later on, the code takes all the channels, sorts them in descending
# order based on their `value`, and removes anything on or past the limit index.
# For example, a value of 75 would keep the top 75 channels.

CHANNELS_LIMIT = 75

# These are the colours that the treemap uses.
# The defaults are courtesy of Tailwind's colour palette.

COLOURS = [
    (0.97, 0.44, 0.44),
    (0.98, 0.57, 0.24),
    (0.99, 0.87, 0.28),
    (0.64, 0.90, 0.21),
    (0.20, 0.83, 0.60),
    (0.13, 0.83, 0.93),
    (0.23, 0.51, 0.96),
    (0.54, 0.36, 0.96),
    (0.85, 0.27, 0.94),
    (0.88, 0.11, 0.28),
    (0.58, 0.63, 0.72)
]

# Adjust the column of the CSV file used for `value`.
# As of writing this comment, [4] is the "Messages posted" comment

COLUMN_INDEX = 4

# ---------------------------------------------------------------------------- #
#                                Data-gathering                                #
# ---------------------------------------------------------------------------- #

# ------------------------------ Setup variables ----------------------------- #

# Both of these are lists of dictionaries.
# Each dictionary is { name: str, value: int }
# The value is what determines the size on the treemap.

channels = []
filtered_channels = []

# ----------------------------- Process CSV file ----------------------------- #

with open("data/treemap-channels.csv") as file:
    reader = csv.reader(file, delimiter=",")

    for row in reader:
        # This conditional causes the rows of blocked channels,
        # and the header row, to be ignored.

        if row[1] != "Description" and row[0] not in BLOCKED_CHANNELS:
            item = {"name": None, "value": None}

            item["name"] = row[0]
            item["value"] = int(row[COLUMN_INDEX])

            channels.append(item)

# -------------------- Sort and finish filtering channels -------------------- #

# This line takes all the channels, sorts them in descending order based
# on their `value`, and removes anything on or past the index CHANNELS_LIMIT.
# For example, a value of 75 would keep the top 75 channels.

filtered_channels = sorted(channels, key=itemgetter(
    "value"), reverse=True
)[:CHANNELS_LIMIT]

# ---------------------------------------------------------------------------- #
#                                   Plotting                                   #
# ---------------------------------------------------------------------------- #

plot.figure(figsize=(1, 1), dpi=DPI)

squarify.plot(
    label=[item["name"] for item in filtered_channels],
    sizes=[item["value"] for item in filtered_channels],
    color=COLOURS
)

plot.axis("off")
plot.show()
