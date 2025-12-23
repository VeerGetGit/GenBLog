from flask import Flask, request, jsonify, render_template, abort
from scraper import scrape_products
from seo_keywords import generate_seo_keywords
from blog_generator import generate_blog
from storage import save_blog, load_blogs

app = Flask(__name__)

@app.route("/generate-blog", methods=["POST"])
def generate():
    data = request.get_json(silent=True)

    if not data or "query" not in data:
        return jsonify({"error": "Query is required"}), 400

    query = data["query"]

    # Scrape products
    products = scrape_products(query)
    product = products[0] if products else query

    # SEO keywords
    keywords = generate_seo_keywords(product)

    # Blog content
    blog_content = generate_blog(product, keywords)

    # Save blog
    blog = save_blog(product, blog_content, keywords)

    return jsonify(blog), 200


@app.route("/")
def home():
    blogs = load_blogs()
    blogs = sorted(blogs, key=lambda x: x["date"], reverse=True)
    return render_template("index.html", blogs=blogs)


@app.route("/post/<post_id>")
def post(post_id):
    blogs = load_blogs()
    blog = next((b for b in blogs if b["id"] == post_id), None)
    if not blog:
        abort(404)
    return render_template("post.html", blog=blog)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
