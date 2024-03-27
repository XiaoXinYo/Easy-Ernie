import time

def getTimestamp(ms: bool=False) -> int:
    return int(time.time() * (1000 if ms else 1))

def timeToTimestamp(text):
    strptime = time.strptime(text, '%Y-%m-%d %H:%M:%S')
    return int(time.mktime(strptime))