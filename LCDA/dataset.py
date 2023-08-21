from LCDA.predicate import *
from LCDA.rule import *
from LCDA.facts import *


##### Predicates #############
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
isInSpace = Predicate(7, 'isInSpace', 2)    # can be converted into a function
#lightHasStatusOFF
lightHasStatusOFF = Predicate(8, 'lightHasStatusOFF', 1)
#lightHasStatusOFF
lightHasStatusON = Predicate(9,'lightHasStatusON', 1)
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

#lock
lock = Predicate(28, 'lock', 1)

#authorized Access
authorizeAccess = Predicate(29, 'authorizeAccess', 1)

#code of
codeof = Predicate(30, 'codeof', 2)

#unlock
unlock = Predicate(31, 'unlock', 1)

#invalid attempts
invalidAttempts3 = Predicate(32, 'invalidAttempts3', 1)

#ison
isOn = Predicate(33, 'isOn', 2)

#forced open
forcedAttempt = Predicate(34, 'forcedAttempt', 1)

spaceTemp = Predicate(36, 'spaceTemp', 2)

spaceTempAbove30 = Predicate(37, 'spaceTempAbove30', 1)

spaceTempBelow18 = Predicate(38, 'spaceTempBelow18', 1)

heater = Predicate(39, 'heater', 1)

cooler = Predicate(40, 'cooler', 1)

spaceTempAbove24 = Predicate(41, 'spaceTempAbove24', 1)

spaceTempBelow25 = Predicate(42, 'spaceTempBelow25', 1)

coolerHasStatusOFF = Predicate(43, 'coolerHasStatusOFF', 1)

heaterHasStatusON = Predicate(44, 'heaterHasStatusON', 1)

heaterHasStatusOFF = Predicate(44, 'heaterHasStatusOFF', 1)




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
set_predicates.add(spaceTempBelow18)
set_predicates.add(spaceTempAbove30)
set_predicates.add(heaterHasStatusOFF)
set_predicates.add(heaterHasStatusON)
set_predicates.add(coolerHasStatusOFF)



######## Facts ##########
factHeater = Fact(1)
factSpace = Fact(2)
factmainDoor = Fact(3)
factInvalidAttempt = Fact(4)
factLock = Fact(5)
factIsOn = Fact(6)
factRoom = Fact(7)
factLight = Fact(8)
factisInRoom = Fact(9)


## room(bedroom)
factRoom.addFactConstant('bedroom')
factRoom.addFacts(room.getPredicateName(), 'bedroom')
factRoom.addFactTerms(room.getPredicateName())

### light(a)

factLight.addFactConstant('light1')
factLight.addFacts(light.getPredicateName(), 'light1')
factLight.addFactTerms(light.getPredicateName())


## space
factSpace.addFactConstant('livingroom')
factSpace.addFacts(space.getPredicateName(), 'livingroom')
factSpace.addFactTerms(space.getPredicateName())

factIsOn.addFactConstant(('Entrance', 'l1'))
factIsOn.addFacts(isOn.getPredicateName(), ('Entrance', 'l1'))
factIsOn.addFactTerms(isOn.getPredicateName())


### isInRoom(a, bedroom)
factisInRoom.addFactConstant(('light1', 'bedroom'))
factisInRoom.addFacts(isInRoom.getPredicateName(), ('light1', 'bedroom'))
factisInRoom.addFactTerms(isInRoom.getPredicateName())


#### Heater(H1)

factHeater.addFactConstant('H1')
factHeater.addFacts(appliance.getPredicateName(), 'H1')
factHeater.addFactTerms(appliance.getPredicateName())



factmainDoor.addFactConstant('Entrance')
factmainDoor.addFacts(mainDoor.getPredicateName(), 'Entrance')
factmainDoor.addFactTerms(mainDoor.getPredicateName())

factInvalidAttempt.addFactConstant('l1')
factInvalidAttempt.addFacts(invalidAttempts3.getPredicateName(), 'l1')
factInvalidAttempt.addFactTerms(invalidAttempts3.getPredicateName())


factLock.addFactConstant('l1')
factLock.addFacts(lock.getPredicateName(), 'l1')
factLock.addFactTerms(lock.getPredicateName())

set_facts = set()

set_facts.add(factRoom)
set_facts.add(factLight)
set_facts.add(factisInRoom)
set_facts.add(factHeater)
set_facts.add(factSpace)
set_facts.add(factIsOn)
set_facts.add(factmainDoor)
set_facts.add(factInvalidAttempt)
set_facts.add(factLock)



#### Rules ################
rule1 = Rule(1)
rule2 = Rule(2)
rule3 = Rule(3)
rule4 = Rule(4)
rule5 = Rule(5)
rule6 = Rule(6)
rule7 = Rule(7)
rule8 = Rule(8)
rule9 = Rule(9)
rule10 = Rule(10)
rule11 = Rule(11)
rule12 = Rule(12)
rule13 = Rule(13)


#   appliance(x) --> space(y), isInSpace(x, y)
rule1.addRuleBodyPredicates(appliance.getPredicateName())
rule1.addRuleExistentialVariable(appliance.getPredicateName(), 'x')
rule1.addRuleConclusion(space.getPredicateName())
rule1.addRuleConclusionVariables(space.getPredicateName(), 'y')
rule1.addRuleConclusion(isInSpace.getPredicateName())
rule1.addRuleConclusionVariables(isInSpace.getPredicateName(), ('x', 'y'))

# ### room(x) --> light(y), isInRoom(y, x)

rule2.addRuleBodyPredicates(room.getPredicateName())
rule2.addRuleExistentialVariable(room.getPredicateName(), 'x')
rule2.addRuleConclusion(light.getPredicateName())
rule2.addRuleConclusionVariables(light.getPredicateName(), 'y')
rule2.addRuleConclusion(isInRoom.getPredicateName())
rule2.addRuleConclusionVariables(isInRoom.getPredicateName(), ('x','y'))


# mainDoor(x) --> lock(y), isonDoor(x,y)
rule3.addRuleBodyPredicates(mainDoor.getPredicateName())
rule3.addRuleExistentialVariable(mainDoor.getPredicateName(), 'x')
rule3.addRuleConclusion(lock.getPredicateName())
rule3.addRuleConclusionVariables(lock.getPredicateName(), 'y')
rule3.addRuleConclusion(isOn.getPredicateName())
rule3.addRuleConclusionVariables(isOn.getPredicateName(), ('x', 'y'))


# ###### light(x), room(y), isInRoom(x, y), not_occupied(y) --> lightStatusOFF(x)

rule4.addRuleBodyPredicates(light.getPredicateName())
rule4.addRuleExistentialVariable(light.getPredicateName(), 'x')
rule4.addRuleBodyPredicates(room.getPredicateName())
rule4.addRuleExistentialVariable(room.getPredicateName(), 'y')
rule4.addRuleBodyPredicates(isInRoom.getPredicateName())
rule4.addRuleExistentialVariable(isInRoom.getPredicateName(), ('x', 'y'))
rule4.addRuleBodyPredicates(not_occupied.getPredicateName())
rule4.addRuleExistentialVariable(not_occupied.getPredicateName(), 'y')
rule4.addRuleConclusion(lightHasStatusOFF.getPredicateName())
rule4.addRuleConclusionVariables(lightHasStatusOFF.getPredicateName(), 'x')



# lock(x), invalidattempts(x, 3) --> forcedAttempt(x)
rule5.addRuleBodyPredicates(lock.getPredicateName())
rule5.addRuleExistentialVariable(lock.getPredicateName(), 'x')
rule5.addRuleBodyPredicates(invalidAttempts3.getPredicateName())
rule5.addRuleExistentialVariable(invalidAttempts3.getPredicateName(), ('y'))
rule5.addRuleConclusion(forcedAttempt.getPredicateName())
rule5.addRuleConclusionVariables(forcedAttempt.getPredicateName(), 'x')


# rule 6: cooler(x)∧space(y)∧isInSpace(x, y)∧spaceTemperature(y,t), spaceTemperatureAbove (y, 30) → coolerHasStatus(x, ON )
rule6.addRuleBodyPredicates(cooler.getPredicateName())
rule6.addRuleExistentialVariable(cooler.getPredicateName(), 'x')
rule6.addRuleBodyPredicates(space.getPredicateName())
rule6.addRuleExistentialVariable(space.getPredicateName(), 'y')
rule6.addRuleBodyPredicates(isInSpace.getPredicateName())
rule6.addRuleExistentialVariable(isInSpace.getPredicateName(), ('x', 'y'))
rule6.addRuleBodyPredicates(spaceTemp.getPredicateName())
rule6.addRuleExistentialVariable(spaceTemp.getPredicateName(), ('y', 't'))
rule6.addRuleBodyPredicates(spaceTempAbove30.getPredicateName())
rule6.addRuleExistentialVariable(spaceTempAbove30.getPredicateName(), 't')
      # coppliancesion
rule6.addRuleConclusion(coolerHasStatusON.getPredicateName())
rule6.addRuleConclusionVariables(coolerHasStatusON.getPredicateName(), 'x')


# rule 7: cooler(x)∧space(y)∧isInSpace(x, y)∧spaceTemperature(y,t), spaceTemperatureBelow (y, 25) → coolerHasStatus(x, OFF )
rule7.addRuleBodyPredicates(cooler.getPredicateName())
rule7.addRuleExistentialVariable(cooler.getPredicateName(), 'x')
rule7.addRuleBodyPredicates(space.getPredicateName())
rule7.addRuleExistentialVariable(space.getPredicateName(), 'y')
rule7.addRuleBodyPredicates(isInSpace.getPredicateName())
rule7.addRuleExistentialVariable(isInSpace.getPredicateName(), ('x', 'y'))
rule7.addRuleBodyPredicates(spaceTemp.getPredicateName())
rule7.addRuleExistentialVariable(spaceTemp.getPredicateName(), ('y', 't'))
rule7.addRuleBodyPredicates(spaceTempBelow25.getPredicateName())
rule7.addRuleExistentialVariable(spaceTempBelow25.getPredicateName(), 't')
      # coppliancesion
rule7.addRuleConclusion(coolerHasStatusOFF.getPredicateName())
rule7.addRuleConclusionVariables(coolerHasStatusOFF.getPredicateName(), 'x')


# rule 8: heater(x)∧space(y)∧isInSpace(x, y)∧spaceTemperature(y,t), spaceTemperatureAbove (y, 24) → heaterHasStatus(x, OFF )
rule8.addRuleBodyPredicates(heater.getPredicateName())
rule8.addRuleExistentialVariable(heater.getPredicateName(), 'x')
rule8.addRuleBodyPredicates(space.getPredicateName())
rule8.addRuleExistentialVariable(space.getPredicateName(), 'y')
rule8.addRuleBodyPredicates(isInSpace.getPredicateName())
rule8.addRuleExistentialVariable(isInSpace.getPredicateName(), ('x', 'y'))
rule8.addRuleBodyPredicates(spaceTemp.getPredicateName())
rule8.addRuleExistentialVariable(spaceTemp.getPredicateName(), ('y', 't'))
rule8.addRuleBodyPredicates(spaceTempAbove24.getPredicateName())
rule8.addRuleExistentialVariable(spaceTempAbove24.getPredicateName(), 't')
      # conclusion
rule8.addRuleConclusion(heaterHasStatusOFF.getPredicateName())
rule8.addRuleConclusionVariables(heaterHasStatusOFF.getPredicateName(), 'x')

# rule 9: heater(x)∧space(y)∧isInSpace(x, y)∧spaceTemperature(y,t), spaceTemperaturebelow (y, 18) → heaterHasStatus(x, ON )
rule9.addRuleBodyPredicates(heater.getPredicateName())
rule9.addRuleExistentialVariable(heater.getPredicateName(), 'x')
rule9.addRuleBodyPredicates(space.getPredicateName())
rule9.addRuleExistentialVariable(space.getPredicateName(), 'y')
rule9.addRuleBodyPredicates(isInSpace.getPredicateName())
rule9.addRuleExistentialVariable(isInSpace.getPredicateName(), ('x', 'y'))
rule9.addRuleBodyPredicates(spaceTemp.getPredicateName())
rule9.addRuleExistentialVariable(spaceTemp.getPredicateName(), ('y', 't'))
rule9.addRuleBodyPredicates(spaceTempBelow18.getPredicateName())
rule9.addRuleExistentialVariable(spaceTempBelow18.getPredicateName(), 't')
      # conclusion
rule9.addRuleConclusion(heaterHasStatusON.getPredicateName())
rule9.addRuleConclusionVariables(heaterHasStatusON.getPredicateName(), 'x')


# mainDoor(x), lock(y),ison(x,y), forcedAttempt(y) --> !
rule10.addRuleBodyPredicates(mainDoor.getPredicateName())
rule10.addRuleExistentialVariable(mainDoor.getPredicateName(), 'x')
rule10.addRuleBodyPredicates(lock.getPredicateName())
rule10.addRuleExistentialVariable(lock.getPredicateName(), 'y')
rule10.addRuleBodyPredicates(isOn.getPredicateName())
rule10.addRuleExistentialVariable(isOn.getPredicateName(), ('x', 'y'))
rule10.addRuleBodyPredicates(forcedAttempt.getPredicateName())
rule10.addRuleExistentialVariable(forcedAttempt.getPredicateName(), 'y')

rule10.addRuleConclusion(alert.getPredicateName())
rule10.addRuleConclusionVariables(alert.getPredicateName(), 'x')



# rule 11: heater(x)∧space(y)∧isInSpace(x, y)∧spaceTemperature(y,27),heaterHasStatus(x, ON ) --> !
rule11.addRuleBodyPredicates(heater.getPredicateName())
rule11.addRuleExistentialVariable(heater.getPredicateName(), 'x')
rule11.addRuleBodyPredicates(space.getPredicateName())
rule11.addRuleExistentialVariable(space.getPredicateName(), 'y')
rule11.addRuleBodyPredicates(isInSpace.getPredicateName())
rule11.addRuleExistentialVariable(isInSpace.getPredicateName(), ('x', 'y'))
rule11.addRuleBodyPredicates(spaceTemp.getPredicateName())
rule11.addRuleExistentialVariable(spaceTemp.getPredicateName(), ('y', '27'))
rule11.addRuleBodyPredicates(heaterHasStatusON.getPredicateName())
rule11.addRuleExistentialVariable(heaterHasStatusON.getPredicateName(), 'x')
rule11.addRuleConclusion(alert.getPredicateName())
rule11.addRuleConclusionVariables(alert.getPredicateName(), 'x')


# # rule 12: light(x), room(y), isInRoom(x, y), not_occupied(y), lightStatusON(x) --> !
rule12.addRuleBodyPredicates(light.getPredicateName())
rule12.addRuleExistentialVariable(light.getPredicateName(), 'x')
rule12.addRuleBodyPredicates(room.getPredicateName())
rule12.addRuleExistentialVariable(room.getPredicateName(), 'y')
rule12.addRuleBodyPredicates(isInRoom.getPredicateName())
rule12.addRuleExistentialVariable(isInRoom.getPredicateName(), ('x', 'y'))
rule12.addRuleBodyPredicates(not_occupied.getPredicateName())
rule12.addRuleExistentialVariable(not_occupied.getPredicateName(), 'y')
rule12.addRuleBodyPredicates(lightHasStatusON.getPredicateName())
rule12.addRuleExistentialVariable(lightHasStatusON.getPredicateName(), 'x' )
# conclusion empty because of negative rule
rule12.addRuleConclusion(alert.getPredicateName())
rule12.addRuleConclusionVariables(alert.getPredicateName(), 'x')




set_rules = set()

set_rules.add(rule1)
set_rules.add(rule2)
set_rules.add(rule3)
set_rules.add(rule4)
set_rules.add(rule5)
set_rules.add(rule6)
set_rules.add(rule7)
set_rules.add(rule8)
set_rules.add(rule9)
set_rules.add(rule10)
set_rules.add(rule11)
set_rules.add(rule12)
