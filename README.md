# Predicting Spurs Total Points Per Game

My ORIGINAL goal for this project was originally to predict the total score of each NBA game throughout the season! However, after doing some research on similar projects, I realized I may not have the most effective tools/skills available to me right now. I definitely look forward to expanding on this project and eventually predict every game's total point outcome.

Given the time that we did have on this project, I'm happy with what I learned along the way. No, I definitely won't be taking this model to Vegas anytime soon, but I know I'll get better over time and implement new techniques.

# Executive Summary

- I acquired the NBA data from Kaggle: https://www.kaggle.com/nathanlauga/nba-games

- I used seasons 2013 - 2019, knowing I wanted to use the 2018-2019 season as my test set. 2019-2020 was suspended due to covid resumed in the bubble, and 2020-2021 was shortened

- While 2014-2016 was my train set, I included 2013 so I could get averages before the 2014 season started

- Speaking of, I had to create all averages columns, since there's no way I could input the actual values when I made a new prediction

- My top model was the LassoLars, although, none of my models were able to beat my mean baseline

- In retrospect, I think my total dataset was too small. My original thinking was to keep the years 'relevant' since I didn't think data from, let's say, 10 years ago would be applicable to more recent years

- None of my features had a strong correlation either, and with more time, I look forward to finding more features to add to my data that will help me predict the total score.

# Data Dictionary

| Feature                    | Datatype                | Definition   |
|:---------------------------|:------------------------|:-------------|
| GAME_DATE_EST              | datetime64[ns]          | date of each game |
| GAME_ID                    | int64                   | individual id for each game |
| SEASON                     | int64                   | start of the season year |
| TEAM_ID_home               | int64                   | individual id for the home team |
| PTS_home                   | float64                 | points scored by the home team |
| FG_PCT_home                | float64                 | percentage of field goals made by the home team |
| FT_PCT_home                | float64                 | percentage of free throws made by the home team |
| FG3_PCT_home               | float64                 | percentage of 3 point field goals made by the home team |
| AST_home                   | float64                 | home team assists|
| REB_home                   | float64                 | home team rebounds|
| TEAM_ID_away               | int64                   | individual id for the away team|
| PTS_away                   | float64                 | points scored by the away team|
| FG_PCT_away                | float64                 | percentage of field goals made by the away team|
| FT_PCT_away                | float64                 | percentage of free throws made by the away team|
| FG3_PCT_away               | float64                 | percentage of 3 point field goals made by the away team|
| AST_away                   | float64                 | away team assists|
| REB_away                   | float64                 | away team rebounds|
| HOME_TEAM_WINS             | int64                   | 1 or 0 for whether or not the home team wins|

Features engineered:
| Feature                    | Datatype                | Definition   |
|:---------------------------|:------------------------|:-------------|
| total_points               | float64                 | total points scored by home and away team |
| home_team                  | object                  | readable 3 letter abbreviation of the home team |
| away_team                  | object                  | readable 3 letter abbreviation of the away team |
| spurs_score                | float64                 | how many points the spurs scored each game |
| 5_game_avg_pts_home        | float64                 | five game rolling average of points scored by the spurs at home|
| 5_game_avg_pts_away        | float64                 | five game rolling average of points scored by the spurs away|
| 5_game_avg_fg_pct_home     | float64                 | five game rolling average of field goal percentage of spurs at home|
| 5_game_avg_fg_pct_away     | float64                 | five game rolling average of field goal percentage of spurs away|
| 5_game_avg_ft_pct_home     | float64                 | five game rolling average of free throw percentage of spurs at home|
| 5_game_avg_ft_pct_away     | float64                 | five game rolling average of free throw percentage of spurs away|
| 5_game_avg_fg3_pct_home    | float64                 | five game rolling average of 3 point fg percentage of spurs at home|
| 5_game_avg_fg3_pct_away    | float64                 | five game rolling average of 3 point fg percentage of spurs away|
| 5_game_avg_assists_home    | float64                 | five game rolling average of assists by spurs at home|
| 5_game_avg_assists_away    | float64                 | five game rolling average of assists by spurs away|
| 5_game_avg_rebounds_home   | float64                 | five game rolling average of rebounds by spurs at home|
| 5_game_avg_rebounds_away   | float64                 | five game rolling average of rebounds by spurs away|

# Project Planning

- Acquire Data from Kaggle
    - I used the games.csv that had the information for all games played from 2003 to 2021
- Prepare Data
    - Used Spurs data from 2013-2018 seasons
    - Create Spurs Score target variable
    = Engineered rolling average features
    - Scale data
- Explore Data
- Modeling
    - Created 4 models
    - LinearRegression (OLS)
    - LassoLars
    - Tweedie Regressor
    - Polynomial Regression
Evaluation
- Mean Baseline RMSE: 10.615598
- RMSE for Lasso + Lars
    - Training/In-Sample:  10.615597610059444 
    - Validation/Out-of-Sample:  11.163917076482761 
    - Test/Out-of-Sample:  14.586886040827023

# How to Reproduce This Project:
You will need to download the CSV's from this data set here: https://www.kaggle.com/nathanlauga/nba-games
All functions are available in my prepare and explore scripts