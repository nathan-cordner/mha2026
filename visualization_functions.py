import pandas as pd
import matplotlib.pyplot as plt

# AI mission mapping
missions_to_countries = {
    "Argentine Mission": [],
    "Armenian Mission": ["Armenia"],
    "Australasian Mission": ["Australia", "New Zealand"],
    "Australian Mission": ["Australia"],
    "Brazilian Mission": [],
    "British Mission": ["United Kingdom", "Channel Islands", "Isle of Man", "Ireland"],
    "California Mission": ["United States"],
    "Canadian Mission": ["Canada"],
    "Carson Valley Mission": ["United States"],
    "Central Pacific Mission": ["Hawaii", "Japan"],
    "Central States Mission": ["United States"],
    "Colorado Mission": ["United States"],
    "Czechoslovak Mission": ["Czechoslovakia"],
    "Danish Mission": ["Denmark"],
    "Danish-Norwegian Mission": ["Denmark", "Norway"],
    "Early Church Mission: Asia": ["China", "India", "Japan"],
    "Early Church Mission: Europe": [
        "United Kingdom", "France", "Germany", "Italy",
        "Spain", "Switzerland", "Netherlands"
    ],
    "Early Church Mission: North America": [
        "United States", "Canada", "Mexico"
    ],
    "Early Church Mission: South America": ["Venezuela"],
    "East Central States Mission": ["United States"],
    "East German Mission": ["Germany", "Austria", "Switzerland"],
    "East Indian Mission": ["India"],
    "Eastern States Mission": ["United States"],
    "Elk Mountain Mission": ["United States"],
    "European Mission": [
        "United Kingdom", "France", "Germany", "Italy",
        "Spain", "Switzerland", "Netherlands"
    ],
    "French Mission": ["France", "Belgium", "Luxembourg", "Quebec"],
    "German Mission": ["Germany"],
    "German and Austrian Mission": ["Germany", "Austria", "Switzerland"],
    "Gibraltar Mission": ["Gibraltar"],
    "Hawaiian Mission": ["Hawaii"],
    "Hong Kong Mission": ["China"],
    "Iceland Mission": ["Iceland"],
    "Indian Territory Mission": ["United States"],
    "Irish Mission": ["Ireland", "United Kingdom"],
    "Italian Mission": ["Italy"],
    "Jamaica Mission": ["Jamaica"],
    "Japan Mission": ["Japan"],
    "Las Vegas Mission": ["United States"],
    "Malta Mission": ["Malta"],
    "Mexican Mission": ["Mexico"],
    "Middle States Mission": ["United States"],
    "Midwives and Nurses Mission": ["United States"],
    "Montana Mission": ["United States"],
    "Netherlands Mission": ["Netherlands"],
    "New England Mission": ["United States", "Nova Scotia", "New Brunswick", "Prince Edward Island", "Newfoundland and Labrador"],
    "New Zealand Mission": ["New Zealand"],
    "North Central States Mission": ["United States"],
    "Northern States Mission": ["United States"],
    "Northwestern States (Great Lakes) Mission": ["United States", "Canada"],
    "Northwestern States (Pacific) Mission": ["United States"],
    "Norwegian Mission": ["Norway"],
    "Palestine-Syrian Mission": ["Syria"],
    "Salmon River Mission": ["United States"],
    "Salt Lake Mission Home": ["United States"],
    "Samoan Mission": ["Samoa"],
    "Scandinavian Mission": [
        "Denmark", "Norway", "Sweden",
        "Finland", "Iceland", "Faroe Islands"
    ],
    "Shoshone Mission": ["United States"],
    "Siam Mission": [],
    "South African Mission": ["South Africa", "Zimbabwe", "Madagascar"],
    "South American Mission": ["Venezuela"],
    "Southern States Mission": ["United States"],
    "Southern Utah Mission": ["United States"],
    "Southwestern States Mission": ["United States"],
    "Spanish American Mission": ["Spain", "Mexico", "Venezuela"],
    "Swedish Mission": ["Sweden"],
    "Swiss Mission": ["Switzerland", "Germany", "Austria"],
    "Swiss and German Mission": ["Switzerland", "Germany", "Austria"],
    "Tahitian Mission": [],
    "Temple Square Mission": ["United States"],
    "Texas Mission": ["United States"],
    "The Tabernacle Choir at Temple Square Mission": ["United States"],
    "Tongan Mission": ["Tonga"],
    "Turkish Mission": ["Turkiye"],
    "Unspecified Native American Mission": ["United States"],
    "Welsh Mission": ["United Kingdom"],
    "West German Mission": ["Germany", "Switzerland", "Austria"],
    "Western States Mission": ["United States"],
    "White Mountain Mission": ["United States"]
}

# list all countries where language learning is less likely
lds_mission_languages = {
    "Argentine Mission": ["Spanish"],
    "Armenian Mission": ["Armenian", "Turkish"],
    "Australasian Mission": ["English"],
    "Australian Mission": ["English"],
    "Brazilian Mission": ["Portuguese"],
    "British Mission": ["English", "Welsh"],
    "California Mission": ["English", "Spanish"],
    "Canadian Mission": ["English", "French"],
    "Carson Valley Mission": ["English"],
    "Central Pacific Mission": ["English", "Hawaiian", "Samoan", "Tongan"],
    "Central States Mission": ["English"],
    "Colorado Mission": ["English"],
    "Czechoslovak Mission": ["Czech", "Slovak", "German"],
    "Danish Mission": ["Danish"],
    "Danish-Norwegian Mission": ["Danish", "Norwegian"],
    "Early Church Mission: Asia": ["Chinese", "Japanese", "Korean", "English"],
    "Early Church Mission: Europe": ["English", "German", "French", "Italian"],
    "Early Church Mission: North America": ["English", "French"],
    "Early Church Mission: South America": ["Spanish", "Portuguese"],
    "East Central States Mission": ["English"],
    "East German Mission": ["German"],
    "East Indian Mission": ["Hindi", "English"],
    "Eastern States Mission": ["English"],
    "Elk Mountain Mission": [],
    "European Mission": ["English", "German", "French", "Dutch", "Italian"],
    "French Mission": ["French"],
    "German Mission": ["German"],
    "German and Austrian Mission": ["German"],
    "Gibraltar Mission": ["English", "Spanish"],
    "Hawaiian Mission": ["Hawaiian", "English"],
    "Hong Kong Mission": ["Cantonese", "English"],
    "Iceland Mission": ["Icelandic"],
    "Indian Territory Mission": [],
    "Irish Mission": ["English", "Irish"],
    "Italian Mission": ["Italian"],
    "Jamaica Mission": ["English"],
    "Japan Mission": ["Japanese"],
    "Las Vegas Mission": ["English", "Spanish"],
    "Malta Mission": ["Maltese", "English"],
    "Mexican Mission": ["Spanish"],
    "Middle States Mission": ["English"],
    "Midwives and Nurses Mission": ["English"],
    "Montana Mission": ["English"],
    "Netherlands Mission": ["Dutch"],
    "New England Mission": ["English"],
    "New Zealand Mission": ["English", "Maori"],
    "North Central States Mission": ["English"],
    "Northern States Mission": ["English"],
    "Northwestern States (Great Lakes) Mission": ["English"],
    "Northwestern States (Pacific) Mission": ["English"],
    "Norwegian Mission": ["Norwegian"],
    "Palestine-Syrian Mission": ["Arabic", "Turkish"],
    "Salmon River Mission": [], # native american mission
    "Salt Lake Mission Home": ["English"],
    "Samoan Mission": ["Samoan"],
    "Scandinavian Mission": ["Danish", "Norwegian", "Swedish"],
    "Shoshone Mission": ["Shoshone"],
    "Siam Mission": ["Thai", "English"],
    "South African Mission": ["English", "Zulu", "Afrikaans", "Dutch"],
    "South American Mission": ["Spanish", "Portuguese"],
    "Southern States Mission": ["English"],
    "Southern Utah Mission": ["English"],
    "Southwestern States Mission": ["English", "Spanish"],
    "Spanish American Mission": ["Spanish"],
    "Swedish Mission": ["Swedish"],
    "Swiss Mission": ["German", "French"],
    "Swiss and German Mission": ["German", "French"],
    "Tahitian Mission": ["Tahitian", "French"],
    "Temple Square Mission": ["English", "Spanish", "French"],
    "Texas Mission": ["English", "Spanish"],
    "The Tabernacle Choir at Temple Square Mission": ["English"],
    "Tongan Mission": ["Tongan"],
    "Turkish Mission": ["Turkish"],
    "Unspecified Native American Mission": [], # native american mission
    "Welsh Mission": ["Welsh", "English"],
    "West German Mission": ["German"],
    "Western States Mission": ["English"],
    "White Mountain Mission": [] # native american mission
}

language_to_countries = {
    "Afrikaans": ["South Africa", "Zimbabwe"],
    "Arabic": ["Syria"],
    "Armenian": ["Armenia"],
    "Cantonese": ["China"],
    #"Cherokee": ["United States"], # filtering out native american languages
    "Chinese": ["China"],
    "Czech": ["Czechoslovakia"],
    "Danish": ["Denmark", "Faroe Islands"],
    "Dutch": ["Belgium", "Netherlands"],
    "English": [ # add south africa, zimbabwe, india, etc?
        "Australia",
        "Canada",
        "Channel Islands",
        "Gibraltar",
        "Hawaii",
        "Ireland",
        "Isle of Man",
        "Jamaica",
        "New Zealand",
        "Saint Vincent and the Grenadines",
        "United Kingdom",
        "United States"
    ],
    "French": ["France", "Quebec", "Belgium", "Switzerland", "Luxembourg"],
    "German": ["Austria", "Germany", "Switzerland", "Luxembourg"],
    "Hawaiian": ["Hawaii"],
    "Hindi": ["India"],
    "Icelandic": ["Iceland"],
    "Irish": ["Ireland"],
    "Italian": ["Italy"],
    "Japanese": ["Japan"],
    "Korean": [],
    "Maltese": ["Malta"],
    "Maori": ["New Zealand"],
    "Norwegian": ["Norway"],
    "Portuguese": ["Brazil"],
    "Samoan": ["Samoa"],
    "Shoshone": ["United States"],
    "Slovak": ["Czechoslovakia"],
    "Spanish": ["Mexico", "Spain", "Venezuela"],
    "Swedish": ["Sweden"],
    "Tahitian": [],
    "Thai": [],
    "Tongan": ["Tonga"],
    "Turkish": ["Turkiye"],
    "Welsh": ["United Kingdom"],
    "Zulu": ["South Africa", "Zimbabwe"]
}


def served_in_country_count(df, filter_mission = None):
    total = 0
    parent = 0

    if not filter_mission == None:
        filter_df = df[df["mission"] == filter_mission]
    else:
        filter_df = df

    years = list(range(1850, 1941))
    # initialize counts
    born_in_country = {x : 0 for x in years}
    parent_from_country = {x : 0 for x in years}
    neither = {x: 0 for x in years}
    
    for i in range(len(filter_df)):
        cur_mission = str(filter_df["mission"].iloc[i]).strip()
        cur_year = filter_df["year"].iloc[i]

        birth_country = str(filter_df["birth_place_country"].iloc[i])
        birth_state = str(filter_df["birth_place_state"].iloc[i])

        parent1_birth_country = str(filter_df["parent1_birthplace_country"].iloc[i])
        parent1_birth_state = str(filter_df["parent1_birthplace_state"].iloc[i])
        parent2_birth_country = str(filter_df["parent2_birthplace_country"].iloc[i])
        parent2_birth_state = str(filter_df["parent2_birthplace_state"].iloc[i])
              
        flag = False
        
        if birth_country in missions_to_countries[cur_mission] or birth_state in missions_to_countries[cur_mission]:
            total += 1
            born_in_country[cur_year] += 1
            flag = True
    
        if not flag:
            # check parents

            if parent1_birth_country in missions_to_countries[cur_mission] or parent1_birth_state in missions_to_countries[cur_mission] or parent2_birth_country in missions_to_countries[cur_mission] or parent2_birth_state in missions_to_countries[cur_mission]:
                parent += 1
                parent_from_country[cur_year] += 1
                flag = True
        if not flag:
            # export to file for review?
            neither[cur_year] += 1
            
    print("Served in home country:", total, len(filter_df), round(total / len(filter_df) * 100, 2))
    print("Including parent home country:", total + parent, len(filter_df), round((total + parent) / len(filter_df) * 100, 2))

    data_dict = {"year" : years,
                 "born_in_country": [born_in_country[x] for x in years],
                 "parent_from_country": [parent_from_country[x] for x in years],
                 "neither": [neither[x] for x in years]}
    
    formatted_df = pd.DataFrame(data_dict)
    formatted_df.set_index("year", inplace = True)    
    
    return formatted_df


def mission_counts_stacked_bars(mission_count_df, title):
    
    fig, ax = plt.subplots()

    mission_count_df.plot.bar(stacked=True, ax = ax, rot = 0, color = [plt.cm.tab20(0), plt.cm.tab20(1), "lightgray"])

    ax.set_xticks(range(0, 91, 10))
    ax.set_title(title)
    
    plt.show()
    
    
def mission_proportions_stacked_bars(mission_count_df, title):
    # convert counts to percentages
    
    proportion_df = mission_count_df.copy()
    columns = ["born_in_country", "parent_from_country", "neither"]
    for c in columns:
        proportion_df[c] = proportion_df[c].astype('float')
    
    for i in range(len(proportion_df)):        
        total = proportion_df["born_in_country"].iloc[i] + \
                proportion_df["parent_from_country"].iloc[i] + \
                proportion_df["neither"].iloc[i]
        
        if total > 0:
            for c in columns:
                proportion_df.loc[i + 1850, c] = (proportion_df[c].iloc[i] / total) * 100
                
    # proportion_df.to_csv("proportion_df.csv")
    
    fig, ax = plt.subplots()

    proportion_df.plot.bar(stacked=True, ax = ax, rot = 0, color = [plt.cm.tab20(0), plt.cm.tab20(1), "lightgray"])

    ax.set_xticks(range(0, 91, 10))
    ax.set_title(title)
    ax.legend(bbox_to_anchor=(1.01, 1))
    
    plt.show()