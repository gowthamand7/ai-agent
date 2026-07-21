import json
import random
import os

def generate_inventory():
    categories = ["Laptop", "Mobile", "TV", "Headphones", "Tablet", "Smartwatch", "Camera", "Speaker"]
    brands = ["TechCorp", "GigaByte", "Sonic", "ViewMaster", "PixelCraft", "AudioMax", "Cyborg", "Nova"]
    adjectives = ["Pro", "Max", "Ultra", "Lite", "Plus", "Essential", "Elite", "Advanced"]
    
    inventory = []
    
    for i in range(1, 101):
        category = random.choice(categories)
        brand = random.choice(brands)
        adjective = random.choice(adjectives)
        name = f"{brand} {category} {adjective} {random.randint(1, 15)}"
        
        # Price ranges based on category
        if category in ["Laptop", "TV"]:
            price = round(random.uniform(500, 2500), 2)
        elif category in ["Mobile", "Tablet", "Camera"]:
            price = round(random.uniform(300, 1200), 2)
        else:
            price = round(random.uniform(50, 300), 2)
            
        discounts = []
        if random.random() > 0.5:
            discounts.append("10% off for members")
        if random.random() > 0.8:
            discounts.append(f"Save ${random.randint(10, 50)} at checkout")
            
        reviews = []
        num_reviews = random.randint(0, 5)
        for _ in range(num_reviews):
            reviews.append({
                "user": f"User{random.randint(100, 999)}",
                "rating": random.randint(1, 5),
                "comment": random.choice([
                    "Great product!", "Not worth the price.", "Highly recommended.", 
                    "Battery life could be better.", "Amazing display.", "Just okay."
                ])
            })
            
        item = {
            "id": f"prod_{i:03d}",
            "name": name,
            "category": category,
            "price": price,
            "description": f"A high-quality {category.lower()} manufactured by {brand}, featuring the latest {adjective.lower()} technologies.",
            "discounts": discounts,
            "reviews": reviews
        }
        
        inventory.append(item)
        
    script_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(script_dir, "..", "inventory.json")
    
    with open(file_path, 'w', encoding='utf-8') as f:
        json.dump(inventory, f, indent=2)
        
    print(f"Generated {len(inventory)} items in {file_path}")

if __name__ == "__main__":
    generate_inventory()
