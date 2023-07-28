import openai
import spacy
import mysql.connector

nlp = spacy.load("en_core_web_sm")

class Product:
    def __init__(self, product_id, title, vendor, product_type, color, inventory_quantity, price):
        self.product_id = product_id
        self.title = title
        self.vendor = vendor
        self.product_type = product_type
        self.color = color
        self.inventory_quantity = inventory_quantity
        self.price = price

    def __repr__(self):
        return f"Product({self.product_id}, {self.title}, {self.vendor}, {self.product_type}, {self.color}, {self.inventory_quantity}, {self.price})"

def extract_keywords(text):
    """
    Extract relevant keywords from the customer prompt using spaCy NLP library.
    """
    # Create a spaCy doc object from the customer prompt
    doc = nlp(text)

    # Extract named entities from the doc object
    named_entities = [ent.text for ent in doc.ents if ent.label_ == "PRODUCT" or ent.label_ == "ORG"]

    # Extract noun chunks from the doc object
    noun_chunks = [chunk.text for chunk in doc.noun_chunks]

    # Combine named entities and noun chunks into a list of keywords
    keywords = named_entities + noun_chunks

    # Return the list of keywords
    return keywords


def load_products():
    """
    Load the products from a MySQL database.
    """
    # Connect to the MySQL database
    cnx = mysql.connector.connect(user='root', password='', port='3306',
                                  host='', database='')
    cursor = cnx.cursor()

    # Define the SQL query to retrieve the products
    query = ("SELECT product_id, title, vendor, product_type, color, sum(inventory_quantity) total, price  FROM tkeesadminshop.shopify_products  group by product_id, title, vendor, product_type, color, price;")

    # Execute the query and fetch the results
    cursor.execute(query)
    rows = cursor.fetchall()

    # Create a list of Product objects from the results
    products = []
    for row in rows:
        product = Product(row[0], row[1], row[2], row[3], row[4], row[5], row[6])
        products.append(product)

    # Close the database connection
    cursor.close()
    cnx.close()

    return products

def format_products(products):
    """
    Format the list of products into a comma-separated string of product names.
    """
    product_names = [product.title for product in products]
    product_list = ", ".join(product_names)
    return product_list

def filter_products(keywords):
    """
    Filter the products in your store based on the extracted keywords.
    """
    # Load the products from your database or data structure
    products = load_products()
    # Filter the products based on the keywords
    filtered_products = []
    for product in products:
        if any(keyword in product.title.lower() or keyword in product.title.lower() for keyword in keywords):
            filtered_products.append(product)

    return filtered_products


# Set up the OpenAI API key
openai.api_key = "sk-sk-mykey"


# Set the API parameters
engine = "text-davinci-002"
max_tokens = 3000
n = 1
temperature = 1

# Send the product list as the prompt to the ChatGPT API and get the generated response



while True:
    # Prompt the user to enter a question
    prompt = input("Enter your question (or 'q' to quit): ")
    # Check if the user wants to quit
    if prompt.lower() == 'q':
        break
    # Send the prompt to the OpenAI API

    # Extract relevant keywords from the prompt using NLP techniques
    keywords = extract_keywords(prompt)

    # Filter the products in your store based on the relevant keywords
    filtered_products = filter_products(keywords)

    # Convert the filtered products to a format suitable for the ChatGPT API
    product_list = format_products(filtered_products)

    response = openai.Completion.create(
        engine=engine,
        prompt=prompt + "I leave in Canada and now we are in spring. So based on my country and the current season and Using this list of products: " + product_list,
        max_tokens=max_tokens,
        n=n,
        temperature=temperature
    )
    # Print the generated response
    print(response.choices[0].text.strip())



# Extract the recommended products from the response
#recommended_products = response.choices[0].text.strip()

# Display the recommended products to the customer
#print("Here are some products we think you'll like: " + recommended_products)