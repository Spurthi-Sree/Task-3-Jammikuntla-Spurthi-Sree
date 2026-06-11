import streamlit as st

#Page Configuration
st.set_page_config(
    page_title="AI Job Recommendation System",
    page_icon="\U0001F916",
    layout="centered"
)

#Title
st.title("\U0001F916 AI Job Recommendation System")
st.write("Get personalized part-time job recommendations based on your interests.")

#Job Database
jobs={
    "Coding": ["Python Developer Intern", "Web Developer" ,"Software Tester"],
    "Design": ["Graphic Designer", "UI/UX Designer" ,"Logo Designer"],
    "Teaching": ["Online Tutor", "Teaching Assistant" ,"Academic Mentor"],
    "Writing": ["Content Writer", "Technical Writer" ,"Blog Writer"],
    "Marketing": ["Digital Marketing Intern", "SEO Executive" ,"Social Media Manager"],
    "Video Editing": ["Video Editor", "Youtude Content Editor" ,"Reel Creator"]
}

#User Selection
selected_interests= st.multiselect(
    "Select Your Interests", list(jobs.keys())
)

#Recommendation Button
if st.button("\U0001F50D Get Recommendations"):
    recommendations=[]
    for interest in selected_interests:
        recommendations.extend(jobs[interest])
    if recommendations:
        st.success("Recommendations Generated Successfully!")
        st.subheader("\U0001F3AF Recommended Jobs")
        for job in recommendations:
            st.write(f"\u2705 {job}")

        #Match Score
        score=min(len(selected_interests)*20,100)
        st.subheader("\U0001F4CA Match Score")
        st.progress(score/100)
        st.write(f"Match Score: {score}%")
    else:
        st.warning("Please select at least one interest.")
