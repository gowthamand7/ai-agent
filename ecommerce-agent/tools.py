import json
import os
from typing import Dict, Any, List
from langchain_core.tools import tool

# Helper function to load inventory
def _load_inventory() -> List[Dict[str, Any]]:
    script_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(script_dir, "inventory.json")
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        return []

@tool
def searchitems(query: str, page: int = 1) -> str:
    """
    Search the e-commerce inventory for a given partial string query.
    
    Args:
        query (str): The search term to match against product names, categories, or descriptions.
        page (int): The page number for pagination (returns 10 items per page). Default is 1.
        
    Returns the first 10 matches by default.
    """
    inventory = _load_inventory()
    query_lower = query.lower()
    
    # Simple search across name, category, and description
    results = [
        item for item in inventory 
        if query_lower in item.get("name", "").lower() 
        or query_lower in item.get("description", "").lower()
        or query_lower in item.get("category", "").lower()
    ]
    
    page_size = 100
    total_results = len(results)
    total_pages = (total_results + page_size - 1) // page_size
    
    start_idx = (page - 1) * page_size
    end_idx = start_idx + page_size
    
    paginated_results = results[start_idx:end_idx]
    
    # Return a simplified view of the items to save context tokens
    output = {
        "query": query,
        "page": page,
        "total_results": total_results,
        "total_pages": total_pages,
        "items": [
            {"id": r["id"], "name": r["name"], "price": r["price"]} 
            for r in paginated_results
        ]
    }
    
    return json.dumps(output, indent=2)

@tool
def getitems(item_ids: List[str]) -> str:
    """
    Get detailed information about specific items using their item IDs.
    
    Args:
        item_ids (List[str]): A list of product IDs (e.g., ["prod_001", "prod_002"]) to fetch details for.
        
    Returns name, category, price, and description for each found item.
    """
    inventory = _load_inventory()
    results = []
    
    for item in inventory:
        if item["id"] in item_ids:
            results.append({
                "id": item["id"],
                "name": item["name"],
                "category": item["category"],
                "price": item["price"],
                "description": item["description"]
            })
            
    return json.dumps({"items": results}, indent=2)

@tool
def available_discounts(item_ids: List[str]) -> str:
    """
    Get available discounts for specific items.
    
    Args:
        item_ids (List[str]): A list of product IDs to fetch discounts for.
    """
    inventory = _load_inventory()
    results = []
    
    for item in inventory:
        if item["id"] in item_ids:
            results.append({"id": item["id"], "discounts": item.get("discounts", [])})
            
    return json.dumps({"items": results}, indent=2)

@tool
def getreviews(item_ids: List[str]) -> str:
    """
    Get customer reviews and ratings for specific items.
    
    Args:
        item_ids (List[str]): A list of product IDs to fetch reviews for.
    """
    inventory = _load_inventory()
    results = []
    
    for item in inventory:
        if item["id"] in item_ids:
            results.append({"id": item["id"], "reviews": item.get("reviews", [])})
            
    return json.dumps({"items": results}, indent=2)
