class WGS84Coord:   #Klassendefinition
    def __init__(self, longitude=0, latitude=0):    #Konstruktor, Standardwert ist 0
        self._setLongitude(longitude)
        self._setLatitude(latitude)

    # Korrektion der Wertebereich (Länge) + Warnung
    def _setLongitude(self, longitude):
        self._longitude = longitude
        while self._longitude < -180:
            self._longitude = 180 + (self._longitude + 180)
            print("Werte nicht im Korrekten Längebereich! Neue Werte:" + str(self._longitude))
        while self._longitude > 180:
            self._longitude = -180 + (self._longitude - 180)
            print("Werte nicht im Korrekten Längebereich! Neue Werte:" + str(self._longitude))

    # Korrektion der Wertebereich (Breite) + Warnung
    def _setLatitude(self, latitude):
        self._latitude = latitude
        while self._latitude < -90:
            self._latitude = -90 - (self._latitude + 90)
            print("Werte nicht im Korrekten Breitebereich! Neue Werte:" + str(self._latitude))
        while self._latitude > 90:
            self._latitude = + 90 - (self._latitude - 90)
            print("Werte nicht im Korrekten Breitebereich! Neue Werte:" + str(self._latitude))

    def _getLongitude(self):
        return self._longitude
    def _getLatitude(self):
        return self._latitude
    def __str__(self):
        return "Richtiger Punkt (" + str(self._longitude) + " " + str(self._latitude) + ")"

    latitude = property(_getLatitude, _setLatitude)
    longitude = property(_getLongitude, _setLongitude)

Koord = WGS84Coord(-200, 115)
print(Koord)
