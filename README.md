# StructSure MVP – AI Deal Structuring Tool

This prototype allows you to:
- Upload a Seller Quote and a Customer PO (PDFs)
- Extract and compare T&Cs
- Generate a risk summary based on clause similarity

## 🔧 Setup Instructions

1. Create a virtual environment:
   ```
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```

2. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

3. Run the app:
   ```
   streamlit run app/main.py
   ```

## 🛠 Tech Stack
- Streamlit (UI)
- PyMuPDF (PDF parsing)
- difflib (clause comparison engine)

This is the MVP version. Future versions will include:
- Redline generation
- CRM integrations
- Role-based workflows
- Real-time legal chat agent