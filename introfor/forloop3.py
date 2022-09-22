#!/usr/bin/env python3
"""RZFeeser | Alta3 Research
   learning about for logic"""

def main():
    """On this farm there was a..."""

    # this is the data we want to loop across
    # it is a list containing 3 dictionaries
    farms = [{"name": "NE Farm", "agriculture": ["sheep", "cows", "pigs", "chickens", "llamas", "cats"]},
         {"name": "W Farm", "agriculture": ["pigs", "chickens", "llamas"]},
         {"name": "SE Farm", "agriculture": ["chickens", "carrots", "celery"]}]

    # loop through list of farms and farm will be equal to one of the dictionaries in farms
    for farm in farms:
        print("The farm name is" + farm.get("name"))

        for agriculture in farm.get("agriculture"):
            print(farm.get("name") + " has got some: " + agriculture)

if __name__ == "__main__":
    main()
