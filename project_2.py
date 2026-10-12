import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv(r"C:\Users\user\Downloads\final_dataset.csv.zip")

#reading csv file
def reading_csv():
    
    df = pd.read_csv(r"C:\Users\user\Downloads\final_dataset.csv.zip")
    print(df.head(10))
    print("*"*60)
    print(df.info())
    print("*"*60)
    print(df.tail(5))
    print("*"*60)
    print(df.describe())
    print("*"*60)
    print(df.shape)
    print("*"*60)
    print(df.size)
    print("*"*60)
    print(df.ndim)
    print("*"*60)
    print(df.index)
    print("*"*60)
    print(df.dtypes)
    print("*"*60)
    


def Data_Cleaning():
    print()
    print(df.isna().sum())
    print("*"*60)
    
    for key,value in df.iterrows():
        if (value == 0).any():
            df.drop(key, inplace = True)
            
    print("*"*60)
    
    print(df.duplicated().sum())
    print("*"*60)
    
    print(df.drop_duplicates(inplace = True))
    print("*"*60)
    
    df["Date"] = pd.to_datetime(df['Date'])
    print("*"*60)
    print(df.dtypes)
    print("Data Cleaning is done ")
    print("*"*60)
   

# selection and filtering:

def home_away_goals(goals,teams):
    
    FTHG = df[df['FTHG']>goals]
    FTAG = df[df['FTAG']>goals]
    
    home = df[(df["HomeTeam"]).isin(teams) & (df["FTHG"]>goals)]
    away = df[(df["AwayTeam"]).isin(teams) & (df["FTAG"]>goals)]
    
    home_goals = (home.groupby("HomeTeam")["FTHG"].sum())
    
    away_goals = (away.groupby("AwayTeam")["FTAG"].sum())
    
    data = pd.DataFrame({
        
        "Matches": [FTHG.shape[0],FTAG.shape[0]],
        "Type": ["Home goals", "Away goals"],
        
        })
    
    data_1 = pd.DataFrame({
        
        "Home Goals": home_goals,
        "Away Goals": away_goals
        
        }).fillna(0)
    
    total_goals = data_1["Home Goals"] + data_1["Away Goals"]
    
    sns.barplot(x = data["Matches"], y = data["Type"])
    plt.title("Home goals Vs Away goals")
    plt.xlabel("Number of Teams")
    plt.show()
    
    plt.pie(
        total_goals,
        labels=total_goals.index,
        autopct="%1.2f%%",
        startangle=90
    )

    plt.title(f"Total Goals Scored by {teams}")
    plt.show()
    
    plt.pie(
        data_1["Home Goals"],
        labels = data_1.index,
        autopct = "%1.2f%%",
        startangle = 90
        
        )
    
    plt.title(f"Home goals for {teams}")
    plt.show()
    
    plt.pie(
        data_1["Away Goals"],
        labels = data_1.index,
        autopct = "%1.2f%%",
        startangle = 90
        
        )
    
    plt.title(f"Away goals for {teams}")
    plt.show()
    
    

def top_bottom_5():
    
    hg = df.groupby("HomeTeam")["FTHG"].sum()
    ag = df.groupby("HomeTeam")["FTAG"].sum()
    
    top_home = hg.nlargest(5)
    bottom_home = hg.nsmallest(5)
    
    top_away = ag.nlargest(5)
    bottom_away = ag.nsmallest(5)
    
    data = pd.DataFrame({
        
        "data": [top_home.sum(),bottom_home.sum()],
        "Type": ["Top goals", "bottom goals"],
        "data_1": [top_away.sum(),bottom_away.sum()]
        
        })
    
    plt.pie(data["data"], labels = data["Type"], autopct = "%1.1f%%", startangle = 90)
    plt.show()
    
    plt.pie(data["data_1"], labels = data["Type"], autopct = "%1.1f%%", startangle = 90)
    plt.show()
    
    print("Top 5 teams scored highest goals in home ground:")
    print(top_home)
    print()
    print("*"*50)
    
    print("Top 5 teams scored lowest goals in home ground:")
    print(bottom_home)
    print()
    print("*"*50)
    
    print("Top 5 teams scored highest goals in away ground:")
    print(top_away)
    print()
    print("*"*50)
    
    print("Top 5 teams scored lowest goals in away ground:")
    print(bottom_away)
    print()
    print("*"*50)
    
def info():
    
    print(df.info())
    
info()
    
def goals(mini_goals,maxi_goals):
    
    total_goals = df.groupby("HomeTeam")[["FTHG","FTAG"]].sum()
    
    print(total_goals.head(5))
    print("*"*60)
    print()
    
    home_goal = df.groupby("HomeTeam")["FTHG"].sum()
    away_goal = df.groupby("HomeTeam")["FTAG"].sum()
    
    totals = np.add(home_goal,away_goal)
    
    result = totals[totals.between(mini_goals,maxi_goals)]
    
    print(result)
    
    plt.pie(result, labels = result.index, autopct = "%1.1f%%", startangle = 90)
    plt.show()
    

def team_name(team):
    
    team_name = (df[df["HomeTeam"].str.lower().str.contains(team) | df["AwayTeam"].str.lower().str.contains(team)])
    
    print(team_name)
    print()
    print("*"*50)
    
    home = df[df["HomeTeam"].str.lower().str.contains(team)]
    away = df[df["AwayTeam"].str.lower().str.contains(team)]
    
    data = pd.Series({
        
        "Home": len(home),
        "Away": len(away),
        
        })
    
    
    print(data)
    print()
    print(data.value_counts())
    print(data.agg(['sum']))
    details = team_name["FTR"].map({"H": "Home Win", "A": "Away Win","D": "Draw"}).value_counts()
    
    plt.pie(details, labels = details.index, autopct = "%1.2f%%", startangle = 90)
    plt.title(f"Home win Vs Away win of {team}")
    plt.show()
    
    plt.scatter(x = "Home", y = "Away", data = data)
    plt.title(f"Home win Vs Away win of {team}")
    plt.show()
    
    plt.hist(data["Home"])
    plt.title(f"Home win of {team}")
    plt.show()
    
    plt.boxplot(data["Home"])
    plt.title(f"Home win of {team}")
    plt.show()
    
    
    
    
def pivot_table():
    
    pivot = pd.pivot_table(
        df,
        values=["FTHG", "FTAG"],
        index="HomeTeam",
        aggfunc=["mean", "sum", "count"]
    )
    
    print(pivot)
    


    
        


        
        
    
    

    
    


    



    


    
    
    
    
    
    
