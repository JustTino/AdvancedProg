import csv
import sqlite3

try:
    # Open the connection to the database
    with sqlite3.connect('my_database.db') as conn:
        cur = conn.cursor()

        # Drop the data from the table so that if we rerun the file, we don't repeat values
        conn.execute('DROP TABLE IF EXISTS deployments')
        print("Table dropped successfully")

        # Create the table again
        conn.execute('CREATE TABLE deployments (country_name TEXT, country_code TEXT, series_name TEXT, series_code TEXT, YR2000 REAL, YR2005 REAL, YR2010 REAL, YR2015 REAL, YR2020 REAL)')
        print("Table created successfully")

    # Open the file to read it into the database
    with open('P_Data_Extract_From_World_Development_Indicators (5)/b4f6bd8c-4a40-4289-9ae0-8eae291cbdce_Data.csv', newline='') as f:
        reader = csv.reader(f, delimiter=",")
        next(reader)  # Skip the header line
        for row in reader:
            try:
                country_name = row[0]
                country_code = row[1]
                series_name = row[2]
                series_code = row[3]

                # Handle non-numeric values with a try-except block
                YR2000 = float(row[4])
                YR2005 = float(row[5])
                YR2010 = float(row[6])
                YR2015 = float(row[7])
                YR2020 = float(row[8])

                cur.execute('INSERT INTO deployments VALUES (?,?,?,?,?,?,?,?,?)', (country_name, country_code, series_name, series_code, YR2000, YR2005, YR2010, YR2015, YR2020))
            except (ValueError, IndexError) as e:
                print(f"Error processing row {row}: {e}")

    print("Data parsed successfully")
    conn.commit()

except sqlite3.Error as e:
    print(f"SQLite error: {e}")

finally:
    if conn:
        conn.close()