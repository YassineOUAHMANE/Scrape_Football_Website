import requests 
from bs4 import BeautifulSoup
import csv

date = input("Enter la date des matches que vous voulez voir sous cette forme mm/dd/yyyy:")
page = requests.get(f"https://www.yallakora.com/match-center/%D9%85%D8%B1%D9%83%D8%B2-%D8%A7%D9%84%D9%85%D8%A8%D8%A7%D8%B1%D9%8A%D8%A7%D8%AA?date={date}")

# Testing HTTP protocol, we got 200 so we got successful responses
print(page.status_code)  # test if we are allowed to scrap the website
soup = BeautifulSoup(page.text, "lxml")  # get the script of Html
matches_details = []
championships = soup.find_all("div", {'class': 'matchCard'})

for championship in championships:
    champion_title = championship.contents[1].find("h2").text.strip()
    All_matches = championship.contents[3].find_all("div")
    number_of_matches = len(All_matches)

    for i in range(number_of_matches):
        # get teams name
        try:
            team_A = All_matches[i].find("div", {'class': 'teamA'}).text.strip()
        except Exception as e:
          continue

        try:
            team_B = All_matches[i].find("div", {'class': 'teamB'}).text.strip()
        except Exception as e:
            continue      
      # get_score  
        match_result = All_matches[i].find("div", {'class': 'MResult'}).find_all("span", {"class": "score"})
        print(match_result)
        try:
         Result1=match_result[0].text.strip()
        except :
           continue 
        try:
          Result2=match_result[1].text.strip()
        except :
           continue  
        score = f"{Result1} - {Result2}"

        # get_match_time
        match_time = All_matches[i].find("div", {"class", "MResult"}).find("span", {"class": "time"}).text.strip()

        # add_match_info_details
        matches_details.append({
            "نوع البطولة": champion_title,
            "الفريق الاول ": team_A,
            "الفريق الثاني": team_B,
            "وقت المباراة": match_time,
            "نتيجة المباراة": score
        })
       


    keys = matches_details[0].keys()
    with open("C:\\Users\\YASSINE\\Desktop\\Scrapper un site de football\\matches_details.csv", "w") as output_file:
        dict_writer = csv.DictWriter(output_file, keys)
        dict_writer.writeheader()
        dict_writer.writerows(matches_details)
        print("file created")
        
    
