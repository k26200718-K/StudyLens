# 📚 StudyLens

StudyLens is a smart learning search engine that turns one learning query into an organized study pack.

## 🚀 Features

- 📚 Learn — Find explanations and useful resources
- 🎥 Watch — Find relevant YouTube videos
- 💻 Practice — Find coding practice resources
- ❓ Explore — Discover related topics
- ⭐ Recommended Learning Path — Follow a simple learning order

## 🛠️ Tech Stack

- Python
- Streamlit
- SerpApi
- python-dotenv

## 💡 How It Works

1. Enter a topic you want to learn.
2. StudyLens searches the web using SerpApi.
3. Results are organized into different learning sections.
4. Students can learn, watch, practice, and explore from one place.

## 🎯 Example

Search:

`Binary Search in C++`

StudyLens creates a structured learning pack with resources for understanding, watching, practicing, and exploring the topic.

## 🔐 Setup

Create a `.env` file and add your SerpApi key:

`SERPAPI_KEY=your_api_key_here`

Then run:

```bash
python -m streamlit run app.py
