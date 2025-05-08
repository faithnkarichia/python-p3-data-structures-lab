spicy_foods = [
    {
        "name": "Green Curry",
        "cuisine": "Thai",
        "heat_level": 9,
    },
    {
        "name": "Buffalo Wings",
        "cuisine": "American",
        "heat_level": 3,
    },
    {
        "name": "Mapo Tofu",
        "cuisine": "Sichuan",
        "heat_level": 6,
    },
]


print("\nget_names()\n")
def get_names(spicy_foods):
    
#     food_names=[]
#     for food in spicy_foods:
#         food_name=food["name"]
#         food_names.append(food_name)
#     return food_names
# print(get_names(spicy_foods))
 food_names=[food["name"]for food in spicy_foods]
 return food_names



print("\nget_spiciest_foods()\n")
def get_spiciest_foods(spicy_foods):
#     very_spicy_foods=[]
#     for food in spicy_foods:
        
        
#         if(food["heat_level"] > 5):
            
#             very_spicy_foods.append(food)
            
#     return very_spicy_foods
# print(get_spiciest_foods(spicy_foods))
 very_spicy_foods=[food for food in spicy_foods if food["heat_level"]>5 ]
 return very_spicy_foods

    
print("\nprint_spicy_foods()\n")
def print_spicy_foods(spicy_foods):
    
    for food in spicy_foods:
      
        print(f"{food.get('name', 'Unknown')} ({food.get('cuisine', 'Unknown')}) | Heat Level: {'🌶' * food.get('heat_level', 0)}")
print(print_spicy_foods(spicy_foods))



    
print("\nget_spicy_food_by_cuisine()\n")
def get_spicy_food_by_cuisine(spicy_foods, cuisine):
   
    for food in spicy_foods:
        if(food["cuisine"]==cuisine):
            return food
    return None
           
print(get_spicy_food_by_cuisine(spicy_foods, "American"))
            


print("\nprint_spiciest_foods()\n")
def print_spiciest_foods(spicy_foods):
    matching_foods = []
    for food in spicy_foods:
        
        if food["heat_level"] > 5:
            matching_foods.append(food)  

    for food in matching_foods:  
        heat_level = food["heat_level"]
        heat_level_with_pepper = "🌶" * heat_level
        print(f"{food['name']} ({food['cuisine']}) | Heat Level: {heat_level_with_pepper}")
print_spiciest_foods(spicy_foods)
    
    

print("\nget_average_heat_level()\n")
def get_average_heat_level(spicy_foods):
      if not spicy_foods:
        return 0  
    
      total_heat = sum(food.get("heat_level", 0) for food in spicy_foods) 
      return total_heat / len(spicy_foods)


     
print(get_average_heat_level(spicy_foods))



print("\ncreate_spicy_food()\n")
def create_spicy_food(spicy_foods, spicy_food):
    spicy_foods.append(spicy_food)
    return spicy_foods
print(create_spicy_food(spicy_foods,   {
        'name': 'Griot',
        'cuisine': 'Haitian',
        'heat_level': 10,
    }))
