import streamlit as st
import webbrowser
import openai

class EmailGenerator:
    def __init__(self, api_key):
        openai.api_key = api_key
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

# Example usage
st.write("API_KEY:", st.secrets["api_key"])
generator = EmailGenerator(api_key)

st.title("Email Generator")
st.text("by Your Name")

email_type = st.selectbox("Select the type of email:", ("Formal/Professional", "Informal"))
recipient = st.text_input("Recipient Name or Position:")
subject = st.text_input("Email Subject:")

if st.button(label="Generate Email"):
    if email_type == "Formal/Professional":
        messages = [
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": f"Write a formal email to {recipient} regarding {subject}."},
        ]
    else:
        messages = [
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": f"Write an informal email to {recipient} about {subject}."},
        ]

    email = generator.generate_email(messages)

    st.subheader("Generated Email:")
    st.text_area("", value=email, height=300, max_chars=None, key=None)
    
   

    if st.button:
        with st.spinner("Generating Email..."):
            email = generator.generate_email(messages)
        st.markdown("# Email Output:")
        st.subheader(email)

        st.markdown("____")
        st.markdown("# Send Your Email")
        st.subheader("You can press the Generate Email Button again if you're unhappy with the model's output")
        
        st.subheader("Otherwise:")
        st.text(email)
        url = "https://mail.google.com/mail/?view=cm&fs=1&to=&su=&body=" + generator.replace_spaces_with_pluses(email)

        st.markdown("[Click me to send the email]({})".format(url))
