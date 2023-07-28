import openai
import re
import json

# Replace 'your_api_key' with your actual OpenAI API key
openai.api_key = "sk-sk-mykey"
# Prepare your prompt
# Prepare your prompt
product_being_purchased = "Flip-Flop"
color_being_purchased = "Black"
colors = ["Brown", "Animal Prints", "Silver - Metalics", "Beach Pearl", "Gold - Metallics", "Black", "Blue", "Gray", "Tan", "Beige", "Cream", "Green", "Orange", "Pink", "Purple", "Red", "Yellow", "White"]
product_types = ["Pant", "LS-Tee", "SS-Tee", "Tank", "Hoodie", "Half Zip", "Sweatpant", "Legging", "Short", "Shirt", "Crewneck", "Jacket", "Bra", "Closed Toe", "Sandal", "Slide", "Flip-Flop", "Jumpsuit", "Turtleneck", "Dress", "Kids-Flip-Flop", "Kids-Crewneck", "Kids-Short", "Kids-SS Tee", "Kids-Sweatpant", "Kids-Hoodie", "Kids-Jumpsuit"]
country = "Canada"
season = "Summer"
prompt = f"A customer in {country} is buying a {color_being_purchased} {product_being_purchased} during the {season}. My store offers products in the following colors: {', '.join(colors)} and product types: {', '.join(product_types)}. Please recommend 5 complementary product types, different from {product_being_purchased}, to complete the look, and suggest the best 5 colors for each product type as a JSON object with keys 'product_type' and 'colors'."

# Call the API
print("API text response:", prompt)

response = openai.Completion.create(
    engine="text-davinci-002",
    prompt=prompt,
    max_tokens=500,
    n=1,
    stop=None,
    temperature=0.7,
)

# Extract the text response
text_response = response.choices[0].text.strip()

# Use a regex pattern to extract product type and color information
pattern = re.compile(r"\"product_type\"\s*:\s*\"(.*?)\",\s*\"colors\"\s*:\s*\[(.*?)\]", re.MULTILINE | re.DOTALL)
matches = pattern.findall(text_response)

# Build the JSON object from the extracted information
recommendations = []
for match in matches:
    product_type = match[0]
    colors = [color.strip() for color in match[1].split(',')]
    recommendation = {
        "product_type": product_type,
        "colors": colors
    }
    recommendations.append(recommendation)

# Ensure there are exactly 5 product type recommendations
while len(recommendations) < 5:
    recommendations.append({"product_type": "", "colors": []})

recommendations = recommendations[:5]

# Ensure there are exactly 5 colors for each product type
for recommendation in recommendations:
    while len(recommendation["colors"]) < 5:
        recommendation["colors"].append("")

    recommendation["colors"] = recommendation["colors"][:5]

# Convert the recommendations list to a JSON string
json_string = json.dumps(recommendations, indent=2)

print("Recommended complementary products in JSON:", json_string)
