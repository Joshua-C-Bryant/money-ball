import pandas as pd
import numpy as np

def clean_games_data(games):
    # Dropping HOME_TEAM_ID and VISITOR_TEAM_ID since their numbers 
    # are the same as TEAM_ID_home and TEAM_ID_away. Dropping Game_Status since its only
    # value is 'Final'
    games.drop(columns = ['HOME_TEAM_ID','VISITOR_TEAM_ID','GAME_STATUS_TEXT'], inplace = True)
    # Changing Game_Date_EST to datetime
    games['GAME_DATE_EST']= pd.to_datetime(games['GAME_DATE_EST'])
    # Dropping the 99 null rows in the DF
    games.drop(games[games.PTS_home.isnull()==True].index, inplace = True)
    # Creating the total points column, this will be our target
    games['total_points'] = games.PTS_home + games.PTS_away
    # Set the index and sort
    df = games.set_index('GAME_DATE_EST').sort_index()
    return df

# Create readable team label #

# This function creates readable 3 letter labels, taken from the ID's in the teams csv
def label_teams_home(df):
    if df['TEAM_ID_home'] == 1610612737:
        return 'ATL'
    if df['TEAM_ID_home'] == 1610612738:
        return 'BOS'
    if df['TEAM_ID_home'] == 1610612739:
        return 'CLE'
    if df['TEAM_ID_home'] == 1610612740:
        return 'NOP'
    if df['TEAM_ID_home']  == 1610612741:
        return 'CHI'
    if df['TEAM_ID_home'] == 1610612742:
        return 'DAL'
    if df['TEAM_ID_home'] == 1610612743:
        return 'DEN'
    if df['TEAM_ID_home'] == 1610612744:
        return 'GSW'
    if df['TEAM_ID_home'] == 1610612745:
        return 'HOU'
    if df['TEAM_ID_home'] == 1610612746:
        return 'LAC'
    if df['TEAM_ID_home'] == 1610612747:
        return 'LAL'
    if df['TEAM_ID_home'] == 1610612748:
        return 'MIA'
    if df['TEAM_ID_home'] == 1610612749:
        return 'MIL'
    if df['TEAM_ID_home'] == 1610612750:
        return 'MIN'
    if df['TEAM_ID_home'] == 1610612751:
        return 'BKN'
    if df['TEAM_ID_home'] == 1610612752:
        return 'NYK'
    if df['TEAM_ID_home'] == 1610612753:
        return 'ORL'
    if df['TEAM_ID_home'] == 1610612754:
        return 'IND'
    if df['TEAM_ID_home'] == 1610612755:
        return 'PHI'
    if df['TEAM_ID_home'] == 1610612756:
        return 'PHX'
    if df['TEAM_ID_home'] == 1610612757:
        return 'POR'
    if df['TEAM_ID_home'] == 1610612758:
        return 'SAC'
    if df['TEAM_ID_home'] == 1610612759:
        return 'SAS'
    if df['TEAM_ID_home'] == 1610612760:
        return 'OKC'
    if df['TEAM_ID_home'] == 1610612761:
        return 'TOR'
    if df['TEAM_ID_home'] == 1610612762:
        return 'UTA'
    if df['TEAM_ID_home'] == 1610612763:
        return 'MEM'
    if df['TEAM_ID_home'] == 1610612764:
        return 'WAS'
    if df['TEAM_ID_home'] == 1610612765:
        return 'DET'
    if df['TEAM_ID_home'] == 1610612766:
        return 'CHA'
    return 'Other'


# And for the away team ID
def label_teams_away(df):
    if df['TEAM_ID_away'] == 1610612737:
        return 'ATL'
    if df['TEAM_ID_away'] == 1610612738:
        return 'BOS'
    if df['TEAM_ID_away'] == 1610612739:
        return 'CLE'
    if df['TEAM_ID_away'] == 1610612740:
        return 'NOP'
    if df['TEAM_ID_away']  == 1610612741:
        return 'CHI'
    if df['TEAM_ID_away'] == 1610612742:
        return 'DAL'
    if df['TEAM_ID_away'] == 1610612743:
        return 'DEN'
    if df['TEAM_ID_away'] == 1610612744:
        return 'GSW'
    if df['TEAM_ID_away'] == 1610612745:
        return 'HOU'
    if df['TEAM_ID_away'] == 1610612746:
        return 'LAC'
    if df['TEAM_ID_away'] == 1610612747:
        return 'LAL'
    if df['TEAM_ID_away'] == 1610612748:
        return 'MIA'
    if df['TEAM_ID_away'] == 1610612749:
        return 'MIL'
    if df['TEAM_ID_away'] == 1610612750:
        return 'MIN'
    if df['TEAM_ID_away'] == 1610612751:
        return 'BKN'
    if df['TEAM_ID_away'] == 1610612752:
        return 'NYK'
    if df['TEAM_ID_away'] == 1610612753:
        return 'ORL'
    if df['TEAM_ID_away'] == 1610612754:
        return 'IND'
    if df['TEAM_ID_away'] == 1610612755:
        return 'PHI'
    if df['TEAM_ID_away'] == 1610612756:
        return 'PHX'
    if df['TEAM_ID_away'] == 1610612757:
        return 'POR'
    if df['TEAM_ID_away'] == 1610612758:
        return 'SAC'
    if df['TEAM_ID_away'] == 1610612759:
        return 'SAS'
    if df['TEAM_ID_away'] == 1610612760:
        return 'OKC'
    if df['TEAM_ID_away'] == 1610612761:
        return 'TOR'
    if df['TEAM_ID_away'] == 1610612762:
        return 'UTA'
    if df['TEAM_ID_away'] == 1610612763:
        return 'MEM'
    if df['TEAM_ID_away'] == 1610612764:
        return 'WAS'
    if df['TEAM_ID_away'] == 1610612765:
        return 'DET'
    if df['TEAM_ID_away'] == 1610612766:
        return 'CHA'
    return 'Other'

