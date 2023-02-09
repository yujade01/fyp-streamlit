import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from functions import *
import time

######################      Read from CSV files   ###############################################
path='NBA shot log 16-17-regular season/'

folder='Shot data/'

ATL = pd.read_csv(path+folder+'shot log ATL.csv')

player_stats = pd.read_csv(path+'Player Regular 16-17 Stats.csv')

player_stats['FullTeamName'] = player_stats['#Team City'] + ' ' + player_stats['#Team Name']

teams = player_stats['FullTeamName'].to_list()
teams.insert(0, " ")

player_stats['FullName'] = player_stats['#FirstName'] + ' ' + player_stats['#LastName']

######################      Layout of Streamlit app   ###############################################

st.set_page_config(layout="wide")

st.title('Shooting Score Analysis of NBA Players in regular season 2016-2017')

with st.expander('About this app'):
  st.write('This app shows the Shooting shot analysis of NBA players in regular season 2016-2017.')
  st.image('https://pbs.twimg.com/profile_images/1392258537993211905/kYxkTjiE_400x400.jpg', width=200)

st.sidebar.header('Input')
#add select box to choose Team
st.sidebar.subheader('NBA Team')
nba_team = st.sidebar.selectbox('Choose an NBA Team to analyse:?', teams)

#add select box to choose player
if(nba_team != ' '):
    players = player_stats[player_stats['FullTeamName']==nba_team]
    selected_team_players = players['FullName'].to_list()
    selected_team_players.insert(0, " ")

    st.sidebar.subheader('NBA player')
    nba_player = st.sidebar.selectbox('Choose a basketball player', selected_team_players)
else:
    st.sidebar.write('Please select NBA Team')

if(nba_team != ' ' and nba_player != ' '):
    st.header('Results')

    my_bar = st.progress(0)

    for percent_complete in range(100):
        time.sleep(0.05)
        my_bar.progress(percent_complete + 1)

    st.balloons()

    #st.write(selected_team_players)

    fullname = str(nba_player)

    index = selected_team_players.index(nba_player)
    #st.write(index)

    position = player_stats['#Position'][index]
    age = int(player_stats['#Age'][index])
    height = player_stats['#Height'][index]
    weight = player_stats['#Weight'][index]
    birth_city = player_stats['#Birth City'][index]
    feet = height[0]
    inch = height[2]

    h_cm = foot_to_cm(feet, inch)

    #st.write(feet)
    #st.write(inch)
    #st.write(type(feet))

    #Player's personal details (Full name, postiion, age, height, weight, birth city)
    st.subheader("Player's Details")

    # Show Player's image

    st.write("Full Name: "+fullname)
    st.write("Position: "+position)
    st.write("Age: ", age)
    st.write("Height: "+height+"( ", h_cm, "cm)")
    st.write("Weight: ", weight)
    st.write("Birth City: "+birth_city)
else:
    st.write(' ')


# col1, col2 = st.columns(2)

# with col1:
#   if nba_team != '':
#     st.write(f' {nba_team}')
#   else:
#     st.write(' ')

# with col2:
#   if nba_player != '':
#     st.write(f'{nba_player}')
#   else:
#     st.write(' ')

st.header('Data analysis')
option = st.selectbox('What would you like to know?', 
['', 'Highest Score in season 16-17', 'Favourite Position', 'Total Games Played', 
'Field Goal 2 Points Attempted', 'Field Goal 2 Points Made', 
'Field Goal 3 Points Attempted', 'Field Goal 3 Points Made', 
'Free Throw Attempted', 'Free Throw Made'])

option = st.selectbox('Match Overview', 
['', 'Shooting Position in the match', 'Total Shots Attempted', 'Total Shots scored', 
'Position that scored', 'Total Shots blocked', 
'Total Shots missed'])

#Plot Basketball court
#Total shots attempted
#Total shots that scored
#Show position that scored
#Total shots that are blocked
#Total shots that are missed

# st.subheader('Comparison among NBA Team')
# options = st.multiselect(
#      'Choose 1 or more NBA Team to compare:',
#      teams)

# st.write('You selected:', options)

fig, ax = plt.subplots()
player_stats.hist(
    bins=8,
    column="#Age",
    grid=False,
    figsize=(8, 8),
    color="#86bf91",
    zorder=2,
    rwidth=0.9,
    ax=ax,
  )
ax.set_title('Age of NBA players in regular season 2016-2017')
st.write(fig)


