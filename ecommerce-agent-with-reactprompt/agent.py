from dotenv import load_dotenv
from langchain.agents import create_agent
from langchain_google_genai import ChatGoogleGenerativeAI
from tools import searchitems, getitems, available_discounts, getreviews, calculate_final_price

load_dotenv()

MODEL = "gemini-3.1-pro"

def run_react_agent():
    # 1. Define our specific tools
    tools = [searchitems, getitems, available_discounts, getreviews, calculate_final_price]

    # 2. Init LLM
    llm = ChatGoogleGenerativeAI(temperature=0, model=MODEL)

    # 3. Define the ReAct prompt instructions (system_prompt)
    prompt = """You are an expert e-commerce shopping assistant.
You must think step-by-step and write out your reasoning before you act.
You have access to tools for searching items, getting details, discounts, reviews, and calculating final prices.
"""

    # 4. Create the Agent
    # In LangChain 1.3+, create_react_agent was moved and renamed to create_agent in langchain.agents!
    agent = create_agent(model=llm, tools=tools, system_prompt=prompt)

    print("🚀 Starting the LangChain 1.3 create_agent!\n")
    query = "I need a highly rated laptop under $1000. Find the best one, tell me its rating, and calculate its final price after all discounts."
    
    # 5. Invoke the graph (LangGraph uses a 'messages' state)
    response = agent.invoke({"messages": [("user", query)]})
    
    print("\n============================")
    print("FINAL OUTPUT:")
    # The final message in the state is the agent's answer
    print(response["messages"][-1].content)

if __name__ == "__main__":
    run_react_agent()
