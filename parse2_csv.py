import csv
import sqlite3

# Open the connection to the database
with sqlite3.connect('my_database.db') as conn:
    cur = conn.cursor()

    # Drop the data from the table so that if we rerun the file, we don't repeat values
    conn.execute('DROP TABLE IF EXISTS deployments')
    print("Table dropped successfully")

    # Create the table again
    conn.execute('CREATE TABLE deployments (country_name TEXT, country_code TEXT, series_name TEXT, series_code TEXT, YR2000 REAL, YR2005 REAL, YR2010 REAL, YR2015 REAL, YR2020 REAL)')
    print("Table created successfully")
# open the file to read it into the database
with open('P_Data_Extract_From_Sustainable_Development_Goals_(SDGs)/b9b9f13f-4057-4993-b3f0-34e42abc3fe6_Data.csv', newline='') as f:
    reader = csv.reader(f, delimiter=",")
    next(reader) # skip the header line
    for row in reader:
        print(row)

        country_name = row[0]
        country_code = row[1]
        series_name = row[2]
        series_code = row[3]
        # Handle non-numeric values with a try-except block
        try:
            YR2000 = float(row[4])
            YR2005 = float(row[5])
            YR2010 = float(row[6])
            YR2015 = float(row[7])
            YR2020 = float(row[8])
        except ValueError:
            # This replaces each non-numeric value with a default value "None"
            YR2000 = None
            YR2005 = None
            YR2010 = None
            YR2015 = None
            YR2020 = None

        cur.execute('INSERT INTO deployments VALUES (?,?,?,?,?,?,?,?,?)', (country_name, country_code, series_name, series_code, YR2000, YR2005, YR2010, YR2015, YR2020))
    print("data parsed successfully");
    conn.commit()
conn.close()
with open('P_Data_Extract_From_World_Development_Indicators (5)/b4f6bd8c-4a40-4289-9ae0-8eae291cbdce_Data.csv', newline='') as f:
  reader = csv.reader(f, delimiter=",")
  next(reader) # skip the header line
  for row in reader:
    print(row)

