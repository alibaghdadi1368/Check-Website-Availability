import streamlit as st
import requests
import time
from PIL import Image

# Banner
banner = Image.open('./images/ACTIVITY.webp')
st.image(banner, width=350)

# Function to format URL to include "https://www."
def format_url(url):
    # Remove http:// or https:// if present
    url = url.replace('http://', '').replace('https://', '')
    # Remove www. if present
    url = url.replace('www.', '')
    # Prepend https://www. to ensure consistency
    formatted_url = 'https://www.' + url
    return formatted_url

# Function to check website availability
def check_site_availability(url):
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'
        }
        response = requests.get(url, timeout=5, headers=headers)
        return response.status_code == 200
    except requests.exceptions.RequestException:
        return False

# Function to update the status of each URL
def update_url_statuses():
    statuses = []
    for url in st.session_state.urls:
        status = check_site_availability(url)
        statuses.append(status)
    return statuses

# Streamlit UI
def main():
    st.title("Website Availability Checker")

    # Session state to store the list of URLs
    if 'urls' not in st.session_state:
        st.session_state.urls = []

    # Session state to store the input field value
    if 'new_url' not in st.session_state:
        st.session_state.new_url = ""

    # Session state to track monitoring status
    if 'monitoring' not in st.session_state:
        st.session_state.monitoring = False

    # Session state to track URL statuses
    if 'statuses' not in st.session_state:
        st.session_state.statuses = []

    new_url = st.text_input("Enter a URL to add to the list:", st.session_state.new_url)

    col1, col2 = st.columns(2)
    with col1:
        # Button to add the URL with formatted URL
        if st.button("Add URL", use_container_width=True):
            formatted_url = format_url(new_url)
            if formatted_url not in st.session_state.urls and new_url != "":
                st.session_state.urls.append(formatted_url)
                st.session_state.statuses.append(None)  # Initialize status as None
                st.success(f"Added {formatted_url} to the list")
                st.session_state.new_url = ""  # Clear the input field after adding
            else:
                st.warning("URL is already in the list")

    with col2:
        # Button to clear the list
        if st.button("Clear List", use_container_width=True):
            st.session_state.urls.clear()
            st.session_state.statuses.clear()

    # Button to check all URLs
    if st.button("Check Availability", use_container_width=True):
        st.session_state.statuses = update_url_statuses()

    # Placeholder for monitoring status
    status_placeholder = st.empty()

    # Button to start monitoring
    if st.button("Start Monitoring", use_container_width=True):
        if not st.session_state.monitoring:
            st.session_state.monitoring = True
            status_placeholder.success("Monitoring is running...")

    # Button to stop monitoring
    if st.button("Stop Monitoring", use_container_width=True):
        if st.session_state.monitoring:
            st.session_state.monitoring = False
            status_placeholder.error("Monitoring has stopped!!!")

    # Display the list of URLs with status emojis
    url_placeholders = []
    for idx, url in enumerate(st.session_state.urls):
        col1, col2 = st.columns([4, 1])
        with col1:
            st.subheader("URL")
            st.write(url)
        with col2:
            st.subheader("Status")
            url_placeholder = st.empty()
            if st.session_state.statuses[idx] is None:
                url_placeholder.write("❓")  # Not yet checked
            elif st.session_state.statuses[idx]:
                url_placeholder.write("✅")  # Available
            else:
                url_placeholder.write("❌")  # Not available
            url_placeholders.append(url_placeholder)

    # Monitoring loop
    if st.session_state.monitoring:
        while st.session_state.monitoring:
            st.session_state.statuses = update_url_statuses()
            for idx, url_placeholder in enumerate(url_placeholders):
                if st.session_state.statuses[idx] is None:
                    url_placeholder.write("❓")  # Not yet checked
                elif st.session_state.statuses[idx]:
                    url_placeholder.write("✅")  # Available
                else:
                    url_placeholder.write("❌")  # Not available
            time.sleep(10)
            st.experimental_rerun()  # Refresh the Streamlit app to show updated statuses

if __name__ == "__main__":
    main()
