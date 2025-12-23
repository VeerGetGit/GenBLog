from groq import Groq
from config import GROQ_API_KEY

client = Groq(api_key=GROQ_API_KEY)

def generate_blog(product, keywords):
    prompt = f"""
    Write a 150-200 word SEO blog post for:
    Product: {product}

    SEO Keywords:
    {', '.join(keywords)}

    Requirements:
    - Natural keyword placement
    - Marketing friendly
    - Informative
    """

    try:
        response = client.chat.completions.create(
            model="openai/gpt-oss-120b",
            messages=[{"role": "user", "content": prompt}]
        )
        return response.choices[0].message.content.strip()

    except Exception as e:
        print("Groq Blog Generator error:", e)
        return f"{product} - SEO blog content could not be generated."
