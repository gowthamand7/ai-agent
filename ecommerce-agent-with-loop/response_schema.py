from typing import List, Dict, Any
from pydantic import BaseModel, Field

class MatchingItem(BaseModel):
    """Details of an item that matches the user's query."""
    item_id: str = Field(description="The unique ID of the product.")
    name: str = Field(description="The name of the product.")
    price: float = Field(description="The price of the product.")
    relevance: str = Field(description="A brief explanation of why this item matches the user's request.")

class AgentResponse(BaseModel):
    """The final structured output from the agent."""
    final_answer: str = Field(description="The final comprehensive answer to the user's query.")
    matching_items: List[MatchingItem] = Field(
        description="A list of specific items from the inventory that match the user's needs."
    )
