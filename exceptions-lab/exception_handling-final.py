import sys

# 1) Fetch name from first argument passed to the script.
# If there is no argument, then exist with a readable error message.
# The potential error here is an IndexError.
try:
    name = sys.argv[1]
except IndexError:
    print("Error: please provide a name and a repeat count to the script.")
    sys.exit(1)


# 2) Convert the second argument to be an integer so that we can repeatedly print out
# the name argument. We should either a ValueError or an IndexError if there weren't enough
# arguments provided.
try:
    repeat_count = int(sys.argv[2])
except IndexError:
    print("Error: please provide a name and a repeat count to the script.")
    sys.exit(1)
except ValueError:
    print("Error: the repeat count needs to be a number.")
    sys.exit(1)

# 3) Open a file called `name_repeated.txt` in the `root_files` directory and write a line for each time the name was
# repeated. If the user running the script doesn't have write permissions for the directory that
# we're writing to then we might see a PermissionError. PermissionError is new as of 3.3, so let's instead catch
# OSError and IOError to make the script more backwards compatible. If an error is caught print to the screen instead.
try:
    f = open("root_files/name_repeated.txt", "w")
except (OSError, IOError) as err:
    print("Error: unable to write file (", err, ")")
    for i in range(1, repeat_count + 1):
        print(i, "-", name)
else:
    names = [name + "\n" for i in range(1, repeat_count + 1)]
    f.writelines(names)
    f.close()
