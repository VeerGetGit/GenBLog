import streamlit as st
import requests

st.title(" AI SEO Blog Generator")

query = st.text_input("Enter product category (e.g. Wireless Earbuds)")

if st.button("Generate Blog") and query.strip():
    with st.spinner("Generating..."):
        try:
            response = requests.post(
                "http://localhost:5000/generate-blog",
                json={"query": query}
            )

            if response.status_code != 200:
                st.error(response.text)
            else:
                res = response.json()

                st.subheader(" Product")
                st.write(res.get("title", "N/A"))

                st.subheader(" SEO Keywords")
                st.write(res.get("keywords", []))

                st.subheader(" Blog Content")
                st.write(res.get("content", ""))

        except Exception as e:
            st.error(f"Error: {e}")
