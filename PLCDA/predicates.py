from classes import Predicate
import random

set_predicates = set()

# room
room = Predicate(1, 'Room', 1)
# light
light = Predicate(2, 'Light', 1)
# isInRoom
isInRoom = Predicate(3, 'isInRoom', 2)
# notOccupied
not_occupied = Predicate(4, 'NotOccupied', 1)
# appliance
appliance = Predicate(5, 'Appliance', 1)
# space
space = Predicate(6, 'Space', 1)
# isInSpace
isInSpace = Predicate(7, 'isInSpace', 2)  # can be converted into a function
# lightHasStatusOFF
lightHasStatusOFF = Predicate(8, 'lightHasStatusOFF', 1)
# lightHasStatusOFF
lightHasStatusON = Predicate(9, 'lightHasStatusON', 1)
# occupied
occupied = Predicate(4, 'Occupied', 2)

applianceCategoryHeating = Predicate(10, 'applianceCategoryHeating', 1)
# Low space humidity
lowHumidity = Predicate(11, 'lowHumidity', 1)
# High space humidity
highHumidity = Predicate(12, 'highHumidity', 1)
# appliance status
coolerHasStatusON = Predicate(13, 'coolerHasStatusON', 1)
# assetCategory Vent
applianceCategoryCooling = Predicate(24, 'applianceCategoryCooling', 1)
# appliance status
applianceHasStatusOFF = Predicate(22, 'applianceHasStatusOFF', 1)

# Space Occupied
spaceNotOccupied = Predicate(25, 'spaceNotOccupied', 1)

# alert
alert = Predicate(26, 'alert', 1)

# mainDoor
mainDoor = Predicate(27, 'mainDoor', 1)

# lock
lock = Predicate(28, 'lock', 1)

# authorized Access
authorizeAccess = Predicate(29, 'authorizeAccess', 1)

# code of
codeof = Predicate(30, 'codeof', 2)

# unlock
unlock = Predicate(31, 'unlock', 1)

# invalid attempts
invalidAttempts3 = Predicate(32, 'invalidAttempts3', 1)

# ison
isOn = Predicate(33, 'isOn', 2)

# forced open
forcedAttempt = Predicate(34, 'forcedAttempt', 1)

spaceTemp = Predicate(36, 'spaceTemp', 2)

spaceTempAbove25 = Predicate(37, 'spaceTempAbove25', 1)

spaceTempBelow15 = Predicate(38, 'spaceTempBelow15', 1)

heater = Predicate(39, 'heater', 1)

cooler = Predicate(40, 'cooler', 1)

spaceTempAbove24 = Predicate(41, 'spaceTempAbove24', 1)

spaceTempBelow25 = Predicate(42, 'spaceTempBelow25', 1)

coolerHasStatusOFF = Predicate(43, 'coolerHasStatusOFF', 1)

heaterHasStatusON = Predicate(44, 'heaterHasStatusON', 1)

heaterHasStatusOFF = Predicate(44, 'heaterHasStatusOFF', 1)

applianceHasStatusON = Predicate(45, 'applianceHasStatusON', 1)

temperatureSensor = Predicate(46, 'temperatureSensor', 1)

smokeDetector = Predicate(47, 'smokeDetector', 1)

zone = Predicate(48, 'zone', 1)

isInZone = Predicate(49, 'isInZone', 2)

alarm = Predicate(50, 'alarm', 1)

alarmHasStatusOFF = Predicate(51, 'alarmHasStatusOFF', 1)

alarmHasStatusON = Predicate(52, 'alarmHasStatusON', 1)

DetectorHasStatusOFF = Predicate(53, 'DetectorHasStatusOFF', 1)

DetectorHasStatusON = Predicate(54, 'DetectorHasStatusON', 1)

smartDevice = Predicate(55, 'smartDevice', 1)

accessList = Predicate(56, 'accessList', 1)

accessListFor = Predicate(57, 'accessListFor', 2)

person = Predicate(58, 'person', 1)

authValue = Predicate(59, 'authValue', 1)

apply = Predicate(60, 'apply', 3)

authorized = Predicate(61, 'authorized', 1)



set_predicates = set()
set_predicates.add(room)
set_predicates.add(light)
set_predicates.add(isInRoom)
set_predicates.add(occupied)
set_predicates.add(not_occupied)
set_predicates.add(appliance)
set_predicates.add(space)
set_predicates.add(isInSpace)
set_predicates.add(lightHasStatusOFF)
set_predicates.add(lightHasStatusON)
set_predicates.add(applianceCategoryHeating)
set_predicates.add(applianceCategoryCooling)
set_predicates.add(coolerHasStatusON)
set_predicates.add(applianceHasStatusOFF)
set_predicates.add(highHumidity)
set_predicates.add(lowHumidity)
set_predicates.add(spaceNotOccupied)
set_predicates.add(alert)
set_predicates.add(mainDoor)
set_predicates.add(lock)
set_predicates.add(isOn)
set_predicates.add(authorizeAccess)
set_predicates.add(unlock)
set_predicates.add(codeof)
set_predicates.add(invalidAttempts3)
set_predicates.add(forcedAttempt)
set_predicates.add(cooler)
set_predicates.add(heater)
set_predicates.add(spaceTempAbove24)
set_predicates.add(spaceTempBelow25)
set_predicates.add(spaceTempBelow15)
set_predicates.add(spaceTempAbove25)
set_predicates.add(heaterHasStatusOFF)
set_predicates.add(heaterHasStatusON)
set_predicates.add(coolerHasStatusOFF)
set_predicates.add(applianceHasStatusON)
set_predicates.add(temperatureSensor)


predicates_names = []
for i in set_predicates:
    n = i.getPredicateName()
    predicates_names.append(n)