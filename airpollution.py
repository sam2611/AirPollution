from matplotlib import pyplot
import numpy as np
import pandas as pd
from matplotlib import style

style.use("ggplot")

df = pd.read_csv('air pollution.csv')
SO2 = df["SO2"].tolist()
NO2 = df["NO2"].tolist()
CO = df["CO"].tolist()
PM2_5 = df["PM2.5"].tolist()
PM10 = df["PM10"].tolist()
Cities = df["Cities"].tolist()

pyplot.plot([], [], label="SO2", color="g", linewidth=5)
pyplot.plot([], [], label="NO2", color="r", linewidth=5)
pyplot.plot([], [], label="CO", color="y", linewidth=5)
pyplot.plot([], [], label="PM2.5", color="m", linewidth=5)
pyplot.plot([], [], label="PM10", color="b", linewidth=5)

pyplot.stackplot(Cities, SO2, NO2, CO, PM2_5, PM10, colors=["g", "r", "y", "m", "b"])

pyplot.title("AIR QUALITY IN INDIA")
pyplot.ylabel("AQI")
pyplot.xlabel("Cities")
# pyplot.tick_params(axis='x', which='major', labelsize=3)
pyplot.grid(True, color="c")
pyplot.legend()
pyplot.show()
