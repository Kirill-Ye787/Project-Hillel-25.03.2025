def say_hi(name, age):
    return f"Hi. My name is {name} and I'm {age} years old"

assert say_hi("Kirill", 34) == "Hi. My name is Kirill and I'm 34 years old", 'Test1'
assert say_hi("Natalia", 50) == "Hi. My name is Natalia and I'm 50 years old", 'Test2'

print('ОК')
print(say_hi("Kirill", 34))
print(say_hi("Natalia", 50))
