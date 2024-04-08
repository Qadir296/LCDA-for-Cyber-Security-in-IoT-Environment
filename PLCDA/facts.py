import random
from classes import Fact
from predicates import *
from Dataset import *


factHeater = Fact(1)
factSpace = Fact(2)
factmainDoor = Fact(3)
factInvalidAttempt = Fact(4)
factLock = Fact(5)
factIsOn = Fact(6)
factRoom = Fact(7)
factLight = Fact(8)
factisInRoom = Fact(9)
factSmokeDetector = Fact(10)
factAlarm = Fact(11)
factSmokeDectStatus = Fact(12)
factAlarmStatus = Fact(13)
factApply = Fact(14)
factPerson = Fact(15)
factSmartDevice = Fact(16)
factAuthorized = Fact(17)

## room(bedroom)
factRoom.addFactConstant('bedroom')
factRoom.addFacts(room.getPredicateName(), 'bedroom')
factRoom.addFactTerms(room.getPredicateName())

### light(a)

factLight.addFactConstant('light1')
factLight.addFacts(light.getPredicateName(), 'light1')
factLight.addFactTerms(light.getPredicateName())

factSmokeDectStatus.addFactConstant('s1')
factSmokeDectStatus.addFacts(DetectorHasStatusON.getPredicateName(), 's1')
factSmokeDectStatus.addFactTerms(DetectorHasStatusON.getPredicateName())

factSmokeDetector.addFactConstant('s1')
factSmokeDetector.addFacts(smokeDetector.getPredicateName(), 's1')
factSmokeDetector.addFactTerms(smokeDetector.getPredicateName())

factAlarm.addFactConstant('a1')
factAlarm.addFacts(alarm.getPredicateName(), 'a1')
factAlarm.addFactTerms(alarm.getPredicateName())

factAlarmStatus.addFactConstant('a1')
factAlarmStatus.addFacts(alarmHasStatusOFF.getPredicateName(), 'a1')
factAlarmStatus.addFactTerms(alarmHasStatusOFF.getPredicateName())

# space
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

factPerson.addFactConstant('Jane')
factPerson.addFacts(person.getPredicateName(), 'Jane')
factPerson.addFactTerms(person.getPredicateName())

factSmartDevice.addFactConstant('Toy')
factSmartDevice.addFacts(smartDevice.getPredicateName(), 'Toy')
factSmartDevice.addFactTerms(smartDevice.getPredicateName())

factApply.addFactConstant(('Jane', 'Toy', 'False'))
factApply.addFacts(apply.getPredicateName(), ('Jane', 'Toy', 'False'))
factApply.addFactTerms(apply.getPredicateName())

factAuthorized.addFactConstant('Jane')
factAuthorized.addFacts(authorized.getPredicateName(), 'Jane')
factAuthorized.addFactTerms(authorized.getPredicateName())
#
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
set_facts.add(factSmokeDectStatus)
set_facts.add(factSmokeDetector)
set_facts.add(factAlarmStatus)
set_facts.add(factAlarm)
set_facts.add(factApply)
set_facts.add(factPerson)
set_facts.add(factAuthorized)
set_facts.add(factSmartDevice)

fact_list = []


for i, predicate in enumerate(set_predicates):
    ident = i + 1
    list_pred = list(set_predicates)
    pred = random.choice(list_pred)
    fact = Fact(ident)
    if pred.getPredicateDegree() == 1:
        fact.addFacts(pred.getPredicateName(), f"Constant_{ident}")
        fact.addFactConstant(f"Constant_{ident}")
    elif pred.getPredicateDegree() == 2:
        fact.addFacts(pred.getPredicateName(), (f"Constant_{ident}", f"Constant_{ident + 1}"))
        fact.addFactConstant((f"Constant_{ident}", f"Constant_{ident + 1}"))
    else:
        fact.addFacts(pred.getPredicateName(), (f"Constant_{ident}", f"Constant_{ident + 1}", f"Constant_{ident + 2}"))
        fact.addFactConstant((f"Constant_{ident}", f"Constant_{ident + 1}", f"Constant_{ident + 2}"))
    set_facts.add(fact)
    fact_list.append(fact)


#### Convert facts into d a dlp file #####

def dlpconversion(facts: list) -> object:
    """

    :param facts:
    :return:
    """
    file_path = "facts_1000.dlp"  # Replace with the desired file name
    # Write the facts to the .dlp file
    with open(file_path, "w") as dlp_file:
        dlp_file.write("@fact:\n")
        for facts in set_facts:
            fac = facts.getFacts()
            for predicate, constant in fac.items():
                dlp_file.write(f"{predicate.lower()} ('{constant}').\n")
    print(f"Facts saved to {file_path}")
    return dlp_file