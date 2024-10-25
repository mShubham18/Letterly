from lib.libraries import *
from src.Letterly.config.configuration import model,generation_config
from apikey import API_KEY

genai.configure(api_key=API_KEY)

st.set_page_config(layout="wide")
st.title("Letterly")
st.text("Cover letters made simple, powerful, and personal.")
with st.sidebar:
    st.title("Welcome, please enter the details: ")
    fullname = st.text_input("Enter your full name",placeholder="ex: John Doe")
    mail_id = st.text_input("Enter your mail id",placeholder="ex: mail@example.com")
    phone_num = st.text_input("Enter your mobile number",placeholder="ex: +91123456789")
    company_name=st.text_input("Name of the targeted company",placeholder="ex: Google")
    job_role=st.selectbox("What's the Role you're applying for ?",Job_roles)
    job_description=st.text_area("Enter the Job description",placeholder="please paste the JD here")

    st.multiselect("Please select your skillset(s)",Skillset)
    degree = st.selectbox("What's your degree ?",Degree)
    p_exp = st.selectbox("What's your professional experience in years ?",("0","1","2","3","4","5","6","7","8","9","10+"))
    if not p_exp == "0":
        prof_journey=st.text_area("Describe your professional journey")
    else:
        personal_projects = st.text_area("Tell us about your personal projects then (if any, else type NA)")
    university = st.text_input("Enter the name of your University/College",placeholder="ex: University of Michigan")
    joining_status=st.selectbox("Are you able to join Immediately",("Yes","No"))
    if joining_status=="No":
        notice_period=st.text_input("Enter your notice period in months"+" Months of Notice period")
    else:
        notice_period="No notice period"
    submit_button = st.button("Generate")

    prompt = (f"Generate a professional cover letter for the candidate named \"{fullname}\" applying for the position of \"{job_role}\" at \"{company_name}\". "
          f"The candidate has the following details: \n"
          f"- Phone Number: \"{phone_num}\"\n"
          f"- Email: \"{mail_id}\"\n"
          f"- Job Description: \"{job_description}\"\n"
          f"- Professional Experience: \"{prof_journey}\"\n"
          f"- Personal Projects: \"{personal_projects}\"\n"
          f"- Academic Background: \"{degree}\" from  \"{university}\"\n"
          f"- Availability or notice period: \"{notice_period}\"\n"
          f"Do not include the *where did you hear about us* part, and please do not include any suggestion \n"
          f"Include today's date, \n"
          f"The cover letter should highlight the candidate's qualifications, relevant experience, and enthusiasm for the role while maintaining a professional tone."
          f"End the letter with a thank you to the hiring manager and sign off with \"Sincerely,\" followed by the candidate's name \"{fullname}\". and other mail, phone number below one another")
if submit_button:
    with st.spinner("Generating your cover letter, please wait..."):
        time.sleep(5)
    response = model.generate_content([prompt])
    st.write(response.text)

