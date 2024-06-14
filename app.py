import streamlit as st
from game_logic import get_computer_choice, determine_winner

st.title("Rock Paper Scissors")

# Initialize session state for user_wins and comp_wins if they don't exist
if 'user_wins' not in st.session_state:
    st.session_state.user_wins = 0
if 'comp_wins' not in st.session_state:
    st.session_state.comp_wins = 0

st.write("Choose your move:")

# Display buttons with icons for Rock, Paper, Scissors
col1, col2, col3 = st.columns(3)

with col1:
    if st.button("🪨 Rock"):
        user_choice = "rock"
        comp_choice = get_computer_choice()
        winner = determine_winner(user_choice, comp_choice)
        
        if winner == "user":
            st.session_state.user_wins += 1
            st.write(f"You chose 🪨, computer chose {comp_choice}. You win!")
        elif winner == "comp":
            st.session_state.comp_wins += 1
            st.write(f"You chose 🪨, computer chose {comp_choice}. You lose!")
        else:
            st.write(f"You chose 🪨, computer chose {comp_choice}. It's a tie!")

with col2:
    if st.button("📄 Paper"):
        user_choice = "paper"
        comp_choice = get_computer_choice()
        winner = determine_winner(user_choice, comp_choice)
        
        if winner == "user":
            st.session_state.user_wins += 1
            st.write(f"You chose 📄, computer chose {comp_choice}. You win!")
        elif winner == "comp":
            st.session_state.comp_wins += 1
            st.write(f"You chose 📄, computer chose {comp_choice}. You lose!")
        else:
            st.write(f"You chose 📄, computer chose {comp_choice}. It's a tie!")

with col3:
    if st.button("✂️ Scissors"):
        user_choice = "scissors"
        comp_choice = get_computer_choice()
        winner = determine_winner(user_choice, comp_choice)
        
        if winner == "user":
            st.session_state.user_wins += 1
            st.write(f"You chose ✂️, computer chose {comp_choice}. You win!")
        elif winner == "comp":
            st.session_state.comp_wins += 1
            st.write(f"You chose ✂️, computer chose {comp_choice}. You lose!")
        else:
            st.write(f"You chose ✂️, computer chose {comp_choice}. It's a tie!")

st.write(f"User Wins: {st.session_state.user_wins}")
st.write(f"Computer Wins: {st.session_state.comp_wins}")

# Display total scores
st.write("### Total Scores")
st.write(f"User: {st.session_state.user_wins}")
st.write(f"Computer: {st.session_state.comp_wins}")