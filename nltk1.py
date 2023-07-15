import os
import sys
import traceback
import pandas as pd
import nltk
from textblob import TextBlob
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.stem import WordNetLemmatizer


def calculate_positive_score(text):
    blob = TextBlob(text)
    return blob.sentiment.polarity


def calculate_negative_score(text):
    blob = TextBlob(text)
    return -blob.sentiment.polarity


def calculate_polarity_score(text):
    blob = TextBlob(text)
    return blob.sentiment.polarity


def calculate_subjectivity_score(text):
    blob = TextBlob(text)
    return blob.sentiment.subjectivity


def calculate_avg_sentence_length(text):
    sentences = sent_tokenize(text)
    total_words = sum(len(word_tokenize(sentence)) for sentence in sentences)

    # Check if there are no sentences
    if len(sentences) == 0:
        return 0

    return total_words / len(sentences)


def calculate_percentage_complex_words(text):
    words = word_tokenize(text)
    complex_words = [word for word in words if syllable_count(word) > 2]

    # Check if there are no words
    if len(words) == 0:
        return 0

    return (len(complex_words) / len(words)) * 100


def calculate_fog_index(text):
    sentences = sent_tokenize(text)
    total_words = sum(len(word_tokenize(sentence)) for sentence in sentences)
    total_sentences = len(sentences)
    complex_words = [word for word in word_tokenize(text) if syllable_count(word) > 2]
    total_complex_words = len(complex_words)

    # Check if the denominator is zero
    if total_sentences == 0 or total_words == 0:
        return 0

    return 0.4 * ((total_words / total_sentences) + (100 * (total_complex_words / total_words)))



def calculate_avg_words_per_sentence(text):
    sentences = sent_tokenize(text)
    words = word_tokenize(text)

    # Check if there are no sentences
    if len(sentences) == 0:
        return 0

    return len(words) / len(sentences)



def calculate_complex_word_count(text):
    words = word_tokenize(text)
    complex_words = [word for word in words if syllable_count(word) > 2]
    return len(complex_words)


def calculate_word_count(text):
    words = word_tokenize(text)
    return len(words)


def syllable_count(word):
    count = 0
    vowels = 'aeiouy'

    # Convert word to lowercase for consistent matching
    word = word.lower()

    # If word is empty, return 0
    if len(word) == 0:
        return 0

    # Check if the word ends with 'e' and remove it for syllable counting
    if word.endswith('e'):
        word = word[:-1]

    # If the word ends with 'le', it is counted as one syllable
    if word.endswith('le') and len(word) > 2 and word[-3] not in vowels:
        count += 1

    # If word ends with 'y' and has at least one character before it, consider it as a syllable
    if word.endswith('y') and len(word) > 1 and word[-2] not in vowels:
        count += 1

    # Count the number of vowel sequences in the word
    prev_char_vowel = False
    for char in word:
        if char in vowels:
            if not prev_char_vowel:
                count += 1
            prev_char_vowel = True
        else:
            prev_char_vowel = False

    # Adjust the count based on special cases

    # If the word starts with 'mc', 'mc' is considered as one syllable
    if word.startswith('mc') and len(word) > 2 and word[2] not in vowels:
        count -= 1

    # If the word starts with 'coo', 'coo' is considered as one syllable
    if word.startswith('coo') and len(word) > 3 and word[3] not in vowels:
        count -= 1

    return count


def count_personal_pronouns(text):
    pronouns = ['i', 'me', 'my', 'mine', 'we', 'us', 'our', 'ours']
    words = word_tokenize(text.lower())
    personal_pronouns = [word for word in words if word in pronouns]
    return len(personal_pronouns)


def calculate_avg_word_length(text):
    words = word_tokenize(text)
    total_length = sum(len(word) for word in words)
    return total_length / len(words)


# Define the folder path where the text files are located
folder_path = "C:\Extracted text\extracted_text"

# Initialize the output dataframe
df_output = pd.DataFrame(columns=['Text File', 'POSITIVE SCORE', 'NEGATIVE SCORE', 'POLARITY SCORE',
                                  'SUBJECTIVITY SCORE', 'AVG SENTENCE LENGTH', 'PERCENTAGE OF COMPLEX WORDS',
                                  'FOG INDEX', 'AVG NUMBER OF WORDS PER SENTENCE', 'COMPLEX WORD COUNT',
                                  'WORD COUNT', 'SYLLABLE PER WORD', 'PERSONAL PRONOUNS',
                                  'AVG WORD LENGTH'])
def sort_by_filename(file_name):
    file_number = int(file_name.split('.')[0])
    return file_number
for file_name in sorted(os.listdir(folder_path), key=sort_by_filename):
    if file_name.endswith('.txt'):
        file_path = os.path.join(folder_path, file_name)

        try:
            # Read the text file
            with open(file_path, 'r', encoding='utf-8') as file:
                text = file.read()

            # Perform textual analysis
            if len(text) > 0:
                print(f"Processing file: {file_name}")
                print(f"Text length: {len(text)}")

                try:
                     positive_score = calculate_positive_score(text)
                     negative_score = calculate_negative_score(text)
                     polarity_score = calculate_polarity_score(text)
                     subjectivity_score = calculate_subjectivity_score(text)
                     avg_sentence_length = calculate_avg_sentence_length(text)
                     percentage_complex_words = calculate_percentage_complex_words(text)
                     fog_index = calculate_fog_index(text)
                     avg_words_per_sentence = calculate_avg_words_per_sentence(text)
                     complex_word_count = calculate_complex_word_count(text)
                     word_count = calculate_word_count(text)
                     words = word_tokenize(text)
                     word_count = len(words)

# Calculate syllable_per_word
                     syllable_per_word = sum(syllable_count(word) for word in words) / word_count if word_count != 0 else 0

# Calculate personal_pronouns
                     personal_pronouns = count_personal_pronouns(text)

# Calculate avg_word_length
                     avg_word_length = sum(len(word) for word in words) / len(words) if len(words) != 0 else 0


                # Add the computed values to the output dataframe
                     df_output = pd.concat([df_output, pd.DataFrame({
                'Text File': [file_name],
                'POSITIVE SCORE': [positive_score],
                'NEGATIVE SCORE': [negative_score],
                'POLARITY SCORE': [polarity_score],
                'SUBJECTIVITY SCORE': [subjectivity_score],
                'AVG SENTENCE LENGTH': [avg_sentence_length],
                'PERCENTAGE OF COMPLEX WORDS': [percentage_complex_words],
                'FOG INDEX': [fog_index],
                'AVG NUMBER OF WORDS PER SENTENCE': [avg_words_per_sentence],
                'COMPLEX WORD COUNT': [complex_word_count],
                'WORD COUNT': [word_count],
                'SYLLABLE PER WORD': [syllable_per_word],
                'PERSONAL PRONOUNS': [personal_pronouns],
                'AVG WORD LENGTH': [avg_word_length]
                })], ignore_index=True)
                except Exception as e:
                    print(f"Error occurred while processing file: {file_name}")
                    print(f"Error message: {str(e)}")
                    print("Traceback:", traceback.format_exc())
            else:
                print(f"Empty text file: {file_name}")
        except Exception as e:
            print(f"Error occurred while processing file: {file_name}")
            print(f"Error message: {str(e)}")

# Save the output dataframe to an Excel file
df_output.to_excel('output1.xlsx', index=False)
