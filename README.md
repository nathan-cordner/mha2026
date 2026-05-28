Starting point:  mission_data_clean.csv from MHA 2025 GitHub
-- manual cleaning of mission bio links in spreadsheet, converting instances of "unknown" back to "nan" (silly numpy)

01 Get FamilySearch Links notebook -- gathers FamilySearch links from missionary profiles, then runs webscraper to access birthplace information about parents of missionaries
-- warning:  scraping data for ~50,000 missionary bios takes a few days!

02 Birthplace Cleaning -- uses AI generated script to standardize birthplace locations, extracting state and country information.
-- Some manual cleaning occurred after this for non-standard locations like people born "At Sea" (replaced with location that family had just departed from)
-- Also added Canadian provinces, which were not included in the script

03 Mission Duration -- scrapes data about mission length from mission bios and calculates number of months served 

04 Add Language Learning Features -- creates and applies the formula that designates whether missionaries were language-learners or not
-- formula considers missionary birthplace, residence at time of call, mission name, areas served in within mission, mission call year, mission length, and parental birthplaces 
-- notebook also includes initial data analysis and visualizations

05 Cleaned Visuals -- visualizes language-learning information found in "language_classification.csv"