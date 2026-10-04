import os
import serpapi
import streamlit as st
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("SERPAPI_KEY")
client = serpapi.Client(api_key=api_key)

st.set_page_config(
    page_title="StudyLens",
    page_icon="📚",
    layout="wide"
)

st.title("📚 StudyLens")
st.subheader("Your smart learning companion")
st.write("Search once. Learn, watch, practice, and explore in one place.")

query = st.text_input(
    "🔎 What do you want to learn?",
    placeholder="Example: Binary Search in C++"
)

if st.button("🚀 Build My Study Pack"):

    if not query:
        st.warning("Please enter a topic first.")

    else:
        # ⭐ LEARNING PATH
        st.header("⭐ Recommended Learning Path")

        col1, col2, col3, col4 = st.columns(4)

        with col1:
            st.info("1️⃣ UNDERSTAND\n\nLearn the concept")

        with col2:
            st.success("2️⃣ WATCH\n\nSee it visually")

        with col3:
            st.warning("3️⃣ PRACTICE\n\nSolve problems")

        with col4:
            st.error("4️⃣ EXPLORE\n\nGo deeper")

        # 📚 LEARN
        st.header("📚 Learn")

        learn_results = client.search({
            "engine": "google",
            "q": query
        })

        organic = learn_results.get("organic_results", [])

        for result in organic[:5]:
            title = result.get("title")
            link = result.get("link")

            if title and link:
                st.markdown(f"🔗 **[{title}]({link})**")

        # 🎥 WATCH
        st.header("🎥 Watch")

        watch_results = client.search({
            "engine": "youtube",
            "search_query": query
        })

        videos = watch_results.get("video_results", [])

        for video in videos[:5]:
            title = video.get("title")
            link = video.get("link")

            if title and link:
                st.markdown(f"▶️ **[{title}]({link})**")

        # 💻 PRACTICE
        st.header("💻 Practice")

        practice_results = client.search({
            "engine": "google",
            "q": query + " coding practice problems"
        })

        practice = practice_results.get("organic_results", [])

        for result in practice[:5]:
            title = result.get("title")
            link = result.get("link")

            if title and link:
                st.markdown(f"💻 **[{title}]({link})**")

        # ❓ EXPLORE
        st.header("❓ Explore Related Topics")

        related_results = client.search({
            "engine": "google",
            "q": query + " related topics"
        })

        related = related_results.get("organic_results", [])

        for result in related[:5]:
            title = result.get("title")
            link = result.get("link")

            if title and link:
                st.markdown(f"🔎 **[{title}]({link})**")

        st.divider()

        st.caption(
            "StudyLens • Powered by SerpApi • Built for students"
        )