#!/usr/bin/env python3.7
# -*- encoding: utf-8 -*-


# Function to format telephone number
def format_telephone_number(telephone):
    if telephone and len(telephone) == 10:  # Assuming telephone is a 10-digit number
        return "{}-{}-{}-{}-{}".format(telephone[:2], telephone[2:4], telephone[4:6], telephone[6:8], telephone[8:])
    else:
        return telephone