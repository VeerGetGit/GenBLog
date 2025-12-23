# 📝 AI-Based SEO Blog Generation Tool (Task 2)

## 📌 Overview

The AI-Based SEO Blog Generation Tool is an automated application that generates SEO-optimized blog posts for e-commerce products.  
The system scrapes product names, generates SEO-friendly keywords using the Groq API (openai-gpt-oss-120B), creates a 150–200 word blog, and publishes it on a self-hosted website.

This tool significantly reduces manual effort in content creation and enables rapid generation of SEO blogs.

---

## 🎯 Objective

The objective of this project is to:

- Scrape product names from an e-commerce website  
- Generate SEO-friendly keywords using AI  
- Create a 150–200 word SEO-optimized blog post  
- Publish blogs automatically on a self-hosted website  
- Provide a user-friendly frontend for blog generation  

---

## ⚙️ Workflow

1. User enters a product category or query through the Streamlit frontend  
2. The system scrapes relevant product names from an e-commerce website  
3. SEO keywords are generated using Groq API (openai-gpt-oss-120B)  
4. Blog content is generated using the AI model  
5. The generated blog is stored in JSON format  
6. Blogs are displayed on a self-hosted Flask website  

---

## 🔄 System Pipeline

User Input
↓
Product Scraper
↓
SEO Keyword Generator (Groq API)
↓
Blog Generator (Groq API)
↓
JSON Storage
↓
Self-Hosted Website (Flask)



---

## 🛠 Technology Stack

- Programming Language: Python  
- Backend: Flask  
- Frontend: Streamlit  
- Web Scraping: Requests, BeautifulSoup  
- AI Model: Groq API (openai-gpt-oss-120B)  
- Storage: JSON  
- Template Engine: Jinja2  
- Version Control: Git & GitHub  

---

## 📦 Modules Overview

- Product Scraper – Extracts product names from e-commerce websites  
- SEO Keyword Generator – Generates SEO-friendly keywords using Groq LLM  
- Blog Generator – Creates a 150–200 word SEO blog post  
- Storage Module – Saves blogs in JSON format  
- Flask Web App – Displays blogs on a self-hosted website  
- Streamlit Frontend – Interface for blog generation  

---

