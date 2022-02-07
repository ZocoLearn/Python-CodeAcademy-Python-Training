message="Hello Tehran!"
my_slice=message[6:13]
print(my_slice)

my_slice=message[:5]#default-->start=0
print(my_slice)

my_slice=message[6:]#default-->stop=end
print(my_slice)

my_slice=message[:]
print(my_slice)

my_slice=message[::2]
print(my_slice)


my_slice=message[::-1]
print(my_slice)