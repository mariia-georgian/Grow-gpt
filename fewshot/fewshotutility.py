import os
from langchain import PromptTemplate
from langchain.prompts.few_shot import FewShotPromptTemplate
from langchain.chat_models import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
from llamaapi import LlamaAPI
from langchain_experimental.llms import ChatLlamaAPI

LLAMA_API_KEY = ""
OPENAI_KEY = ""


class FewShotUtility:

    def __init__(self, examples, prefix, suffix, input_variables, example_template, example_variables):
        self.examples = examples
        self.prefix = prefix
        self.suffix = suffix
        self.input_variables = input_variables
        self.example_template = example_template
        self.example_variables = example_variables

    def get_prompt(self, question):
        prompt_template = FewShotPromptTemplate(
            examples=self.examples,
            example_prompt=self.get_prompt_template(),
            prefix=self.prefix,
            suffix=self.suffix,
            input_variables=self.input_variables
        )
        prompt = prompt_template.format(question=question)
        return prompt

    def get_prompt_template(self):
        example_prompt = PromptTemplate(
            input_variables=self.example_variables,
            template=self.example_template
        )
        return example_prompt

    @staticmethod
    def send_prompt_llama(prompt):
        llama = LlamaAPI(LLAMA_API_KEY)
        model = ChatLlamaAPI(client=llama)
        prompt_template = ChatPromptTemplate.from_template(prompt)
        message = prompt_template.format_messages()
        response = model(message)
        return response.content

    @staticmethod
    def send_prompt_gpt(prompt):
        prompt_template = ChatPromptTemplate.from_template(prompt)
        message = prompt_template.format_messages()
        llm = ChatOpenAI(model_name='gpt-4', temperature=0, openai_api_key=OPENAI_KEY)
        response = llm(message)
        return response.content