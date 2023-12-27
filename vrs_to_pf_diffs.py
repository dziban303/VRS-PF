import csv

# this is the csv for vrs, should be untar'd and in the same directory as this script
csv_vrs = 'FullAircraft.csv'
csv_vrs_diff = 'vrs_to_pf_diffs.csv'
csv_vrs_row0 = 'AircraftID'

# the full list of plane-alert csvs, processed one by one so the same logic could be used to download and process, rather than globbing plane-alert*.csv
#csvs_pf=['plane-alert-civ.csv','plane-alert-db.csv','plane-alert-gov.csv','plane-alert-mil.csv','plane-alert-pia.csv','plane-alert-pol.csv','plane-alert-twitter-blocked.csv','plane-alert-ukraine.csv']
csvs_pf=['plane-alert-db.csv','plane-alert-ukraine.csv']
csv_pf_header='$ICAO,$Registration,$Operator,$Type,$ICAO Type,#CMPG,$Tag 1,$#Tag 2,$#Tag 3,Category,$#Link\n'
icaos_pf=[]
rows_vrs=[]

print('start')

# go through the pf files and get all icaos and stuff them into an array so we can reference later
for csv_pf in csvs_pf:

    with open(csv_pf) as file_obj_pf:
        
        reader_obj_pf = csv.reader(file_obj_pf)

        for row in reader_obj_pf:

            icaos_pf.append(row[0])

#  read th VRS file and build an array of PF formatted lines for entries that don't exist
#with open(csv_vrs) as file_obj_vrs:
with open(csv_vrs, mode="r", encoding="utf-8", errors="ignore") as file_obj_vrs:
    
    reader_obj_vrs = csv.reader(file_obj_vrs)

    for row in reader_obj_vrs:

        if row[0] != csv_vrs_row0 and row[3] not in icaos_pf:
            row_vrs=f'{row[3]},{row[6]},{row[21]},{row[14]},{row[13]},,,,,,\n'
            rows_vrs.append(row_vrs)

# if we have something in our array then output to file
if len(rows_vrs) > 0:

    with open(csv_vrs_diff,'w') as file_obj_vrs_diff:

        file_obj_vrs_diff.write(csv_pf_header)
        file_obj_vrs_diff.writelines(rows_vrs)

print('end')
