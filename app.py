import streamlit as st
import openai

# 1. Setup Page
st.set_page_config(page_title="The Sourcing Sensei", layout="centered")
st.title("🎯 The Sourcing Sensei")
st.subheader("JD Decoder & Recruitment Educator")

# 2. Sidebar for API Key (Keep it secure!)
api_key = st.sidebar.text_input("Enter OpenAI API Key", type="password")

if api_key:
    openai.api_key = api_key
    
    # 3. File Upload
    uploaded_file = st.file_uploader("Upload a Job Description (PDF or Text)", type=["pdf", "txt"])
    
    if uploaded_file:
        jd_text = uploaded_file.read().decode("utf-8") # Simplified for demo
        
        # 4. The Instruction Prompt (The Guardrails)
        prompt = f"""
        Analyze the following Job Description:
        {jd_text}
        
        STRICT RULES:
        1. Breakdown skills into: Primary, Secondary, and Preferable.
        2. Explain 2-3 technologies to the recruiter as a mentor.
        3. Provide the LOGIC for Boolean/X-Ray searches (which operators and keywords to use).
        4. NEVER provide a pre-written search string.
        """
        
        if st.button("Decode JD"):
            with st.spinner("Analyzing technology..."):
                response = openai.ChatCompletion.create(
                    model="gpt-4o", # Or gpt-5-mini in 2026
                    messages=[{"role": "user", "content": prompt}]
                )
                st.markdown(response.choices[0].message.content)
else:
    st.info("Please enter your OpenAI API key in the sidebar to start.")