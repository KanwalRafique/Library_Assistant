from library_agents import (
    UserContext,
    search_book,
    check_availability,
    library_timings,
    borrow_book,
    return_book,
    recommend_books,
    is_library_query
)

# -------------------------
# Initialize user
# -------------------------
user = UserContext(name="Abbas", member_id="12345")

print("💬 Welcome to the Library Assistant!")

while True:
    user_input = input("User: ").strip()
    user_input_lower = user_input.lower()

    # -------------------------
    # Exit condition
    # -------------------------
    if user_input_lower in ["exit", "quit", "bye", "goodbye"]:
        print("Assistant: Goodbye! Have a nice day! 👋")
        break

    # -------------------------
    # Check if input is library-related
    # -------------------------
    if not is_library_query(user_input):
        print("Assistant: ❌ Sorry, I only answer library-related questions.")
        continue

    # -------------------------
    # Detect intent
    # -------------------------
    if any(word in user_input_lower for word in ["time", "open", "timings"]):
        print(f"Assistant: {library_timings()}")
    elif "borrow" in user_input_lower:
        title = user_input_lower.replace("borrow", "").strip().title()
        print(f"Assistant: {borrow_book(title, user)}")
    elif "return" in user_input_lower:
        title = user_input_lower.replace("return", "").strip().title()
        print(f"Assistant: {return_book(title, user)}")
    elif any(word in user_input_lower for word in ["recommend", "want"]):
        categories = ["Programming", "Science", "History"]
        found_category = None
        for cat in categories:
            if cat.lower() in user_input_lower:
                found_category = cat
                break
        if found_category:
            print(f"Assistant: {recommend_books(found_category)}")
        else:
            print("Assistant: Please tell me the category (Programming, Science, History, etc.)")
    else:
        title = user_input.strip().title()
        print(f"Assistant: {search_book(title)}")

# -------------------------
# End of chat message
# -------------------------
print("\n💡 You can type 'exit' or 'quit' anytime to end the chat.")
