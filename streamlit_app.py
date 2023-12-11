# Importing necessary libraries
import pandas
import requests
import snowflake.connector
import streamlit

# Using Streamlit to create a title for the web application
streamlit.title('Todd\'s New Healthy Diner')

# Adding headers and text to the application to create a Breakfast Menu
streamlit.header('Breakfast Menu')
streamlit.text('🥣 Omega 3 & Blueberry Oatmeal')
streamlit.text('🥗 Kale, Spinach & Rocket Smoothie')
streamlit.text('🐔 Hard-Boiled Free-Range Egg')
streamlit.text('🥑🍞 Avocado Toast')

# Adding a header for a section where users can build their own fruit smoothie
streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

# Loading a CSV file into a Pandas DataFrame. The CSV file contains data about various fruits.
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")

# Setting the index of the DataFrame to the 'Fruit' column for easier data manipulation
my_fruit_list = my_fruit_list.set_index('Fruit')

# Creating a multi-select widget in the Streamlit app for users to select fruits
fruits_selected = streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['Avocado','Strawberries'])

# Filtering the DataFrame based on the user's fruit selection
fruits_to_show = my_fruit_list.loc[fruits_selected]

# Displaying the filtered DataFrame in the Streamlit app
streamlit.dataframe(fruits_to_show)

# Adding another header for a section called "Fruityvice Fruit Advice!"
streamlit.header("Fruityvice Fruit Advice!")
fruit_choice = streamlit.text_input('What fruit would you like information about?','Kiwi')
streamlit.write('The user entered ', fruit_choice)

# Making an HTTP GET request to an API for information about watermelon
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + fruit_choice)

# Normalizing the JSON data to create a flat table and loading it into a Pandas DataFrame
fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())

# Displaying the normalized data in the Streamlit app
streamlit.dataframe(fruityvice_normalized)
