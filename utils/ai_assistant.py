from openai import OpenAI


class InventoryAIAssistant:
    def __init__(self):
        self.client = OpenAI()

    def generate_response(self, question, inventory, sales, role):
        inventory_summary = "\n".join(
            [f"- {item['name']}: price ${item['price']}, stock {item['stock']}" for item in inventory]
        )

        sales_summary = "\n".join(
            [f"- {sale.get('item_name')}: quantity {sale.get('quantity')}, employee {sale.get('employee')}" for sale in sales]
        )

        prompt = f"""
You are an AI assistant for a small business inventory app.

User role: {role}

Current inventory:
{inventory_summary}

Recent sales:
{sales_summary}

Answer the user's question using the inventory and sales data.
Give practical business advice about stock, sales, or restocking.
If the question is unrelated, redirect them back to inventory management.

User question:
{question}
"""

        response = self.client.responses.create(
            model="gpt-4.1-mini",
            input=prompt
        )

        return response.output_text