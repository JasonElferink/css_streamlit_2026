# -*- coding: utf-8 -*-
"""
Created on Wed Jan 28 12:15:27 2026

@author: Jason
"""

import streamlit as st
import pandas as pd
import base64
import requests

# Set page title
st.set_page_config(page_title="Jason Elferink", layout="wide")

#Menu
menu = st.radio(
        "Go to:",
        ["About", "Education", "Publications & Outputs", "CV", "Contact"],
        horizontal=True,
        label_visibility="collapsed",
    )
#Studies info
Undergrad = pd.DataFrame({
    "BSc in Microbiology and Biochemistry at North-West University": ["Year 1", "Year 2", "Year 3"],
    "Average %": [74, 75, 72],
    "Year completed": pd.date_range(start="2019-01-01", periods=3, freq='YS').strftime('%Y')
})

Hons = pd.DataFrame({
    "BSc Honours in Biochemistry at North-West University": ["Year 1"],
    "Average %": [65.6],
    "Year completed": pd.date_range(start="2022-01-01", periods=1, freq='YS').strftime('%Y'),
})

Masters = pd.DataFrame({
    "Skill": ["ICP-MS", "Molecular biology skills", "Enzymatics", "LC-MS", "Seahorse XFe96"]})

Pub = pd.DataFrame([
    {
        "Year": 2025,
        "Author": "Elferink J.",
        "Title": "Establishing a method to determine the mitochondrial metallome in a mouse model.",
        "Type": "Oral presentation",
        "Event": "Mitochondrial disease research in South Africa: from gene editing to gene therapy",
        "Location": "Potchefstroom, South Africa",
        "Dates": "January 13th - 14th"
    },
    {
        "Year": 2023,
        "Author": "Van der Walt G, Elferink J, Lindeque JZ, Mason SW, Louw R.",
        "Title": "Subcellular metabolomics: a pipeline for compartment specific metabolic investigations in a mouse model of Leigh syndrome.",
        "Type": "Poster presentation",
        "Event": "EuroMit 2023",
        "Location": "Bologna, Italy",
        "Dates": "June 11th – 15th"
    },
    {
        "Year": 2022,
        "Author": "Louw R",
        "Title": "Metabolic investigation of Leigh Syndrome – the search for novel treatment options.",
        "Type": "Oral presentation (invited talk)",
        "Event": "Mitocon 2022",
        "Location": "Rome, Italy/Online",
        "Dates": "October 7th – 8th"
    }
])

# Sections based on menu selection
if menu == "About":
    st.title("About")
    
    # Collect basic information
    name = "Jason Elferink"
    field = "Biochemistry"
    institution = "North-West University"
    Department = "Biomedical and Molecular Metabolism"

    # Display basic profile information
    st.write(f"**Name:** {name}")
    st.write(f"**Field of Research:** {field}")
    st.write(f"**Institution:** {institution}")
    st.write(f"**Department:** {Department}")
    
    # Photo 
    file_id = "1T0AkrA1dxVmauaaC5Abte19yzeSjufr0"
    url = f"https://drive.google.com/uc?export=view&id={file_id}"
    response = requests.get(url)
    st.image(response.content, caption="Genomics Conference - 2025")
    st.write("I am a postgraduate researcher at North-West University in South Africa, currently completing my Master's degree in Biochemistry with a specialization in mitochondrial biology and metal homeostasis. My research combines advanced bioinformatics methods with ICP-MS analytical techniques to investigate mitochondrial diseases, particularly focusing on how metal dysregulation impacts cellular dysfunction. I'm intermediate in Python programming for multi-omics data analysis and visualization, developing custom scripts for data cleaning, statistical analysis, and principal component analysis using libraries like Pandas, NumPy, and Matplotlib. With aspirations to pursue a PhD and build a career in scientific research, I'm passionate about making meaningful contributions to understanding disease mechanisms and developing innovative therapeutic strategies that bridge fundamental research with real-world medical applications.")



elif menu == "Publications & Outputs":
    st.title("Publications & Outputs")
    st.dataframe(Pub, hide_index=True)
    

elif menu == "Education":
    st.title("Education")
    st.sidebar.header("Degree")
    
    # Tabbed view for STEM data
    data_option = st.sidebar.selectbox(
        "Choose a Degree",
        ["Undergrad", "Honours", "Masters"]
    )

    if data_option == "Undergrad":
        st.write("### NWU")
        st.dataframe(Undergrad, hide_index=True)
        st.image("https://services.nwu.ac.za/sites/services.nwu.ac.za/files/files/designs-branding/NWU-Stacked-Logo-Purple-Digital.png")
        
      

    elif data_option == "Honours":
        st.write("### NWU")
        st.dataframe(Hons, hide_index=True)
        st.image("https://services.nwu.ac.za/sites/services.nwu.ac.za/files/files/designs-branding/NWU-Stacked-Logo-Purple-Digital.png")

       

    elif data_option == "Masters":
        st.title("The effect of a complex 1 deficeincy on the mitochondrial metallome in a leigh Syndrome mouse model")
        st.write("My MSc research at North-West University focuses on developing and optimizing a robust method for quantifying metals within mitochondria isolated from mouse brain and liver tissue. Specifically, I'm investigating mitochondrial metal homeostasis—particularly iron, copper, manganese, calcium, and magnesium—in the context of Leigh syndrome using Ndufs4 knockout (KO) mice as a disease model. The research involves refining mitochondrial isolation protocols to maximize yield and purity, validating ICP-MS analytical methods for accurate metal quantification, and performing statistical analysis to identify differences in mitochondrial metal profiles between Ndufs4 KO and wild-type mice, including potential sex-specific variations. This work builds on pilot studies showing significant alterations in iron and manganese levels in mitochondria from Leigh syndrome models, contributing to our understanding of how metal dysregulation impacts mitochondrial dysfunction in neurodegenerative diseases.")
        st.dataframe(Masters, hide_index=True)
        st.image("https://services.nwu.ac.za/sites/services.nwu.ac.za/files/files/designs-branding/NWU-Stacked-Logo-Purple-Digital.png")

elif menu == "CV":
    # Add CV PDF
    st.header("CURRICULUM VITAE")

   # Add CV PDF
    CV_file_id = "1R8WhqJAw67WaXbiAYgebfRZ5NbSncJfx"

# Use Google Drive's preview directly
    pdf_preview = f'<iframe src="https://drive.google.com/file/d/{CV_file_id}/preview" width="700" height="1000" allow="autoplay"></iframe>'
    st.markdown(pdf_preview, unsafe_allow_html=True)

   
elif menu == "Contact":
    # Add a contact section
    st.header("Contact Information")
    email = "jason.elferink@nwu.ac.za"
    st.write("Feel free to reach me at:")
    st.write(f"Email: {email}")
    st.write("Tel: +27 71 547 0738")
    st.write("Building F3 room 205")
    with st.form("contact_form"):
            st.header("📬 Contact")
            
            name = st.text_input("Name", placeholder="Your name")
            email = st.text_input("Email", placeholder="your.email@example.com")
            phone = st.text_input("Phone", placeholder="+27 21 555 1234")
            message = st.text_area("Message", placeholder="Write your message here...")
            
            submit = st.form_submit_button("Send Message")
            
            if submit:
                if not name or not email or not message:
                    st.error("Please fill out all required fields!")
                elif "@" not in email:
                    st.error("Please enter a valid email address!")
                else:
                    st.success("Thank you! Your message has been sent.")
                    

    st.markdown("_********Contact does not work, beyond my scope of Python, just a proof of concept.********_",)

st.markdown(
    """
    <style>
    .stApp {
        background-image: url("https://static.vecteezy.com/system/resources/previews/021/916/442/original/hexagonal-with-glowing-particles-on-dark-blue-background-science-technology-medicine-chemistry-data-network-background-design-illustration-vector.jpg");
        background-size: cover;
        background-position: center;
        background-attachment: fixed;
    }
    </style>
    """,
    unsafe_allow_html=True,
)




