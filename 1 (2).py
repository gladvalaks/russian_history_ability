import json
import sys
import pprint


def get_text(num):
    with open("data_file.json", "r") as write_file:
        txt = json.load(write_file)
        if num >= 0 and num <= 494:
            return txt['history'][str(num)]
        else:
            if num < 0:
                return txt['history']['0']
            else:
                return txt['history']['494']

print(get_text(-1))
print(get_text(345))
print(get_text(600))

