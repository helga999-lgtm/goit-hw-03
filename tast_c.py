text = "hello world"
result = text.split()
print(result)  # Виведе: ['hello', 'world']

clean = '   spacious   '.strip()
print(clean) # spacious

print('TestHook'.removeprefix('Test')) # Hook
print('TestHook'.removeprefix('Hook')) # TestHook

intab = "aeiou"
outtab = "12345"
trantab = str.maketrans(intab, outtab)

str = "This is string example"
print(str.translate(trantab))

intab = "aeiou"
trantab = str.maketrans('', '', intab)

str = "This is string example"
print(str.translate(trantab))
