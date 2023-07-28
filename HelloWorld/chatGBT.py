import openai

# Replace "your_api_key" with your actual API key
openai.api_key = "sk-sk-mykey"
while True:
    # Prompt the user to enter a question
    prompt = input("Enter your question (or 'q' to quit): ")
    # Check if the user wants to quit
    if prompt.lower() == 'q':
        break
    # Send the prompt to the OpenAI API
    response = openai.Completion.create(
        engine="text-davinci-002",  # You can use other engines like "text-curie-002" or "text-babbage-002"
        prompt=prompt,
        max_tokens=2000,  # Limit the response length
        n=1,  # Number of responses to generate
        stop=None,  # You can define a stop sequence if needed
        temperature=0.8,  # Controls the randomness of the response
    )

    # Print the generated response
    print(response.choices[0].text.strip())