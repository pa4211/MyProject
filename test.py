import streamlit as st
import requests
import json
import os
from typing import Dict, Any
from pydantic import BaseConfig

class AzureOpenAIChat:
    def __init__(self):
        self.API_ENDPOINT = st.secrets.get("AZURE_OPENAI_API_ENDPOINT", "")
        self.API_KEY = st.secrets.get("AZURE_OPENAI_API_KEY", "")

    def generate_response(self, query: str, max_tokens: int = 2000)->Dict[str, Any]:
        """Generate response from Azure OpenAI"""
        headers = {
            "Content-Type": "application/json",
            "api-key": self.API_KEY,
        }

        data = {
            "messages": [{"role": "user", "content": query}],
            "max_tokens": max_tokens,
            "temperature": 0.7,
            "top_p": 1,
            "frequency_penalty": 0,
            "presence_penalty": 0,
        
            
        }
        response = requests.post(self.API_ENDPOINT, headers=headers, json=data)
        response.raise_for_status()  # Automatically raises an error for HTTP issues
        return response.json()
    
def main():
        st.set_page_config(page_title="Azure OpenAI Chat", page_icon="💬")
        st.title("AI-Powered Healthy Recipe Generator 🍲")
        ingredients = st.text_input("Enter ingredients")
        time=st.text_input("time")
        fat= st.text_input("fat%")
        calories = st.text_input("calories")
        if st.button("Generate Recipe"):
            # Dynamically create the OpenAI prompt
            prompt = f"""
            Create two healthy recipes using the following constraints:
            ingredients: {ingredients}.
            cookingtime : {time}
            fat: {fat}
            calories: {calories}
            Provide a simple step-by-step Indian only recipe 
            Format strictly in json as a list of dictionaries, with the following keys 
            :"name", "ingredient",  "fat", "cookingtime", "calories", "instructions"
            """
            chat_client = AzureOpenAIChat()
            response = chat_client.generate_response(prompt)
            st.subheader("AI-Generated Recipe")
            #recipe_content = response["choices"][0]["message"]["content"]
            recipe_content = response["choices"][0]["message"]["content"]
            recipe_content = recipe_content.replace("```json", "").replace("```", "").strip()
            recipe_json = json.loads(recipe_content)
            #recipe_json0 = recipe_json[0] 
            #recipe_json1 = recipe_json[1] #recipe_json = recipe_json[] 
            #st.write(recipe_json0.get("name", "N/A"))
            #st.write(recipe_json1.get("name", "N/A"))
            for recipe in recipe_json:
                st.write(recipe.get("name", "N/A"))
                st.write(str(recipe.get("ingredient", "N/A")))
                st.write(recipe.get("fat", "N/A"))
                st.write(recipe.get("cookingtime", "N/A"))
                st.write(recipe.get("calories", "N/A"))
                st.write(str(recipe.get("instructions", "N/A")))
                st.write("\n")
            #st.write(recipe_json) # Use .get() to avoid errors if "fat" is missing
            st.table(recipe_json)
            st.write(recipe_json)
        
# Display the fat content
            #st.write(f"Fat Content: {fat_content}")
            #data= json.loads(recipe_content)
            #df = pd.DataFrame(data)

if __name__ == "__main__":
    main()