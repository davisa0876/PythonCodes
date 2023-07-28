import openai

# Set up the OpenAI API key
openai.api_key = "sk-sk-mykey"

# Define the prompt based on customer input
prompt = "I am looking for a new pair of running shoes. Can you recommend a list of 10 good options?"

# Set the API parameters
engine = "text-davinci-002"
max_tokens = 100
n = 1
temperature = 0.7

# Send the prompt to the API and get the generated response
response = openai.Completion.create(
    engine=engine,
    prompt=prompt,
    max_tokens=max_tokens,
    n=n,
    temperature=temperature
)

# Extract the recommended products from the response
recommended_products = response.choices[0].text.strip()

# Display the recommended products to the customer
print("Here are some running shoes we think you'll like: " + recommended_products)