# Think Module
# Modes: Intepreted Inner Situation, Intpreted Outer Situation
# Outputs: thoughts/feelings/actions
# 


from datatype import Thought, Feeling, Action
# import langchain packages
from langchain.chains import LLMChain
from langchain.llms import OpenAI
from langchain.prompts import load_prompt
import json

class Think():
    def __init__(self) -> None:
        llm = OpenAI(temperature=0.9)
        inner_prompt = load_prompt("think_inner_prompt.yaml")
        outer_prompt = load_prompt("think_outer_prompt.yaml")
        self.inner_chain = LLMChain(llm=llm, prompt=inner_prompt)
        self.outer_chain = LLMChain(llm=llm, prompt=outer_prompt)
    
    def inner_situation(self, situation) -> dict:
        json_data = self.inner_chain.run(situation)
        # thoughts, feelings, actions
        data = json.loads(json_data)
        thoughts, feelings, actions = data["thoughts"], data["feelings"], data["actions"]
        return thoughts, feelings, actions
    
    def outer_situation(self, situation) -> dict:
        json_data = self.outer_chain.run(situation)
        return json.loads(json_data)