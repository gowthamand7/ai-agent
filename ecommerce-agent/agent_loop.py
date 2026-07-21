from dotenv import load_dotenv
from langsmith import traceable
from langchain_core.messages import SystemMessage, HumanMessage, ToolMessage
from langchain_google_genai import ChatGoogleGenerativeAI
from tools import searchitems, getitems, available_discounts, getreviews, calculate_final_price

load_dotenv()

MAX_ITERATIONS = 10
# We use gemini-3.1-pro to ensure it has strong enough reasoning to loop properly
MODEL = "gemini-3.1-flash-lite"

@traceable(name="E-Commerce Custom Agent Loop")
def run_agent(question: str):
    # 1. Define our specific tools
    tools = [searchitems, getitems, available_discounts, getreviews, calculate_final_price]
    tools_dict = {t.name: t for t in tools}

    # 2. Init LLM and bind tools
    llm = ChatGoogleGenerativeAI(temperature=0, model=MODEL)
    llm_with_tools = llm.bind_tools(tools)

    print(f"Question: {question}")
    print("=" * 60)

    # 3. Setup the initial memory with a strong System Prompt
    messages = [
        SystemMessage(
            content=(
                "You are an expert e-commerce shopping assistant. "
                "You have access to an inventory system through several tools. "
                "STRICT RULES:\n"
                "1. If you don't know an item's ID, use 'searchitems' first to find it.\n"
                "2. When calculating prices, always use the 'calculate_final_price' tool rather than guessing.\n"
                "3. You can call multiple tools at the same time if needed (e.g., getting reviews and discounts simultaneously).\n"
                "4. CRITICAL: Before calling any tools, you MUST first output a brief text explanation of your thought process and what you plan to do next. Do not call a tool without writing your thoughts first!"
            )
        ),
        HumanMessage(content=question),
    ]

    # 4. The ReAct Loop
    for iteration in range(1, MAX_ITERATIONS + 1):
        print(f"\n--- Iteration {iteration} ---")

        # Invoke the LLM
        ai_message = llm_with_tools.invoke(messages)
        
        # We MUST append the AI's message to the memory immediately so it remembers calling the tools
        messages.append(ai_message)

        # Print the LLM's internal thinking to make it interactive!
        if ai_message.content:
            print(f"🤔 [Thinking]:\n{ai_message.content}\n")

        tool_calls = getattr(ai_message, "tool_calls", [])

        # If it didn't call any tools, it means it has arrived at the final answer
        if not tool_calls:
            print("=" * 60)
            print(f"🎉 Final Answer:\n\n{ai_message.content}")
            return ai_message.content

        # Process ALL tool calls concurrently (supports multiple tools in one iteration)
        for tool_call in tool_calls:
            tool_name = tool_call.get("name")
            tool_args = tool_call.get("args", {})
            tool_call_id = tool_call.get("id")

            print(f"🛠️  [Executing Tool]: {tool_name} with args: {tool_args}")

            tool_to_use = tools_dict.get(tool_name)
            if tool_to_use is None:
                observation = f"Error: Tool '{tool_name}' not found"
            else:
                try:
                    observation = tool_to_use.invoke(tool_args)
                except Exception as e:
                    observation = f"Tool Execution Error: {str(e)}"

            print(f"📥 [Tool Result]:\n{observation}\n")

            # Append the result of the tool to the message history so the LLM can read it
            messages.append(
                ToolMessage(content=str(observation), tool_call_id=tool_call_id)
            )

    print("ERROR: Max iterations reached without a final answer")
    return None

if __name__ == "__main__":
    print("🚀 Starting the Custom E-Commerce ReAct Agent!\n")
    # A complex query that requires searching, checking reviews, and calculating final price
    query = "Can you find the best display tablet and highly recomanded laptop ?"
    run_agent(query)