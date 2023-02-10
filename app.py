import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from functions import *
import time

######################      Read from CSV files   ###############################################
path='NBA shot log 16-17-regular season/'

folder='Shot data/'

player_stats = pd.read_csv(path+'Player Regular 16-17 Stats.csv')

player_stats['FullTeamName'] = player_stats['#Team City'] + ' ' + player_stats['#Team Name']

teams = player_stats['FullTeamName'].to_list()

teams = list(dedupe(teams))

teams.insert(0, " ")

player_stats['FullName'] = player_stats['#FirstName'] + ' ' + player_stats['#LastName']

######################      Layout of Streamlit app   ###############################################

st.set_page_config(layout="wide")

st.title('Shooting Score Analysis of NBA Players in regular season 2016-2017')

with st.expander('About this app'):
  st.write('This app shows the details and shooting position of NBA players in regular season 2016-2017.')
  st.image('https://pbs.twimg.com/profile_images/1392258537993211905/kYxkTjiE_400x400.jpg', width=200)

st.sidebar.header('Input')
#add select box to choose Team
st.sidebar.subheader('NBA Team')
nba_team = st.sidebar.selectbox('Choose a NBA Team to analyse?', teams)

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
    #st.write(player_stats)
    #st.write(selected_team_players)

    fullname = str(nba_player)

    for index, row in player_stats.iterrows():
        if row['FullName'] == fullname:
            playerindex = index
    #st.write(index)

    position = player_stats['#Position'][playerindex]
    age = int(player_stats['#Age'][playerindex])
    height = player_stats['#Height'][playerindex]
    weight = player_stats['#Weight'][playerindex]
    birth_city = player_stats['#Birth City'][playerindex]
    feet = height[0]
    inch = height[2]

    h_cm = foot_to_cm(feet, inch)

    kg = round(lbs_to_kg(weight),2)

    total_games = player_stats['#GamesPlayed'][playerindex]
    Fg2PtAtt = player_stats['#Fg2PtAtt'][playerindex]
    Fg2PtMade = player_stats['#Fg2PtMade'][playerindex]
    Fg3PtAtt = player_stats['#Fg3PtAtt'][playerindex]
    Fg3PtMade = player_stats['#Fg3PtMade'][playerindex]
    FtAtt = player_stats['#FtAtt'][playerindex]
    FtMade = player_stats['#FtMade'][playerindex]

    #Player's personal details (Full name, postiion, age, height, weight, birth city)
    st.subheader("Player's Details")

    col1, col2 = st.columns(2)

    with col1:
        st.write("Full Name: "+fullname)
        st.write("Position: "+position)
        st.write("Age: ", age)
        st.write("Height: "+height+"( ", h_cm, "cm)")
        st.write("Weight: ", weight, 'lbs '+'(', kg, 'kg)')
        st.write("Birth City: "+str(birth_city))

    with col2:
        # option = st.selectbox('What would you like to know?', 
        # ['', 'Total Games Played', 
        # 'Field Goal 2 Points Attempted', 'Field Goal 2 Points Made', 
        # 'Field Goal 3 Points Attempted', 'Field Goal 3 Points Made', 
        # 'Free Throw Attempted', 'Free Throw Made'])

        #if option == 'Total Games Played':
            st.write('Total Games Played: ', total_games)

        #elif option == 'Field Goal 2 Points Attempted':
            st.write('Field Goal 2 Points Attempted: ', Fg2PtAtt)

        #elif option == 'Field Goal 2 Points Made':
            st.write('Field Goal 2 Points Made', Fg2PtMade)
        
        #elif option == 'Field Goal 3 Points Attempted':
            st.write('Field Goal 3 Points Attempted', Fg3PtAtt)

        #elif option == 'Field Goal 3 Points Made':
            st.write('Field Goal 3 Points Made', Fg3PtMade)

        #elif option == 'Free Throw Attempted':
            st.write('Free Throw Attempted', FtAtt)

        #elif option == 'Free Throw Made':
            st.write('Free Throw Made', FtMade)

    st.header('Data analysis')

    #Get abbrevation of NBA team
    abbreviation = pd.read_csv(path+'NBA team name vs abbreviation.csv')
    #st.write(abbreviation)

    for index, row in abbreviation.iterrows():
        if row['Franchise'] == nba_team:
            abbindex = index
            break

    #st.write(abbindex)
    abb = abbreviation['Abbreviation/Acronym'][abbindex]
    #st.write(abb)

    selected_team = pd.read_csv(path+folder+'shot log '+abb+'.csv')
    #st.subheader('Description of the data from '+abb+' shot log')
    #st.write(selected_team.describe())
    
    selected_player_in_team = selected_team[(selected_team['shoot player'] == fullname)]
    st.subheader("Shot log of "+fullname)

    #selected_player_in_team['shot_made'] = 0
    #selected_player_in_team['shot_made'] = selected_player_in_team['shot_made'].mask(selected_player_in_team['current shot outcome'] == 'SCORED', 1)

    st.write(selected_player_in_team)
    #Plot Basketball court
    st.subheader('Shooting x and y coordinate in the basketball court')
    fig, ax = create_court(fullname)
    ax.scatter('location x', 'location y', marker='.', s=120,
            lw=2, data=selected_player_in_team)
    #c=selected_player_in_team.shot_made  
    st.write(fig)
