"""
PA Voter Export Data Dictionary - 2019 Dec 06
"""

FULL_VOTER_EXPORT_HEADER = [
    "ID Number",  # (String)  SURE Voter ID number
    "Title",  # (String)  
    "Last Name",  # (String)  
    "First Name",  # (String)  
    "Middle Name",  # (String)  
    "Suffix",  # (String)  
    "Gender",  # (String)  F=Female, M=Male, U=Unknown
    "DOB",  # (Date)  MM/DD/YYYY
    "Registration Date",  # (Date)  MM/DD/YYYY
    "Voter Status",  # (String)  A=Active, I=Inactive
    "Status Change Date",  # (Date)  MM/DD/YYYY
    "Party Code",  # (String)  See Political Party Code documentation
    "House Number",  # (String)  Residential
    "House Number Suffix",  # (String)  Residential
    "Street Name",  # (String)  Residential
    "Apartment Number",  # (String)  Residential
    "Address Line 2",  # (String)  Residential
    "City",  # (String)  Residential
    "State",  # (String)  Residential
    "Zip",  # (String)  Residential
    "Mail Address 1",  # (String)  Mailing
    "Mail Address 2",  # (String)  Mailing
    "Mail City",  # (String)  Mailing
    "Mail State",  # (String)  Mailing
    "Mail Zip",  # (String)  Mailing
    "Last Vote Date",  # (Date)  MM/DD/YYYY
    "Precinct Code",  # (String)  
    "Precinct Split ID",  # (String)  
    "Date Last Changed",  # (Date)  MM/DD/YYYYY
    "Custom Data 1",  # (String)  Legacy system ID number
    "District 1",  # (String)  See Zone Code and Zone Type documentation for District 1 to District 40
    "District 2",  # (String)  
    "District 3",  # (String)  
    "District 4",  # (String)  
    "District 5",  # (String)  
    "District 6",  # (String)  
    "District 7",  # (String)  
    "District 8",  # (String)  
    "District 9",  # (String)  
    "District 10",  # (String)  
    "District 11",  # (String)  
    "District 12",  # (String)  
    "District 13",  # (String)  
    "District 14",  # (String)  
    "District 15",  # (String)  
    "District 16",  # (String)  
    "District 17",  # (String)  
    "District 18",  # (String)  
    "District 19",  # (String)  
    "District 20",  # (String)  
    "District 21",  # (String)  
    "District 22",  # (String)  
    "District 23",  # (String)  
    "District 24",  # (String)  
    "District 25",  # (String)  
    "District 26",  # (String)  
    "District 27",  # (String)  
    "District 28",  # (String)  
    "District 29",  # (String)  
    "District 30",  # (String)  
    "District 31",  # (String)  
    "District 32",  # (String)  
    "District 33",  # (String)  
    "District 34",  # (String)  
    "District 35",  # (String)  
    "District 36",  # (String)  
    "District 37",  # (String)  
    "District 38",  # (String)  
    "District 39",  # (String)  
    "District 40",  # (String)  
    "Election 1 Vote Method",  # (String)  See Election Map documentation for Election 1 to Election 40. AP=At Polls, AB=Absentee, MB = Mail-In Ballot, P=Provisional
    "Election 1 Party",  # (String)  See Political Party Code documentation for Election 1 to Election 40.
    "Election 2 Vote Method",  # (String)  
    "Election 2 Party",  # (String)  
    "Election 3 Vote Method",  # (String)  
    "Election 3 Party",  # (String)  
    "Election 4 Vote Method",  # (String)  
    "Election 4 Party",  # (String)  
    "Election 5 Vote Method",  # (String)  
    "Election 5 Party",  # (String)  
    "Election 6 Vote Method",  # (String)  
    "Election 6 Party",  # (String)  
    "Election 7 Vote Method",  # (String)  
    "Election 7 Party",  # (String)  
    "Election 8 Vote Method",  # (String)  
    "Election 8 Party",  # (String)  
    "Election 9 Vote Method",  # (String)  
    "Election 9 Party",  # (String)  
    "Election 10 Vote Method",  # (String)  
    "Election 10 Party",  # (String)  
    "Election 11 Vote Method",  # (String)  
    "Election 11 Party",  # (String)  
    "Election 12 Vote Method",  # (String)  
    "Election 12 Party",  # (String)  
    "Election 13 Vote Method",  # (String)  
    "Election 13 Party",  # (String)  
    "Election 14 Vote Method",  # (String)  
    "Election 14 Party",  # (String)  
    "Election 15 Vote Method",  # (String)  
    "Election 15 Party",  # (String)  
    "Election 16 Vote Method",  # (String)  
    "Election 16 Party",  # (String)  
    "Election 17 Vote Method",  # (String)  
    "Election 17 Party",  # (String)  
    "Election 18 Vote Method",  # (String)  
    "Election 18 Party",  # (String)  
    "Election 19 Vote Method",  # (String)  
    "Election 19 Party",  # (String)  
    "Election 20 Vote Method",  # (String)  
    "Election 20 Party",  # (String)  
    "Election 21 Vote Method",  # (String)  
    "Election 21 Party",  # (String)  
    "Election 22 Vote Method",  # (String)  
    "Election 22 Party",  # (String)  
    "Election 23 Vote Method",  # (String)  
    "Election 23 Party",  # (String)  
    "Election 24 Vote Method",  # (String)  
    "Election 24 Party",  # (String)  
    "Election 25 Vote Method",  # (String)  
    "Election 25 Party",  # (String)  
    "Election 26 Vote Method",  # (String)  
    "Election 26 Party",  # (String)  
    "Election 27 Vote Method",  # (String)  
    "Election 27 Party",  # (String)  
    "Election 28 Vote Method",  # (String)  
    "Election 28 Party",  # (String)  
    "Election 29 Vote Method",  # (String)  
    "Election 29 Party",  # (String)  
    "Election 30 Vote Method",  # (String)  
    "Election 30 Party",  # (String)  
    "Election 31 Vote Method",  # (String)  
    "Election 31 Party",  # (String)  
    "Election 32 Vote Method",  # (String)  
    "Election 32 Party",  # (String)  
    "Election 33 Vote Method",  # (String)  
    "Election 33 Party",  # (String)  
    "Election 34 Vote Method",  # (String)  
    "Election 34 Party",  # (String)  
    "Election 35 Vote Method",  # (String)  
    "Election 35 Party",  # (String)  
    "Election 36 Vote Method",  # (String)  
    "Election 36 Party",  # (String)  
    "Election 37 Vote Method",  # (String)  
    "Election 37 Party",  # (String)  
    "Election 38 Vote Method",  # (String)  
    "Election 38 Party",  # (String)  
    "Election 39 Vote Method",  # (String)  
    "Election 39 Party",  # (String)  
    "Election 40 Vote Method",  # (String)  
    "Election 40 Party",  # (String)  
    "Home Phone",  # (String)  
    "County",  # (String)  County Name the voter is currently registered in.
    "Mail Country",  # (String)  
]

ZONE_TYPE_EXPORT_HEADER = [
    "County Name",  # (String)  "County the file is exported for. Ex. ADAMS, CUMBERLAND, DAUPHIN, etc."
    "Zone Number",  # (Int)  "District field found in the voter export. Ex. 1, 2, 3, etc."
    "Zone Short Name",  # (String)  Ex. Prec, WD, SC, STH, STS, USC, etc.
    "Zone Long Name",  # (String)  "Description. Ex. Precinct, Ward, School District, State House, State Senate, U.S. Congress, etc."
]

ZONE_CODE_EXPORT_HEADER = [
    "County Name",  # (String)  "County the file is exported for. Ex. ADAMS, CUMBERLAND, DAUPHIN, etc."
    "Zone Number",  # (Int)  "Appropriate district field found in the voter export. Ex. 1, 2, 3, etc."
    "Zone Code",  # (String)  "Code found in the district field located in the voter export. Ex. MN11, JD402, 11-1, etc."
    "Zone Description",  # (String)  "Description of the Zone Code. Ex. MAIN TOWNSHIP, 123 JUDICIAL DISTRICT, JONES TOWNSHIP, etc."
]

ELECTION_MAPPING_HEADER = [
    "County Name",  # (String)  "County the file is exported for. Ex. ADAMS, CUMBERLAND, DAUPHIN, etc."
    "Election Number",  # (Int)  "Appropriate election field found in the voter export. Ex. 5, 1, 7, etc."
    "Election Description",  # (String)  "Name of the election setup by the county. Ex. 2006 General Primary, 2000 General, etc."
    "Election Date",  # (Date)  MM/DD/YYYY
]

CENSUS_GEOCODE_RESULT_HEADER = [
    'ID Number',
    'Sent Address', 
    'Match Status', 
    'Match Type', 
    'Matched Address', 
    'Lng/Lat', 
    'TIGER/Line ID', 
    'Street Side',
]

