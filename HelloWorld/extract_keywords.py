import openai
import spacy
import mysql.connector

# Load the spaCy language model
nlp = spacy.load("en_core_web_sm")

# Set up the OpenAI API key
openai.api_key = "sk-sk-mykey"


# Set the API parameters
engine = "text-davinci-002"
max_tokens = 3000
n = 1
temperature = 0.7

def load_products():
    """
    Load the products from a MySQL database.
    """
    # Connect to the MySQL database
    cnx = mysql.connector.connect(user='root', password='', port='3306',
                                  host='', database='')
    cursor = cnx.cursor()

    # Define the SQL query to retrieve the products
    query = ("SELECT color FROM tkeesadminshop.shopify_products  group by  color;")

    # Execute the query and fetch the results
    cursor.execute(query)
    rows = cursor.fetchall()

    # Close the database connection
    cursor.close()
    cnx.close()

    # Create a list of Product objects from the results
    products = 'Colors: '
    for row in rows:
        products =  products + row[0] + ', '


    return products

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

# Load the list of products
products = load_products()

while True:
    # Prompt the user to enter a question
    prompt = input("Enter your question (or 'q' to quit): ")
    if prompt.lower() == 'q':
        break
    # Generate a response using the OpenAI API
    prompt = prompt + ",using a natural language as answer, give me a list of  besties colors based on my season and my country and on my list of colors. I leave in USA and my current season is Spring, this is my list of colors: " +products
    print (prompt)
    response = openai.Completion.create(
        engine=engine,
        prompt= prompt ,
        max_tokens=max_tokens,
        n=n,
        temperature=temperature
    )
    print (response.choices[0].text.strip())