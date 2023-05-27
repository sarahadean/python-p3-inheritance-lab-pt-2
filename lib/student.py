class Student:
    def __init__(self):
        self
    
    def hello(self):
        print("Hey there! I'm so excited to learn stuff.")

    def raise_hand(self):
        print("Pick me!")

class ChattyStudent(Student):
    def __init__(self):
        self
    
    def hello(self):
        super().hello()
        print("How are you doing today? I'm okay, but I'm kind of tired. Did you watch The Walking Dead last night? You didn't?! Oh man, it was so crazy! What, you don't want any spoilers? Okay well let me just tell you who died...")
    
    def raise_hand(self):
        for s in range(0, 10):
            super().raise_hand()
        
        
            
# george = Student()
# # george.raise_hand()

# jessica = ChattyStudent()

# # jessica.hello()
# #successfully printed

# jessica.raise_hand()
    
