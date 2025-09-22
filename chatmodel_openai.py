from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers.base import BaseOutputParser
from dotenv import load_dotenv
import os

load_dotenv()

chat_model = ChatOpenAI(api_key=os.environ['OPENAI_API_KEY'])

# result = chat_model.invoke('Hi!')
# print(result)

messages = [HumanMessage(content='I have onions, carrots, eggs, bread'),
            HumanMessage(content='I have salt, pepper'),
            HumanMessage(content='Give me a recipe to make with these ingredients only')]
# result = chat_model.invoke(messages)
# print(result.content)

template = 'You are a helpful assistant that translates {input_language} to {output_language}.'
human_template = '{text}'

chat_prompt = ChatPromptTemplate.from_messages([
    ('system', template),
    ('human', human_template)
])
message = chat_prompt.format_messages(input_language='English', output_language='French', text='I love programming!')

# result = chat_model.invoke(messages)
# print(result.content)

class AnswerOutputParser(BaseOutputParser):
    def parse(self, text:str):
        """Parse the output of an LLM"""
        return text.strip().split('answer = ')

template = """You are a helpful assistant that solves math problems and shows your work.
            Output each step and return the answer in the following format: answer = <answer here>.
            Make sure to output answer in all lowercase and to have exactly one space and one equal sign following it."""
human_template = '{problem}'
chat_prompt = ChatPromptTemplate.from_messages([
    ('system', template),
    ('human', human_template)
])

# messages = chat_prompt.format_messages(problem='3x^2 + 2 - 10 = 0')
# result = chat_model.invoke(messages)
# steps, answer = AnswerOutputParser().parse(result.content)
# print('Steps: ', steps)
# print('Answer: ', answer)

chat = chat_prompt | chat_model | AnswerOutputParser()
result = chat.invoke({'problem': '3x^2 + 2 - 10 = 0'})
print(result)   