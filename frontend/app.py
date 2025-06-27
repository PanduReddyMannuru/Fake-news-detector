import streamlit as st
from streamlit_lottie import st_lottie
import requests

# App config
st.set_page_config(page_title="Fake News Detector", layout="wide")

# Function to load Lottie animation
def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

# Load a Lottie animation
lottie_news = load_lottieurl("https://assets2.lottiefiles.com/packages/lf20_4kx2q32n.json")

# Custom CSS for creative look
st.markdown("""
    <style>
    section[data-testid="stSidebar"] { display: none !important; }
    header[data-testid="stHeader"] { display: none; }
    .block-container { padding-top: 0.5rem; } /* Reduced top padding */
    .hero {
        background: linear-gradient(135deg, #ede9fe 60%, #c7d2fe 100%);
        border-radius: 18px;
        padding: 2.5rem 2rem 2rem 2rem;
        margin-bottom: 2rem;
        box-shadow: 0 4px 24px rgba(124,58,237,0.08);
        text-align: center;
    }
    .hero-title {
        font-size: 2.8rem;
        color: #4c1d95;
        font-weight: 800;
        margin-bottom: 0.5rem;
    }
    .hero-desc {
        font-size: 1.3rem;
        color: #6d28d9;
        margin-bottom: 1.5rem;
    }
    .creative-btn {
        background: linear-gradient(90deg,#7c3aed,#818cf8);
        color: white;
        border: none;
        border-radius: 8px;
        padding: 0.7rem 2rem;
        font-size: 1.1rem;
        font-weight: 600;
        margin: 1rem 0;
        cursor: pointer;
        transition: background 0.3s;
        box-shadow: 0 2px 8px rgba(124,58,237,0.08);
    }
    .creative-btn:hover {
        background: linear-gradient(90deg,#818cf8,#7c3aed);
    }
    .footer-btn {
        background: #ede9fe;
        color: #4c1d95;
        border: none;
        border-radius: 999px;
        padding: 0.4rem 1.1rem;
        font-size: 1rem;
        font-weight: 600;
        margin: 0 0.2rem;
        cursor: pointer;
        transition: background 0.2s, color 0.2s;
        box-shadow: 0 1px 4px rgba(124,58,237,0.06);
        display: inline-block;
        vertical-align: middle;
    }
    .footer-btn:hover {
        background: #c7d2fe;
        color: #6d28d9;
    }
    .news-check-section {
        background: linear-gradient(90deg,#f3e8ff 60%,#c7d2fe 100%);
        border-radius: 16px;
        padding: 2rem 1.5rem;
        margin-bottom: 2.5rem;
        margin-top: 2rem;
        box-shadow: 0 2px 12px rgba(124,58,237,0.07);
    }
    .footer {
        width: 100%;
        position: fixed;
        left: 0;
        bottom: 0;
        background: #fff;
        z-index: 100;
        padding: 1rem 0 0.5rem 0;
        text-align: center;
        color: #a1a1aa;
        font-size: 1rem;
        border-top: 1px solid #ede9fe;
    }
    </style>
""", unsafe_allow_html=True)

# Hero Section
st.markdown("""
    <div class="hero">
        <div class="hero-title">📰 Fake News Detector</div>
        <div class="hero-desc">
            Instantly analyze news headlines and articles for authenticity.<br>
            Powered by intelligent logic and a creative interface.
        </div>
    </div>
""", unsafe_allow_html=True)

# Lottie Animation
if lottie_news:
    st_lottie(lottie_news, height=220, key="news")

# News Check Section
st.markdown("""
    <div class="news-check-section">
        <h2 style="color:#4c1d95; margin-bottom:0.7rem;">🔎 Check Your News</h2>
        <p style="color:#6d28d9; margin-bottom:1.2rem;">Paste a news headline or article below and click <b>Analyze</b> to see if it's likely fake or real.</p>
    </div>
""", unsafe_allow_html=True)

news_input = st.text_area("Enter news headline or article...", height=120, key="news_input")

analyze_btn = st.button("🧠 Analyze", key="analyze_btn", help="Check if the news is fake or real")

if analyze_btn:
    if news_input.strip() == "":
        st.warning("Please enter some news text to analyze.")
    else:
        # Placeholder logic for demonstration
        # Replace this with your ML model or API call
        import random
        result = random.choice(["🟢 This news appears REAL!", "🔴 This news appears FAKE!"])
        st.markdown(f"""
            <div style="background: #ede9fe; border-radius: 12px; padding: 1.2rem; margin-top:1rem; text-align:center; font-size:1.3rem; color:#4c1d95; font-weight:600;">
                {result}
            </div>
        """, unsafe_allow_html=True)

# Add a clear prompt and styled navigation buttons at the end of the page, above the footer
st.markdown('''
    <div style="text-align:center; margin-bottom:2.5rem;">
        <div style="font-size:1.15rem; color:#4c1d95; font-weight:600; margin-bottom:1rem;">
            Want to know more or get in touch?
        </div>
        <div style="display: flex; justify-content: center; gap: 1rem;">
            <a href="/about" style="text-decoration:none;">
                <button class="footer-btn" style="min-width:120px;">ℹ️ About Us</button>
            </a>
            <a href="/contact" style="text-decoration:none;">
                <button class="footer-btn" style="min-width:120px;">📫 Contact</button>
            </a>
        </div>
    </div>
''', unsafe_allow_html=True)

# Footer (centered copyright and GitHub)
st.markdown("""
    <div class="footer" style="display: flex; justify-content: center; align-items: center;">
        <span>© 2025 Syntax Squad &mdash;
            <a href=\"https://github.com/syntax-squad\" style=\"color:#7c3aed; margin-left: 0.5rem;\">GitHub</a>
        </span>
    </div>
""", unsafe_allow_html=True)
