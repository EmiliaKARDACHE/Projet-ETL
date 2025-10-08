import requests
import os
import pandas as pd
from dotenv import load_dotenv
from time import sleep

# Load API key
load_dotenv()
API_KEY = os.getenv("SPOONACULAR_API_KEY")

# Folder to save CSV
OUTPUT_CSV = "data/raw/Spoonacular/spoonacular_recipes_sample.csv"

def search_recipes_by_ingredients(ingredients, number=1, ranking=1, ignorePantry=True):
    """
    Search recipes by ingredients using Spoonacular API.
    Produces URL with '+' for spaces and ',' for commas exactly as expected.
    """
    base_url = "https://api.spoonacular.com/recipes/findByIngredients"

    # Join ingredients with ', ' and replace spaces with '+'
    ingredients_str = ", ".join(ingredients)
    ingredients_param = ingredients_str.replace(" ", "+")

    # Manually construct URL
    url = f"{base_url}?ingredients={ingredients_param}&number={number}&apiKey={API_KEY}&includeNutrition=true"

    print("🔗 Request URL:", url)

    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
        print(response.text)
        return []
    except Exception as err:
        print(f"Other error occurred: {err}")
        return []

def get_full_recipe_info(recipe_id):
    """
    Fetch full information about a recipe by ID
    """
    url = f"https://api.spoonacular.com/recipes/{recipe_id}/information"
    params = {"apiKey": API_KEY, "includeNutrition": False}

    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error for recipe {recipe_id}: {http_err}")
        return None
    except Exception as err:
        print(f"Other error for recipe {recipe_id}: {err}")
        return None

def build_dataset(ingredients_list, number_per_search=1):
    """
    Build a dataset CSV from multiple ingredient searches
    """
    all_recipes = []

    for ingredients in ingredients_list:
        print(f"Searching recipes for: {ingredients}")
        search_results = search_recipes_by_ingredients(ingredients, number=number_per_search)

        for r in search_results:
            recipe_id = r.get("id")
            data = get_full_recipe_info(recipe_id)
            if not data:
                continue

            all_recipes.append({
                "id": data.get("id"),
                "title": data.get("title"),
                "image": data.get("image"),
                "imageType": data.get("imageType"),
                "servings": data.get("servings"),
                "readyInMinutes": data.get("readyInMinutes"),
                "cookingMinutes": data.get("cookingMinutes"),
                "preparationMinutes": data.get("preparationMinutes"),
                "license": data.get("license"),
                "sourceName": data.get("sourceName"),
                "sourceUrl": data.get("sourceUrl"),
                "spoonacularSourceUrl": data.get("spoonacularSourceUrl"),
                "healthScore": data.get("healthScore"),
                "spoonacularScore": data.get("spoonacularScore"),
                "pricePerServing": data.get("pricePerServing"),
                "cheap": data.get("cheap"),
                "creditsText": data.get("creditsText"),
                "cuisines": ", ".join(data.get("cuisines", [])),
                "dairyFree": data.get("dairyFree"),
                "diets": ", ".join(data.get("diets", [])),
                "gaps": data.get("gaps"),
                "glutenFree": data.get("glutenFree"),
                "instructions": data.get("instructions"),
                "ketogenic": data.get("ketogenic"),
                "lowFodmap": data.get("lowFodmap"),
                "occasions": ", ".join(data.get("occasions", [])),
                "sustainable": data.get("sustainable"),
                "vegan": data.get("vegan"),
                "vegetarian": data.get("vegetarian"),
                "veryHealthy": data.get("veryHealthy"),
                "veryPopular": data.get("veryPopular"),
                "whole30": data.get("whole30"),
                "weightWatcherSmartPoints": data.get("weightWatcherSmartPoints"),
                "dishTypes": ", ".join(data.get("dishTypes", [])),
                "extendedIngredients": ", ".join([ing.get("original", "") for ing in data.get("extendedIngredients", [])]),
                "usedIngredients": ", ".join([ing.get("original", "") for ing in r.get("usedIngredients", [])]) if r else None,
                "missedIngredients": ", ".join([ing.get("original", "") for ing in r.get("missedIngredients", [])]) if r else None,
                "winePairing": data.get("winePairing", {}).get("pairingText") if data.get("winePairing") else None,
                "pairedWines": ", ".join(data.get("winePairing", {}).get("pairedWines", [])) if data.get("winePairing") else None,
                "productMatches": ", ".join([p.get("title", "") for p in data.get("winePairing", {}).get("productMatches", [])]) if data.get("winePairing") else None,
                "summary": data.get("summary")
            })

            sleep(0.2)  # be gentle with the API

    # Save CSV
    df = pd.DataFrame(all_recipes)
    os.makedirs(os.path.dirname(OUTPUT_CSV), exist_ok=True)
    df.to_csv(OUTPUT_CSV, index=False, encoding="utf-8")
    print(f"✅ {len(df)} recipes saved to {OUTPUT_CSV}")


if __name__ == "__main__":
    # Example: list of ingredient lists to search
    ingredients_list = [
        ["salmon", "lemon", "dill"],
        ["beef", "onion", "garlic"],
        ["pasta", "tomato", "basil"]
    ]
    build_dataset(ingredients_list, number_per_search=1)
