from classes import Rule
from predicates import *

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
rule14 = Rule(14)
rule15 = Rule(15)
rule16 = Rule(16)
rule17 = Rule(17)
rule18 = Rule(18)
rule19 = Rule(19)
rule20 = Rule(20)
rule21 = Rule(21)
rule22 = Rule(22)
rule23 = Rule(23)
rule24 = Rule(24)
rule25 = Rule(25)
rule26 = Rule(26)

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
rule2.addRuleConclusionVariables(isInRoom.getPredicateName(), ('x', 'y'))

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

# lock(x), invalid-attempts(x, 3) --> forcedAttempt(x)
rule5.addRuleBodyPredicates(lock.getPredicateName())
rule5.addRuleExistentialVariable(lock.getPredicateName(), 'x')
rule5.addRuleBodyPredicates(invalidAttempts3.getPredicateName())
rule5.addRuleExistentialVariable(invalidAttempts3.getPredicateName(), ('y'))
rule5.addRuleConclusion(forcedAttempt.getPredicateName())
rule5.addRuleConclusionVariables(forcedAttempt.getPredicateName(), 'x')

# rule 6: cooler(x)∧space(y)∧isInSpace(x, y)∧spaceTemperature(y,t), spaceTemperatureAbove (y, 25) → coolerHasStatus(
# x, ON )
rule6.addRuleBodyPredicates(cooler.getPredicateName())
rule6.addRuleExistentialVariable(cooler.getPredicateName(), 'x')
rule6.addRuleBodyPredicates(space.getPredicateName())
rule6.addRuleExistentialVariable(space.getPredicateName(), 'y')
rule6.addRuleBodyPredicates(isInSpace.getPredicateName())
rule6.addRuleExistentialVariable(isInSpace.getPredicateName(), ('x', 'y'))
rule6.addRuleBodyPredicates(spaceTemp.getPredicateName())
rule6.addRuleExistentialVariable(spaceTemp.getPredicateName(), ('y', 't'))
rule6.addRuleBodyPredicates(spaceTempAbove25.getPredicateName())
rule6.addRuleExistentialVariable(spaceTempAbove25.getPredicateName(), 't')
# coppliancesion
rule6.addRuleConclusion(coolerHasStatusON.getPredicateName())
rule6.addRuleConclusionVariables(coolerHasStatusON.getPredicateName(), 'x')

# rule 7: cooler(x)∧space(y)∧isInSpace(x, y)∧spaceTemperature(y,t), spaceTemperatureBelow (y, 25) → coolerHasStatus(
# x, OFF )
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

# rule 9: heater(x)∧space(y)∧isInSpace(x, y)∧spaceTemperature(y,t), spaceTemperaturebelow (y, 15) → heaterHasStatus(
# x, ON )
rule9.addRuleBodyPredicates(heater.getPredicateName())
rule9.addRuleExistentialVariable(heater.getPredicateName(), 'x')
rule9.addRuleBodyPredicates(space.getPredicateName())
rule9.addRuleExistentialVariable(space.getPredicateName(), 'y')
rule9.addRuleBodyPredicates(isInSpace.getPredicateName())
rule9.addRuleExistentialVariable(isInSpace.getPredicateName(), ('x', 'y'))
rule9.addRuleBodyPredicates(spaceTemp.getPredicateName())
rule9.addRuleExistentialVariable(spaceTemp.getPredicateName(), ('y', 't'))
rule9.addRuleBodyPredicates(spaceTempBelow15.getPredicateName())
rule9.addRuleExistentialVariable(spaceTempBelow15.getPredicateName(), 't')
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
rule12.addRuleExistentialVariable(lightHasStatusON.getPredicateName(), 'x')
# conclusion empty because of negative rule
rule12.addRuleConclusion(alert.getPredicateName())
rule12.addRuleConclusionVariables(alert.getPredicateName(), 'x')

## ∀x, ∀y appliance(x), space(y), isInSpace(x, y), spaceOccupied(y,NULL) → applianceStatus(x,OFF)
rule14.addRuleBodyPredicates(appliance.getPredicateName())
rule14.addRuleExistentialVariable(appliance.getPredicateName(), 'x')
rule14.addRuleBodyPredicates(space.getPredicateName())
rule14.addRuleExistentialVariable(space.getPredicateName(), 'y')
rule14.addRuleBodyPredicates(isInSpace.getPredicateName())
rule14.addRuleExistentialVariable(isInSpace.getPredicateName(), ('x', 'y'))
rule14.addRuleBodyPredicates(spaceNotOccupied.getPredicateName())
rule14.addRuleExistentialVariable(spaceNotOccupied.getPredicateName(), 'y')

# conclusion
rule14.addRuleConclusion(applianceHasStatusOFF.getPredicateName())
rule14.addRuleConclusionVariables(applianceHasStatusOFF.getPredicateName(), 'x')

# ∀x, ∀y appliance(x), space(y), isInSpace(x, y), occupied(y,NULL), applianceStatus(x,ON) → ⊥
rule15.addRuleBodyPredicates(appliance.getPredicateName())
rule15.addRuleExistentialVariable(appliance.getPredicateName(), 'x')
rule15.addRuleBodyPredicates(space.getPredicateName())
rule15.addRuleExistentialVariable(space.getPredicateName(), 'y')
rule15.addRuleBodyPredicates(isInSpace.getPredicateName())
rule15.addRuleExistentialVariable(isInSpace.getPredicateName(), ('x', 'y'))
rule15.addRuleBodyPredicates(spaceNotOccupied.getPredicateName())
rule15.addRuleExistentialVariable(spaceNotOccupied.getPredicateName(), 'y')
rule15.addRuleBodyPredicates(applianceHasStatusON.getPredicateName())
rule15.addRuleExistentialVariable(applianceHasStatusON.getPredicateName(), 'x')

# conclusion
rule15.addRuleConclusion(alert.getPredicateName())
rule15.addRuleConclusionVariables(alert.getPredicateName(), 'x')

# ∀x temperatureSensor(x) → ∃y space(y), isInSpace(x, y)
rule16.addRuleBodyPredicates(temperatureSensor.getPredicateName())
rule16.addRuleExistentialVariable(temperatureSensor.getPredicateName(), 'x')
rule16.addRuleConclusion(space.getPredicateName())
rule16.addRuleConclusionVariables(space.getPredicateName(), 'y')
rule16.addRuleConclusion(isInSpace.getPredicateName())
rule16.addRuleConclusionVariables(isInSpace.getPredicateName(), ('x', 'y'))

# ∀t, ∀y spaceTemperature(y, t) → ∃x temperatureSensor(x), space(y), isInSpace(x, y)
rule17.addRuleBodyPredicates(spaceTemp.getPredicateName())
rule17.addRuleExistentialVariable(spaceTemp.getPredicateName(), ('y', 't'))
rule17.addRuleConclusion(space.getPredicateName())
rule17.addRuleConclusionVariables(space.getPredicateName(), 'y')
rule17.addRuleConclusion(temperatureSensor.getPredicateName())
rule17.addRuleConclusionVariables(temperatureSensor.getPredicateName(), 'x')
rule17.addRuleConclusion(isInSpace.getPredicateName())
rule17.addRuleConclusionVariables(isInSpace.getPredicateName(), ('x', 'y'))

# ∀x smokeDetector(x) → ∃y zone(y), isInZone(x, y)
rule18.addRuleBodyPredicates(smokeDetector.getPredicateName())
rule18.addRuleExistentialVariable(smokeDetector.getPredicateName(), 'x')
rule18.addRuleConclusion(zone.getPredicateName())
rule18.addRuleConclusionVariables(zone.getPredicateName(), 'y')
rule18.addRuleConclusion(isInZone.getPredicateName())
rule18.addRuleConclusionVariables(isInZone.getPredicateName(), ('x', 'y'))

# ∀x alarm(x) → ∃y zone(y), isInZone(x, y)
rule19.addRuleBodyPredicates(alarm.getPredicateName())
rule19.addRuleExistentialVariable(alarm.getPredicateName(), 'x')
rule19.addRuleConclusion(zone.getPredicateName())
rule19.addRuleConclusionVariables(zone.getPredicateName(), 'y')
rule19.addRuleConclusion(isInZone.getPredicateName())
rule19.addRuleConclusionVariables(isInZone.getPredicateName(), ('x', 'y'))

# ∀x, ∀z smokeDector(x), zone(z), isInZone(x, z), smokeDectorStatus(x,ON) → ∃y, alarm(y), isInZone(y, z),
# alarmStatus(y,ON)
rule20.addRuleBodyPredicates(smokeDetector.getPredicateName())
rule20.addRuleExistentialVariable(smokeDetector.getPredicateName(), 'x')
rule20.addRuleBodyPredicates(zone.getPredicateName())
rule20.addRuleExistentialVariable(zone.getPredicateName(), 'z')
rule20.addRuleBodyPredicates(isInZone.getPredicateName())
rule20.addRuleExistentialVariable(isInZone.getPredicateName(), ('x', 'z'))
rule20.addRuleBodyPredicates(DetectorHasStatusON.getPredicateName())
rule20.addRuleExistentialVariable(DetectorHasStatusON.getPredicateName(), 'x')
rule20.addRuleConclusion(alarm.getPredicateName())
rule20.addRuleConclusionVariables(alarm.getPredicateName(), 'y')
rule20.addRuleConclusion(isInZone.getPredicateName())
rule20.addRuleConclusionVariables(isInZone.getPredicateName(), ('y', 'z'))
rule20.addRuleConclusion(alarmHasStatusON.getPredicateName())
rule20.addRuleConclusionVariables(alarmHasStatusON.getPredicateName(), 'y')

# ∀x, ∀y, ∀z smokeDector(x), smokeDectorStatus(x,ON), alarm(y), alarmStatus(y,OFF) → ⊥

rule21.addRuleBodyPredicates(smokeDetector.getPredicateName())
rule21.addRuleExistentialVariable(smokeDetector.getPredicateName(), 'x')
rule21.addRuleBodyPredicates(DetectorHasStatusON.getPredicateName())
rule21.addRuleExistentialVariable(DetectorHasStatusON.getPredicateName(), 'x')
rule21.addRuleBodyPredicates(alarm.getPredicateName())
rule21.addRuleExistentialVariable(alarm.getPredicateName(), 'y')
rule21.addRuleBodyPredicates(alarmHasStatusOFF.getPredicateName())
rule21.addRuleExistentialVariable(alarmHasStatusOFF.getPredicateName(), 'y')
rule21.addRuleConclusion(alert.getPredicateName())
rule21.addRuleConclusionVariables(alert.getPredicateName(), 'y')

# ∀x, smartDevice(x) → ∃y, accessList(y), accessListFor(x, y)
rule22.addRuleBodyPredicates(smartDevice.getPredicateName())
rule22.addRuleExistentialVariable(smartDevice.getPredicateName(), 'x')
rule22.addRuleConclusion(accessList.getPredicateName())
rule22.addRuleConclusionVariables(accessList.getPredicateName(), 'y')
rule22.addRuleConclusion(accessListFor.getPredicateName())
rule22.addRuleConclusionVariables(accessListFor.getPredicateName(), ('x', 'y'))

# ∀x, ∀y person(x), smartDevice(y) → ∃z authValue(z), apply(x, y, z)
rule23.addRuleBodyPredicates(person.getPredicateName())
rule23.addRuleExistentialVariable(person.getPredicateName(), 'x')
rule23.addRuleBodyPredicates(smartDevice.getPredicateName())
rule23.addRuleExistentialVariable(smartDevice.getPredicateName(), 'y')
rule23.addRuleConclusion(authValue.getPredicateName())
rule23.addRuleConclusionVariables(authValue.getPredicateName(), 'z')
rule23.addRuleConclusion(apply.getPredicateName())
rule23.addRuleConclusionVariables(apply.getPredicateName(), ('x', 'y', 'z'))

# ∀x, ∀y person(x), smartDevice(y), apply(x, y, True) → authorized(x)
rule24.addRuleBodyPredicates(person.getPredicateName())
rule24.addRuleExistentialVariable(person.getPredicateName(), 'x')
rule24.addRuleBodyPredicates(smartDevice.getPredicateName())
rule24.addRuleExistentialVariable(smartDevice.getPredicateName(), 'y')
rule24.addRuleBodyPredicates(apply.getPredicateName())
rule24.addRuleExistentialVariable(apply.getPredicateName(), ('x', 'y', 'z'))
rule24.addRuleConclusion(authorized.getPredicateName())
rule24.addRuleConclusionVariables(authorized.getPredicateName(), 'x')

# ∀x, ∀y person(x), smartDevice(y), apply(x, y, FALSE), authorized(x) → ⊥
rule25.addRuleBodyPredicates(person.getPredicateName())
rule25.addRuleExistentialVariable(person.getPredicateName(), 'x')
rule25.addRuleBodyPredicates(smartDevice.getPredicateName())
rule25.addRuleExistentialVariable(smartDevice.getPredicateName(), 'y')
rule25.addRuleBodyPredicates(apply.getPredicateName())
rule25.addRuleExistentialVariable(apply.getPredicateName(), ('x', 'y', 'z'))
rule25.addRuleBodyPredicates(authorized.getPredicateName())
rule25.addRuleExistentialVariable(authorized.getPredicateName(), 'x')
rule25.addRuleConclusion(alert.getPredicateName())
rule25.addRuleConclusionVariables(alert.getPredicateName(), 'x')

# rule 26: heater(x)∧space(y)∧isInSpace(x, y)∧spaceTemperature(y,13),heaterHasStatus(x, OFF ) --> !
rule26.addRuleBodyPredicates(heater.getPredicateName())
rule26.addRuleExistentialVariable(heater.getPredicateName(), 'x')
rule26.addRuleBodyPredicates(space.getPredicateName())
rule26.addRuleExistentialVariable(space.getPredicateName(), 'y')
rule26.addRuleBodyPredicates(isInSpace.getPredicateName())
rule26.addRuleExistentialVariable(isInSpace.getPredicateName(), ('x', 'y'))
rule26.addRuleBodyPredicates(spaceTemp.getPredicateName())
rule26.addRuleExistentialVariable(spaceTemp.getPredicateName(), ('y', '13'))
rule26.addRuleBodyPredicates(heaterHasStatusOFF.getPredicateName())
rule26.addRuleExistentialVariable(heaterHasStatusOFF.getPredicateName(), 'x')
rule26.addRuleConclusion(alert.getPredicateName())
rule26.addRuleConclusionVariables(alert.getPredicateName(), 'x')

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
set_rules.add(rule26)
set_rules.add(rule14)
set_rules.add(rule15)
set_rules.add(rule16)
set_rules.add(rule17)
set_rules.add(rule18)
set_rules.add(rule19)
set_rules.add(rule20)
set_rules.add(rule21)
set_rules.add(rule22)
set_rules.add(rule23)
set_rules.add(rule24)
set_rules.add(rule25)
