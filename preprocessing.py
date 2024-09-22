import re
import nltk
from nltk.corpus import stopwords

# Downloading necessary NLTK resources
#nltk.download('punkt')  # Sentence and word tokenization
nltk.download('punkt_tab')
nltk.download('stopwords')  # Stopwords for text cleaning

# Now run your text processing logic

# Preload stopwords
stop_words = set(stopwords.words('english'))

def preprocess_text(text):
    """Cleans the text by removing special characters, digits, and stopwords, while preserving important content."""
    if not isinstance(text, str):
        return ""

    # Remove special characters and digits
    text = re.sub(r'\W+', ' ', text)  # Keeps letters and spaces
    text = re.sub(r'\d+', '', text)  # Removes digits
    
    # Convert to lowercase
    text = text.lower()
    
    # Tokenize the text into words
    words = nltk.word_tokenize(text)
    
    # Remove stopwords while keeping meaningful words
    cleaned_words = [word for word in words if word not in stop_words]
    
    # Reconstruct the cleaned text
    cleaned_text = ' '.join(cleaned_words)
    
    return cleaned_text

# Example usage
if __name__ == "__main__":
    user_input = input("Enter the text to preprocess: ")
    cleaned_text = preprocess_text(user_input)
    print("Cleaned text:", cleaned_text)
