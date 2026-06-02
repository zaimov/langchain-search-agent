from typing import List
from pydantic import BaseModel, Field
from dotenv import load_dotenv

load_dotenv()
from langchain.agents import create_agent
from langchain.tools import tool
from langchain_core.messages import HumanMessage
from langchain_openai import ChatOpenAI
from langchain_tavily import TavilySearch

class Source(BaseModel):
    """Scheme for a source used by the agent"""
    url:str = Field(description="The URL of the source")

class AgentResponse(BaseModel):
    """Scheme for agent reponse with answer and sources"""

    answer:str = Field(description="The agent's answer to the query")
    sources:List[Source] = Field(default_factory=list, description="The sources used by the agent to answer the query")

llm = ChatOpenAI(model="gpt-5")
tools = [TavilySearch()]
agent = create_agent(model=llm, tools=tools, response_format=AgentResponse)

def main():
    print("Hello from langchain-search-engine!")
    result = agent.invoke({"messages":HumanMessage(content="What is the weather in New York?")})
    print(result)


if __name__ == "__main__":
    main()
