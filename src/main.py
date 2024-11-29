import streamlit as st
from scraper import (
    twitterpost,
    instascrape,
    redditscrape,
    tiktokscrape
)
from parse import parse_with_ollama

# Streamlit UI
st.title("AI Web Scraper")
twitID = st.text_input("Enter post ID for twitter or ...")


# Step 1: Scrape the Website

if st.button("Scrape twitter post"):
    if twitID:
        st.write("Scraping the post...")

        # Scrape the website
        content = twitterpost(twitID)
       

        # Store the DOM content in Streamlit session state
        st.session_state.dom_content = content

        # Display the DOM content in an expandable text box
        with st.expander("View Content"):
            st.text_area("Content", content, height=300)

if st.button("Scrape instagram post"):
    if twitID:
        st.write("Scraping the post...")

        # Scrape the website
        content = instascrape(twitID)
       

        # Store the DOM content in Streamlit session state
        st.session_state.dom_content = content

        # Display the DOM content in an expandable text box
        with st.expander("View Content"):
            st.text_area("Content", content, height=300)
if st.button("Scrape reddit post"):
    if twitID:
        st.write("Scraping the post...")

        # Scrape the website
        content = redditscrape(twitID)
       

        # Store the DOM content in Streamlit session state
        st.session_state.dom_content = content

        # Display the DOM content in an expandable text box
        with st.expander("View Content"):
            st.text_area("Content", content, height=300)
if st.button("Scrape tiktok post"):
    if twitID:
        st.write("Scraping the post...")

        # Scrape the website
        content = tiktokscrape(twitID)
       

        # Store the DOM content in Streamlit session state
        st.session_state.dom_content = content

        # Display the DOM content in an expandable text box
        with st.expander("View Content"):
            st.text_area("Content", content, height=300)

# Step 2: Ask Questions About the DOM Content
if "dom_content" in st.session_state:
    parse_description = st.text_area("Describe what you want to parse")

    if st.button("Parse Content"):
        if parse_description:
            st.write("Parsing the content...")

            # Call the parsing function with the description and DOM content
            parsed_result = parse_with_ollama(parse_description, st.session_state.dom_content)
            
            # Display the result
            st.write("Parsed Result:")
            st.text_area("Result", parsed_result, height=300)
