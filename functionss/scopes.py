cafe="CoffeeCut"   # Globle Scope     top level script

def order_cofee():
    coffee_name="Espresso"    #Local scope.

    print(f"Local Scope of Coffe is: {coffee_name}")

print(f"Globale scope of Function Cafe Name is: {cafe}")

coffee_names="latte"   #outer of function if nested
order_cofee()
print(f"outer scop of function {coffee_names}")


def user_id():
    user_id="Khush@gmail"   #enclosing scope ....Inner function → Outer function = ENCLOSING scope

    def user_pass():
        user_password="123#abc"
        print(f"user id is: {user_id}")
        print(f"user password is: {user_password}")
    user_pass()
user_id()
