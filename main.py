import streamlit as st
from bs4 import BeautifulSoup
import requests

st.set_page_config(
    page_title="LATEST NEWS",
    page_icon="🌐"
)

# Add custom CSS to change the background color to blue
st.markdown(
    """
    <style>
    body {
        color: #fff;
        background-color: #0000FF;
    }
    .stButton>button {
        border: 2px solid #4CAF50; /* Green */
        background-color: white; 
        color: black;
        padding: 10px 24px;
        cursor: pointer;
        border-radius: 8px;
    }
    .stButton>button:hover {
        background-color: #4CAF50;
        color: white;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.markdown(
    """
<h1 style='text-align:center; color: white;'>LATEST NEWS</h1>
""",
    unsafe_allow_html=True,
)
st.write("##")

st.image("news.jpg", use_column_width="auto")
st.write("##")

st.write("## Select the Date: ")
st.write("##")

year, month, day = st.columns(3)
year_select = year.selectbox("Select year:", options=["2024", "2023", "2022"])
month_select = month.selectbox(
    "Select month:",
    options=[
        "january",
        "february",
        "march",
        "april",
        "may",
        "june",
        "july",
        "august",
        "september",
        "october",
        "november",
        "december",
    ],
)
day_select = day.selectbox("Select day: ", options=[str(i) for i in range(1, 32)])
st.write("##")
toggle_btn = st.toggle("Hindi")
st.write("##")

Scrap_btn = st.button("Scrap")

# Adjusted the custom-box style for better visibility on a blue background
box_style = """
    <style>
        .custom-box {
            padding: 10px;
            border: 2px solid white;
            border-radius: 10px;
            background-color: #fff; /* Changed background color for visibility */
            color: black; /* Changed text color for visibility */
            margin-bottom: 10px;
        }
        .custom-box a {
            color: #0000FF !important;
            text-decoration: none !important;
            font-weight: bold !important;
        }
    </style>
"""

count = 1
if Scrap_btn:
    text_language = "1"
    if toggle_btn:
        text_language = "2"
    url = (
        "https://sarkaripariksha.com/gk-and-current-affairs/"
        + year_select
        + "/"
        + month_select
        + "/"
        + str(day_select)
        + "/"
        + text_language
        + "/"
    )
    req = requests.get(url)
    soup = BeautifulSoup(req.text, "html.parser")

    news_list = soup.find_all("div", class_="examlist-details-img-box")
    for news_item in news_list:
        a_tag = news_item.find("h2").find("a")
        p_tag = news_item.find("p")

        news_title = a_tag.get_text(strip=True)
        href_link = a_tag["href"]
        st.markdown(box_style, unsafe_allow_html=True)
        st.markdown(
            f"""<div class="custom-box">{count}- <a href="{href_link}">{news_title}</a></div>""",
            unsafe_allow_html=True,
        )
        count = count + 1
