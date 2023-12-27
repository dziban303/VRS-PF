import csv

# this is the csv for vrs, should be untar'd and in the same directory as this script
csv_vrs = 'FullAircraft.csv'
csv_vrs_diff = 'pf_to_vrs_diffs.csv'
csv_vrs_header='AircraftID,FirstCreated,LastModified,ModeS,ModeSCountry,Country,Registration,CurrentRegDate,PreviousID,FirstRegDate,Status,DeRegDate,Manufacturer,ICAOTypeCode,Type,SerialNo,PopularName,GenericName,AircraftClass,Engines,OwnershipStatus,RegisteredOwners,MTOW,TotalHours,YearBuilt,CofACategory,CofAExpiry,UserNotes,Interested,UserTag,InfoURL,PictureURL1,PictureURL2,PictureURL3,UserBool1,UserBool2,UserBool3,UserBool4,UserBool5,UserString1,UserString2,UserString3,UserString4,UserString5,UserInt1,UserInt2,UserInt3,UserInt4,UserInt5,OperatorFlagCode\n'

# the full list of plane-alert csvs, processed one by one so the same logic could be used to download and process, rather than globbing plane-alert*.csv
#csvs_pf=['plane-alert-civ.csv','plane-alert-db.csv','plane-alert-gov.csv','plane-alert-mil.csv','plane-alert-pia.csv','plane-alert-pol.csv','plane-alert-ukraine.csv']
csvs_pf=['plane-alert-db.csv','plane-alert-ukraine.csv']
csv_pf_row0 = '$ICAO'
icaos_vrs=[]
rows_pf=[]

print('start')

# get all icaos from vrs and stuff them into an array so we can reference later
#with open(csv_vrs) as file_obj_vrs:
with open(csv_vrs, mode="r", encoding="utf-8", errors="ignore") as file_obj_vrs:

    reader_obj_vrs = csv.reader(file_obj_vrs)

    for row in reader_obj_vrs:

        icaos_vrs.append(row[3])

# go through the pf files and build an array of VRS formatted lines for entries that don't exist
for csv_pf in csvs_pf:

    with open(csv_pf) as file_obj_pf:
        
        reader_obj_pf = csv.reader(file_obj_pf)

        for row in reader_obj_pf:

            if row[0] != csv_pf_row0 and row[0] not in icaos_vrs:
                if len(row) > 2:
                    row_pf=f',,,{row[0]},,,{row[1]},,,,,,,{row[4]},{row[3]},,,,,,,{row[2]},,,,,,,,,,,,,,,,,,,,,,,,,,,,\n'
                else:
                    row_pf=f',,,{row[0]},,,{row[1]},,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,\n'
                rows_pf.append(row_pf)

# if we have something in our array then output to file
if len(rows_pf) > 0:

    with open(csv_vrs_diff,'w') as file_obj_vrs_diff:

        file_obj_vrs_diff.write(csv_vrs_header)
        file_obj_vrs_diff.writelines(rows_pf)

print('end')
