class Animal:
    def __init__(self, name):
        self.name=name
    
    def speak(self, sound):
        print(f"{self.name} will make some noise like {sound}")
class Dog(Animal):
    def speak(self):
        print(f"{self.name} will bark")
    
name=input("input name of your animal ")
sound=input(f"input sound that {name} makes ")
anim=Dog("rex")
anim.speak()
Animal(name).speak(sound)