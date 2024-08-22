 #Write a simple user defined function that greets a person in such a way that 
# It should accept both the name of the person and message you want to deliver.
#ii) If no message is provided, it should greet a default message ‘How are you’
def greet_person(name, message="How are you?"):
    print(&"Hello,{name}!{message}")
    greet_person("srinu", "it's a great to see you" )
    greet_person("srinu")
