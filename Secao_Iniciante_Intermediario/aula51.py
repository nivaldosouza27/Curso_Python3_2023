### Generator Functions ###

def generator (n, maximum):
    while True:
        yield n
        n += 1

        if n>= maximum:
            return

gen = generator(n=0, maximum=100)
for n in gen:
    print(n)