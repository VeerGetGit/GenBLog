from groq import Groq
from config import GROQ_API_KEY

client = Groq(api_key=GROQ_API_KEY)

def generate_seo_keywords(product_name):
    prompt = f"""
    Generate 4 SEO-friendly keywords for the product:
    {product_name}

    Return only a comma-separated list, without numbers or extra text.
    """

    try:
        res = client.chat.completions.create(
            model="openai/gpt-oss-120b",
            messages=[{"role": "user", "content": prompt}]
        )

        content = res.choices[0].message.content.strip()
        keywords = [kw.strip() for kw in content.split(",") if kw.strip()]

        return keywords if keywords else [product_name]

    except Exception as e:
        print("Groq AI SEO error:", e)
        return [product_name]
