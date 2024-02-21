katz_deli = []


def line(katz_deli):
    if not katz_deli:
       print("The line is currently empty.")
    else:
        message = "The line is currently:" 
        for index, customer in enumerate(katz_deli, start=1 ):
            message += f" {index}. {customer}"
        print(message)

print(line(katz_deli))

def take_a_number(katz_deli, name):
    katz_deli.append(name)
    print(f"Welcome, {name}. You are number {len(katz_deli)} in line.")


def now_serving(katz_deli): 
    if not katz_deli:
        print("There is nobody waiting to be served!") 
    else:
        customer_in_line = katz_deli.pop(0) 
        print(f"Currently serving {customer_in_line}.")



