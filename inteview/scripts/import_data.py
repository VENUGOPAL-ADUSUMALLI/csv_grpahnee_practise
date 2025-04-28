import pandas as pd
from inteview.models import Book

# Read CSV file into a DataFrame
csv_file_path = 'books.csv'

df = pd.read_csv(csv_file_path, on_bad_lines="skip")

# Iterate through the DataFrame and create Book instances
for index, row in df.iterrows():
    book = Book(
        title=row['title'],
        authors=row['authors'],
        average_rating=row['average_rating'],
        isbn=row['isbn'],
        isbn13=row['isbn13'],
        language_code=row['language_code'],
        num_pages=row['  num_pages'],
        rating_count=row['ratings_count'],
        text_review_count=row['text_reviews_count'],
        publication_date=row['publication_date'],  # NOTE: 'auto_now=True' will overwrite this if not changed
        publisher=row['publisher'],
    )
    book.save()

print("CSV data has been loaded into the Django database.")
