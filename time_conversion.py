def timeConversion(s):
    military = s[0:len(s) - 2]

    if s[8:10] == "PM":
        if s[0:2] != "12":
            military = str(int(military[0:2]) + 12) + s[2:len(military)]
    elif s[8:10] == "AM":
        if s[0:2] == "12":
            military = "00" + s[2:len(military)]
    elif s[8:10] != "PM" or s[8:10] != "AM":
        return None

    return military


print(timeConversion("12:00:00PM"))
