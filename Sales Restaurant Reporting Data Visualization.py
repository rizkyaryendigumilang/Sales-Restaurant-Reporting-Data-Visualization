import streamlit as st
import pandas as pd
import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title = 'Sales Report Order',
    layout = 'wide'
)

base="light"
primaryColor="#677ce4"
secondaryBackgroundColor="#fafafb"
textColor="#000000"
font="serif"

st.header("Sales Restaurant Reporting Data Visualization")
st.caption("Oleh : Rizky Aryendi Gumilang")
st.subheader("Oders Overview Dashboard")

st.write("Currently, our restaurant does not have a reporting system or dashboard to monitor sales. As a result, we are having difficulty presenting our achievements to stakeholders. ")
st.write("They are only getting raw sales data from Excel that is difficult to understand. ")


def main():
    # Specify the desired box size
    box_width = 600
    box_height = 500

    # HTML content with CSS styles for centering and fitting
    html_temp = f""" <div style="display: flex; justify-content: center; align-items: center; height: {box_height}px; width: {box_width}px; overflow: hidden;"> <iframe width="100%" height="100%" src="https://lookerstudio.google.com/embed/reporting/bca699b4-b105-4ca5-b47c-fe962b247170/page/LlGJD" frameborder="0" style="border: 0; max-width: 100%; max-height: 100%;" allowfullscreen sandbox="allow-storage-access-by-user-activation allow-scripts allow-same-origin allow-popups allow-popups-to-escape-sandbox"> </iframe> </div>"""
    # Display the HTML content using st.markdown
    st.markdown(html_temp, unsafe_allow_html=True)

if __name__ == "__main__":
    main()


st.subheader("Data Report Dashboard")
st.write("This dashboard is designed to make it easy for restaurant stakeholders to filter reporting data based on available filters, such as total revenue per month, menu categories with high sales, top sales menu items.")
import streamlit as st
import streamlit.components.v1 as components


def main():
    # Specify the desired width and height
    box_width = 595
    box_height = 450

    # HTML content with updated width and styles for the iframe
    html_temp = f""" <div style="display: flex; justify-content: center; align-items: center; height: {box_height}px; width: {box_width}px; overflow: hidden; padding: 0;"> <div style="position: relative; width: 100%; height: 0; padding-bottom: {box_height/box_width*100}%;"><!-- 16:9 aspect ratio --> <iframe width="100%" height="100%" src="https://lookerstudio.google.com/embed/reporting/d422d547-acb0-4271-88df-707f18851077/page/bOpnD" frameborder="0" style="border: none; position: absolute; top: 0; left: 0; width: 100%; height: 100%;" allowfullscreen sandbox="allow-storage-access-by-user-activation allow-scripts allow-same-origin allow-popups allow-popups-to-escape-sandbox"> </iframe> /div>  </div> """

    # Display the HTML content using st.markdown
    st.markdown(html_temp, unsafe_allow_html=True)

if __name__ == "__main__":
    main()


st.subheader("Category Menu")
st.write("Filter sales reports by category and menu item")
st.write("takeholders can drill down into sales reports by menu item and category ")
import streamlit as st
import streamlit.components.v1 as components

def main():
    # Specify the desired width and height
    box_width = 600
    box_height = 400

    # HTML content with CSS styles for centering and fitting
    html_temp = f"""<div style="display: flex; justify-content: center; align-items: center; height: {box_height}px; width: {box_width}px; overflow: hidden;"><iframe width="{box_width}" height="{box_height}" src="https://lookerstudio.google.com/embed/reporting/b9769a9b-c033-4910-bcb7-3d89623b3fc8/page/NhpnD" frameborder="0" style="border: 0; max-width: 100%; max-height: 100%;" allowfullscreen sandbox="allow-storage-access-by-user-activation allow-scripts allow-same-origin allow-popups allow-popups-to-escape-sandbox"> </iframe>    </div> """

    # Display the HTML content using st.markdown
    st.markdown(html_temp, unsafe_allow_html=True)

if __name__ == "__main__":
    main()

st.caption("Data source : https://www.mavenanalytics.io/data-playground")

st.subheader("Display Sales Report by Item Menu Type")
st.write("Stakeholders can identify target markets by menu item type for customers")
import streamlit as st
import streamlit.components.v1 as components

def main():
    # Specify the desired width and height
    box_width = 670
    box_height = 450

    # HTML content with CSS styles for centering and fitting
    html_temp = f""" <div style="display: flex; justify-content: center; align-items: center; height: {box_height}px; width: {box_width}px; overflow: hidden;"><iframe width="{box_width}" height="{box_height}" src="https://lookerstudio.google.com/embed/reporting/8b882926-8a72-45a8-8c6f-150c3762a4ce/page/OkpnD"frameborder="0" style="border: 0; max-width: 100%; max-height: 100%;" allowfullscreen sandbox="allow-storage-access-by-user-activation allow-scripts allow-same-origin allow-popups allow-popups-to-escape-sandbox"> </iframe> </div>"""    # Display the HTML content using st.markdown
   
    st.markdown(html_temp, unsafe_allow_html=True)

if __name__ == "__main__":
    main()

st.subheader("Graphic Report Dashboard")
st.write("This feature showcases weekly sales results and offers versatile dynamic filtering")
st.write("View sales reports by monthly sales range")
st.write("Stakeholders can set sales range filters to analyze category performance for each menu item, informing, new product development for targeted markets. ")

def main():
    # Specify the desired width and height
    box_width = 600
    box_height = 450

    # HTML content with CSS styles for centering and fitting
    html_temp = f""" <div style="display: flex; justify-content: center; align-items: center; height: {box_height}px; width: {box_width}px; overflow: hidden;">  <iframe width="{box_width}" height="{box_height}" src="https://lookerstudio.google.com/embed/reporting/8ff06948-e8a0-471f-a4e4-260097bc9f25/page/lGXoD" frameborder="0" scrolling="no" style="border: 0; max-width: 100%; max-height: 100%;" allowfullscreen sandbox="allow-storage-access-by-user-activation allow-scripts allow-same-origin allow-popups allow-popups-to-escape-sandbox">  </iframe> </div> """
    # Display the HTML content using st.markdown
    st.markdown(html_temp, unsafe_allow_html=True)

if __name__ == "__main__":
    main()


st.subheader("Products Produced")

st.write("The dashboard will be created using Google Looker Studio because it is easy to access without installing an application. Additionally, the tool is supported by many features that can support marketing research and data manage")
st.caption("https://lookerstudio.google.com/reporting/b357af35-231f-44e0-915e-1581a58369e8")
