# FROM https://github.com/martinohanlon/flightdata/blob/master/flightdata.py
#

from flightdata import FlightData
from time import sleep

myflights = FlightData()
while True:
	#loop through each aircraft found
	for aircraft in myflights.aircraft:

		#read the aircraft data
		print(aircraft.hex)
		print(aircraft.squawk)
		print(aircraft.flight)
		print(aircraft.lat)
		print(aircraft.lon)
		print(aircraft.validposition)
		print(aircraft.altitude)
		print(aircraft.vert_rate)
		print(aircraft.track)
		print(aircraft.validtrack)
		print(aircraft.speed)
		print(aircraft.messages)
		print(aircraft.seen)
		print(aircraft.mlat)

sleep(1)

#refresh the flight data
myflights.refresh()
