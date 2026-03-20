# def print_kwargs(**kwargs):
#   for key,value in kwargs.items():
#     print(f"{key}: {value}")

# print_kwargs(name="raman")
# print_kwargs(name="raman" , role="Backend Developer")
# print_kwargs(name="raman" , role="Backend Developer", comp_name="Google")

def demo(*args, **kwargs):
    print("Args:", args)
    print("Kwargs:", kwargs)

demo(1, 2, 3, name="Raman", age=21)

# def format_value(name , value):
#   print ("Name: " , name , "Value: ", value )

# format_value(name="Raman" , value="Billionorie")
# format_value(value="Billionorie" , name="raman")
# format_value( value="Billionorie") 

