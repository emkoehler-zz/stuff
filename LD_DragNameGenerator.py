#!/usr/bin/env python
import logging
import sys

import ldclient
import pandas as pd
from collections import OrderedDict

#root = logging.getLogger()
#root.setLevel(logging.INFO)
#ch = logging.StreamHandler(sys.stdout)
#ch.setLevel(logging.INFO)
#formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
#ch.setFormatter(formatter)
#root.addHandler(ch)

if __name__ == "__main__":
  ldclient.set_sdk_key("sdk-3ae95d87-da7e-4deb-8f08-1d6d0961abcb")

  user = {
    "key": "rupaul@vh1.com",
    "firstName": "RuPaul",
    "lastName": "Andre Charles",
    "custom": {
      "groups": "beta_testers"
    }
  }

  show_feature1 = ldclient.get().variation("first-name", user, False)
#  show_feature2 = ldclient.get().variation("last-name", user, False)

  if show_feature1:
      # load data frame with first name data
      firstNameData = {'LetterFirstName': { 'A': 'Amethyst', 'B': 'Bold', 'C': 'Curvy', 'D': 'Daring', 'E': 'Electric', 'F': 'Fatal', 'G': 'Grace', 'H': 'Horrendous', 'I': 'Ign', 'J': 'Jolly', 'K': 'Killer', 'L': 'Loud', 'M': 'Magnificent', 'N': 'Nasty', 'O': 'Orange', 'P': 'Plain', 'Q': 'Queen', 'R': 'Righteous', 'S': 'Saucy', 'T': 'Terrifying', 'U': 'Unicorn', 'V': 'Vivacious', 'W': 'Wild', 'X': 'Xanthic', 'Y': 'Yummy', 'Z': 'Zesty'},
                       'LetterLastName': {'Aries': 'Impulse', 'Taurus': 'Bull', 'Gemini': 'Twoface', 'Cancer': 'Moody','Leo': 'Star', 'Virgo': 'Flawless', 'Libra': 'Flake', 'Scorpio': 'Intense','Sagittarius': 'Airborne', 'Capricorn': 'Ambition', 'Aquarius': 'Ice','Pisces': 'Spacey'}
                       }
      df = pd.DataFrame.from_dict(firstNameData)

      # have a line with welcome printed
      print ("Welcome to the Drag Name Generator - in honor of pride month!")
      firstname = input("Please enter the letter of your first name : ")
      while not firstname.isalpha() or len(firstname) != 1:
          print ("You typed something wrong!")
          firstname = input("Please enter the letter of your first name : ")
      # match letter to output name field
      dragFirstName = firstNameData["LetterFirstName"][firstname]
      # print output drag name
      print("Your Drag First Name is: ", dragFirstName)
  else:
    print ("Not showing your feature")

  ldclient.get().close() # close the client before exiting the program - ensures that all events are delivered