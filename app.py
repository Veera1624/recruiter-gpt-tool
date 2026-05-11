import streamlit as st
import openai

# Page Config
st.set_page_config(page_title="Sourcing Sensei", page_icon="🎯")
st.title("🎯 Sourcing Sensei: JD Decoder")

# Sidebar for API Key
with st.sidebar:
    st.header("Settings")
    api_key = st.text_input("Enter OpenAI API Key", type="password")
    st.info("Your key is used only for this session.")

if api_key:
    openai.api_key = api_key
    
    # --- Input Section ---
    st.markdown("### Step 1: Provide the Job Description")
    tab1, tab2 = st.tabs(["📄 Upload File", "📝 Paste Text"])
    
    jd_content = ""

    with tab1:
        uploaded_file = st.file_uploader("Upload JD (TXT or PDF)", type=["pdf", "txt"])
        if uploaded_file:
            # Simple text extraction for demonstration
            jd_content = uploaded_file.read().decode("utf-8")

    with tab2:
        pasted_text = st.text_area("Paste the JD here...", height=300)
        if pasted_text:
            jd_content = pasted_text

    # --- Analysis Section ---
    if jd_content:
        if st.button("Analyze & Educate"):
            prompt = f"""
            Act as a Senior Tech Sourcing Mentor. Analyze this JD:
            {jd_content}
            
            Provide:
            1. Skill Breakdown: (Primary, Secondary, Preferable).
            2. Tech Education: Explain 2-3 complex terms from the JD for a non-tech recruiter.
            3. Search Strategy Logic: Explain keywords and operators needed for Naukri, LinkedIn, and GitHub.
            
            IMPORTANT: Do NOT provide actual Boolean strings or links. Explain the logic so the recruiter learns.
            """
            
            with st.spinner("Decoding the tech stack..."):
                try:
                    response = openai.ChatCompletion.create(
                        model="gpt-4o",
                        messages=[{"role": "user", "content": prompt}]
                    )
                    st.success("Analysis Complete!")
                    st.markdown("---")
                    st.markdown(response.choices[0].message.content)
                except Exception as e:
                    st.error(f"Error: {e}")
    else:
        st.write("Waiting for a JD...")
else:
    st.warning("Please enter your API key in the sidebar to begin.")
