#!/usr/bin/env python
import logging
import sys

import ldclient
import pandas as pd
from collections import OrderedDict
import uuid

#root = logging.getLogger()
#root.setLevel(logging.INFO)
#ch = logging.StreamHandler(sys.stdout)
#ch.setLevel(logging.INFO)
#formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
#ch.setFormatter(formatter)
#root.addHandler(ch)

if __name__ == "__main__":
  ldclient.set_sdk_key("sdk-2d3f57a1-ea83-49e8-938e-f1f352898abc")

  # load dictionaries with name/sign data
  firstNameMap = { 'a': 'Amethyst', 'b': 'Bold', 'c': 'Curvy', 'd': 'Daring', 'e': 'Electric', 'f': 'Fatal', 'g': 'Grace', 'h': 'Horrendous', 'i': 'Ign', 'j': 'Jolly', 'k': 'Killer', 'l': 'Loud', 'm': 'Magnificent', 'n': 'Nasty', 'o': 'Orange', 'p': 'Plain', 'q': 'Queen', 'r': 'Righteous', 's': 'Saucy', 't': 'Terrifying', 'u': 'Unicorn', 'v': 'Vivacious', 'w': 'Wild', 'x': 'Xanthic', 'y': 'Yummy', 'z': 'Zesty'}
  lastNameMap = {'aries': 'Impulse', 'taurus': 'Bull', 'gemini': 'Twoface', 'cancer': 'Moody','leo': 'Star', 'virgo': 'Flawless', 'libra': 'Flake', 'scorpio': 'Intense','sagittarius': 'Airborne', 'capricorn': 'ambition', 'aquarius': 'Ice','pisces': 'Spacey'}

  # start generator
  playagain = "yes"
  while playagain.lower() == "yes":
    print ("Welcome to the Drag Name Generator!")
    # get user info
    firstname = input("Please enter your first name: ")
    while not firstname.isalpha():
        print ("You typed something wrong!")
        firstname = input("Please enter your first name: ")
    firstnameletter = firstname[:1]
    dragFirstName = firstNameMap[firstnameletter.lower()]
    
    sign = input("Please enter your astrological sign: ")
    while sign.lower() not in lastNameMap:
        print ("You typed something wrong!")
        sign = input("Please enter your astrological sign: ")
    dragLastName = lastNameMap[sign.lower()]

    # set user info
    user = {
      "key": uuid.uuid4(),
      "firstName": firstname,
      "custom": {
        "astroSign": sign
      }
    }

    # evaluate feature flag
    disable_lastname = ldclient.get().variation("dg-first-name-only", user, False)

    if disable_lastname:
      print("Your Drag First Name is: ", dragFirstName)
    else:
      print("Your Drag Name is: ", dragFirstName," ", dragLastName)

    # check if they want to play again
    playagain = input("Would you like to generate another drag name? Enter ""Yes"" or ""No"": ")
    while playagain.lower() != "yes" and playagain.lower() != "no":
        print ("You typed something wrong!")
        playagain = input("Would you like to generate another drag name? Enter ""Yes"" or ""No"": ")

  ldclient.get().close() # close the client before exiting the program - ensures that all events are delivered
