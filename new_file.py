import second_group


people = [second_group.Person("Tom", 23),
          second_group.Student("Bob", 19, "Harvard"),
          second_group.Employee("Sam", 35, "Google")]


for person in people:
    person.display_info()
    print()