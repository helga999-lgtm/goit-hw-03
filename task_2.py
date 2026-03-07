from random import randint, sample
min_value = 1
max_value = 1000
length = 8

get_numbers_ticket = set()
while len(get_numbers_ticket) != length:
    get_numbers_ticket.add(randint(min_value, max_value))

print(list(get_numbers_ticket))

