# AI chatbot system
# Modules: Think, Feel, Act, Memory
# Two triggers: Inner Situation, Outer Situation

from think import Think
from memory import Memory
from feel import Feel
from act import Act
from characteristics import Characteristic
# import langchain packages
from langchain.chains import LLMChain
from langchain.llms import OpenAI
from langchain.prompts import load_prompt


class System():
    def __init__(self) -> None:
        self.think = Think()
        self.feel = Feel()
        self.act = Act()
        self.memory = Memory()
        # mode: inner, outer, idle, wait_inner, wait_outer
        # TODO: flowchart of mode
        self.status = "idle"
        self.input_buffer = []
        # chains
        llm = OpenAI(temperature=0.9)
        inner_prompt = load_prompt("interpret_inner_prompt.yaml")
        outer_prompt = load_prompt("interpret_outer_prompt.yaml")
        self.inner_chain = LLMChain(llm=llm, prompt=inner_prompt)
        self.outer_chain = LLMChain(llm=llm, prompt=outer_prompt)
        # settings
        
    def handle_input(self, input) -> None:
        # 1. Interpret Input
        self.input_buffer.append(input)
        pass
    
    def process_thoughts(self, thoughts) -> None:
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
        # the actions maybe are waiting to be executed
        related_actions = self.act.get_queing_actions()
        interpreted_situation = self.outer_chain.run(situation, related_long_term_memory, related_short_term_memory, related_charactaristics, related_feelings, related_actions)
        # think
        thoughts, feelings, actions = self.think.outer_situation(interpreted_situation)
        # thoughts: write to memory / change inner situation / set timer
        
        
        
    
    