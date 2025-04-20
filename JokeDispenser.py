def jokes():
    import pyjokes
    permit = input("Want some jokes? (yes/no): ").lower()
    if permit == "yes":
        joke = pyjokes.get_joke(language='en',category='neutral')
        print("\n")
        print(joke)
        print("\n")
        jokes()
    elif permit == "no":
        print("Ok")
    else:
        print("\n")
        print('Wrong Statement')
        print("\n")
        jokes()
jokes()
