import pandas as pd
import random
from itertools import combinations
from pandas import DataFrame
import streamlit as st
#import plotly.express as px


#df = pd.read_excel("players.xlsx")
# Create an empty list
#players = []
# Iterate over each row
#for index, rows in df.iterrows():
    # Create list for the current row
 #   my_list = [rows.Player,rows.Level]
    # append the list to the final list
  #  players.append(my_list)

def power(player):
   return int(player)
def tpower(team):
    tp=0
    for i in team:
        tp+=power(i[1])
    return tp
def powerdiff(team1,team2):
    diff=abs(tpower(team1)-tpower(team2))
    return diff
#def displayteams(bal1teams):


#    print("-----------")
    #    print(bal1teams[0], "Score:", tpower(bal1teams[0]))
    #    print(bal1teams[1], "Score:", tpower(bal1teams[1]))
    #    print("-----------")

def balance(players):
    perteam=int(len(players)/2)
    #print ("Players per team:",perteam)

    comb = combinations(players, perteam)

    min=1000
    team1=[]
    team2=[]
    balteams=[]
    balteam = []
    c=0
    for i in comb:
        c=c+1
        t1=i
        t2= [p for p in players if p not in t1]

        diff=powerdiff(t1,t2)
        if diff<min:
            min=powerdiff(t1,t2)
            team1=t1
            team2=t2
            balteam.clear()
            balteam.append(t1[:])
            balteam.append(t2[:])
            balteams.clear()
            balteams.append(balteam[:])

        elif diff==min:
            balteam.clear()
            balteam.append(t1[:])
            balteam.append(t2[:])
            balteams.append(balteam[:])
    return balteams
# print("Balanced team :")
#displayteams(random.choice(balteams))

st.title("Ranked Balanced Team Generator V 0.1")
st.markdown("Made by MuddassirLateef")
st.sidebar.title("Help")
st.sidebar.header("Format for entering Players:")
st.sidebar.markdown("<Player1>,<Player1Level>")
st.sidebar.markdown("<Player2>,<Player2Level>")
st.sidebar.header("Example:")
st.sidebar.markdown("John,2")
st.sidebar.markdown("Drake,3")
st.sidebar.markdown("Alex,4")
st.sidebar.markdown("Sam,2")


st.info("Only enter even number of players,\nit will automatically split it into two teams \nand make the most balanced teams based on rank")
s = st.text_area("Enter Teams below and press Ctrl+Enter to Apply:","",200)
x=[]
players=[]
for i in s.splitlines():
    x.clear()
    for j in i.split(','):
        x.append(j)
    players.append(x[:])
balteams=balance(players)
st.button('Regenerate')
st.balloons()
selectedteam = random.choice(balteams)

df1 = DataFrame(selectedteam[0],columns=['Name','Level'])
df2 = DataFrame(selectedteam[1],columns=['Name','Level'])
st.dataframe(df1.style.highlight_max())
st.text("Total Power:"+str(tpower(selectedteam[0])))
st.dataframe(df2.head())
st.text("Total Power:"+str(tpower(selectedteam[1])))
