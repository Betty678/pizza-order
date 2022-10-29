print("Welcome to pizza order deliveries")
size=str(input("Which size do you want? small,medium or large"))
add_pepperoni=str(input("do you want pepperoni? yes or no"))
cheese=str(input("do you want cheese? yes or no"))
small_pizza=15
medium_pizza=20
large_pizza=25
small_pepperoni=2
lm_pepperoni=3
extra_cheese=1
if size==("small"):
    total=small_pizza
    print(f"The amount of pizza is ${total}")
    if add_pepperoni==("yes"):
        total=small_pizza+small_pepperoni
        print(f"The amount of pizza with pepperoni is ${total}")
        if cheese==("yes"):
            total=small_pizza+small_pepperoni+extra_cheese
            print(f"The amount of pizza with cheese and pepperoni is ${total}")
        else:
            total=small_pizza+small_pepperoni+extra_cheese
            print(f"The amount of pizza with cheese and pepperoni is ${total}")
    else:
        print(f"The amount of pizza is ${total}")
elif size == ("medium"):
    total=medium_pizza
    print(f"The amount of pizza is ${total}")
    if add_pepperoni==("yes"):
        total=medium_pizza+lm_pepperoni
        print(f"The amount of pizza with pepperoni is ${total}")
        if cheese==("yes"):
            total=medium_pizza+lm_pepperoni+extra_cheese
            print(f"The amount of pizza with cheese and pepperoni is ${total}")
        else:
            total=medium_pizza+lm_pepperoni+extra_cheese
            print(f"The amount of pizza with cheese and pepperoni is ${total}")
    else:
        print(f"The amount of pizza is ${total}")
elif size ==("large"):
    total=large_pizza
    print(f"The amount of pizza is ${total}")
    if add_pepperoni==("yes"):
        total=large_pizza+lm_pepperoni
        print(f"The amount of pizza with pepperoni is ${total}")
        if cheese==("yes"):
            total=large_pizza+lm_pepperoni+extra_cheese
            print(f"The amount of pizza with cheese and pepperoni is ${total}")
        else:
            total=large_pizza+lm_pepperoni+extra_cheese
            print(f"The amount of pizza with cheese and pepperoni is ${total}")
    else:
        print(f"The amount of pizza is ${total}")
    
     
    
    
    
