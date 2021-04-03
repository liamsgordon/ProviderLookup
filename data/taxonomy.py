import csv
import sys
import psycopg2
import psycopg2.extras

# notes: insert index, lookup relational database normalization,
# notes: force null to make text into int, date. etc. Use var char instead of text
# notes: build associated table for taxonomy and NPI file

#connects to pgAdmin 4 database
conn = psycopg2.connect(
            host='localhost',
            user = "postgres",
            database="lookup",
            password = "liam15",
            port = "5432"
            )
print("connection")
#connection is established

#cursor is intiated
cur = conn.cursor()

#CREATE ID COLUMN - as first column (hidden column)

#creates an empty table with the columns we desire
cur.execute('DROP TABLE IF EXISTS taxonomy')
cur.execute('''
CREATE TABLE "taxonomy" (
    Index INT, 
    Code VARCHAR,
    Grouping VARCHAR,
    Classification VARCHAR,
    Specialization VARCHAR,
    Definition VARCHAR,
    Effective_Date VARCHAR,
    Deactivation VARCHAR,
    Last_Modified_Date VARCHAR,
    Notes VARCHAR,
    display VARCHAR
);
''')

print("created table")
#table intiated

#asks for input in terminal and will auto input the CSV file we want
fname = input('Enter the taxonomy csv file name')
if len(fname) < 1 : fname= "nucc_taxonomy_210.csv"

with open(fname) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter= ',')
    next(csv_file)
    count = 1
    for row in csv_reader:
        #print(row)
        Index=count # call it ID
        count+=1
        Code1=row[0]
        Grouping=row[1]
        Classification=row[2]
        Specialization=row[3]
        Definition=row[4]
        Effective_Date=row[5]
        Deactivation=row[6]
        Last_Modified_Date=row[7]
        Notes=row[8]
        display=row[9]
        query =  "INSERT INTO taxonomy (Index, Code, Grouping, Classification, Specialization, Definition, Effective_Date, Deactivation, Last_Modified_Date, Notes, display) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);"
        data = (Index, Code1, Grouping, Classification, Specialization, Definition, Effective_Date, Deactivation, Last_Modified_Date, Notes, display)
        cur.execute(query, data)
        conn.commit()
        


cur.close()
conn.close()