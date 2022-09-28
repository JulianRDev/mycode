#!/usr/bin/env python3
"""Returning the location of the ISS in latitude/longitude"""
import requests
import datetime
import reverse_geocoder as rgeo

NASA_URL= "http://api.open-notify.org/iss-now.json"
def main():

    ## Send HTTPS GET to the API
    resp= requests.get(NASA_URL).json()

    ## print response
    print(resp)

    # current location of ISS
    print("Current Location of the ISS: ")
    time_stamp = datetime.datetime.fromtimestamp(resp['timestamp']) 
    print(f"TimeStamp: {time_stamp}")
    # grabbing the current long and lat from response
    print(f"Longitude: {resp['iss_position']['longitude']}")
    print(f"Latitude: {resp['iss_position']['latitude']}")
    #using long and lat to get city and country 
    lat = resp['iss_position']['latitude']
    lon = resp['iss_position']['longitude']
    # reverse_geocoder MUST be passed a tuple as the argument!
    coords_tuple= (lat, lon)
    
    coordinates = rgeo.search(coords_tuple)

    print(f"City: {coordinates[0]['name']}")
if __name__ == "__main__":
    main()
