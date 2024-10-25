from lib.libraries import *
from src.Letterly.config.configuration import model, generation_config
#from apikey import API_KEY
from docx import Document
import streamlit as st
import time
API_KEY = os.getenv('API_KEY')
genai.configure(api_key=API_KEY)

st.set_page_config(layout="wide")
st.title("Letterly")
st.text("Cover letters made simple, powerful, and personal.")

with st.sidebar:
    st.title("Welcome, please enter the details: ")
    fullname = st.text_input("Enter your full name", placeholder="ex: John Doe")
    mail_id = st.text_input("Enter your mail id", placeholder="ex: mail@example.com")
    phone_num = st.text_input("Enter your mobile number", placeholder="ex: +91123456789")
    company_name = st.text_input("Name of the targeted company", placeholder="ex: Google")
    job_role = st.selectbox("What's the Role you're applying for?", Job_roles)
    job_description = st.text_area("Enter the Job description", placeholder="please paste the JD here")

    st.multiselect("Please select your skillset(s)", Skillset)
    degree = st.selectbox("What's your degree?", Degree)
    p_exp = st.selectbox("What's your professional experience in years?", ("0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10+"))

    if p_exp != "0":
        prof_journey = st.text_area("Describe your professional journey")
    else:
        personal_projects = st.text_area("Tell us about your personal projects then (if any, else type NA)")
    
    university = st.text_input("Enter the name of your University/College", placeholder="ex: University of Michigan")
    joining_status = st.selectbox("Are you able to join Immediately?", ("Yes", "No"))

    if joining_status == "No":
        notice_period = st.text_input("Enter your notice period in months" + " Months of Notice period")
    else:
        notice_period = "No notice period"

    submit_button = st.button("Generate")

    prompt = (f"Generate a professional cover letter for the candidate named \"{fullname}\" applying for the position of \"{job_role}\" at \"{company_name}\". "
              f"The candidate has the following details: \n"
              f"- Phone Number: \"{phone_num}\"\n"
              f"- Email: \"{mail_id}\"\n"
              f"- Job Description: \"{job_description}\"\n"
              f"- Professional Experience: \"{prof_journey}\"\n"
              f"- Personal Projects: \"{personal_projects}\"\n"
              f"- Skill set of candidate: \"{Skillset}\"\n"
              f"- Academic Background: \"{degree}\" from \"{university}\"\n"
              f"- Availability or notice period: \"{notice_period}\"\n"
              f"Do not include the *where did you hear about us* part, and please do not include any suggestion \n"
              f"Always use: Dear Hiring Manager, {company_name}, \n"
              f"Include current date i.e today's date \n"
              f"The cover letter should highlight the candidate's qualifications, relevant experience, and enthusiasm for the role while maintaining a professional tone."
              f"End the letter with a thank you to the hiring manager and sign off with \"Sincerely,\" followed by the candidate's name \"{fullname}\". and other mail, phone number below one another")

if submit_button:
    with st.spinner("Generating your cover letter, please wait..."):
        time.sleep(18)
    response = model.generate_content([prompt])
    st.write(response.text)


    cover_letter_text = response.text
    
    docx_filename = f"Files/cover_letter_{company_name}.docx"
    doc = Document()
    doc.add_paragraph(cover_letter_text)
    doc.save(docx_filename)

    # Provide a download button for the .docx file
    with open(docx_filename, "rb") as file:
        st.download_button(
            label="Download Cover Letter",
            data=file,
            file_name=docx_filename,
            mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document"
        )

footer = """<style>
:root {
    --footer-text-color: black; /* Light mode text color */
}

@media (prefers-color-scheme: dark) {
    :root {
        --footer-text-color: white; /* Dark mode text color */
    }
}

a:link, a:visited {
    color: blue;
    text-decoration: underline;
}

a:hover, a:active {
    color: red;
    background-color: transparent;
    text-decoration: underline;
}

.footer {
    position: fixed;
    left: 0;
    bottom: 0;
    width: 100%;
    color: var(--footer-text-color);
    text-align: center;
    background-color: transparent; /* Make background transparent */
    font-size: 14px;
}

.footer p {
    display: inline;
}

.footer a {
    display: inline; /* Ensure the link is inline */
    color: var(--footer-text-color);
}
</style>
<div class="footer">
<p>Developed with ❤ by <a href="https://github.com/mShubham18/Letterly" target="_blank"> Shubham Mishra</a></p>
</div>
"""

st.markdown(footer, unsafe_allow_html=True)