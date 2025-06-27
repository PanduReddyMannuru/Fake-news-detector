import streamlit as st

st.set_page_config(page_title="About", page_icon="ℹ️")

# Custom CSS for clarity and creativity
st.markdown("""
    <style>
    header[data-testid="stHeader"] { display: none; }
    .about-hero {
        background: linear-gradient(135deg, #ede9fe 60%, #c7d2fe 100%);
        border-radius: 18px;
        padding: 2.5rem 2rem 2rem 2rem;
        margin-bottom: 2rem;
        box-shadow: 0 4px 24px rgba(124,58,237,0.08);
        text-align: center;
    }
    .about-title {
        font-size: 2.3rem;
        color: #4c1d95;
        font-weight: 800;
        margin-bottom: 0.5rem;
    }
    .about-desc {
        font-size: 1.15rem;
        color: #6d28d9;
        margin-bottom: 1.5rem;
    }
    .about-section {
        background: #fff;
        border-radius: 14px;
        box-shadow: 0 2px 12px rgba(124,58,237,0.07);
        padding: 1.5rem 1.5rem 1.2rem 1.5rem;
        margin: 0 auto 2rem auto;
        max-width: 600px;
        text-align: left;
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
    .back-home-btn {
        background: linear-gradient(90deg,#818cf8,#7c3aed);
        color: white;
        border: none;
        border-radius: 999px;
        padding: 0.5rem 1.5rem;
        font-size: 1.05rem;
        font-weight: 600;
        margin-bottom: 1.5rem;
        margin-top: 0.5rem;
        cursor: pointer;
        transition: background 0.2s;
        box-shadow: 0 2px 8px rgba(124,58,237,0.08);
        display: inline-block;
    }
    .back-home-btn:hover {
        background: linear-gradient(90deg,#7c3aed,#818cf8);
    }
    .main-container {
        max-width: 700px;
        margin: 0.2rem auto 2.5rem auto;  /* Further reduced top margin */
        padding: 0.5rem 1.5rem 2.5rem 1.5rem;  /* Reduced top padding */
        box-sizing: border-box;
    }
    </style>
""", unsafe_allow_html=True)

st.markdown('<div class="main-container">', unsafe_allow_html=True)

st.markdown("""
    <div class="about-hero">
        <div class="about-title">ℹ️ About This App</div>
        <div class="about-desc">
            Welcome to the <b>Fake News Detector</b>!<br>
            This app helps you quickly check if a news headline or article is likely to be <b>real</b> or <b>fake</b> using intelligent logic and a creative interface.
        </div>
    </div>
""", unsafe_allow_html=True)

st.markdown("""
    <div class="about-section">
        <h4>📝 How to Use:</h4>
        <ol>
            <li>Go to the <b>main page</b> (Home).</li>
            <li>Paste or type any news headline or article in the input box.</li>
            <li>Click <b>Analyze</b> to instantly see if the news is likely <span style="color:green;font-weight:600;">REAL</span> or <span style="color:red;font-weight:600;">FAKE</span>.</li>
        </ol>
        <hr style="margin:1.2rem 0;">
        <h4>🚀 Key Highlights:</h4>
        <ul>
            <li>✅ Clean & colorful interface</li>
            <li>🔍 Real-time analysis based on your input</li>
            <li>📄 Multi-page layout for easy navigation</li>
            <li>💻 Built entirely with Python & Streamlit</li>
        </ul>
        <div style="margin-top:1.2rem;">
            <b>Note:</b> This is a demo app by <b>Syntax Squad</b>. AI model integration is coming soon for even better accuracy!
        </div>
    </div>
""", unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)  # Close main-container

# Add navigation buttons (Back to Home and Contact) at the end of the page, above the footer
st.markdown('''
    <div style="text-align:center; margin-bottom:2.5rem; display: flex; justify-content: center; gap: 0.5rem;">
        <a href="/" style="text-decoration:none;">
            <button class="back-home-btn">🏠 Back to Home</button>
        </a>
        <a href="/contact" style="text-decoration:none;">
            <button class="footer-btn">📫 Contact</button>
        </a>
    </div>
''', unsafe_allow_html=True)

# Footer (only copyright and GitHub)
st.markdown("""
    <div class="footer" style="display: flex; justify-content: center; align-items: center;">
        <span>© 2025 Syntax Squad &mdash;
            <a href=\"https://github.com/syntax-squad\" style=\"color:#7c3aed; margin-left: 0.5rem;\">GitHub</a>
        </span>
    </div>
""", unsafe_allow_html=True)
