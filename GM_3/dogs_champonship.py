

class dog:

    def __init__(self, name, age, weight, type_):
        self.n = name
        self.a = age
        self.w = weight
        self.t = type_


class championship:

    def __init__(self, space, prize):
        self.s = space
        self.p = prize
        self.requrements = {
            "weight": 5,
            "type": ["boxer", "bulldog"],
            "age": 0.5
        }

        self.dogs = []

    def check_dog(self, dog):
        if dog.w < self.requrements["weight"] and dog.t in self.requrements['type'] and dog.a > self.requrements["age"]:
            return [True, f"{dog.n} you are ready for challenges"]
        return [False, f"{dog.n} you aren't ready for challenges"]

    def add(self,dog):
        result = self.check_dog(dog)
        if result[0] == True and self.s > 0:
            self.dogs.append(dog)
            self.s -= 1
        elif self.s == 0:
            return f"{dog.n} there is no space for you"
        return result[1]




dog_1 = dog("jerry", 1, 10, "german shephard")
dog_2 = dog("larry", 0.7, 2, "boxer")
dog_3 = dog("garry", 0.7, 4, "bulldog")
dog_4 = dog("sherry", 0.7, 4, "boxer")


arena = championship(3,1_000_000)

print(arena.add(dog_1))
print(arena.add(dog_2))
print(arena.add(dog_3))
print(arena.add(dog_4))

dog_ages = [dog.a for dog in arena.dogs]
av_age = round(sum(dog_ages) /len(dog_ages))

print(av_age)




