from PIL import Image
import requests
import streamlit as st
from streamlit_lottie import st_lottie

st.set_page_config(page_title="Jorge Baez", page_icon=":computer:", layout="wide")

def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code !=200:
        return None
    return r.json()

def local_css(file_name):
    with open (file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

local_css("Style/style.css")

lottie_coding = load_lottieurl("https://assets10.lottiefiles.com/packages/lf20_49rdyysj.json")
tickets = Image.open("Images/tickets.png")
consolidado = Image.open("Images/consolidado.png")
ila = Image.open("Images/ila.png")

with st.container():
    st.subheader("Hi, I am Jorge Baez :wave:")
    st.title("Data Analyst")
    st.write("I am a systems engineer with emphasis on data analysis and business intelligence for decision making through Power BI, SQL and Python")


with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("What I do")
        st.write("##")
        st.write(
            """
            - Creation of high-level Dashboards through Power BI.
            - Analysis and survey of requirements for the creation of dashboards in Power BI.
            - SQL queries for data validation.
            - Creation and documentation of internal processes.
            - Data validation through Microsoft Excel and SQL.
            """ 
        )

    with right_column:
        st_lottie(lottie_coding, height=250, key="coding")

with st.container():
    st.write("---")
    st.header("My projects")
    st.write("#")
    image_column, text_column = st.columns((1,2))
    with image_column:
        st.image(tickets)


    with text_column:
        st.subheader("Tickets per day") 
        st.write(
            """
            This project was carried out to show the behavior of the external and internal requirements 
            (tickets). In addition, you can view their distribution by months and hours to optimize the 
            use of resources.
            """
        )   
        st.markdown("[Watch the example...](https://app.powerbi.com/view?r=eyJrIjoiMzdiYzE1ODctODEzMC00ZGU2LWE3ZTktMDNmN2JhYTNmNDAxIiwidCI6IjNkNmQwOGMxLWJlMzAtNDhjNy05NWQzLTI0NTA3MTQ4ZmQ0NCJ9)")

with st.container():
    image_column, text_column = st.columns((1,2))
    with image_column:
        st.image(consolidado)


    with text_column:
        st.subheader("Operation Report by zone") 
        st.write(
            """
           This project shows the consolidated behavior of customer service operations in service rooms. 
           Attention and waiting time is shown for each of the venues and for officials.
            """
        )   
        st.markdown("[Watch the example...](https://app.powerbi.com/view?r=eyJrIjoiNTIwMzVmYTctNWQxZC00ZDdkLTk4NjUtMTExODZkNjQ3MWYwIiwidCI6IjNkNmQwOGMxLWJlMzAtNDhjNy05NWQzLTI0NTA3MTQ4ZmQ0NCJ9)")

with st.container():
    image_column, text_column = st.columns((1,2))
    with image_column:
        st.image(ila)


    with text_column:
        st.subheader("Impact LatinAmerica") 
        st.write(
            """
           This project was carried out for a pro-church organization. Through it, you can view various metrics in different Latin American countries. Each country is personalized with its flag, includes details for each country and is available in Spanish and English.
            """
        )   
        st.markdown("[Watch the example...](https://app.powerbi.com/view?r=eyJrIjoiNTkxMzE5MjEtZjBlYS00MmI3LWFhMDMtNjBiM2ZmMjkwYjFmIiwidCI6IjUxMWFjZTc5LTk0MjMtNGE1Ny1iMmEwLWM0Y2VjZDI4MmQxNiJ9)")        


with st.container():
    st.write("---")
    st.header("Get in touch with me")
    st.write("##")

    contact_form = """
    <form action="https://formsubmit.co/jorgebaez7@gmail.com" method="POST">
     <input type="text" name="name" placeholder="Your name" required>
     <input type="email" name="email"placeholder="Your email" required>
     <textarea name = "message" placeholder "Your message here" required></textarea>
     <button type="submit">Send</button>
    </form>
    """
    left_column, right_column = st.columns(2)
    with left_column:
        st.markdown(contact_form,unsafe_allow_html=True)
    with right_column:
        st.empty()
