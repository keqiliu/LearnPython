my_name = 'Xiao zhu Keqi'
my_age = 28
my_height = 159
my_weight = 61.2
my_eyes = 'Brown'
my_teeth = 'White'  # why need to specify teeth color, otherwise what? :)
my_hair = 'Black'

print(f"Let's talk about {my_name}")
print(f"She's {my_height} cm tall.")
print(f"She's {my_weight} kg heavy, about {round(my_weight)}")  # round() is "4 down 5 up" rule
print(f"She's got {my_eyes} eyes and {my_hair} hair.")
print(f"Her teeth are usually {my_teeth} depending on",
      "how much coffee or tea she has recently.")

# this line is tricky, try to get it exactly right
total = my_age + my_height + my_weight
print(f"If I add {my_age}, {my_height}, and {my_weight} I get {total}.")
