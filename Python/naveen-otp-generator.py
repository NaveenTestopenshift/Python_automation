import math
import random
import os

digits = "0123456789"


def otp_gen():
    otp = ""
    for i in range(4):
        otp += digits[math.floor(random.random() * 10)]
    return otp


print("print 6 digit otp", otp_gen())
