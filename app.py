import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import functions
import time
from PIL import Image
######################      Read from CSV files   ###############################################
path='NBA shot log 16-17-regular season/'

folder='Shot data/'

player_stats = pd.read_csv(path+'Player Regular 16-17 Stats.csv')

player_stats['FullTeamName'] = player_stats['#Team City'] + ' ' + player_stats['#Team Name']

teams = player_stats['FullTeamName'].to_list()
#positions = player_stats['#Position'].to_list()

teams = list(functions.dedupe(teams))
#positions = list(functions.dedupe(positions))

teams.insert(0, " ")
#positions.insert(0, " ")

player_stats['FullName'] = player_stats['#FirstName'] + ' ' + player_stats['#LastName']

######################      Layout of Streamlit app   ###############################################

st.set_page_config(layout="wide")

#st.title('Basketball Shooting Score Analysis of NBA Players in regular season 2016-2017')
st.markdown(f'<h1 style="color:red;">{"Basketball Shooting Score Analysis of NBA Players in regular season 2016-2017"}</h1>', unsafe_allow_html=True)

with st.expander('About this app'):
    st.write('This app shows the information and shooting position of NBA players in regular season 2016-2017.')
    st.image('https://pbs.twimg.com/profile_images/1392258537993211905/kYxkTjiE_400x400.jpg', width=200)
    
with st.expander('Five Main Roles in NBA Basketball'):
    st.write("""1. **Point Guard**: Often referred to as the **floor general**, 
            is typically the team's **primary ball-handler and playmaker**. They are responsible 
            for initiating the **team's offense**, setting up plays, and distributing the ball to their teammates. 
            Point guards are **skilled in dribbling, passing, and court vision**.""")
    st.write("""2. **Shooting Guard**: Also known as the off-guard or two-guard, is primarily 
            responsible for **scoring points**. They are usually an **excellent shooter from mid-range** and beyond the 
            three-point line. Shooting guards are often off-ball players, meaning they move without the ball to 
            get open for shots or cuts to the basket. They should have **good shooting accuracy**, the ability to 
            create their own shot.""")
    st.write("""3. **Small Forward**: Also known as the three, is a **versatile player** who can 
            contribute in various aspects of the game. They are often a **combination of a shooting guard and a 
            power forward**. Small forwards should possess a mix of **scoring ability, ball-handling skills**, 
            and **defensive prowess**. They can play inside the paint, **drive to the basket, shoot from mid-range**, 
            and even hit **three-pointers**.""")
    st.write("""4. **Power Forward**: Often referred to as the four, is typically a **strong and physical player** who 
            excels in both scoring and rebounding. They are skilled in scoring from close to the basket and 
            **mid-range jump shots**. Power forwards are responsible for **grabbing rebounds** on both ends of the 
            court, defending the paint, and setting screens to **create scoring opportunities** for their 
            teammates.""")
    st.write("""5. **Center**: Also known as the five or **big man**, is usually the **tallest player** on the team and plays close 
            to the basket. They are responsible for **rebounding, shot-blocking**, and defending the paint. 
            Centers often **score through dunks, layups, and close-range shots**. They also set screens, 
            roll to the basket for scoring opportunities, and protect the rim on defense.""")


st.sidebar.markdown(f'<h2 style="color:red;">{"Final Year Project"}</h2>', unsafe_allow_html=True)
#add select box to choose Team
st.sidebar.subheader('NBA Team')
nba_team = st.sidebar.selectbox('Choose a NBA Team to analyse?', teams)

#add select box to choose player
if(nba_team != ' '):
    players = player_stats[player_stats['FullTeamName']==nba_team]
    selected_team_players = players['FullName'].to_list()
    selected_team_players.insert(0, " ")

    # st.sidebar.subheader('Player Position')
    # player_position = st.sidebar.selectbox('Choose a player position', positions)

    st.sidebar.subheader('NBA player')
    nba_player = st.sidebar.selectbox('Choose a NBA basketball player', selected_team_players)
else:
    st.sidebar.write('Please select NBA Team')

    #Figure's image
    figure_folder = 'figure_images/'
    img_extension = '.jpg'
    fig1 = Image.open(figure_folder + 'age_distribution' + img_extension)
    fig2 = Image.open(figure_folder + 'barplot_favourite_shot_type' + img_extension)
    fig3 = Image.open(figure_folder + 'boxplot_age_position' + img_extension)
    fig4 = Image.open(figure_folder + 'boxplot_height_position' + img_extension)
    fig5 = Image.open(figure_folder + 'histogram_shot_distance' + img_extension)
    fig6 = Image.open(figure_folder + 'histogram_overall_percentage' + img_extension)
    fig7 = Image.open(figure_folder + 'shot_count' + img_extension)
    fig8 = Image.open(figure_folder + 'heatmap' + img_extension)

    st.header('Exploratory Data Analysis (EDA)')
    st.subheader('Top 10 Point Guards with the Highest Field Goal Percentange in NBA regular season 16-17')

    top10pg = pd.read_csv("TOP10PG.csv")
    st.write(top10pg)
    st.write("*** Only NBA players more than 40% Field Goal Percentage and Field Goal Attempted more than 1000 shots***")

    st.subheader('Age Distribution of NBA Players')
    st.image(fig1, width=500)
    st.subheader('Shot type count of NBA Players')
    st.image(fig2, width=500)
    st.subheader('Boxplot of Age according to position of NBA Players')
    st.image(fig3, width=500)
    st.subheader('Boxplot of Height according to position of NBA Players')
    st.image(fig4, width=500)
    st.subheader('Histogram of Shot Distance')
    st.image(fig5, width=500)
    st.subheader('Histogram of Overall Percentage of Point Guards')
    st.image(fig6, width=500)
    st.subheader('Shot count by distance based on 1000 sample data')
    st.image(fig7, width=500)
    st.subheader('Heatmap - Correlation between features')
    st.image(fig8, width=500)

if(nba_team != ' ' and nba_player != ' '):
    st.subheader('Results')
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
    length = len(height)
    feet = height[0]
    #inch = height[2]
    if len(height) == 5:
        inch = height[2] + height[3]
    elif len(height) == 4:
        inch = height[2]

    h_cm = functions.foot_to_cm(feet, inch)

    weight = player_stats['#Weight'][playerindex]
    birth_city = player_stats['#Birth City'][playerindex]
    kg = round(functions.lbs_to_kg(weight),2)

    total_games = player_stats['#GamesPlayed'][playerindex]
    Fg2PtAtt = player_stats['#Fg2PtAtt'][playerindex]
    Fg2PtMade = player_stats['#Fg2PtMade'][playerindex]
    Fg3PtAtt = player_stats['#Fg3PtAtt'][playerindex]
    Fg3PtMade = player_stats['#Fg3PtMade'][playerindex]
    FtAtt = player_stats['#FtAtt'][playerindex]
    FtMade = player_stats['#FtMade'][playerindex]
    
    FtPercentage = (FtMade/FtAtt)*100
    Fg2PtPercentage = (Fg2PtMade/Fg2PtAtt)*100
    Fg3PtPercentage = (Fg3PtMade/Fg3PtAtt)*100
    
    #Player's image
    st.subheader(fullname)
    img_folder = 'player_images/'
    img_extension = '.jpg'
    image = Image.open(img_folder + fullname + img_extension)

    st.image(image, width=300)
    
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
    
    st.write('Free Throw Percentage:', float('{:.2f}'.format(FtPercentage)), '%')
    st.write('2 Points Field Goal Percentage:', float('{:.2f}'.format(Fg2PtPercentage)), '%')
    st.write('3 Points Field Goal Percentage:', float('{:.2f}'.format(Fg3PtPercentage)), '%')

    selected_player_in_team = selected_team[(selected_team['shoot player'] == fullname)]
    st.subheader("Shot log of "+fullname)

    #FGM = Field Goal Made 0 - MISSED, 1 - SCORED
    selected_player_in_team['FGM'] = np.where(selected_player_in_team['current shot outcome'] == 'SCORED', '1', '0')

    #selected_player_in_team['shot_made'] = selected_player_in_team['shot_made'].mask(selected_player_in_team['current shot outcome'] == 'MISSED', 0)
    #selected_player_in_team['shot_made'] = selected_player_in_team['shot_made'].mask(selected_player_in_team['current shot outcome'] == 'SCORED', 1)

    st.write(selected_player_in_team)

    st.header('Data Visualization')
    #Plot Basketball court
    st.subheader('Shooting position in the basketball court')
    st.write("SCORED - Blue dot")
    st.write("MISSED - Red dot")
    fig, ax = functions.create_court(fullname)
    fig.patch.set_facecolor('xkcd:black')

    colors = {'0': 'red', '1': 'blue'}
    ax.scatter('location x', 'location y', c=selected_player_in_team['FGM'].map(colors), marker='o', s=100,
    lw=2, data=selected_player_in_team)
    st.write(fig)

