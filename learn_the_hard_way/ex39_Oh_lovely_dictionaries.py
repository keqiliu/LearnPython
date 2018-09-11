states = {
    'Oregon': 'OR',
    'Florida': 'FL',
    'California': 'CA',
    'New York': 'NY',
    'Michigan': 'MI'
}

cities = {
    'CA': 'San Francison',
    'MI': 'Lanxin',
    'FL': 'Orlando',
    'Aiya': 'lalalalala',
    'wo': 'hao kun',
    'bubu': 'zuibang'
}

# add more to dictionary!
cities['NY'] = 'New York'
cities['OR'] = 'Portland'

# print out some cities
print('-' * 10)
print("NY State has: ", cities['NY'])
print("OR State has: ", cities['OR'])

print('-' * 10)
print("Michigan's abbr. is: ", states['Michigan'])
print("Florida's abbr. is: ", states['Florida'])

print('-' * 10)
print("Florida has: ", cities[states['Florida']])

print('-' * 10)
for state, abbrev in list(states.items()):
    print(f"{state} is abbreviated {abbrev}")


# dict.items return tuples with two variables: key + value
print('-' * 10)
for abbrev, city in cities.items():  # on need to use list() outside dict.items
    print(f"{abbrev} --- {city}")

print('-' * 10)
for state, abbrev in states.items():  # on need to use list() outside dict.items
    print(f"{state} has {cities[abbrev]}")

print('-' * 10)
# this get is SAFE!!! no error even for key not existing!!!
state = states.get('Texas')

# if state is None:  # this is the same as below!!!
if not state:
    print('Sorry, key not defined.')

# get can also define DEFAULT VALUE
city = cities.get('TX', 'knowhere')  # default value is defined here!!!
print(f"The city for the state 'TX' is: {city}")
