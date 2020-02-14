# 1) Import the built-in `math` module

# 2) Import the `reverse` and `shuffle` from the custom `strhelpers` module (Needs to be created)

name = "Kevin Bacon"

assert math.ceil(14.11) == 15, f"Expected 15, but got {math.ceil(14.11)}"
assert (
    reverse(name) == "nocaB niveK"
), f"Expected 'nocaB niveK', but got {reverse(name)}"
assert type(shuffle(name)) == str, f"Expected a string, but got {type(shuffle(name))}"
assert sorted(shuffle(name)) == sorted(
    name
), f"Expected [' ', 'B', 'K', 'a', 'c', 'e', 'i', 'n', 'n', 'o', 'v'], but got {sorted(shuffle(name))}"

