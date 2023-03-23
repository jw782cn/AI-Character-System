# AI chatbot system
# Modules: Think, Feel, Act, Memory
# Two triggers: Inner Situation, Outer Situation

from think import Think
from memory import Memory
from feel import Feel
from act import Act
from characteristics import Characteristic

class System():
    def __init__(self) -> None:
        self.think = Think()
        self.feel = Feel()
        self.act = Act()
        self.memory = Memory()
        # mode: inner, outer, idle, wait_inner, wait_outer
        self.status = "idle"
        self.input_buffer = []
        
    def handle_input(self, input) -> None:
        # 1. Interpret Input
        self.input_buffer.append(input)
        pass
    
    # Trigger: Outer Situation
    def outer_situation(self, situation) -> dict:
        # 1. Access Related Memory (if any) -> interpreted outer situation
        # 2. Think about the situation -> thoughts/feelings/actions
        # 3. Write to Memory / Evoke Inner Situation Change / Write to Feel / Write to Act
        self.mode = "outer"
        related_long_term_memory, related_short_term_memory = self.memory.read_related_memory(situation)
        related_charactaristics = self.Characteristic.get_characteristics()
        related_feelings = self.feel.get_feelings()
        related_actions = self.act.get_queing_actions()
    
    