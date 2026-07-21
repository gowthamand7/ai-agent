from typing import List

from pydantic import BaseModel, Field

class Source(BaseModel):
    """Schema for a source used by the agent"""
    url: str = Field(description="The URL of the source.")

class AgentResponse(BaseModel):
    """Schema for the final response of the search agent"""
    answer: str = Field(description="The final answer to the user's query.")
    sources: List[Source] = Field(description="A list of sources used to formulate the answer.")
