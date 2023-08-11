import nltk
from better_profanity import profanity
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import requests
import webbrowser

# Download required resources from NLTK
# nltk.download('stopwords')
# nltk.download('punkt')

# Initialize better_profanity
profanity.load_censor_words()


# Function to fetch website content
def get_website_content(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.text
    else:
        return None

def detect_cyberbullying(text):
    # Tokenize the text and remove punctuation
    words = word_tokenize(text)
    words = [word for word in words if word.isalpha()]

    # Remove stopwords
    stop_words = set(stopwords.words('english'))
    words = [word for word in words if word not in stop_words]

    # Check for profanity and cyberbullying terms
    for word in words:
        if profanity.contains_profanity(word):
            return True  # Detected profanity

    return False  # No cyberbullying detected


# URL of the website to scan
website_url = "https://pypi.org/project/better-profanity/"

# Fetch website content
content = get_website_content(website_url)

# Check for cyberbullying in the website content
if content:
    if detect_cyberbullying(content):
        print("Cyberbullying detected on the website:", website_url)
        # Redirect the user to cybercrime.gov.in
        webbrowser.open("https://cybercrime.gov.in/Webform/Crime_AuthoLogin.aspx")
    else:
        print("No cyberbullying detected on the website:", website_url)
else:
    print("Failed to fetch website content.")

# Test the function with a sample text
#text = "all the best"
#if detect_cyberbullying(text):
 #   print("Cyberbullying detected.")
    # Redirect the user to cybercrime.gov.in
  #  webbrowser.open("https://cybercrime.gov.in")
#else:
   # print("No cyberbullying detected.")
