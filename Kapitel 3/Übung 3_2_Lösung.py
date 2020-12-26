class WGS84Coord:
    def __init__(self, lng=0, lat=0):
        self.setlongitude(lng)
        self.setlatitude(lat)

    def __str__(self):
        return f"[{self._longitude},{self._latitude}]"

    def setlongitude(self, lng):
        if lng > 180 or lng < 180:
            print("Wertebereich falsch, Länge sollte von -180 bis 180 sein")

        rest = lng % 360
        if rest <= 180:
            self._longitude = rest
        elif rest > 180:
            self._longitude = -360+rest

    def setlatitude(self, lat):
        if lat > 90 or lat < -90:
            print("Wertebereich falsch, Breite sollte von -90 bis 90 sein")

        rest = lat % 360
        if rest >= 0 and rest <= 90:
            self._latitude = rest
        elif rest > 90 and rest <= 270:
            self._latitude = 180-rest
        elif rest > 270:
            self._latitude = rest-360

    def ausgabe(self):
        print(self._longitude, self._latitude)

c = WGS84Coord(-200,115)
print(c)
