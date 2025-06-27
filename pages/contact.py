import streamlit as st

st.set_page_config(page_title="Contact", page_icon="📬")

# Improved responsive CSS
st.markdown("""
    <style>
    header[data-testid="stHeader"] { display: none; }
    .main-container {
        max-width: 700px;
        margin: 0.2rem auto 2.5rem auto;  /* Further reduced top margin */
        padding: 0.5rem 1.5rem 2.5rem 1.5rem;  /* Reduced top padding */
        box-sizing: border-box;
    }
    .contact-hero {
        background: linear-gradient(135deg, #c7d2fe 60%, #ede9fe 100%);
        border-radius: 18px;
        padding: 2.5rem 2rem 2rem 2rem;
        margin-bottom: 2rem;
        box-shadow: 0 4px 24px rgba(124,58,237,0.08);
        text-align: center;
    }
    .contact-title {
        font-size: 2.3rem;
        color: #4c1d95;
        font-weight: 800;
        margin-bottom: 0.5rem;
    }
    .contact-desc {
        font-size: 1.15rem;
        color: #6d28d9;
        margin-bottom: 1.5rem;
    }
    .contact-section {
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
    @media (max-width: 900px) {
        .main-container { max-width: 98vw; padding: 1rem 0.5rem 2.5rem 0.5rem; }
        .contact-section { max-width: 98vw; }
    }
    </style>
""", unsafe_allow_html=True)

st.markdown('<div class="main-container">', unsafe_allow_html=True)

st.markdown("""
    <div class="contact-hero">
        <div class="contact-title">📬 Contact Syntax Squad</div>
        <div class="contact-desc">
            We're always excited to collaborate or hear feedback from fellow developers, mentors, and AI enthusiasts!
        </div>
    </div>
""", unsafe_allow_html=True)

st.markdown("""
    <div class="contact-section">
        <h4>🔗 Connect with Us</h4>
        <ul>
            <li>📧 Email: <a href="mailto:syntax.squad.team@gmail.com">syntax.squad.team@gmail.com</a></li>
            <li>🐙 GitHub: <a href="https://github.com/syntax-squad" target="_blank">github.com/syntax-squad</a></li>
            <li>💼 LinkedIn: <a href="https://linkedin.com/company/syntax-squad" target="_blank">linkedin.com/company/syntax-squad</a></li>
        </ul>
        <div style="margin-top:1.2rem;">
            <b>We look forward to connecting with you!</b>
        </div>
    </div>
""", unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)  # Close main-container

# Add navigation buttons (Back to Home and About) at the end of the page, above the footer
st.markdown('''
    <div style="text-align:center; margin-bottom:2.5rem; display: flex; justify-content: center; gap: 0.5rem;">
        <a href="/" style="text-decoration:none;">
            <button class="back-home-btn">🏠 Back to Home</button>
        </a>
        <a href="/about" style="text-decoration:none;">
            <button class="footer-btn">ℹ️ About</button>
        </a>
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
