import streamlit as st
import openai
from config import OPENAI_API_KEY

# Initialize OpenAI client (Corrected for OpenAI v1)
client = openai.Client(api_key=OPENAI_API_KEY)

# Best prompt for high-quality blog generation
PROMPT_TEMPLATE = """
You are an expert content writer. Write a highly engaging, creative, and trendy blog post on the topic: "{topic}". 
Make it informative, SEO-friendly, and structured with a captivating introduction, engaging subheadings, and a strong conclusion.
Target Audience: {audience}
Word Count: {word_count}
Ensure it is unique, well-researched, and highly readable.
"""

def generate_blog(topic, word_count, audience):
    try:
        response = client.chat.completions.create(
            model="gpt-4",  # Change to "gpt-3.5-turbo" if needed
            messages=[
                {"role": "system", "content": "You are a professional blog writer."},
                {"role": "user", "content": PROMPT_TEMPLATE.format(topic=topic, word_count=word_count, audience=audience)}
            ],
            temperature=0.7
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        return f"⚠️ Error: {e}"

# Streamlit UI
st.set_page_config(page_title="AI Blog Generator", layout="wide")

st.title("📝 AI-Powered Blog Generator")
st.write("Generate high-quality blog posts instantly with AI!")

topic = st.text_input("Enter Blog Topic", placeholder="e.g. Future of AI in Healthcare")
word_count = st.slider("Word Count", min_value=300, max_value=2000, step=100, value=800)
audience = st.selectbox("Target Audience", ["General Public", "Tech Enthusiasts", "Business Professionals", "Students", "Researchers"])

if st.button("Generate Blog"):
    with st.spinner("Generating... Please wait."):
        blog_content = generate_blog(topic, word_count, audience)
        st.subheader("Generated Blog:")
        st.write(blog_content)
