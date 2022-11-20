import random



class base:
    def __init__(self,max_users,pass_len):
        self.pasword_length = pass_len
        self.base = {1: ['mari', 'maro@gmail.com', 'xachapuri']}
        self.max_users = max_users
        
    # ბაზაში დამატება
    def registration(self,nickname,gmail,password):

        # pass len limit
        if len(password) < self.pasword_length:
            return "Try longer password"

        # generate random id by conditions + base size
        self.id = random.randint(1,len(nickname+password+gmail))

        # try creating new id if problem occures
        while self.id  in  self.base.keys():
            self.id = random.randint(1,len(nickname+password+gmail*len(self.base.keys())))

        # check if nickname is in base 
        for i in self.base.values(): 
            if nickname  in i or gmail in i: 
                return "user already is in base"
        # add user if max users is more than zero
        if self.max_users > 0 :
            self.base[self.id] = [nickname,gmail,password]
            self.max_users -= 1
            return "user added"
    # ბაზაში შესვლა
    def login(self, nickname, password):

        # if pasword is not correct
        if len(password) < self.pasword_length:
            return "Try longer password"

        # check if nickname is in base 
        for id,lst in self.base.items(): 
            # if pasword and nickname correct
            if nickname  in lst and password in lst: 
                return f"\nuserid: {id} \nurl: https://facebook.com/{id}/\n"
            # if pasword and nickname incorrect
            elif nickname  not in lst and password not in lst: 
                return f"'{nickname}' is not registered"
            # if pasword or nickname incorrect
            elif nickname not in lst or password not in lst:
                return "password or nickname is incorrect"  

            

database = base(2,6)

# registration atempt
database.registration("a","a@gmail.com","xachapuri")

database.registration("b","a@gmail.com","xachapuri")
database.registration("a","b@gmail.com","xachapuri")

print()

print(database.base)
print()
# login atempt
print(database.login("a","xachapuri"))
print(database.login("b","xachapuri"))

print(database.login("a","xachapur"))
print(database.login("Asda","xaaschaasdpur"))


print()
print(database.login("mari","maro@gmail.com"))
print(database.base[1])
print()
print(database.base[1][0])
print(database.base[1][1])
print(database.base[1][2])