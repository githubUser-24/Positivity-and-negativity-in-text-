from nltk.tokenize import sent_tokenize
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import tkinter as tk

# Function to perform sentiment analysis
def perform_sentiment_analysis():
    # Get the user input from the text entry widget
    user_input = text_entry.get()

    # Text Summarization using NLTK
    sentences = sent_tokenize(user_input)
    num_sentences = 2  # Set the number of sentences for the summary
    important_sentences = sentences[:num_sentences]
    summary = ' '.join(important_sentences)

    # Sentiment Analysis using VADER
    analyzer = SentimentIntensityAnalyzer()
    sentiment_scores = analyzer.polarity_scores(user_input)
    compound_score = sentiment_scores['compound']

    # Determine sentiment label and accuracy
    if compound_score >= 0.05:
        sentiment = "Positive"
        color = "green"
        accuracy = f"{compound_score * 100:.2f}%"
        sentiment_label_text = "Good"
    elif compound_score <= -0.05:
        sentiment = "Negative"
        color = "red"
        accuracy = f"{-compound_score * 100:.2f}%"
        sentiment_label_text = "Bad"
    else:
        sentiment = "Neutral"
        color = "gray"
        accuracy = "N/A"
        sentiment_label_text = "Neutral"

    # Update labels in the GUI with the sentiment analysis results
    sentiment_label.config(text=f"Sentiment: {sentiment} ({sentiment_label_text})", fg=color)
    text_summary.delete(1.0, tk.END)  # Clear previous summary
    text_summary.insert(tk.END, summary)
    sentiment_result_label.config(text=f"Sentiment Analysis Result: {sentiment} (Accuracy: {accuracy})")

    # Print results to the console
    print("\nSentiment Analysis:")
    print("Sentiment Score:", sentiment_scores)
    print("Sentiment:", sentiment)
    print("Accuracy:", accuracy)

# Create a GUI window
root = tk.Tk()
root.title("Sentiment Analysis")

# Create a label and entry for user input
input_label = tk.Label(root, text="Enter a Sentence:")
input_label.pack()

text_entry = tk.Entry(root, width=50)
text_entry.pack()

# Create a button to trigger sentiment analysis
analyze_button = tk.Button(root, text="Analyze", command=perform_sentiment_analysis)
analyze_button.pack()

# Create labels to display sentiment and summary
sentiment_label = tk.Label(root, text="Sentiment:", font=("Times new roman", 14))
sentiment_label.pack()
summary_label = tk.Label(root, text="Text Summary:", font=("Times new Roman", 12))
summary_label.pack()

# Create a text box to display the text summary
text_summary = tk.Text(root, height=10, width=50)
text_summary.pack()

# Display sentiment analysis results in the GUI
sentiment_result_label = tk.Label(root, text="Sentiment Analysis Result:", font=("Times new roman", 12))
sentiment_result_label.pack()

# Create a function to close the GUI
def close_window():
    root.destroy()

# Create a button to close the GUI
exit_button = tk.Button(root, text="Exit", command=close_window)
exit_button.pack()

# Display the GUI
root.mainloop()
