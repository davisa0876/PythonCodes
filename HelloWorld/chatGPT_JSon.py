import openai

# Replace 'your_api_key' with your actual OpenAI API key
openai.api_key = "sk-sk-mykey"

# Prepare your prompt
product_being_purchased = "Hoodie"
color_being_purchased = "Black"
colors = ["Brown", "Animal Prints", "Silver - Metalics", "Beach Pearl", "Gold - Metallics", "Black", "Blue", "Gray", "Tan", "Beige", "Cream", "Green", "Orange", "Pink", "Purple", "Red", "Yellow", "White"]
product_types = ["Gift Cards", "Pant", "LS-Tee", "SS-Tee", "Tank", "Hoodie", "Half Zip", "Sweatpant", "Legging", "Short", "Shirt", "Crewneck", "Jacket", "Bra", "Closed Toe", "Sandal", "Slide", "Flip-Flop", "Jumpsuit", "Turtleneck", "Dress", "Kids-Flip-Flop", "Kids-Crewneck", "Kids-Short", "Kids-SS Tee", "Kids-Sweatpant", "Kids-Hoodie", "Kids-Jumpsuit"]
country = "USA"
season = "Spring"
prompt = f"A customer in {country} is buying {product_being_purchased} {color_being_purchased} during the {season}. My store offers products in the following colors: {', '.join(colors)} and product types: {', '.join(product_types)}. Please recommend a 2 complementary product type to complete the look, and suggest the best 2 colors a for each product type as a JSON object with keys 'product_type' and 'colors'."
print(prompt)
# Call the API
response = openai.Completion.create(
    engine="text-davinci-002",
    prompt=prompt,
    max_tokens=500,
    n=1,
    stop=None,
    temperature=0.8,
)
# Extract the recommendation JSON from the response
json_string = response.choices[0].text.strip()
print(json_string)
