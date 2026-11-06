
import streamlit as st

# Page configuration
st.set_page_config(
    page_title="AI Career Intelligence",
    page_icon="🚀",
    layout="wide"
)

# Main title
st.title("AI Career Intelligence & Skill Development Platform")

st.write(
    "Discover your career opportunities, "
    "analyze your skills and build your learning roadmap."
)

# Sidebar navigation
st.sidebar.title("Navigation")

page = st.sidebar.selectbox(
    "Select Module",
    [
        "Home",
        "Resume Analyzer",
        "Job Recommendation",
        "Job Matching",
        "Skill Gap Analysis",
        "Learning Roadmap"
    ]
)

if page == "Home":

    st.header("Welcome to AI Career Intelligence")

    st.write("Start your career analysis here.")

    name = st.text_input("Enter your name")

    role = st.selectbox(
        "Select your target career",
        [
            "AI Engineer",
            "Machine Learning Engineer",
            "Data Scientist",
            "Data Analyst",
            "Python Developer"
        ]
    )

    if st.button("Get Started"):

        if name.strip():

            st.success(f"Welcome, {name}!")

            st.write("Your target role:", role)

        else:

            st.warning("Please enter your name.")

elif page == "Resume Analyzer":

    st.header("Resume Analyzer")

    st.file_uploader(
        "Upload your resume PDF",
        type=["pdf"]
    )

elif page == "Job Recommendation":

    st.header("Job Recommendation")

    st.info("Job recommendation module is coming soon.")

elif page == "Job Matching":

    st.header("Job Matching")

    st.info("Job matching module is coming soon.")

elif page == "Skill Gap Analysis":

    st.header("Skill Gap Analysis")

    st.info("Skill gap analysis module is coming soon.")

elif page == "Learning Roadmap":

    st.header("Personalized Learning Roadmap")

    st.info("Learning roadmap module is coming soon.")
