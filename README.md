# NLP-Text-Analysis
This repository provides a collection of tools and utilities for Natural Language Processing (NLP) text analysis. It includes scripts that perform various NLP tasks such as sentiment analysis, readability assessment, linguistic feature extraction, and text extraction from HTML articles.

## Requirements

- Python 3.x
- pandas
- requests
- beautifulsoup4
- nltk
- textblob

You can install the required dependencies using pip:

```
pip install pandas requests beautifulsoup4 nltk textblob
```

## Usage

1. Clone the repository or download the source code.
2. Prepare an Excel file named `input.xlsx` with columns `URL_ID` and `URL`, where `URL_ID` is the identifier for each URL and `URL` contains the URLs of the HTML articles to extract text from.
3. Run the script:

```
python extract_articles1.py
```

The script will read the `input.xlsx` file, extract the text from the HTML articles, and save the extracted text in individual text files.

4. Run the script for textual analysis:

```
python nltk1.py
```

The script will iterate over each text file, perform NLP text analysis, and calculate various metrics and linguistic features. The results will be saved in an Excel file named `output1.xlsx`.

## Customization

- Adjust the input Excel file name and columns in the code if necessary.
- Customize the metrics and features calculated by modifying the corresponding functions in the `nltk1.py` script.
- Modify the code according to your specific requirements or add additional NLP text analysis functions as needed.

## Limitations

- The code assumes that the HTML articles follow a standard structure and can be extracted using BeautifulSoup.
- The code assumes that the text files are in UTF-8 encoding. If your files have a different encoding, modify the file reading section accordingly.
- This repository provides a basic set of NLP text analysis utilities and text extraction from HTML articles. It may not cover all possible NLP tasks or complex scenarios. Feel free to extend the code and add more functionalities as needed.
