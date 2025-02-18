import pymongo
import csv

client = pymongo.MongoClient("localhost", 27017)
db = client["data5000"]
collection_clean_data = db["data_clean"]
collection_nt_focus = db["national_focus"]

with open('data/data_clean_v3.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow([
        "C_YEAR", "C_MNTH", "C_WDAY", "C_HOUR", "C_SEV", "C_VEHS", "C_CONF", "C_RCFG", "C_WTHR", "C_RSUR",
        "C_RALN", "C_TRAF", "V_ID", "V_TYPE", "V_YEAR", "P_ID", "P_SEX", "P_AGE", "P_PSN", "P_ISEV",
        "P_SAFE", "P_USER", "C_CASE", "CAR_AGE"
    ])

    for data in collection_clean_data.find():
        # print(data)
        if data['P_SEX'] == 'M':
            data['P_SEX'] = '1'
        elif data['P_SEX'] == 'F':
            data['P_SEX'] = '0'
        car_age = int(data['C_YEAR']) - int(data['V_YEAR'])
        if car_age < 0: car_age = 0
        writer.writerow([
            int(data['C_YEAR']), int(data['C_MNTH']), int(data['C_WDAY']), int(data['C_HOUR']), int(data['C_SEV']),
            int(data['C_VEHS']), int(data['C_CONF']), int(data['C_RCFG']), int(data['C_WTHR']), int(data['C_RSUR']),
            int(data['C_RALN']), int(data['C_TRAF']), int(data['V_ID']), int(data['V_TYPE']), int(data['V_YEAR']),
            int(data['P_ID']), int(data['P_SEX']), int(data['P_AGE']), int(data['P_PSN']), int(data['P_ISEV']),
            int(data['P_SAFE']), int(data['P_USER']), int(data['C_CASE']), car_age
        ])
        # print("Insert 1 row...")
        if int(data['P_PSN']) == 11 and int(data['V_TYPE']) == 1 and (int(data['P_SAFE']) == 1 or int(data['P_SAFE']) == 2 or int(data['P_SAFE']) == 13):
            collection_nt_focus.insert_one(data)

    print("job complete!")
