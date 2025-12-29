# def multiple(*arg):
#     return arg

# print(multiple("khushboo","atul"))  #postional multiple value arguments
# # print(multiple())

def mobile(*brand_name ,**details):
    print(f"Brand name is: {','.join(brand_name)}")
    print("About Mobile: ")

    for key,val in details.items():
        print(f".{key.capitalize()},{val}")

mobile("Samsung","iphone",color="White",storage="128Gb",battery="65000mh")


