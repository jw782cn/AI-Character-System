# definition of data types

# thoughts/feelings/actions

class Thought():
    def __init__(self, thought) -> None:
        self.thought = thought
        
    def __str__(self) -> str:
        return self.thought
    
class Feeling():
    def __init__(self, feeling) -> None:
        self.feeling = feeling
        
    def __str__(self) -> str:
        return self.feeling
    
class Action():
    def __init__(self, action) -> None:
        self.action = action
        
    def __str__(self) -> str:
        return self.action