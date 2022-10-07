

a = 213
b = 'Joker'
c = [a,b,"123",12.3, [1,2,3],True,False]

print(c[0])
print(c[-1])
print(len(c))

# ? slicing start:end
print(c[:3])

# ? slicing start:end:step
print(c[::2])

# ? slicing start:end:step
print(c[::-1])

c = c[::-1]
print(c)

c.append("a")

print(c)

c.insert(2,"a")

print(c)



c.extend([1,2,3,4,5,65,6,6,7,7,7,8,8,8])

print(c)