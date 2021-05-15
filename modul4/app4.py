# Create a conversation function that uses nonlocal variables to keep track of information provided in the conversation

def conversation() -> tuple:  # we can hint the type of object returned by the function with  "-> [type]"
    name = ''
    city = ''

    def hello():
        print("Hello John!")

    def hello_response():
        nonlocal name
        name = input("My name is ")

    def question():
        print(name, ",how is the weather?")

    def response():
        print('It is sunny today')

    def response2():
        print(city, "is a very nice city.")

    def question2():
        nonlocal city
        city = input("Do you like ")

    return hello, hello_response, question, response, question2, response2


c = conversation()

for line_function in c:  # this will iterate the tuple returned by conversation function
    line_function()  # we call teh function that variable line_function is pointing to using ()
