birthday = {
    "Ares": 666,
    "Zeus": 1997,
    "Hermes": 1
}

if __name__ == '__main__':
    print("Welcome to the birthday dictionary. We know the birthdays of: ")
    for name in birthday:
        print(name)

    print('Who\'s birthday do you want to look up?')
    name = input()
    if name in birthday:
        print("{fname}\'s birthday is {date}".format(fname=name, date=birthday[name]))
    else:
        print("We don't have information about birthday of: " + name)
