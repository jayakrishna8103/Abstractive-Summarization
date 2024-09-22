from transformers import pipeline
import warnings
import os
from preprocessing import preprocess_text  # Import your preprocessing function

# Suppress TensorFlow logging (info and warning)
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
warnings.filterwarnings("ignore")

# Initialize the summarization pipeline with a specific model
summarizer = pipeline("summarization", model="sshleifer/distilbart-cnn-12-6")

def summarize_text(text, max_length=200, min_length=50):
    # Generate the summary using the model
    summary = summarizer(
        text,
        max_length=max_length,
        min_length=min_length,
        do_sample=False,
        clean_up_tokenization_spaces=True
    )
    return summary[0]['summary_text']

def generate_abstractive_summary(text):
    # Call the summarize_text function to get the summary
    return summarize_text(text)

def post_process_summary(summary):
    # Improve the summary clarity and reduce redundancy
    sentences = summary.split('. ')
    unique_sentences = list(dict.fromkeys(sentences))  # Remove duplicates while maintaining order

    # Join the processed summary sentences
    final_summary = '. '.join(unique_sentences).strip()

    # Capitalize the first letter and ensure it ends with a period
    if final_summary:
        final_summary = final_summary[0].capitalize() + final_summary[1:]
        if not final_summary.endswith('.'):
            final_summary += '.'

    return final_summary

if __name__ == "__main__":
    text = input("Enter the text you want to summarize: ")
    cleaned_text = preprocess_text(text)  # Use your preprocessing function here
    summary = generate_abstractive_summary(cleaned_text)
    processed_summary = post_process_summary(summary)
    print("\nSummary:")
    print(processed_summary)
