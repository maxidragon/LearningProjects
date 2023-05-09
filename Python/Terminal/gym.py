class Gym:
    gym_in_city = {}

    def __init__(self, name, city, price, discount):

        self.name = name
        self.city = city
        self.price = price
        self.exercises = []
        self.discount = discount
        try:
            Gym.gym_in_city[self.city] += 1
        except KeyError:
            Gym.gym_in_city[self.city] = 1

    def add_exercises(self, *exercises):
        for exercise in exercises:
            self.exercises.append(exercise)

    def add_discount(self, discount):
        if self.discount:
            self.price = (self.price / 100) * (100 - discount)

    def set_owner(self, owner):
        self.__owner = owner
    def __str__(self):
        try:
            return f'Name: {self.name}\nCity: {self.city}\nOwner: {self.__owner}'
        except AttributeError:
            return f'Name: {self.name}\nCity: {self.city}'
    def __len__(self):
        return len(self.exercises)
    def __getitem__(self, key):
        try:
            return self.exercises[key]
        except IndexError as e:
            return e
gym1 = Gym('gym1', 'Warszawa', 200, True)
gym2 = Gym('gym2', 'Poznań', 35, False)
gym1 = Gym('gym3', 'Warszawa', 100, False)
gym1.add_exercises('joga', 'crossfit')
gym1.add_discount(5)
gym1.set_owner('Jan Kowalski')
# gym1.set_owner('Jan Nowak')
print(gym2)
print(len(gym1))
print(gym1[9])