import sys

# 1) Fetch name from first argument passed to the script.
# If there is no argument, then exist with a readable error message.
# The potential error here is an IndexError.
name = sys.argv[1]


# 2) Convert the second argument to be an integer so that we can repeatedly print out
# the name argument. We should either a ValueError or an IndexError if there weren't enough
# arguments provided.
repeat_count = int(sys.argv[2])


# 3) Open a file called `name_repeated.txt` in the `root_files` directory and write a line for each time the name was
# repeated. If the user running the script doesn't have write permissions for the directory that
# we're writing to then we might see a PermissionError. PermissionError is new as of 3.3, so let's instead catch
# OSError and IOError to make the script more backwards compatible. If an error is caught print to the screen instead.
f = open("root_files/name_repeated.txt", "w")
names = [name + "\n" for i in range(1, repeat_count + 1)]
f.writelines(names)
f.close()
