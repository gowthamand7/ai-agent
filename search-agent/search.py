from dotenv import load_dotenv
from langchain_tavily import TavilySearch

load_dotenv()

# Create the Tavily Search Tool
# We can configure max_results and other properties based on what we need.
search_tool = TavilySearch(
    max_results=100,
    search_depth="advanced", # options are "basic" or "advanced"
)

if __name__ == "__main__":
    # A simple test to verify the tool works
    query = "What are the latest AI news today?"
    print(f"Running search for: '{query}'\n")
    
    try:
        results = search_tool.invoke({"query": query})
        
        for i, result in enumerate(results, 1):
            print(f"Result {i}:")
            print(f"URL: {result.get('url')}")
            print(f"Content: {result.get('content')}\n")
    except Exception as e:
        print(f"Error running search: {e}")
        print("Please ensure your TAVILY_API_KEY is correctly set in your root .env file.")
