import streamlit as st
import webbrowser
import openai

class EmailGenerator:
    def __init__(self, api_key):
        openai.api_key = st.secrets["API_KEY"]
        self.model = "gpt-3.5-turbo"

    def generate_email(self, messages):
        response = openai.ChatCompletion.create(
            model=self.model,
            messages=messages
        )
        return response.choices[0].message.content.strip()

    def replace_spaces_with_pluses(self, sample):
            """Returns a string with each space being replaced with a plus so the email hyperlink can be formatted properly"""
            changed = list(sample)
            for i, c in enumerate(changed):
                if(c == ' ' or c =='  ' or c =='   ' or c=='\n' or c=='\n\n'):
                    changed[i] = '+'
            return ''.join(changed)

# Create an instance of the EmailGenerator
generator = EmailGenerator(st.secrets["API_KEY"])

# Set the page layout
st.set_page_config(
    page_title="Email Generator",
    page_icon="✉️",
    layout="wide",
    initial_sidebar_state="auto"
)

# Define the header
st.header("WriteAssist")
st.subheader("by Jagteshwar Singh")
st.markdown("---")

# Define the content area
st.title("Generate Email")
st.text("Choose the email type, recipient, and subject below:")

# Email generation form
email_type = st.selectbox("Select the type of email:", ("Formal/Professional", "Informal"))
recipient = st.text_input("Recipient Name or Position:")
subject = st.text_input("Email Subject:")

if st.button(label="Generate Email"):
    if email_type == "Formal/Professional":
        messages = [
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": f"Write a formal email to {recipient} regarding {subject}."},
        ]
        pass
    else:
        messages = [
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": f"Write an informal email to {recipient} about {subject}."},
        ]
        pass

    # Display the generated email
    st.subheader("Generated Email:")
    st.text_area("", value=email, height=300, max_chars=None, key=None)
    st.markdown("---")

    # Send email button
    if st.button("Send Email"):
        url = "https://mail.google.com/mail/?view=cm&fs=1&to=&su=&body=" + generator.replace_spaces_with_pluses(email)
        webbrowser.open_new_tab(url)

# Define the footer
st.markdown("---")
st.subheader("Contact Information")
st.text("Connect with me on GitHub: [Your GitHub Profile](https://github.com/DiaboloX)")
st.text("Find me on LinkedIn: [Your LinkedIn Profile](https://www.linkedin.com/in/your-linkedin-profile)")
