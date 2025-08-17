# Library Assistant

💬 **Library Assistant** is an interactive Python program that helps users search for books, check availability, borrow books, and get library timings in a friendly chat interface.

---

## Features

- Search for books by category or name.
- Check availability of books (only for registered members).
- Borrow and return books.
- View library working hours.
- Ignore non-library related questions.
- Easy-to-use interactive chat interface.

---

## Demo Interaction

```text
💬 Welcome to the Library Assistant!
User: I want a Programming book
Assistant: 📚 Recommended books: Python 101
User: Borrow Python 101
Assistant: ✅ You have successfully borrowed 'Python 101'.
User: When does the library open?
Assistant: 🕒 Our library is open Monday to Saturday, 9 AM to 6 PM.
User: exit
Assistant: 👋 Goodbye!


```
# Book Database

The assistant manages the following books:

book_db = {
    "Python 101": {"copies": 5, "category": "Programming"},
    "Deep Learning Guide": {"copies": 2, "category": "AI"},
    "Basic Mathematics": {"copies": 5, "category": "Mathematics"},
    "Physics Fundamentals": {"copies": 3, "category": "Science"},
    "History of Pakistan": {"copies": 3, "category": "History"},
}


# Installation

# Clone the repository:

git clone https://github.com/your-username/library-assistant.git

cd library-assistant


Install dependencies

Run the assistant using:

python main.py


Type your request, such as searching for a book or borrowing one.

Type exit to quit the assistant.

Project Structure

library-assistant/

│
├── main.py           # Main script to run the assistant
├── library_agents.py # Functions for book search, borrow, return, timings
├── book_db.py        # Book database
└── README.md         # Project documentation


