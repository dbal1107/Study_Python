from teample import Teample

teamLists =[
    {
        "name": "김소희",
        "gender": "여",
        "birth": "4/13",
        "age": 26,
        "mbti": "ESTJ"
    },
    {
        "name": "차선영",
        "gender": "여",
        "birth": "8/14",
        "age": 25,
        "mbti": "ESTP"
    },
    {
        "name": "전유미",
        "gender": "여",
        "birth": "11/7",
        "age": 31,
        "mbti": "ISTP"
    },
    {
        "name": "최서윤",
        "gender": "여",
        "birth": "9/12",
        "age": 26,
        "mbti": "INFJ"
    },
    {
        "name": "최윤아",
        "gender": "여",
        "birth": "11/20",
        "age": 25,
        "mbti": "ENFJ"
    }
]
teamList =[]
for idx in range(len(teamLists)):
    teamList.append(Teample(
        idx+1,
        teamLists[idx]["name"],
        teamLists[idx]["gender"],
        teamLists[idx]["birth"],
        teamLists[idx]["age"],
        teamLists[idx]["mbti"]
    ))

for team in teamList:
    print(team.name)
    print(team.mbti)

# print(teamLists)

# print("*"*13)
# for team in teamLists:
#     print("*",team.get("name").center(7),"*")
# print("*"*13)


# print(teamList[0].values())
# print(teamList[0]["name"])
# print(teamList[0].get("birth"))#값찾기
# teamList[0]["age"]=2 #위치찾기
# teamList[1]["birth"]=1
#
# for team in teamList:
#     print(team.get("m_name"))
#     print(team.get("rank"))