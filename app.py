import streamlit as st
import random

# Page setup
st.set_page_config(page_title="Organize Your Perfect Event", page_icon="🎉")

# Styling for a modern, minimalist look
st.markdown("""
    <style>
    .title { font-size: 2em; color: #4B8BBE; text-align: center; font-weight: bold; }
    .subheader { font-size: 1.5em; color: #333333; }
    .result { font-size: 1.3em; font-weight: bold; color: #228B22; }
    .highlight { font-size: 1.1em; color: #DD4B39; font-weight: bold; }
    .progress { font-size: 1.1em; color: #4B8BBE; }
    </style>
""", unsafe_allow_html=True)

# Title
st.markdown('<p class="title">Organize Your Perfect Event: Traditional vs. rentArest</p>', unsafe_allow_html=True)
st.write("Plan your event first the traditional way and then using rentArest to see the difference!")

# Define variables to store total times
if "traditional_time" not in st.session_state:
    st.session_state["traditional_time"] = 0
if "rentArest_time" not in st.session_state:
    st.session_state["rentArest_time"] = 0

# Step 1: Traditional Planning Method
if "traditional_completed" not in st.session_state:
    st.write("## Step 1: Traditional Planning Method")
    st.write("### Imagine you are organizing your event step-by-step without any digital assistance.")

    def traditional_method():
        # Initialize total time
        total_time = 0

        # Task 1: Venue Selection
        st.write("**Task 1: Select a Venue**")
        venue_choice = st.radio("Where will you start?", ["Select an option", "Browse online listings", "Visit venues in person", "Ask friends for recommendations"], key="venue_choice")
        if venue_choice != "Select an option":
            if venue_choice == "Browse online listings":
                total_time += random.randint(60, 90)
            elif venue_choice == "Visit venues in person":
                total_time += random.randint(120, 180)
            else:
                total_time += random.randint(40, 60)

        # Task 2: Catering
        st.write("**Task 2: Arrange Catering**")
        catering_choice = st.radio("How will you arrange catering?", ["Select an option", "Search local caterers online", "Visit catering businesses", "Order from a popular restaurant"], key="catering_choice")
        if catering_choice != "Select an option":
            if catering_choice == "Search local caterers online":
                total_time += random.randint(60, 90)
            elif catering_choice == "Visit catering businesses":
                total_time += random.randint(90, 120)
            else:
                total_time += random.randint(45, 60)

        # Task 3: Entertainment
        st.write("**Task 3: Book Entertainment**")
        entertainment_choice = st.radio("How will you arrange entertainment?", ["Select an option", "Hire a DJ", "Book live performers", "Set up a playlist yourself"], key="entertainment_choice")
        if entertainment_choice != "Select an option":
            if entertainment_choice == "Hire a DJ":
                total_time += random.randint(40, 60)
            elif entertainment_choice == "Book live performers":
                total_time += random.randint(90, 120)
            else:
                total_time += random.randint(20, 30)

        # Check if all tasks have selections before completing
        if venue_choice != "Select an option" and catering_choice != "Select an option" and entertainment_choice != "Select an option":
            st.session_state["traditional_time"] = total_time
            st.session_state["traditional_completed"] = True
            st.write(f"**Total time for traditional planning: {total_time} minutes**")

    traditional_method()

# Step 2: rentArest Planning Method
if "traditional_completed" in st.session_state and "rentArest_completed" not in st.session_state:
    st.write("## Step 2: Planning with rentArest")
    st.write("### Now see how rentArest simplifies the entire process with just a few clicks.")

    def rentArest_method():
        total_time = 0

        # Task 1: Venue Selection
        st.write("**Task 1: Select a Venue**")
        st.write("With rentArest, you quickly find a venue that meets your needs with just a few clicks.")
        total_time += 10

        # Task 2: Catering
        st.write("**Task 2: Arrange Catering**")
        st.write("rentArest provides a list of caterers tailored to your budget and preferences.")
        total_time += 10

        # Task 3: Book Entertainment
        st.write("**Task 3: Book Entertainment**")
        st.write("With rentArest, you can book entertainment in minutes from recommended options.")
        total_time += 5

        # Total time for rentArest method
        st.session_state["rentArest_time"] = total_time
        st.session_state["rentArest_completed"] = True
        st.write(f"**Total time with rentArest: {total_time} minutes**")

    rentArest_method()

# Step 3: Compare Results
if "traditional_completed" in st.session_state and "rentArest_completed" in st.session_state:
    st.write("## Results Comparison")
    st.write(f"**Traditional planning took: {st.session_state['traditional_time']} minutes.**")
    st.write(f"**Planning with rentArest took: {st.session_state['rentArest_time']} minutes.**")
    
    time_saved = st.session_state["traditional_time"] - st.session_state["rentArest_time"]
    st.write(f"**Time saved using rentArest: {time_saved} minutes!**")
    st.success("With rentArest, planning becomes faster, more efficient, and hassle-free!")
