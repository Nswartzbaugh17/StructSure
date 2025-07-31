import streamlit as st
import fitz  # PyMuPDF
from difflib import SequenceMatcher

# App config
st.set_page_config(page_title="StructSure", layout="wide")
st.title("StructSure – AI-Powered Deal Structuring")
st.markdown("Upload your **Seller Quote** and **Customer PO** to begin clause comparison and risk evaluation.")

# File uploaders
quote_file = st.file_uploader("📄 Upload Seller Quote (PDF)", type=["pdf"])
po_file = st.file_uploader("📄 Upload Buyer PO (PDF)", type=["pdf"])

# PDF text extraction function
def extract_text_from_pdf(uploaded_file):
    with fitz.open(stream=uploaded_file.read(), filetype="pdf") as doc:
        return "\n".join([page.get_text() for page in doc])

# Text comparison function
def compare_texts(text1, text2):
    ratio = SequenceMatcher(None, text1, text2).ratio()
    return round(ratio * 100, 2)

# Main logic once both files are uploaded
if quote_file and po_file:
    quote_text = extract_text_from_pdf(quote_file)
    po_text = extract_text_from_pdf(po_file)

    # Similarity Score
    st.subheader("🔍 Clause Comparison Summary")
    match_score = compare_texts(quote_text, po_text)
    st.metric(label="Document Similarity", value=f"{match_score}%", delta=None)

    # Raw Text Display
    st.subheader("📋 Raw Extracted Terms & Conditions")
    with st.expander("Seller Quote Clauses"):
        st.text(quote_text[:3000])
    with st.expander("Buyer PO Clauses"):
        st.text(po_text[:3000])

    # Risk Summary Output
    st.subheader("⚠️ Risk Summary")
    if match_score > 85:
        st.success("Low legal risk. Documents are largely aligned.")
    elif match_score > 60:
        st.warning("Moderate legal risk. Review differences manually.")
    else:
        st.error("High legal risk. Major term differences detected.")
