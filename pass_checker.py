import streamlit as st

def check_password_strength(password):
    # Initialize the score
    score = 0

    # Rule 1: Check if the password is at least 8 characters long
    if len(password) >= 8:
        score += 1

    # Rule 2: Check if the password has both uppercase and lowercase letters
    has_upper = any(char.isupper() for char in password)
    has_lower = any(char.islower() for char in password)
    if has_upper and has_lower:
        score += 1

    # Rule 3: Check if the password has at least one digit
    if any(char.isdigit() for char in password):
        score += 1

    # Rule 4: Check if the password has at least one special character
    special_chars = "!@#$%^&*"
    if any(char in special_chars for char in password):
        score += 1

    # Returns the score
    return score
# feedbacks
def give_feedback(score):
    if score <= 2:
        return "Weak password! 😟\nSuggestions: Make it longer, add uppercase/lowercase letters, digits, or special characters."
    elif score <= 4:
        return "Moderate password! 😐\nSuggestions: Add more security features like special characters or digits."
    else:
        return "Strong password! 😎 Great job!"

# Streamlit App
st.title("Password Strength Checker 🛡️")
st.write("Enter your password below to check its strength.")

# Input field for the password
password = st.text_input("Password", type="password")

# Check the password strength when the user enters something
if password:
    score = check_password_strength(password)
    feedback = give_feedback(score)
    
    # Display the feedback
    st.write(f"**Score:** {score}/5")
    st.write(feedback)