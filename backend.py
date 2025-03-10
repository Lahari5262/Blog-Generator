import openai
from config import OPENAI_API_KEY

openai.api_key = OPENAI_API_KEY

def generate_blog(topic, word_count, audience):
    prompt = f"""
    Write a {word_count}-word blog post on "{topic}" that is **highly unique, creative, and trendy**.  
    - Make it engaging with an attention-grabbing introduction.  
    - Use a conversational and relatable tone.  
    - Include real-world examples, data, or current trends.  
    - Add an intriguing storytelling element or thought-provoking perspective.  
    - Format it with subheadings, bullet points, and short paragraphs for readability.  
    - End with a powerful conclusion that leaves the reader inspired or taking action.  
    Audience: {audience}
    """

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",  # Change to LLaMA 2 if using Meta's API
        messages=[{"role": "system", "content": "You are an expert blog writer with deep knowledge of digital trends."},
                  {"role": "user", "content": prompt}],
        temperature=0.85,  # More creative output
        max_tokens=word_count * 2,  # Adjust for better length control
        top_p=0.95
    )
    
    return response["choices"][0]["message"]["content"]
