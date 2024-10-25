# Documentation

**Letterly** is a AI-Powered web application developed to simplify the process of generating personalized cover letters for job applicants. By providing relevant personal and job-related details, the app leverages AI to create tailored cover letters, making the job application process more efficient and accessible.

## 🚩 **Problem Statement**

For many fresh job applicants, crafting a unique and professional cover letter for each company can be a tedious and time-consuming task. These applicants often struggle to articulate their skills and experiences in a compelling manner, leading to generic letters that fail to capture the attention of hiring managers. The need for customization based on specific job descriptions further complicates this process, resulting in frustration and potential missed opportunities.

## 🌟 **Objective**

The primary goal of Letterly is to streamline the cover letter creation process by utilizing advanced AI technology, making it a valuable tool for job seekers and applicants.

**Letterly** addresses this problem by:
1. Allowing users to input their personal and job-related information.
2. Generating a professional cover letter using AI models based on user inputs.
3. Providing a downloadable cover letter in `.docx` format.
4. Offering a user-friendly interface built with Streamlit for ease of use.

## 🔄 **Workflow**

1. **Input Personal Information**: Users provide specific details like their name, contact information, and job specifics.
2. **AI-Driven Cover Letter Generation**: Letterly interacts with an AI model to generate a tailored cover letter based on user-provided details.
3. **Download Option**: Users can download the generated cover letter in a formatted `.docx` file.
4. **Output**: Users receive a professional cover letter ready for submission with minimal effort.

## 🧑🏻‍💻 **Working**

<img src="Resources/workflow.gif" alt="Working Demo">

## 🛠️ **Features**
- **AI-Powered Cover Letter Generation**: Utilizes natural language processing (NLP) to create tailored cover letters.
- **User-Friendly Interface**: Built on Streamlit, making it accessible and straightforward for users.
- **Downloadable Output**: Provides an option to download generated cover letters in `.docx` format.
- **Modular Programming**: Code is organized into modules for improved maintainability and scalability.

## 🛠 **Setup Instructions**

To run the project locally, follow the steps below:

### Prerequisites

Ensure you have the following installed:
- Python 3.12
- Streamlit
- Required API key for AI content generation (if applicable)

### 1. Clone the Repository

```bash
git clone https://github.com/mShubham18/Letterly.git
cd Letterly
```

### 2. Install Dependencies

Install the required packages by running:

```bash
pip install -r requirements.txt
```

### 3. Set Up Environment Variables

You'll need to add your API key for AI content generation. You can set this up in `apikey.py`:

```python
# if running locally
API_KEY = '<YOUR_API_KEY>'
```

### 4. Run the Application

Start the Streamlit server:

```bash
streamlit run app.py
```

### 5. Access the Application

Visit `http://localhost:8501` to view and interact with **Letterly**.

## 🚀 **Deployment**

Letterly is deployed using **Streamlit Cloud**. You can access the live version of the app here:

[Check it now](https://letterly-ai.streamlit.app/)

NOTE: Streamlit Community Cloud makes applications sleep during inactivity for 2 days; therefore, if shown, click on "`Yes, Get this app back up!`" button.

## 🎯 **Future Enhancements**

- Add features to track user submissions and application status.

Happy Coding ;)
