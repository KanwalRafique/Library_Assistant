from typing import Optional
from pydantic import BaseModel
from book_db import book_db

# -------------------------
# User Context
# -------------------------
class UserContext(BaseModel):
    name: str
    member_id: Optional[str] = None
    borrowed_books: list = []

# -------------------------
# Guardrail
# -------------------------
def is_library_query(user_input: str) -> bool:
    keywords = ["book", "library", "availability", "timings", "borrow", "return", "search", "recommend"]
    return any(word in user_input.lower() for word in keywords)

# -------------------------
# Function Tools
# -------------------------
def search_book(title: str) -> str:
    if title in book_db:
        info = book_db[title]
        return f"✅ '{title}' by {info['author']} is available. Copies: {info['copies']}."
    return f"❌ '{title}' is not in our library."

def check_availability(title: str, member_id: Optional[str] = None) -> str:
    if not member_id:
        return "⚠️ Only registered members can check availability."
    if title not in book_db:
        return f"❌ '{title}' does not exist in the library."
    copies = book_db[title]["copies"]
    return f"📚 '{title}' has {copies} copies available." if copies > 0 else f"❌ '{title}' is currently out of stock."

def library_timings() -> str:
    return "🕒 Our library is open Monday to Saturday, 9 AM to 6 PM."

def borrow_book(title: str, user: UserContext) -> str:
    if title not in book_db:
        return f"❌ '{title}' does not exist in the library."
    if book_db[title]["copies"] <= 0:
        return f"❌ '{title}' is currently out of stock."
    book_db[title]["copies"] -= 1
    user.borrowed_books.append(title)
    return f"✅ You have successfully borrowed '{title}'."

def return_book(title: str, user: UserContext) -> str:
    if title not in user.borrowed_books:
        return f"❌ You did not borrow '{title}'."
    user.borrowed_books.remove(title)
    book_db[title]["copies"] += 1
    return f"✅ You have successfully returned '{title}'."

def recommend_books(category: str) -> str:
    recs = [title for title, info in book_db.items() if info["category"].lower() == category.lower()]
    if not recs:
        return f"❌ No recommendations found for category '{category}'."
    return "📚 Recommended books: " + ", ".join(recs)





# from typing import Optional
# from agents import Agent, Runner, function_tool, input_guardrail, RunContextWrapper
# from pydantic import BaseModel
# from book_db import book_db


# # -------------------------
# # STEP 1: User Context
# # -------------------------
# class UserContext(BaseModel):
#     name: str
#     member_id: Optional[str] = None


# # -------------------------
# # STEP 2: Guardrail Agent
# # -------------------------
# guardrail_agent = Agent(
#     name="guardrail_agent",
#     instructions="You are a library-only assistant. Reject any non-library questions."
# )


# # -------------------------
# # STEP 3: Function Tools
# # -------------------------
# @function_tool
# def search_book(title: str) -> str:
#     """Search for a book in the library database."""
#     if title in book_db:
#         return f"✅ '{title}' is available in our library."
#     return f"❌ '{title}' is not available in our library."


# @function_tool
# def check_availability(title: str, member_id: Optional[str] = None) -> str:
#     """Check availability of a book (only for registered members)."""
#     if not member_id:
#         return "⚠️ Only registered members can check availability."
#     if title not in book_db:
#         return f"❌ '{title}' does not exist in the library."
#     copies = book_db[title]["copies"]
#     return f"📚 '{title}' has {copies} copies available." if copies > 0 else f"❌ '{title}' is currently out of stock."


# @function_tool
# def library_timings() -> str:
#     """Provide library opening hours."""
#     return "🕒 Our library is open Monday to Saturday, 9 AM to 6 PM."


# # -------------------------
# # STEP 4: Input Guardrail
# # -------------------------
# @input_guardrail
# def guardrail_function(user_input: str, ctx: RunContextWrapper) -> bool:
#     """Block non-library related queries."""
#     keywords = ["book", "library", "availability", "timings", "borrow", "search"]
#     return any(word in user_input.lower() for word in keywords)


# # -------------------------
# # STEP 5: Library Agent
# # -------------------------
# library_agent = Agent(
#     name="library_agent",
#     instructions="You are a helpful library assistant. Always greet users with their name if available.",
#     tools=[search_book, check_availability, library_timings],
# )


