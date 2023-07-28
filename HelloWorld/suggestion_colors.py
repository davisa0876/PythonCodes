import openai
import spacy

# Load the spaCy language model
nlp = spacy.load("en_core_web_sm")

# Set up the OpenAI API key
openai.api_key = "sk-"

# Set the API parameters
engine = "text-davinci-002"
max_tokens = 3000
n = 1
temperature = 0.7


def load_products():
    """
    Load the products from your data source.
    """
    # Replace this with your actual data source
    # For this example, I'm using a list of colors
    colors = ["red", "blue", "green", "yellow", "pink", "purple", "orange", "brown", "black", "white"]

    # Return the list of colors as a string
    return ", ".join(colors)


def extract_location(text):
    """
    Extract the user's location from their input using spaCy.
    """
    # Define the spaCy entities to search for
    location_entities = ['GPE', 'LOC']

    # Parse the input text with spaCy
    doc = nlp(text)

    # Extract named entities from the text
    entities = [ent for ent in doc.ents if ent.label_ in location_entities]

    # Extract the most common entity (assumed to be the user's location)
    if entities:
        location = max(set(entities), key=entities.count).text
        return location
    else:
        return None


def get_outfit_suggestions(prompt, location, season):
    """
    Get outfit suggestions based on the user's input, location, and season.
    """
    products = load_products()
    prompt = f"{prompt} Please suggest a suitable outfit for the {season} season in {location}, considering the following colors: {products}."

    response = openai.Completion.create(
        engine=engine,
        prompt=prompt,
        max_tokens=max_tokens,
        n=n,
        temperature=temperature
    )
    return response.choices[0].text.strip()


while True:
    # Prompt the user to enter a question
    prompt = input("Enter your question (or 'q' to quit): ")
    location = input("Enter your country: ")
    season   = input("Enter the current season (Spring, Summer, Fall, or Winter): ")

    # Get outfit suggestions
    suggestions = get_outfit_suggestions(prompt, location, season)
    print(suggestions)
