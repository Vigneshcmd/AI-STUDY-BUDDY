import streamlit as st
import cohere

# === Setup Cohere API ===
API_KEY = "NCTvVQrgBvnbLbyVx0akk3kNNNDOdKuvBkS7Oux5"
co = cohere.Client(API_KEY)

# === Streamlit UI ===
st.set_page_config(page_title="AI Study Buddy", page_icon="📚")
st.title("📖 AI Study Buddy")
st.subheader("Ask me to explain any topic in simple terms!")

topic = st.text_input("📝 Enter a topic to explain")
explain_button = st.button("🔍 Explain")

if explain_button and topic.strip():
    with st.spinner("Thinking... 🤔"):
        try:
            prompt = f"Explain {topic.strip()} in simple terms:"
            response = co.generate(
                model='command-r-plus',
                prompt=prompt,
                max_tokens=200,
                temperature=0.7
            )
            explanation = response.generations[0].text.strip()

            st.success("✅ Here's the explanation:")
            st.markdown(explanation)

        except Exception as e:
            st.error(f"Something went wrong: {e}")
else:
    st.info("Enter a topic above and click 'Explain'")

