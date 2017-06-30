name = raw_input("Name:")
salutation = raw_input("Salutation:")
age = raw_input("Age:")
height = raw_input("height:")

print "%s %s %d %d" % (salutation, name, int(age), int(height))

# %r -> Literals
# %s -> String
# %c -> Char
# %d, %i -> Signed decimal integer
# %u -> Unsigned decimal integer
# %x -> Lower case hex
# %X -> Upper case hex
# %f -> floating point real number
