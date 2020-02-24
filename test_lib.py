from people_repository.people_repository import peopleRepository
import json
import setuptools

peopleRepository.createPerson('Adrian', 'Ferreres', 'ardi@mail.com')
listPeople  = peopleRepository.listPeople(0,5)
jsonList = json.dumps(listPeople)

onePerson = peopleRepository.searchPersonById("1")
jsonPerson = json.dumps(onePerson)

print('People list: {}'.format(jsonList))
print('One person: {}'.format(jsonPerson))