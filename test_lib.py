from repository.people_repository import peopleRepository
import json
import setuptools

peopleRepository.createPerson('Adrian', 'Ferreres', 'ardi@mail.com')
listPeople  = peopleRepository.listPeople(0,5)
jsonList = json.dumps(listPeople)

print('People list: {}'.format(jsonList))