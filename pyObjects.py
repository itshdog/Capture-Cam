import pyDBaccess

class license: 
    def __init__(self, plateNumber, date, time, latitude, longitude):
        self._LicensePlateNum = plateNumber
        self._Date = date
        self._Time = time
        self._Latitude = latitude
        self._Longitude = longitude

    @property
    def LicensePlateNum(self):
        return self._LicensePlateNum

    @property
    def Date(self):
        return self._Date

    @property
    def Time(self):
        return self._Time

    @property
    def Latitude(self):
        return self._Latitude

    @property
    def Longitude(self):
        return self._Longitude

def returnOBJ(dbConn, lnum):
    sqlQ = """Select plateNum, date, time, latitude, longitude
    from AmberAlertPlates
    where plateNum = (?)"""
    try:
        s = pyDBaccess.selectOneRow(dbConn, sqlQ, [lnum])
        newObject = license(s[0], s[1], s[2], s[3], s[4])
    except:
        return []

    return newObject


def search4Plate(dbConn, lnum):
    sqlQ = """Select plateNum, date, time, latitude, longitude from AmberAlertPlates where plateNum = (?)"""
    try:
        s = pyDBaccess.selectOneRow(dbConn, sqlQ, [lnum])
        newObject = license(s[0], s[1], s[2], s[3], s[4])
    except Exception:
        return 0
    # if newObject == 0:
        # return 0;
    # else:
    return newObject



def importPlate(dbConn, plate, date, time, lat, longe):
    sqlQ = """Insert into AmberAlertPlates(plateNum, date, time, latitude, longitude)
                  values((?), (?), (?), (?), (?));"""

    #Tests for if plate is in the database if not returns 0
    check4plate = """select plateNum
        from AmberAlertPlates
        where plateNum = (?);"""

    s = pyDBaccess.selectOneRow(dbConn, check4plate, [plate])
    if s:
        return 0 

    try:
        pyDBaccess.performAction(dbConn, sqlQ, [plate, date, time, lat, longe])
    except Exception as err:
        print(err)
        return 0

    return 1

def UpdatePlate(dbConn, plate, date, time, lat, longe):
    sqlQ = """UPDATE AmberAlertPlates SET date = (?), time = (?), latitude = (?), longitude = (?)
 WHERE plateNum = (?);"""

    try:
        pyDBaccess.performAction(dbConn, sqlQ, [date, time, lat, longe, plate])
        newObject = license(plate, date, time, lat, longe)
    except Exception as err:
        print(err)
        return 0
    return newObject