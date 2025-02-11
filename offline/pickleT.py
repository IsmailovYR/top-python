import pickle

#data = {'name': "alice", 'age': 24, 'city': 'new york'}

class Person:
    health = 100
    @classmethod
    def print_health(cls):
        print(cls.health)

    def __init__(self, name, age, is_student=False):
        self.name = name
        self.age = age
        self.is_student = is_student
        self.__gender = None

    def invert_is_student(self):
        self.is_student = not self.is_student

    @staticmethod
    def to_learn():
        print('im learning')

    def __str__(self):
        return f"Person name={self.name}, age={self.age}"

person = Person("alice", 24)

with open('person.pkl', 'wb') as file:
    pickle.dump(person, file)

with open('person.pkl', 'rb') as file:
    loaded_data = pickle.load(file)

print(loaded_data)

"""
Задание 1
Есть некоторый словарь, который хранит названия
стран и столиц. Название страны используется в качестве
ключа, название столицыв качестве значения. Необходимо
реализовать: добавление данных, удаление данных, поиск
данных, редактирование данных, сохранение и загрузку
данных (используя упаковку и распаковку).
Задание 2
Есть некоторый словарь, который хранит названия
музыкальных групп(исполнителей) и альбомов. Название группы используется в качестве ключа, название
альбомов в качестве значения. Необходимо реализовать:
добавление данных, удаление данных, поиск данных,
редактирование данных, сохранение и загрузку данных
(используя упаковку и распаковку)."""