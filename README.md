This project is designed to encode messages sent to the Kargil border, ensuring they are difficult for the enemy to decode. The encoding scheme changes based on the date, providing an additional layer of security.

# Encoding Rules
Odd Days:
A = 01, B = 02, C = 03, ..., Z = 26
Even Days:
A = 501, B = 502, C = 503, ..., Z = 526
For example, the message "Attack submarine near Karachi" would be encoded differently depending on the date:

# Odd Day Encoding:
Attack submarine near Karachi becomes 01 20 20 01 03 11 19 21 02 01 18 01 14 05 14 05 01 18 11 01 18 01 03 08 09
# Even Day Encoding:
Attack submarine near Karachi becomes 501 520 520 501 503 511 519 521 502 501 518 501 514 505 514 505 501 518 511 501 518 501 503 508 509
Spaces and non-alphabetic characters are preserved.

# Prerequisites
Python 3.x
Django

# Installation
# Clone the repository:
git clone https://github.com/sarth360/indian-army-message-encoder.git

# Create a virtual environment and activate it:
python -m venv env
source env/bin/activate (On Windows, use `env\Scripts\activate`)

# Install the required packages:
pip install -r requirements.txt
# Run the Django development server:
python manage.py runserver

# Usage
To encode a message:

Navigate to the home page (http://127.0.0.1:8000/app1/).
Enter your message in the provided form and click "Encode".
View the encoded message on the success page (http://127.0.0.1:8000/app1/success/).

To view encoded messages:
Visit the success page (http://127.0.0.1:8000/app1/success/) to see all previously encoded messages along with their original texts.


