from dotenv import load_dotenv
from langsmith import traceable
from langchain.agents import create_agent
from langchain.tools import tool
from langchain_core.messages import HumanMessage
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_openrouter import ChatOpenRouter
from search import search_tool
from response_schema import AgentResponse

load_dotenv()

llm = ChatGoogleGenerativeAI(temperature=0, model="gemini-3.1-flash-lite")
#llm = ChatOpenRouter(temperature=0, model="openrouter/free")
tool = [search_tool]
agent = create_agent(model=llm, tools=tool, response_format=AgentResponse)

@traceable
def main():
        print("Hello from langchain search agent")
        result = agent.invoke(
              {
                    "messages": HumanMessage(
                          content="What are the latest AI news today?"
                    )
              }
        )
        print(result)


if __name__ == "__main__":
    main()