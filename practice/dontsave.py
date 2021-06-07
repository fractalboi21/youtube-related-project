import re
string = "2H14M55S"

#2H14M55S  -> 8095 
def hours2seconds(hms):
    h = 0
    m = 0
    s = 0
    pattern = "[HMS]"
    hms = re.split(pattern,hms)
    hms.remove("")
    s = int(hms[-1])
    m = int(hms[-2])
    h = int(hms[-3])
    seconds = int(h*3600 + m*60 + s*1)
    return seconds