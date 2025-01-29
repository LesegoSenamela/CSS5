# -*- coding: utf-8 -*-
"""
Created on Wed Jan 29 11:59:45 2025

@author: senam
"""

import streamlit as st
import pandas as pd
import datetime

# Title of the app
st.title("Researcher Profile Page")

# Collect basic information
name = "Lesego Senamela"
field = "Computer Sciences"
institution = "University of Science"

# Display basic profile information
st.header("Researcher Overview")
st.write(f"**Name:** {name}")
st.write(f"**Field of Research:** {field}")
st.write(f"**Institution:** {institution}")

# Add a section for publications
st.header("Publications")
uploaded_file = st.file_uploader("Upload a CSV of Publications", type="csv")

if uploaded_file:
    publications = pd.read_csv(uploaded_file)
    st.dataframe(publications)

    # Add filtering for year or keyword
    keyword = st.text_input("Filter by keyword", "")
    if keyword:
        filtered = publications[
            publications.apply(lambda row: keyword.lower() in row.astype(str).str.lower().values, axis=1)
        ]
        st.write(f"Filtered Results for '{keyword}':")
        st.dataframe(filtered)
    else:
        st.write("Showing all publications")

# Add a section for visualizing publication trends
st.header("Publication Trends")
if uploaded_file:
    if "Installs" in publications.columns:
        year_counts = publications["Installs"].value_counts().sort_index()
        st.bar_chart(year_counts)
    else:
        st.write("The CSV does not have a 'Installs' column to visualize trends.")

#section to enter a birthday 
date = st.date_input("Record the last dat of editing", datetime.date(2005, 9, 17))
st.write("Your last edits were: ", date)

# Add a contact section
st.header("Contact Information")
email = "senamelalesego@gmail.com"
st.write(f"You can reach {name} at {email}.")