letter ="hey my name is {} & i am from {}"  #OLD APPROACH
country="India"
name="harry"
print(letter.format(name,country))
#NEW APPROACH (F STRING)
letter =f"hey my name is {name} & i am from {country}"
print(f"for only {name} & {country:.2s}")  