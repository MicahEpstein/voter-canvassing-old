#!/usr/bin/env python3

import pathlib
import concurrent.futures
import csv
import pdb
import click
import io
import json
import requests
import sys
import time

from data_dicts import FULL_VOTER_EXPORT_HEADER, CENSUS_GEOCODE_RESULT_HEADER

CUT_VOTER_EXPORT_HEADER = [
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

    "TIGER/Line Match Status",
    "TIGER/Line Match Type",
    "TIGER/Line Matched Address",
    "TIGER/Line Lng/Lat",

    "Last Vote Date",  # (Date)  MM/DD/YYYY
    "Precinct Code",  # (String)  
    "Precinct Split ID",  # (String)  
    "Date Last Changed",  # (Date)  MM/DD/YYYYY
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

@click.group()
def process_site_data():
    pass

@process_site_data.command()
@click.argument('voter_export_infile', type=click.File('rU'))
@click.argument('geocoded_addresses_infile', type=click.File('rU'))
@click.argument('cut_files_folder', type=click.Path(exists=True))
@click.option('--format', default='csv')
def cut_turf(voter_export_infile, geocoded_addresses_infile, cut_files_folder, format):
    writers = {}

    reader = csv.DictReader(geocoded_addresses_infile)
    geos = {row['ID Number']: row for row in reader}

    reader = csv.DictReader(voter_export_infile, fieldnames=FULL_VOTER_EXPORT_HEADER, delimiter='\t')
    for record in reader:
        precinct = record['Precinct Code']
        voter_id = record['ID Number']
        geo = geos[voter_id]

        record['TIGER/Line Match Status'] = geo['Match Status']
        record['TIGER/Line Match Type'] = geo['Match Type']
        record['TIGER/Line Matched Address'] = geo['Matched Address']
        record['TIGER/Line Lng/Lat'] = geo['Lng/Lat']

        if precinct not in writers:
            precinct_outfile_path = pathlib.Path(cut_files_folder) / f'{precinct}.{format}'

            if format == 'jsonl':
                writers[precinct] = precinct_outfile_path.open(mode='w')
            elif format == 'csv':
                writers[precinct] = csv.DictWriter(precinct_outfile_path.open(mode='w'), fieldnames=CUT_VOTER_EXPORT_HEADER, extrasaction='ignore')
                writers[precinct].writeheader()

        if format == 'jsonl':
            writers[precinct].write(json.dumps(record) + '\n')
        elif format== 'csv':
            writers[precinct].writerow(record)

@process_site_data.command()
@click.argument('voter_export_infile', type=click.File('rU'))
@click.argument('geocoded_outfile', type=click.File('w'))
def geocode_voters(voter_export_infile, geocoded_outfile):
    data_to_geocode = []
    reader = csv.DictReader(voter_export_infile, fieldnames=FULL_VOTER_EXPORT_HEADER, delimiter='\t')

    geocode_futures = []
    group_count = 0

    with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
        def send_latest_data_to_geocoder():
            nonlocal group_count
            nonlocal data_to_geocode

            group_count += 1
            print(f'Queueing {len(data_to_geocode)} addresses in group {group_count}...', file=sys.stderr)
            future = executor.submit(geocode_voters, data_to_geocode[:], group_count)
            geocode_futures.append(future)
            data_to_geocode = []

        for voter_row in reader:
            uniq_id = voter_row['ID Number']
            address = ' '.join(filter(None, [
                voter_row['House Number'],
                voter_row['House Number Suffix'],
                voter_row['Street Name']
            ]))
            city = voter_row['City']
            state = voter_row['State']
            zipcode = voter_row['Zip']

            row_to_geocode = (uniq_id, address, city, state, zipcode)
            data_to_geocode.append(row_to_geocode)
            
            if len(data_to_geocode) == 5_000:
                send_latest_data_to_geocoder()

        if data_to_geocode:
            send_latest_data_to_geocoder()
        
        writer = csv.writer(geocoded_outfile)
        writer.writerow(CENSUS_GEOCODE_RESULT_HEADER)
        for future in geocode_futures:
            writer.writerows(future.result())

def geocode_voters(data_to_geocode, group_count):
    buffer = io.StringIO()
    writer = csv.writer(buffer)
    writer.writerows(data_to_geocode)

    start = time.time()
    print(f'Geocoding {len(data_to_geocode)} addresses in group {group_count}...', file=sys.stderr)
    response = requests.post(
        'https://geocoding.geo.census.gov/geocoder/locations/addressbatch',
        data={'benchmark': 'Public_AR_Current'},
        files={'addressFile': ('addresses.csv', buffer.getvalue())}
    )
    print(f'Geocoded {len(data_to_geocode)} addresses in group {group_count} in {time.time() - start} seconds...', file=sys.stderr)
    reader = csv.reader(io.StringIO(response.text))
    return list(reader)

if __name__ == '__main__':
    process_site_data()