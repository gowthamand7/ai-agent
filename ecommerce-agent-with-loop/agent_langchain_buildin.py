from dotenv import load_dotenv
from langsmith import traceable
from langchain.agents import create_agent
from langchain.tools import tool
from tools import searchitems, getitems, available_discounts, getreviews
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import HumanMessage, SystemMessage
from response_schema import AgentResponse

load_dotenv()

llm = ChatGoogleGenerativeAI(temperature=0, model="gemini-3.1-flash-lite")
tool = [searchitems, getitems, available_discounts, getreviews]
agent = create_agent(model=llm, tools=tool, response_format=AgentResponse)
#agent = create_agent(model=llm, tools=tool)

@traceable
def run_agent():
     response = agent.invoke(
          {
           "messages": [
                SystemMessage(content="You are an e-commerce assistant. Use the searchitems tool to find products. Once you have found relevant items, you MUST STOP calling tools and immediately return the final structured response with the matching items."),
                HumanMessage(content = "Can you give me a tablet with best display ? ")
            ]
          }
     )
     print("Final Answer:", response['structured_response'].final_answer)
     print("\n--- Matching Items ---")
     for item in response['structured_response'].matching_items:
        print(f"Product: {item.name} (ID: {item.item_id})")
        print(f"Price: ${item.price}")
        print(f"Why it matches: {item.relevance}\n")

if __name__ == "__main__":
    run_agent()
