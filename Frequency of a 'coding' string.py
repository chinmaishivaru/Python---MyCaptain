str = input("Please enter a string\n")
frequencies = {}
def most_frequency(str):
    for i in str:
        if i in frequencies:
            frequencies[i] += 1
        else:
            frequencies[i] = 1

most_frequency(str)
print(sorted(frequencies.items(), key = lambda kv:(kv[1], kv[0]),reverse=True))
