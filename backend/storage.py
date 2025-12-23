import json
import uuid
from datetime import datetime

BLOG_FILE = "blogs.json"

def load_blogs():
    try:
        with open(BLOG_FILE, "r") as f:
            return json.load(f)
    except:
        return []

def save_blog(title, content, keywords):
    blogs = load_blogs()

    blog = {
        "id": str(uuid.uuid4()),
        "title": title,
        "content": content,
        "keywords": keywords,
        "date": datetime.now().strftime("%Y-%m-%d %H:%M")
    }

    blogs.append(blog)

    with open(BLOG_FILE, "w") as f:
        json.dump(blogs, f, indent=4)

    return blog
