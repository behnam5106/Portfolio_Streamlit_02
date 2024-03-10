import streamlit as st

def main():
    # Customizing background color and font for different sections
    st.markdown(
        """
        <style>
        .section-header {
            background-color: #264653;
            color: white;
            padding: 10px;
            border-radius: 5px;
            margin-bottom: 10px;
        }
        .section-content {
            background-color: #2a9d8f;
            color: white;
            padding: 10px;
            border-radius: 5px;
            margin-bottom: 20px;
        }
        .footer {
            background-color: #e9c46a;
            color: black;
            padding: 10px;
            border-radius: 5px;
            margin-top: 20px;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    # Main content
    st.title("Professional Portfolio")
    st.markdown("---")

    # About Me section
    st.markdown("<div class='section-header'>About Me</div>", unsafe_allow_html=True)
    st.markdown("<div class='section-content'>", unsafe_allow_html=True)
    st.write("""
    I am a passionate and dedicated professional with experience in [Your Field]. 
    My expertise lies in [Your Expertise].
    """)
    st.markdown("</div>", unsafe_allow_html=True)

    # Skills section
    st.markdown("<div class='section-header'>Skills</div>", unsafe_allow_html=True)
    st.markdown("<div class='section-content'>", unsafe_allow_html=True)
    st.write("""
    - Skill 1
    - Skill 2
    - Skill 3
    """)
    st.markdown("</div>", unsafe_allow_html=True)

    # Education section
    st.markdown("<div class='section-header'>Education</div>", unsafe_allow_html=True)
    st.markdown("<div class='section-content'>", unsafe_allow_html=True)
    st.write("""
    - Degree: [Your Degree]
    - University: [University Name]
    - Year: [Year of Graduation]
    """)
    st.markdown("</div>", unsafe_allow_html=True)

    # Work Experience section
    st.markdown("<div class='section-header'>Work Experience</div>", unsafe_allow_html=True)
    st.markdown("<div class='section-content'>", unsafe_allow_html=True)
    st.write("""
    - Position: [Your Position]
    - Company: [Company Name]
    - Duration: [Duration]
    """)
    st.markdown("</div>", unsafe_allow_html=True)

    # Projects section
    st.markdown("<div class='section-header'>Projects</div>", unsafe_allow_html=True)
    st.markdown("<div class='section-content'>", unsafe_allow_html=True)
    st.subheader("Project 1")
    st.write("""
    - Project Description
    - Tools/Technologies Used
    - [Link to GitHub/Website]
    """)
    st.markdown("</div>", unsafe_allow_html=True)

    # Additional buttons and selectors
    if st.button("Click Me!"):
        st.write("You clicked the button!")

    option = st.selectbox("Select an option", ["Option 1", "Option 2", "Option 3"])
    st.write(f"You selected: {option}")

    # Footer section
    st.markdown("---")
    st.markdown("<div class='footer'>© 2024 Your Name</div>", unsafe_allow_html=True)

if __name__ == "__main__":
    main()