import streamlit as st
import random
import string

# Function to check password strength
def check_password_strength(password):
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
    # Bonus Rule: Give an extra point if all rules are met
    if score == 4:
        score += 1
    return score

# Function to give feedback
def give_feedback(score):
    if score <= 2:
        return "Weak password! 😟\nSuggestions: Make it longer, add uppercase/lowercase letters, digits, or special characters."
    elif score <= 4:
        return "Moderate password! 😐\nSuggestions: Add more security features like special characters or digits."
    else:
        return "Strong password! 😎 Great job!"

# Function to generate a strong password
def generate_strong_password(length=12):
    # Define character sets
    uppercase = string.ascii_uppercase
    lowercase = string.ascii_lowercase
    digits = string.digits
    special_chars = "!@#$%^&*"
    
    # Combine all characters
    all_chars = uppercase + lowercase + digits + special_chars
    
    # Ensure the password meets all requirements
    while True:
        password = ''.join(random.choice(all_chars) for _ in range(length))
        if (any(char in uppercase for char in password) and
            any(char in lowercase for char in password) and
            any(char in digits for char in password) and
            any(char in special_chars for char in password)):
            return password

# Streamlit App
st.title("Password Strength Checker & Generator 🛡️🔐")
st.write("Check your password strength or generate a strong password!")

# Add a sidebar for password generation
with st.sidebar:
    st.header("Generate a Strong Password")
    password_length = st.slider("Select password length", 8, 20, 12)
    if st.button("Generate Password"):
        strong_password = generate_strong_password(password_length)
        st.success(f"Generated Password: `{strong_password}`")

# Main app for password checking
st.header("Check Your Password Strength")
password = st.text_input("Enter your password to check its strength", type="password")

if password:
    score = check_password_strength(password)
    feedback = give_feedback(score)
    
    st.write(f"**Score:** {score}/5")
    st.write(feedback)