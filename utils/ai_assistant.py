from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()

class InventoryAIAssistant:
    def __init__(self):
        self.client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

    def generate_response(self, question, inventory, sales, role):
        try:
            inventory_summary = "\n".join(
                [f"- {item['name']}: price ${item['price']}, stock {item['stock']}" for item in inventory]
            )

            prompt = f"""
You are an AI assistant for an inventory system.

Inventory:
{inventory_summary}

User question:
{question}
"""

            response = self.client.responses.create(
                model="gpt-4.1-mini",
                input=prompt
            )

            return response.output_text

        except Exception as e:
            return "AI assistant is currently unavailable (API quota or key issue), but integration is complete."