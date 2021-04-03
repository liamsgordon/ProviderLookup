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
cur.execute('DROP TABLE IF EXISTS npicheck')
cur.execute('''
CREATE TABLE "npicheck" (
    NPI INT,
    Entity_Type_Code VARCHAR,
    Replacement_NPI VARCHAR,
    Employer_Identification_Number VARCHAR,
    Provider_Organization_Name VARCHAR,
    Provider_Last_Name VARCHAR,
    Provider_First_Name VARCHAR,
    Provider_Middle_Name VARCHAR,
    Provider_Name_Prefix_Text VARCHAR,
    Provider_Name_Suffix_Text VARCHAR,
    Provider_Credential_Text VARCHAR,
    Provider_Other_Organization_Name VARCHAR,
    Provider_Other_Organization_Name_Type_Code VARCHAR,
    Provider_Other_Last_Name VARCHAR,
    Provider_Other_First_Name VARCHAR,
    Provider_Other_Middle_Name VARCHAR,
    Provider_Other_Name_Prefix_Text VARCHAR,
    Provider_Other_Name_Suffix_Text VARCHAR,
    Provider_Other_Credential_Text VARCHAR,
    Provider_Other_Last_Name_Type_Code VARCHAR,
    Provider_First_Line_Business_Mailing_Address VARCHAR,
    Provider_Second_Line_Business_Mailing_Address VARCHAR,
    Provider_Business_Mailing_Address_City_Name VARCHAR,
    Provider_Business_Mailing_Address_State_Name VARCHAR,
    Provider_Business_Mailing_Address_Postal_Code VARCHAR,
    Provider_Business_Mailing_Address_Country_Code_If_outside_US VARCHAR,
    Provider_Business_Mailing_Address_Telephone_Number VARCHAR,
    Provider_Business_Mailing_Address_Fax_Number VARCHAR,
    Provider_First_Line_Business_Practice_Location_Address VARCHAR,
    Provider_Second_Line_Business_Practice_Location_Address VARCHAR,
    Provider_Business_Practice_Location_Address_City_Name VARCHAR,
    Provider_Business_Practice_Location_Address_State_Name VARCHAR,
    Provider_Business_Practice_Location_Address_Postal_Code VARCHAR,
    Provider_Business_Practice_Location_Address_Country_Code VARCHAR,
    Provider_Business_Practice_Location_Address_Telephone_Number VARCHAR,
    Provider_Business_Practice_Location_Address_Fax_Number VARCHAR,
    Provider_Enumeration_Date VARCHAR,
    Last_Update_Date VARCHAR,
    NPI_Deactivation_Reason_Code VARCHAR,
    NPI_Deactivation_Date VARCHAR,
    NPI_Reactivation_Date VARCHAR,
    Provider_Gender_Code VARCHAR,
    Authorized_Official_Last_Name VARCHAR,
    Authorized_Official_First_Name VARCHAR,
    Authorized_Official_Middle_Name VARCHAR,
    Authorized_Official_Title_or_Position VARCHAR,
    Authorized_Official_Telephone_Number VARCHAR,
    Healthcare_Provider_Taxonomy_Code_1 VARCHAR,
    Grouping VARCHAR,
    Classification VARCHAR,
    Specialization VARCHAR,
    Definition VARCHAR,
    Effective_Date VARCHAR,
    Deactivation VARCHAR,
    Last_Modified_Date VARCHAR,
    Notes VARCHAR,
    Display_Name VARCHAR,
    Provider_License_Number_1 VARCHAR,
    Provider_License_Number_State_Code_1 VARCHAR,
    Healthcare_Provider_Primary_Taxonomy_Switch_1 VARCHAR,
    Healthcare_Provider_Taxonomy_Code_Code_2 VARCHAR,
    Provider_License_Number_2 VARCHAR,
    Provider_License_Number_State_Code_2 VARCHAR,
    Healthcare_Provider_Primary_Taxonomy_Switch_2 VARCHAR, 
    Healthcare_Provider_Taxonomy_Code_Code_3 VARCHAR,
    Provider_License_Number_3 VARCHAR,
    Provider_License_Number_State_Code_3 VARCHAR,
    Healthcare_Provider_Primary_Taxonomy_Switch_3 VARCHAR,
    Healthcare_Provider_Taxonomy_Code_Code_4 VARCHAR,
    Provider_License_Number_4 VARCHAR,
    Provider_License_Number_State_Code_4 VARCHAR,
    Healthcare_Provider_Primary_Taxonomy_Switch_4 VARCHAR,
    Healthcare_Provider_Taxonomy_Code_Code_5 VARCHAR,
    Provider_License_Number_5 VARCHAR,
    Provider_License_Number_State_Code_5 VARCHAR,
    Healthcare_Provider_Primary_Taxonomy_Switch_5 VARCHAR, 
    Healthcare_Provider_Taxonomy_Code_Code_6 VARCHAR,
    Provider_License_Number_6 VARCHAR,
    Provider_License_Number_State_Code_6 VARCHAR,
    Healthcare_Provider_Primary_Taxonomy_Switch_6 VARCHAR,
    Healthcare_Provider_Taxonomy_Code_Code_7 VARCHAR,
    Provider_License_Number_7 VARCHAR,
    Provider_License_Number_State_Code_7 VARCHAR,
    Healthcare_Provider_Primary_Taxonomy_Switch_7 VARCHAR,
    Healthcare_Provider_Taxonomy_Code_Code_8 VARCHAR,
    Provider_License_Number_8 VARCHAR,
    Provider_License_Number_State_Code_8 VARCHAR,
    Healthcare_Provider_Primary_Taxonomy_Switch_8 VARCHAR,
    Healthcare_Provider_Taxonomy_Code_Code_9 VARCHAR,
    Provider_License_Number_9 VARCHAR,
    Provider_License_Number_State_Code_9 VARCHAR,
    Healthcare_Provider_Primary_Taxonomy_Switch_9 VARCHAR,
    Provider_License_Number_10 VARCHAR,
    Provider_License_Number_State_Code_10 VARCHAR,
    Healthcare_Provider_Primary_Taxonomy_Switch_10 VARCHAR,
    Healthcare_Provider_Taxonomy_Code_Code_11 VARCHAR,
    Provider_License_Number_11 VARCHAR,
    Provider_License_Number_State_Code_11 VARCHAR,
    Healthcare_Provider_Primary_Taxonomy_Switch_11 VARCHAR,
    Healthcare_Provider_Taxonomy_Code_Code_12 VARCHAR,
    Provider_License_Number_12 VARCHAR,
    Provider_License_Number_State_Code_12 VARCHAR,
    Healthcare_Provider_Primary_Taxonomy_Switch_12 VARCHAR, 
    Healthcare_Provider_Taxonomy_Code_Code_13 VARCHAR,
    Provider_License_Number_13 VARCHAR,
    Provider_License_Number_State_Code_13 VARCHAR,
    Healthcare_Provider_Primary_Taxonomy_Switch_13 VARCHAR, 
    Healthcare_Provider_Taxonomy_Code_Code_14 VARCHAR,
    Provider_License_Number_14  VARCHAR,
    Provider_License_Number_State_Code_14 VARCHAR,
    Healthcare_Provider_Primary_Taxonomy_Switch_14 VARCHAR, 
    Healthcare_Provider_Taxonomy_Code_Code_15 VARCHAR,
    Provider_License_Number_15 VARCHAR,
    Provider_License_Number_State_Code_15 VARCHAR,
    Healthcare_Provider_Primary_Taxonomy_Switch_15 VARCHAR,
    Other_Provider_Identifier_1 VARCHAR,
    Other_Provider_Identifier_Type_Code_1 VARCHAR,
    Other_Provider_Identifier_State_1 VARCHAR,
    Other_Provider_Identifier_Issuer_1 VARCHAR,
    Other_Provider_Identifier_2 VARCHAR,
    Other_Provider_Identifier_Type_Code_2 VARCHAR,
    Other_Provider_Identifier_State_2 VARCHAR,
    Other_Provider_Identifier_Issuer_2 VARCHAR,
    Other_Provider_Identifier_3 VARCHAR,
    Other_Provider_Identifier_Type_Code_3 VARCHAR,
    Other_Provider_Identifier_State_3 VARCHAR,
    Other_Provider_Identifier_Issuer_3 VARCHAR,
    Other_Provider_Identifier_4 VARCHAR,
    Other_Provider_Identifier_Type_Code_4 VARCHAR,
    Other_Provider_Identifier_State_4 VARCHAR,
    Other_Provider_Identifier_Issuer_4 VARCHAR,
    Other_Provider_Identifier_5 VARCHAR,
    Other_Provider_Identifier_Type_Code_5 VARCHAR,
    Other_Provider_Identifier_State_5 VARCHAR,
    Other_Provider_Identifier_Issuer_5 VARCHAR,
    Other_Provider_Identifier_6 VARCHAR,
    Other_Provider_Identifier_Type_Code_6 VARCHAR,
    Other_Provider_Identifier_State_6 VARCHAR,
    Other_Provider_Identifier_Issuer_6 VARCHAR,
    Other_Provider_Identifier_7 VARCHAR,
    Other_Provider_Identifier_Type_Code_7 VARCHAR,
    Other_Provider_Identifier_State_7 VARCHAR,
    Other_Provider_Identifier_Issuer_7 VARCHAR,
    Other_Provider_Identifier_8 VARCHAR,
    Other_Provider_Identifier_Type_Code_8 VARCHAR,
    Other_Provider_Identifier_State_8 VARCHAR,
    Other_Provider_Identifier_Issuer_8 VARCHAR,
    Other_Provider_Identifier_9 VARCHAR,
    Other_Provider_Identifier_Type_Code_9 VARCHAR,
    Other_Provider_Identifier_State_9 VARCHAR,
    Other_Provider_Identifier_Issuer_9 VARCHAR,
    Other_Provider_Identifier_10 VARCHAR,
    Other_Provider_Identifier_Type_Code_10 VARCHAR,
    Other_Provider_Identifier_State_10 VARCHAR,
    Other_Provider_Identifier_Issuer_10 VARCHAR,
    Other_Provider_Identifier_11 VARCHAR,
    Other_Provider_Identifier_Type_Code_11 VARCHAR,
    Other_Provider_Identifier_State_11 VARCHAR,
    Other_Provider_Identifier_Issuer_11 VARCHAR,
    Other_Provider_Identifier_12 VARCHAR,
    Other_Provider_Identifier_Type_Code_12 VARCHAR,
    Other_Provider_Identifier_State_12 VARCHAR,
    Other_Provider_Identifier_Issuer_12 VARCHAR,
    Other_Provider_Identifier_13 VARCHAR,
    Other_Provider_Identifier_Type_Code_13 VARCHAR,
    Other_Provider_Identifier_State_13 VARCHAR,
    Other_Provider_Identifier_Issuer_13 VARCHAR,
    Other_Provider_Identifier_14 VARCHAR,
    Other_Provider_Identifier_Type_Code_14 VARCHAR,
    Other_Provider_Identifier_State_14 VARCHAR,
    Other_Provider_Identifier_Issuer_14 VARCHAR,
    Other_Provider_Identifier_15 VARCHAR,
    Other_Provider_Identifier_Type_Code_15 VARCHAR,
    Other_Provider_Identifier_State_15 VARCHAR,
    Other_Provider_Identifier_Issuer_15 VARCHAR,
    Other_Provider_Identifier_16 VARCHAR,
    Other_Provider_Identifier_Type_Code_16 VARCHAR,
    Other_Provider_Identifier_State_16 VARCHAR,
    Other_Provider_Identifier_Issuer_16 VARCHAR,
    Other_Provider_Identifier_17 VARCHAR,
    Other_Provider_Identifier_Type_Code_17 VARCHAR,
    Other_Provider_Identifier_State_17 VARCHAR,
    Other_Provider_Identifier_Issuer_17 VARCHAR,
    Other_Provider_Identifier_18 VARCHAR,
    Other_Provider_Identifier_Type_Code_18 VARCHAR,
    Other_Provider_Identifier_State_18 VARCHAR,
    Other_Provider_Identifier_Issuer_18 VARCHAR,
    Other_Provider_Identifier_19 VARCHAR,
    Other_Provider_Identifier_Type_Code_19 VARCHAR,
    Other_Provider_Identifier_State_19 VARCHAR,
    Other_Provider_Identifier_Issuer_19 VARCHAR,
    Other_Provider_Identifier_20 VARCHAR,
    Other_Provider_Identifier_Type_Code_20 VARCHAR,
    Other_Provider_Identifier_State_20 VARCHAR,
    Other_Provider_Identifier_Issuer_20 VARCHAR,
    Other_Provider_Identifier_21 VARCHAR,
    Other_Provider_Identifier_Type_Code_21 VARCHAR,
    Other_Provider_Identifier_State_21 VARCHAR,
    Other_Provider_Identifier_Issuer_21 VARCHAR,
    Other_Provider_Identifier_22 VARCHAR,
    Other_Provider_Identifier_Type_Code_22 VARCHAR,
    Other_Provider_Identifier_State_22 VARCHAR,
    Other_Provider_Identifier_Issuer_22 VARCHAR,
    Other_Provider_Identifier_23 VARCHAR,
    Other_Provider_Identifier_Type_Code_23 VARCHAR,
    Other_Provider_Identifier_State_23 VARCHAR,
    Other_Provider_Identifier_Issuer_23 VARCHAR,
    Other_Provider_Identifier_24 VARCHAR,
    Other_Provider_Identifier_Type_Code_24 VARCHAR,
    Other_Provider_Identifier_State_24 VARCHAR,
    Other_Provider_Identifier_Issuer_24 VARCHAR,
    Other_Provider_Identifier_25 VARCHAR,
    Other_Provider_Identifier_Type_Code_25 VARCHAR,
    Other_Provider_Identifier_State_25 VARCHAR,
    Other_Provider_Identifier_Issuer_25 VARCHAR,
    Other_Provider_Identifier_26 VARCHAR,
    Other_Provider_Identifier_Type_Code_26 VARCHAR,
    Other_Provider_Identifier_State_26 VARCHAR,
    Other_Provider_Identifier_Issuer_26 VARCHAR,
    Other_Provider_Identifier_27 VARCHAR,
    Other_Provider_Identifier_Type_Code_27 VARCHAR,
    Other_Provider_Identifier_State_27 VARCHAR,
    Other_Provider_Identifier_Issuer_27 VARCHAR,
    Other_Provider_Identifier_28 VARCHAR,
    Other_Provider_Identifier_Type_Code_28 VARCHAR,
    Other_Provider_Identifier_State_28 VARCHAR,
    Other_Provider_Identifier_Issuer_28 VARCHAR,
    Other_Provider_Identifier_29 VARCHAR,
    Other_Provider_Identifier_Type_Code_29 VARCHAR,
    Other_Provider_Identifier_State_29 VARCHAR,
    Other_Provider_Identifier_Issuer_29 VARCHAR,
    Other_Provider_Identifier_30 VARCHAR,
    Other_Provider_Identifier_Type_Code_30 VARCHAR,
    Other_Provider_Identifier_State_30 VARCHAR,
    Other_Provider_Identifier_Issuer_30 VARCHAR,
    Other_Provider_Identifier_31 VARCHAR,
    Other_Provider_Identifier_Type_Code_31 VARCHAR,
    Other_Provider_Identifier_State_31 VARCHAR,
    Other_Provider_Identifier_Issuer_31 VARCHAR,
    Other_Provider_Identifier_32 VARCHAR,
    Other_Provider_Identifier_Type_Code_32 VARCHAR,
    Other_Provider_Identifier_State_32 VARCHAR,
    Other_Provider_Identifier_Issuer_32 VARCHAR,
    Other_Provider_Identifier_33 VARCHAR,
    Other_Provider_Identifier_Type_Code_33 VARCHAR,
    Other_Provider_Identifier_State_33 VARCHAR,
    Other_Provider_Identifier_Issuer_33 VARCHAR,
    Other_Provider_Identifier_34 VARCHAR,
    Other_Provider_Identifier_Type_Code_34 VARCHAR,
    Other_Provider_Identifier_State_34 VARCHAR,
    Other_Provider_Identifier_Issuer_34 VARCHAR,
    Other_Provider_Identifier_35 VARCHAR,
    Other_Provider_Identifier_Type_Code_35 VARCHAR,
    Other_Provider_Identifier_State_35 VARCHAR,
    Other_Provider_Identifier_Issuer_35 VARCHAR,
    Other_Provider_Identifier_36 VARCHAR,
    Other_Provider_Identifier_ype_Code_36 VARCHAR,
    Other_Provider_Identifier_State_36 VARCHAR,
    Other_Provider_Identifier_Issuer_36 VARCHAR,
    Other_Provider_Identifier_37 VARCHAR,
    Other_Provider_Identifier_Type_Code_37 VARCHAR,
    Other_Provider_Identifier_State_37 VARCHAR,
    Other_Provider_Identifier_Issuer_37 VARCHAR,
    Other_Provider_Identifier_38 VARCHAR,
    Other_Provider_Identifier_Type_Code_38 VARCHAR,
    Other_Provider_Identifier_State_38 VARCHAR,
    Other_Provider_Identifier_Issuer_38 VARCHAR,
    Other_Provider_Identifier_39 VARCHAR,
    Other_Provider_Identifier_Type_Code_39 VARCHAR,
    Other_Provider_Identifier_State_39 VARCHAR,
    Other_Provider_Identifier_Issuer_39 VARCHAR,
    Other_Provider_Identifier_40 VARCHAR,
    Other_Provider_Identifier_Type_Code_40 VARCHAR,
    Other_Provider_Identifier_State_40 VARCHAR,
    Other_Provider_Identifier_Issuer_40 VARCHAR,
    Other_Provider_Identifier_41 VARCHAR,
    Other_Provider_Identifier_Type_Code_41 VARCHAR,
    Other_Provider_Identifier_State_41 VARCHAR,
    Other_Provider_Identifier_Issuer_41 VARCHAR,
    Other_Provider_Identifier_42 VARCHAR,
    Other_Provider_Identifier_Type_Code_42 VARCHAR,
    Other_Provider_Identifier_State_42 VARCHAR,
    Other_Provider_Identifier_Issuer_42 VARCHAR,
    Other_Provider_Identifier_43 VARCHAR,
    Other_Provider_Identifier_Type_Code_43 VARCHAR,
    Other_Provider_Identifier_State_43 VARCHAR,
    Other_Provider_Identifier_Issuer_43 VARCHAR,
    Other_Provider_Identifier_44 VARCHAR,
    Other_Provider_Identifier_Type_Code_44 VARCHAR,
    Other_Provider_Identifier_State_44 VARCHAR,
    Other_Provider_Identifier_Issuer_44 VARCHAR,
    Other_Provider_Identifier_45 VARCHAR,
    Other_Provider_Identifier_Type_Code_45 VARCHAR,
    Other_Provider_Identifier_State_45 VARCHAR,
    Other_Provider_Identifier_Issuer_45 VARCHAR,
    Other_Provider_Identifier_46 VARCHAR,
    Other_Provider_Identifier_Type_Code_46 VARCHAR,
    Other_Provider_Identifier_State_46 VARCHAR,
    Other_Provider_Identifier_Issuer_46 VARCHAR,
    Other_Provider_Identifier_47 VARCHAR,
    Other_Provider_Identifier_Type_Code_47 VARCHAR,
    Other_Provider_Identifier_State_47 VARCHAR,
    Other_Provider_Identifier_Issuer_47 VARCHAR,
    Other_Provider_Identifier_48 VARCHAR,
    Other_Provider_Identifier_Type_Code_48 VARCHAR,
    Other_Provider_Identifier_State_48 VARCHAR,
    Other_Provider_Identifier_Issuer_48 VARCHAR, 
    Other_Provider_Identifier_49 VARCHAR,
    Other_Provider_Identifier_Type_Code_49 VARCHAR,
    Other_Provider_Identifier_State_49 VARCHAR,
    Other_Provider_Identifier_Issuer_49 VARCHAR,
    Other_Provider_Identifier_50 VARCHAR,
    Other_Provider_Identifier_Type_Code_50 VARCHAR,
    Other_Provider_Identifier_State_50 VARCHAR,
    Other_Provider_Identifier_Issuer_50 VARCHAR,
    Is_Sole_Proprietor VARCHAR,
    Is_Organization_Subpart VARCHAR,
    Parent_Organization_LBN VARCHAR,
    Parent_Organization_TIN VARCHAR,
    Authorized_Official_Name_Prefix_Text VARCHAR,
    Authorized_Official_Name_Suffix_Text VARCHAR,
    Authorized_Official_Credential_Text VARCHAR,                                                                                                                                                                                                       
    Healthcare_Provider_Taxonomy_Group_1 VARCHAR,
    Healthcare_Provider_Taxonomy_Group_2 VARCHAR,    
    Healthcare_Provider_Taxonomy_Group_3 VARCHAR,    
    Healthcare_Provider_Taxonomy_Group_4 VARCHAR,
    Healthcare_Provider_Taxonomy_Group_5 VARCHAR,
    Healthcare_Provider_Taxonomy_Group_6 VARCHAR,
    Healthcare_Provider_Taxonomy_Group_7 VARCHAR,
    Healthcare_Provider_Taxonomy_Group_8 VARCHAR,
    Healthcare_Provider_Taxonomy_Group_9 VARCHAR,
    Healthcare_Provider_Taxonomy_Group_10 VARCHAR,
    Healthcare_Provider_Taxonomy_Group_11 VARCHAR,
    Healthcare_Provider_Taxonomy_Group_12 VARCHAR,
    Healthcare_Provider_Taxonomy_Group_13 VARCHAR,
    Healthcare_Provider_Taxonomy_Group_14 VARCHAR,
    Healthcare_Provider_Taxonomy_Group_15 VARCHAR,
    Certification_Date VARCHAR
);
''')

print("created table")
#table intiated

fname = input('Enter the crossectional csv file name')
if len(fname) < 1 : fname= "npidata_pfile_20050523-20210307.csv"

count = 1

with open(fname) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter= ',')
    next(csv_file)
    for row in csv_reader:
        Index=count
        count+=1
        NPI=int(row[0])
        Entity_Type_Code=row[1]
        Replacement_NPI=row[2]
        Employer_Identification_Number=row[3]
        Provider_Organization_Name=row[4]
        Provider_Last_Name=row[5]
        Provider_First_Name=row[6]
        Provider_Middle_Name=row[7]
        Provider_Name_Prefix_Text=row[8]
        Provider_Name_Suffix_Text=row[9]
        Provider_Credential_Text=row[10]
        Provider_Other_Organization_Name=row[11]
        Provider_Other_Organization_Name_Type_Code=row[12]
        Provider_Other_Last_Name=row[13]
        Provider_Other_First_Name=row[14]
        Provider_Other_Middle_Name=row[15]
        Provider_Other_Name_Prefix_Text=row[1]
        Provider_Other_Name_Suffix_Text=row[17]
        Provider_Other_Credential_Text=row[18]
        Provider_Other_Last_Name_Type_Code=row[19]
        Provider_First_Line_Business_Mailing_Address=row[20]
        Provider_Second_Line_Business_Mailing_Address=row[21]
        Provider_Business_Mailing_Address_City_Name=row[22]
        Provider_Business_Mailing_Address_State_Name=row[23]
        Provider_Business_Mailing_Address_Postal_Code=row[24]
        Provider_Business_Mailing_Address_Country_Code_If_outside_US=row[25]
        Provider_Business_Mailing_Address_Telephone_Number=row[2]
        Provider_Business_Mailing_Address_Fax_Number=row[27]
        Provider_First_Line_Business_Practice_Location_Address=row[28]
        Provider_Second_Line_Business_Practice_Location_Address=row[29]
        Provider_Business_Practice_Location_Address_City_Name=row[30]
        Provider_Business_Practice_Location_Address_State_Name=row[31]
        Provider_Business_Practice_Location_Address_Postal_Code=row[32]
        Provider_Business_Practice_Location_Address_Country_Code=row[33]
        Provider_Business_Practice_Location_Address_Telephone_Number=row[34]
        Provider_Business_Practice_Location_Address_Fax_Number=row[35]
        Provider_Enumeration_Date=row[36]
        Last_Update_Date=row[37]
        NPI_Deactivation_Reason_Code=row[38]
        NPI_Deactivation_Date=row[39]
        NPI_Reactivation_Date=row[40]
        Provider_Gender_Code=row[41]
        Authorized_Official_Last_Name=row[42]
        Authorized_Official_First_Name=row[43]
        Authorized_Official_Middle_Name=row[44]
        Authorized_Official_Title_or_Position=row[45]
        Authorized_Official_Telephone_Number=row[4]
        Healthcare_Provider_Taxonomy_Code_1=row[47]
        Provider_License_Number_1=row[48]
        Provider_License_Number_State_Code_1=row[49]
        Healthcare_Provider_Primary_Taxonomy_Switch_1=row[50]
        Healthcare_Provider_Taxonomy_Code_Code_2=row[51]
        Provider_License_Number_2=row[52]
        Provider_License_Number_State_Code_2=row[53]
        Healthcare_Provider_Primary_Taxonomy_Switch_2=row[54] 
        Healthcare_Provider_Taxonomy_Code_Code_3=row[55]
        Provider_License_Number_3=row[5]
        Provider_License_Number_State_Code_3=row[57]
        Healthcare_Provider_Primary_Taxonomy_Switch_3=row[58]
        Healthcare_Provider_Taxonomy_Code_Code_4=row[59]
        Provider_License_Number_4=row[60]
        Provider_License_Number_State_Code_4=row[61]
        Healthcare_Provider_Primary_Taxonomy_Switch_4=row[62]
        Healthcare_Provider_Taxonomy_Code_Code_5=row[63]
        Provider_License_Number_5=row[64]
        Provider_License_Number_State_Code_5=row[65]
        Healthcare_Provider_Primary_Taxonomy_Switch_5=row[6]
        Healthcare_Provider_Taxonomy_Code_Code_6=row[67]
        Provider_License_Number_6=row[68]
        Provider_License_Number_State_Code_6=row[69]
        Healthcare_Provider_Primary_Taxonomy_Switch_6=row[70]
        Healthcare_Provider_Taxonomy_Code_Code_7=row[71]
        Provider_License_Number_7=row[72]
        Provider_License_Number_State_Code_7=row[73]
        Healthcare_Provider_Primary_Taxonomy_Switch_7=row[74]
        Healthcare_Provider_Taxonomy_Code_Code_8=row[75]
        Provider_License_Number_8=row[7]
        Provider_License_Number_State_Code_8=row[77]
        Healthcare_Provider_Primary_Taxonomy_Switch_8=row[78]
        Healthcare_Provider_Taxonomy_Code_Code_9=row[79]
        Provider_License_Number_9=row[80]
        Provider_License_Number_State_Code_9=row[81]
        Healthcare_Provider_Primary_Taxonomy_Switch_9=row[82]
        Provider_License_Number_10=row[83]
        Provider_License_Number_State_Code_10=row[84]
        Healthcare_Provider_Primary_Taxonomy_Switch_10=row[85]
        Healthcare_Provider_Taxonomy_Code_Code_11=row[8]
        Provider_License_Number_11=row[87]
        Provider_License_Number_State_Code_11=row[88]
        Healthcare_Provider_Primary_Taxonomy_Switch_11=row[89]
        Healthcare_Provider_Taxonomy_Code_Code_12=row[90]
        Provider_License_Number_12=row[91]
        Provider_License_Number_State_Code_12=row[92]
        Healthcare_Provider_Primary_Taxonomy_Switch_12=row[93]
        Healthcare_Provider_Taxonomy_Code_Code_13=row[94]
        Provider_License_Number_13=row[95]
        Provider_License_Number_State_Code_13=row[9]
        Healthcare_Provider_Primary_Taxonomy_Switch_13=row[97]
        Healthcare_Provider_Taxonomy_Code_Code_14=row[98]
        Provider_License_Number_14=row[99]
        Provider_License_Number_State_Code_14=row[100]
        Healthcare_Provider_Primary_Taxonomy_Switch_14=row[101]
        Healthcare_Provider_Taxonomy_Code_Code_15=row[102]
        Provider_License_Number_15=row[103]
        Provider_License_Number_State_Code_15=row[104]
        Healthcare_Provider_Primary_Taxonomy_Switch_15=row[105]
        Other_Provider_Identifier_1=row[10]
        Other_Provider_Identifier_Type_Code_1=row[107]
        Other_Provider_Identifier_State_1=row[108]
        Other_Provider_Identifier_Issuer_1=row[109]
        Other_Provider_Identifier_2=row[110]
        Other_Provider_Identifier_Type_Code_2=row[111]
        Other_Provider_Identifier_State_2=row[112]
        Other_Provider_Identifier_Issuer_2=row[113]
        Other_Provider_Identifier_3=row[114]
        Other_Provider_Identifier_Type_Code_3=row[115]
        Other_Provider_Identifier_State_3=row[11]
        Other_Provider_Identifier_Issuer_3=row[117]
        Other_Provider_Identifier_4=row[118]
        Other_Provider_Identifier_Type_Code_4=row[119]
        Other_Provider_Identifier_State_4=row[120]
        Other_Provider_Identifier_Issuer_4=row[121]
        Other_Provider_Identifier_5=row[122]
        Other_Provider_Identifier_Type_Code_5=row[123]
        Other_Provider_Identifier_State_5=row[124]
        Other_Provider_Identifier_Issuer_5=row[125]
        Other_Provider_Identifier_6=row[12]
        Other_Provider_Identifier_Type_Code_6=row[127]
        Other_Provider_Identifier_State_6=row[128]
        Other_Provider_Identifier_Issuer_6=row[129]
        Other_Provider_Identifier_7=row[130]
        Other_Provider_Identifier_Type_Code_7=row[131]
        Other_Provider_Identifier_State_7=row[132]
        Other_Provider_Identifier_Issuer_7=row[133]
        Other_Provider_Identifier_8=row[134]
        Other_Provider_Identifier_Type_Code_8=row[135]
        Other_Provider_Identifier_State_8=row[136]
        Other_Provider_Identifier_Issuer_8=row[137]
        Other_Provider_Identifier_9=row[138]
        Other_Provider_Identifier_Type_Code_9=row[140]
        Other_Provider_Identifier_State_9=row[141]
        Other_Provider_Identifier_Issuer_9=row[142]
        Other_Provider_Identifier_10=row[143]
        Other_Provider_Identifier_Type_Code_10=row[144]
        Other_Provider_Identifier_State_10=row[145]
        Other_Provider_Identifier_Issuer_10=row[146]
        Other_Provider_Identifier_Type_Code_11=row[147]
        Other_Provider_Identifier_State_11=row[148]
        Other_Provider_Identifier_Issuer_11=row[149]
        Other_Provider_Identifier_12=row[150]
        Other_Provider_Identifier_Type_Code_12=row[151]
        Other_Provider_Identifier_State_12=row[152]
        Other_Provider_Identifier_Issuer_12=row[153]
        Other_Provider_Identifier_13=row[154]
        Other_Provider_Identifier_Type_Code_13=row[155]
        Other_Provider_Identifier_State_13=row[156]
        Other_Provider_Identifier_Issuer_13=row[157]
        Other_Provider_Identifier_14=row[158]
        Other_Provider_Identifier_Type_Code_14=row[159]
        Other_Provider_Identifier_State_14=row[160]
        Other_Provider_Identifier_Issuer_14=row[161]
        Other_Provider_Identifier_15=row[162]
        Other_Provider_Identifier_Type_Code_15=row[163]
        Other_Provider_Identifier_State_15=row[164]
        Other_Provider_Identifier_Issuer_15=row[165]
        Other_Provider_Identifier_16=row[166]
        Other_Provider_Identifier_Type_Code_16=row[167]
        Other_Provider_Identifier_State_16=row[168]
        Other_Provider_Identifier_Issuer_16=row[169]
        Other_Provider_Identifier_17=row[170]
        Other_Provider_Identifier_Type_Code_17=row[171]
        Other_Provider_Identifier_State_17=row[172]
        Other_Provider_Identifier_Issuer_17=row[173]
        Other_Provider_Identifier_18=row[174]
        Other_Provider_Identifier_Type_Code_18=row[175]
        Other_Provider_Identifier_State_18=row[176]
        Other_Provider_Identifier_Issuer_18=row[177]
        Other_Provider_Identifier_19=row[178]
        Other_Provider_Identifier_Type_Code_19=row[179]
        Other_Provider_Identifier_State_19=row[180]
        Other_Provider_Identifier_Issuer_19=row[181]
        Other_Provider_Identifier_20=row[182]
        Other_Provider_Identifier_Type_Code_20=row[183]
        Other_Provider_Identifier_State_20=row[184]
        Other_Provider_Identifier_Issuer_20=row[185]
        Other_Provider_Identifier_21=row[186]
        Other_Provider_Identifier_Type_Code_21=row[187]
        Other_Provider_Identifier_State_21=row[188]
        Other_Provider_Identifier_Issuer_21=row[189]
        Other_Provider_Identifier_22=row[190]
        Other_Provider_Identifier_Type_Code_22=row[191]
        Other_Provider_Identifier_State_22=row[192]
        Other_Provider_Identifier_Issuer_22=row[193]
        Other_Provider_Identifier_23=row[194]
        Other_Provider_Identifier_Type_Code_23=row[195]
        Other_Provider_Identifier_State_23=row[196]
        Other_Provider_Identifier_Issuer_23=row[197]
        Other_Provider_Identifier_24=row[198]
        Other_Provider_Identifier_Type_Code_24=row[199]
        Other_Provider_Identifier_State_24=row[200]
        Other_Provider_Identifier_Issuer_24=row[201]
        Other_Provider_Identifier_25=row[202]
        Other_Provider_Identifier_Type_Code_25=row[203]
        Other_Provider_Identifier_State_25=row[204]
        Other_Provider_Identifier_Issuer_25=row[205]
        Other_Provider_Identifier_26=row[206]
        Other_Provider_Identifier_Type_Code_26=row[207]
        Other_Provider_Identifier_State_26=row[208]
        Other_Provider_Identifier_Issuer_26=row[209]
        Other_Provider_Identifier_27=row[210]
        Other_Provider_Identifier_Type_Code_27=row[211]
        Other_Provider_Identifier_State_27=row[212]
        Other_Provider_Identifier_Issuer_27=row[213]
        Other_Provider_Identifier_28=row[214]
        Other_Provider_Identifier_Type_Code_28=row[215]
        Other_Provider_Identifier_State_28=row[216]
        Other_Provider_Identifier_Issuer_28=row[217]
        Other_Provider_Identifier_29=row[218]
        Other_Provider_Identifier_Type_Code_29=row[219]
        Other_Provider_Identifier_State_29=row[220]
        Other_Provider_Identifier_Issuer_29=row[221]
        Other_Provider_Identifier_30=row[222]
        Other_Provider_Identifier_Type_Code_30=row[223]
        Other_Provider_Identifier_State_30=row[224]
        Other_Provider_Identifier_Issuer_30=row[225]
        Other_Provider_Identifier_31=row[226]
        Other_Provider_Identifier_Type_Code_31=row[227]
        Other_Provider_Identifier_State_31=row[228]
        Other_Provider_Identifier_Issuer_31=row[229]
        Other_Provider_Identifier_32=row[230]
        Other_Provider_Identifier_Type_Code_32=row[231]
        Other_Provider_Identifier_State_32=row[232]
        Other_Provider_Identifier_Issuer_32=row[233]
        Other_Provider_Identifier_33=row[234]
        Other_Provider_Identifier_Type_Code_33=row[235]
        Other_Provider_Identifier_State_33=row[236]
        Other_Provider_Identifier_Issuer_33=row[237]
        Other_Provider_Identifier_34=row[238]
        Other_Provider_Identifier_Type_Code_34=row[239]
        Other_Provider_Identifier_State_34=row[240]
        Other_Provider_Identifier_Issuer_34=row[241]
        Other_Provider_Identifier_35=row[242]
        Other_Provider_Identifier_Type_Code_35=row[243]
        Other_Provider_Identifier_State_35=row[244]
        Other_Provider_Identifier_Issuer_35=row[245]
        Other_Provider_Identifier_36=row[246]
        Other_Provider_Identifier_ype_Code_36=row[247]
        Other_Provider_Identifier_State_36=row[248]
        Other_Provider_Identifier_Issuer_36=row[249]
        Other_Provider_Identifier_37=row[250]
        Other_Provider_Identifier_Type_Code_37=row[251]
        Other_Provider_Identifier_State_37=row[252]
        Other_Provider_Identifier_Issuer_37=row[253]
        Other_Provider_Identifier_38=row[254]
        Other_Provider_Identifier_Type_Code_38=row[255]
        Other_Provider_Identifier_State_38=row[256]
        Other_Provider_Identifier_Issuer_38=row[257]
        Other_Provider_Identifier_39=row[258]
        Other_Provider_Identifier_Type_Code_39=row[259]
        Other_Provider_Identifier_State_39=row[260]
        Other_Provider_Identifier_Issuer_39=row[261]
        Other_Provider_Identifier_40=row[262]
        Other_Provider_Identifier_Type_Code_40=row[263]
        Other_Provider_Identifier_State_40=row[264]
        Other_Provider_Identifier_Issuer_40=row[265]
        Other_Provider_Identifier_41=row[266]
        Other_Provider_Identifier_Type_Code_41=row[267]
        Other_Provider_Identifier_State_41=row[268]
        Other_Provider_Identifier_Issuer_41=row[269]
        Other_Provider_Identifier_42=row[270]
        Other_Provider_Identifier_Type_Code_42=row[271]
        Other_Provider_Identifier_State_42=row[272]
        Other_Provider_Identifier_Issuer_42=row[273]
        Other_Provider_Identifier_43=row[274]
        Other_Provider_Identifier_Type_Code_43=row[274]
        Other_Provider_Identifier_State_43=row[275]
        Other_Provider_Identifier_Issuer_43=row[276]
        Other_Provider_Identifier_44=row[277]
        Other_Provider_Identifier_Type_Code_44=row[278]
        Other_Provider_Identifier_State_44=row[279]
        Other_Provider_Identifier_Issuer_44=row[280]
        Other_Provider_Identifier_45=row[281]
        Other_Provider_Identifier_Type_Code_45=row[282]
        Other_Provider_Identifier_State_45=row[283]
        Other_Provider_Identifier_Issuer_45=row[284]
        Other_Provider_Identifier_46=row[285]
        Other_Provider_Identifier_Type_Code_46=row[286]
        Other_Provider_Identifier_State_46=row[287]
        Other_Provider_Identifier_Issuer_46=row[288]
        Other_Provider_Identifier_47=row[289]
        Other_Provider_Identifier_Type_Code_47=row[290]
        Other_Provider_Identifier_State_47=row[291]
        Other_Provider_Identifier_Issuer_47=row[292]
        Other_Provider_Identifier_48=row[293]
        Other_Provider_Identifier_Type_Code_48=row[294]
        Other_Provider_Identifier_State_48=row[295]
        Other_Provider_Identifier_Issuer_48=row[296] 
        Other_Provider_Identifier_49=row[297]
        Other_Provider_Identifier_Type_Code_49=row[298]
        Other_Provider_Identifier_State_49=row[299]
        Other_Provider_Identifier_Issuer_49=row[300]
        Other_Provider_Identifier_50=row[301]
        Other_Provider_Identifier_Type_Code_50=row[302]
        Other_Provider_Identifier_State_50=row[303]
        Other_Provider_Identifier_Issuer_50=row[304]
        Is_Sole_Proprietor=row[305]
        Is_Organization_Subpart=row[306]
        Parent_Organization_LBN=row[307]
        Parent_Organization_TIN=row[308]
        Authorized_Official_Name_Prefix_Text=row[309]
        Authorized_Official_Name_Suffix_Text=row[310]
        Authorized_Official_Credential_Text=row[311]                                                                                                                                                                                                 
        Healthcare_Provider_Taxonomy_Group_1=row[312]
        Healthcare_Provider_Taxonomy_Group_2=row[313]
        Healthcare_Provider_Taxonomy_Group_3=row[314]
        Healthcare_Provider_Taxonomy_Group_4=row[315]
        Healthcare_Provider_Taxonomy_Group_5=row[316]
        Healthcare_Provider_Taxonomy_Group_6=row[317]
        Healthcare_Provider_Taxonomy_Group_7=row[318]
        Healthcare_Provider_Taxonomy_Group_8=row[319]
        Healthcare_Provider_Taxonomy_Group_9=row[320]
        Healthcare_Provider_Taxonomy_Group_10=row[321]
        Healthcare_Provider_Taxonomy_Group_11=row[322]
        Healthcare_Provider_Taxonomy_Group_12=row[323]
        Healthcare_Provider_Taxonomy_Group_13=row[324]
        Healthcare_Provider_Taxonomy_Group_14=row[325]
        Healthcare_Provider_Taxonomy_Group_15=row[326]
        Certification_Date=[327] 
        #clean up line, too long

        query =  "INSERT INTO npicheck (NPI, Entity_Type_Code, Replacement_NPI, Employer_Identification_Number, Provider_Organization_Name, Provider_Last_Name, Provider_First_Name, Provider_Middle_Name, Provider_Name_Prefix_Text, Provider_Name_Suffix_Text, Provider_Credential_Text, Provider_Other_Organization_Name, Provider_Other_Organization_Name_Type_Code, Provider_Other_Last_Name, Provider_Other_First_Name, Provider_Other_Middle_Name, Provider_Other_Name_Prefix_Text, Provider_Other_Name_Suffix_Text, Provider_Other_Credential_Text, Provider_Other_Last_Name_Type_Code, Provider_First_Line_Business_Mailing_Address, Provider_Second_Line_Business_Mailing_Address, Provider_Business_Mailing_Address_City_Name, Provider_Business_Mailing_Address_State_Name, Provider_Business_Mailing_Address_Postal_Code, Provider_Business_Mailing_Address_Country_Code_If_outside_US, Provider_Business_Mailing_Address_Telephone_Number, Provider_Business_Mailing_Address_Fax_Number, Provider_First_Line_Business_Practice_Location_Address, Provider_Second_Line_Business_Practice_Location_Address, Provider_Business_Practice_Location_Address_City_Name, Provider_Business_Practice_Location_Address_State_Name, Provider_Business_Practice_Location_Address_Postal_Code, Provider_Business_Practice_Location_Address_Country_Code, Provider_Business_Practice_Location_Address_Telephone_Number, Provider_Business_Practice_Location_Address_Fax_Number, Provider_Enumeration_Date, Last_Update_Date, NPI_Deactivation_Reason_Code, NPI_Deactivation_Date, NPI_Reactivation_Date, Provider_Gender_Code, Authorized_Official_Last_Name, Authorized_Official_First_Name, Authorized_Official_Middle_Name, Authorized_Official_Title_or_Position, Authorized_Official_Telephone_Number, Healthcare_Provider_Taxonomy_Code_1, Provider_License_Number_1, Provider_License_Number_State_Code_1, Healthcare_Provider_Primary_Taxonomy_Switch_1, Healthcare_Provider_Taxonomy_Code_Code_2, Provider_License_Number_2, Provider_License_Number_State_Code_2, Healthcare_Provider_Primary_Taxonomy_Switch_2, Healthcare_Provider_Taxonomy_Code_Code_3, Provider_License_Number_3, Provider_License_Number_State_Code_3, Healthcare_Provider_Primary_Taxonomy_Switch_3, Healthcare_Provider_Taxonomy_Code_Code_4, Provider_License_Number_4, Provider_License_Number_State_Code_4, Healthcare_Provider_Primary_Taxonomy_Switch_4, Healthcare_Provider_Taxonomy_Code_Code_5, Provider_License_Number_5, Provider_License_Number_State_Code_5, Healthcare_Provider_Primary_Taxonomy_Switch_5, Healthcare_Provider_Taxonomy_Code_Code_6, Provider_License_Number_6, Provider_License_Number_State_Code_6, Healthcare_Provider_Primary_Taxonomy_Switch_6, Healthcare_Provider_Taxonomy_Code_Code_7, Provider_License_Number_7, Provider_License_Number_State_Code_7, Healthcare_Provider_Primary_Taxonomy_Switch_7, Healthcare_Provider_Taxonomy_Code_Code_8, Provider_License_Number_8, Provider_License_Number_State_Code_8, Healthcare_Provider_Primary_Taxonomy_Switch_8, Healthcare_Provider_Taxonomy_Code_Code_9, Provider_License_Number_9, Provider_License_Number_State_Code_9, Healthcare_Provider_Primary_Taxonomy_Switch_9, Provider_License_Number_10, Provider_License_Number_State_Code_10, Healthcare_Provider_Primary_Taxonomy_Switch_10, Healthcare_Provider_Taxonomy_Code_Code_11, Provider_License_Number_11, Provider_License_Number_State_Code_11, Healthcare_Provider_Primary_Taxonomy_Switch_11, Healthcare_Provider_Taxonomy_Code_Code_12, Provider_License_Number_12, Provider_License_Number_State_Code_12, Healthcare_Provider_Primary_Taxonomy_Switch_12, Healthcare_Provider_Taxonomy_Code_Code_13, Provider_License_Number_13, Provider_License_Number_State_Code_13, Healthcare_Provider_Primary_Taxonomy_Switch_13, Healthcare_Provider_Taxonomy_Code_Code_14, Provider_License_Number_14, Provider_License_Number_State_Code_14, Healthcare_Provider_Primary_Taxonomy_Switch_14, Healthcare_Provider_Taxonomy_Code_Code_15, Provider_License_Number_15, Provider_License_Number_State_Code_15, Healthcare_Provider_Primary_Taxonomy_Switch_15, Other_Provider_Identifier_1, Other_Provider_Identifier_Type_Code_1, Other_Provider_Identifier_State_1, Other_Provider_Identifier_Issuer_1, Other_Provider_Identifier_2, Other_Provider_Identifier_Type_Code_2, Other_Provider_Identifier_State_2, Other_Provider_Identifier_Issuer_2, Other_Provider_Identifier_3, Other_Provider_Identifier_Type_Code_3, Other_Provider_Identifier_State_3, Other_Provider_Identifier_Issuer_3, Other_Provider_Identifier_4, Other_Provider_Identifier_Type_Code_4, Other_Provider_Identifier_State_4, Other_Provider_Identifier_Issuer_4, Other_Provider_Identifier_5, Other_Provider_Identifier_Type_Code_5, Other_Provider_Identifier_State_5, Other_Provider_Identifier_Issuer_5, Other_Provider_Identifier_6, Other_Provider_Identifier_Type_Code_6, Other_Provider_Identifier_State_6, Other_Provider_Identifier_Issuer_6, Other_Provider_Identifier_7, Other_Provider_Identifier_Type_Code_7, Other_Provider_Identifier_State_7, Other_Provider_Identifier_Issuer_7, Other_Provider_Identifier_8, Other_Provider_Identifier_Type_Code_8, Other_Provider_Identifier_State_8, Other_Provider_Identifier_Issuer_8, Other_Provider_Identifier_9, Other_Provider_Identifier_Type_Code_9, Other_Provider_Identifier_State_9, Other_Provider_Identifier_Issuer_9, Other_Provider_Identifier_10, Other_Provider_Identifier_Type_Code_10, Other_Provider_Identifier_State_10, Other_Provider_Identifier_Issuer_10, Other_Provider_Identifier_Type_Code_11, Other_Provider_Identifier_State_11, Other_Provider_Identifier_Issuer_11, Other_Provider_Identifier_12, Other_Provider_Identifier_Type_Code_12, Other_Provider_Identifier_State_12, Other_Provider_Identifier_Issuer_12, Other_Provider_Identifier_13, Other_Provider_Identifier_Type_Code_13, Other_Provider_Identifier_State_13, Other_Provider_Identifier_Issuer_13, Other_Provider_Identifier_14, Other_Provider_Identifier_Type_Code_14, Other_Provider_Identifier_State_14, Other_Provider_Identifier_Issuer_14, Other_Provider_Identifier_15, Other_Provider_Identifier_Type_Code_15, Other_Provider_Identifier_State_15, Other_Provider_Identifier_Issuer_15, Other_Provider_Identifier_16, Other_Provider_Identifier_Type_Code_16, Other_Provider_Identifier_State_16, Other_Provider_Identifier_Issuer_16, Other_Provider_Identifier_17, Other_Provider_Identifier_Type_Code_17, Other_Provider_Identifier_State_17, Other_Provider_Identifier_Issuer_17, Other_Provider_Identifier_18, Other_Provider_Identifier_Type_Code_18, Other_Provider_Identifier_State_18, Other_Provider_Identifier_Issuer_18, Other_Provider_Identifier_19, Other_Provider_Identifier_Type_Code_19, Other_Provider_Identifier_State_19, Other_Provider_Identifier_Issuer_19, Other_Provider_Identifier_20, Other_Provider_Identifier_Type_Code_20, Other_Provider_Identifier_State_20, Other_Provider_Identifier_Issuer_20, Other_Provider_Identifier_21, Other_Provider_Identifier_Type_Code_21, Other_Provider_Identifier_State_21, Other_Provider_Identifier_Issuer_21, Other_Provider_Identifier_22, Other_Provider_Identifier_Type_Code_22, Other_Provider_Identifier_State_22, Other_Provider_Identifier_Issuer_22, Other_Provider_Identifier_23, Other_Provider_Identifier_Type_Code_23, Other_Provider_Identifier_State_23, Other_Provider_Identifier_Issuer_23, Other_Provider_Identifier_24, Other_Provider_Identifier_Type_Code_24, Other_Provider_Identifier_State_24, Other_Provider_Identifier_Issuer_24, Other_Provider_Identifier_25, Other_Provider_Identifier_Type_Code_25, Other_Provider_Identifier_State_25, Other_Provider_Identifier_Issuer_25, Other_Provider_Identifier_26, Other_Provider_Identifier_Type_Code_26, Other_Provider_Identifier_State_26, Other_Provider_Identifier_Issuer_26, Other_Provider_Identifier_27, Other_Provider_Identifier_Type_Code_27, Other_Provider_Identifier_State_27, Other_Provider_Identifier_Issuer_27, Other_Provider_Identifier_28, Other_Provider_Identifier_Type_Code_28, Other_Provider_Identifier_State_28, Other_Provider_Identifier_Issuer_28, Other_Provider_Identifier_29, Other_Provider_Identifier_Type_Code_29, Other_Provider_Identifier_State_29, Other_Provider_Identifier_Issuer_29, Other_Provider_Identifier_30, Other_Provider_Identifier_Type_Code_30, Other_Provider_Identifier_State_30, Other_Provider_Identifier_Issuer_30, Other_Provider_Identifier_31, Other_Provider_Identifier_Type_Code_31, Other_Provider_Identifier_State_31, Other_Provider_Identifier_Issuer_31, Other_Provider_Identifier_32, Other_Provider_Identifier_Type_Code_32, Other_Provider_Identifier_State_32, Other_Provider_Identifier_Issuer_32, Other_Provider_Identifier_33, Other_Provider_Identifier_Type_Code_33, Other_Provider_Identifier_State_33, Other_Provider_Identifier_Issuer_33, Other_Provider_Identifier_34, Other_Provider_Identifier_Type_Code_34, Other_Provider_Identifier_State_34, Other_Provider_Identifier_Issuer_34, Other_Provider_Identifier_35, Other_Provider_Identifier_Type_Code_35, Other_Provider_Identifier_State_35, Other_Provider_Identifier_Issuer_35, Other_Provider_Identifier_36, Other_Provider_Identifier_ype_Code_36, Other_Provider_Identifier_State_36, Other_Provider_Identifier_Issuer_36, Other_Provider_Identifier_37, Other_Provider_Identifier_Type_Code_37, Other_Provider_Identifier_State_37, Other_Provider_Identifier_Issuer_37, Other_Provider_Identifier_38, Other_Provider_Identifier_Type_Code_38, Other_Provider_Identifier_State_38, Other_Provider_Identifier_Issuer_38, Other_Provider_Identifier_39, Other_Provider_Identifier_Type_Code_39, Other_Provider_Identifier_State_39, Other_Provider_Identifier_Issuer_39, Other_Provider_Identifier_40, Other_Provider_Identifier_Type_Code_40, Other_Provider_Identifier_State_40, Other_Provider_Identifier_Issuer_40, Other_Provider_Identifier_41, Other_Provider_Identifier_Type_Code_41, Other_Provider_Identifier_State_41, Other_Provider_Identifier_Issuer_41, Other_Provider_Identifier_42, Other_Provider_Identifier_Type_Code_42, Other_Provider_Identifier_State_42, Other_Provider_Identifier_Issuer_42, Other_Provider_Identifier_43, Other_Provider_Identifier_Type_Code_43, Other_Provider_Identifier_State_43, Other_Provider_Identifier_Issuer_43, Other_Provider_Identifier_44, Other_Provider_Identifier_Type_Code_44, Other_Provider_Identifier_State_44, Other_Provider_Identifier_Issuer_44, Other_Provider_Identifier_45, Other_Provider_Identifier_Type_Code_45, Other_Provider_Identifier_State_45, Other_Provider_Identifier_Issuer_45, Other_Provider_Identifier_46, Other_Provider_Identifier_Type_Code_46, Other_Provider_Identifier_State_46, Other_Provider_Identifier_Issuer_46, Other_Provider_Identifier_47, Other_Provider_Identifier_Type_Code_47,Other_Provider_Identifier_State_47, Other_Provider_Identifier_Issuer_47, Other_Provider_Identifier_48, Other_Provider_Identifier_Type_Code_48, Other_Provider_Identifier_State_48, Other_Provider_Identifier_Issuer_48, Other_Provider_Identifier_49, Other_Provider_Identifier_Type_Code_49, Other_Provider_Identifier_State_49, Other_Provider_Identifier_Issuer_49, Other_Provider_Identifier_50, Other_Provider_Identifier_Type_Code_50, Other_Provider_Identifier_State_50, Other_Provider_Identifier_Issuer_50, Is_Sole_Proprietor, Is_Organization_Subpart, Parent_Organization_LBN, Parent_Organization_TIN, Authorized_Official_Name_Prefix_Text, Authorized_Official_Name_Suffix_Text, Authorized_Official_Credential_Text, Healthcare_Provider_Taxonomy_Group_1, Healthcare_Provider_Taxonomy_Group_2, Healthcare_Provider_Taxonomy_Group_3, Healthcare_Provider_Taxonomy_Group_4, Healthcare_Provider_Taxonomy_Group_5, Healthcare_Provider_Taxonomy_Group_6, Healthcare_Provider_Taxonomy_Group_7, Healthcare_Provider_Taxonomy_Group_8, Healthcare_Provider_Taxonomy_Group_9, Healthcare_Provider_Taxonomy_Group_10, Healthcare_Provider_Taxonomy_Group_11,Healthcare_Provider_Taxonomy_Group_12,Healthcare_Provider_Taxonomy_Group_13, Healthcare_Provider_Taxonomy_Group_14, Healthcare_Provider_Taxonomy_Group_15, Certification_Date) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);"
        data = (NPI, Entity_Type_Code, Replacement_NPI, Employer_Identification_Number, Provider_Organization_Name, Provider_Last_Name, Provider_First_Name, Provider_Middle_Name, Provider_Name_Prefix_Text, Provider_Name_Suffix_Text, Provider_Credential_Text, Provider_Other_Organization_Name, Provider_Other_Organization_Name_Type_Code, Provider_Other_Last_Name, Provider_Other_First_Name, Provider_Other_Middle_Name, Provider_Other_Name_Prefix_Text, Provider_Other_Name_Suffix_Text, Provider_Other_Credential_Text, Provider_Other_Last_Name_Type_Code, Provider_First_Line_Business_Mailing_Address, Provider_Second_Line_Business_Mailing_Address, Provider_Business_Mailing_Address_City_Name, Provider_Business_Mailing_Address_State_Name, Provider_Business_Mailing_Address_Postal_Code, Provider_Business_Mailing_Address_Country_Code_If_outside_US, Provider_Business_Mailing_Address_Telephone_Number, Provider_Business_Mailing_Address_Fax_Number, Provider_First_Line_Business_Practice_Location_Address, Provider_Second_Line_Business_Practice_Location_Address, Provider_Business_Practice_Location_Address_City_Name, Provider_Business_Practice_Location_Address_State_Name, Provider_Business_Practice_Location_Address_Postal_Code, Provider_Business_Practice_Location_Address_Country_Code, Provider_Business_Practice_Location_Address_Telephone_Number, Provider_Business_Practice_Location_Address_Fax_Number, Provider_Enumeration_Date, Last_Update_Date, NPI_Deactivation_Reason_Code, NPI_Deactivation_Date, NPI_Reactivation_Date, Provider_Gender_Code, Authorized_Official_Last_Name, Authorized_Official_First_Name, Authorized_Official_Middle_Name, Authorized_Official_Title_or_Position, Authorized_Official_Telephone_Number, Healthcare_Provider_Taxonomy_Code_1, Provider_License_Number_1, Provider_License_Number_State_Code_1, Healthcare_Provider_Primary_Taxonomy_Switch_1, Healthcare_Provider_Taxonomy_Code_Code_2, Provider_License_Number_2, Provider_License_Number_State_Code_2, Healthcare_Provider_Primary_Taxonomy_Switch_2, Healthcare_Provider_Taxonomy_Code_Code_3, Provider_License_Number_3, Provider_License_Number_State_Code_3, Healthcare_Provider_Primary_Taxonomy_Switch_3, Healthcare_Provider_Taxonomy_Code_Code_4, Provider_License_Number_4, Provider_License_Number_State_Code_4, Healthcare_Provider_Primary_Taxonomy_Switch_4, Healthcare_Provider_Taxonomy_Code_Code_5, Provider_License_Number_5, Provider_License_Number_State_Code_5, Healthcare_Provider_Primary_Taxonomy_Switch_5, Healthcare_Provider_Taxonomy_Code_Code_6, Provider_License_Number_6, Provider_License_Number_State_Code_6, Healthcare_Provider_Primary_Taxonomy_Switch_6, Healthcare_Provider_Taxonomy_Code_Code_7, Provider_License_Number_7, Provider_License_Number_State_Code_7, Healthcare_Provider_Primary_Taxonomy_Switch_7, Healthcare_Provider_Taxonomy_Code_Code_8, Provider_License_Number_8, Provider_License_Number_State_Code_8, Healthcare_Provider_Primary_Taxonomy_Switch_8, Healthcare_Provider_Taxonomy_Code_Code_9, Provider_License_Number_9, Provider_License_Number_State_Code_9, Healthcare_Provider_Primary_Taxonomy_Switch_9, Provider_License_Number_10, Provider_License_Number_State_Code_10, Healthcare_Provider_Primary_Taxonomy_Switch_10, Healthcare_Provider_Taxonomy_Code_Code_11, Provider_License_Number_11, Provider_License_Number_State_Code_11, Healthcare_Provider_Primary_Taxonomy_Switch_11, Healthcare_Provider_Taxonomy_Code_Code_12, Provider_License_Number_12, Provider_License_Number_State_Code_12, Healthcare_Provider_Primary_Taxonomy_Switch_12, Healthcare_Provider_Taxonomy_Code_Code_13, Provider_License_Number_13, Provider_License_Number_State_Code_13, Healthcare_Provider_Primary_Taxonomy_Switch_13, Healthcare_Provider_Taxonomy_Code_Code_14, Provider_License_Number_14, Provider_License_Number_State_Code_14, Healthcare_Provider_Primary_Taxonomy_Switch_14, Healthcare_Provider_Taxonomy_Code_Code_15, Provider_License_Number_15, Provider_License_Number_State_Code_15, Healthcare_Provider_Primary_Taxonomy_Switch_15, Other_Provider_Identifier_1, Other_Provider_Identifier_Type_Code_1, Other_Provider_Identifier_State_1, Other_Provider_Identifier_Issuer_1, Other_Provider_Identifier_2, Other_Provider_Identifier_Type_Code_2, Other_Provider_Identifier_State_2, Other_Provider_Identifier_Issuer_2, Other_Provider_Identifier_3, Other_Provider_Identifier_Type_Code_3, Other_Provider_Identifier_State_3, Other_Provider_Identifier_Issuer_3, Other_Provider_Identifier_4, Other_Provider_Identifier_Type_Code_4, Other_Provider_Identifier_State_4, Other_Provider_Identifier_Issuer_4, Other_Provider_Identifier_5, Other_Provider_Identifier_Type_Code_5, Other_Provider_Identifier_State_5, Other_Provider_Identifier_Issuer_5, Other_Provider_Identifier_6, Other_Provider_Identifier_Type_Code_6, Other_Provider_Identifier_State_6, Other_Provider_Identifier_Issuer_6, Other_Provider_Identifier_7, Other_Provider_Identifier_Type_Code_7, Other_Provider_Identifier_State_7, Other_Provider_Identifier_Issuer_7, Other_Provider_Identifier_8, Other_Provider_Identifier_Type_Code_8, Other_Provider_Identifier_State_8, Other_Provider_Identifier_Issuer_8, Other_Provider_Identifier_9, Other_Provider_Identifier_Type_Code_9, Other_Provider_Identifier_State_9, Other_Provider_Identifier_Issuer_9, Other_Provider_Identifier_10, Other_Provider_Identifier_Type_Code_10, Other_Provider_Identifier_State_10, Other_Provider_Identifier_Issuer_10, Other_Provider_Identifier_Type_Code_11, Other_Provider_Identifier_State_11, Other_Provider_Identifier_Issuer_11, Other_Provider_Identifier_12, Other_Provider_Identifier_Type_Code_12, Other_Provider_Identifier_State_12, Other_Provider_Identifier_Issuer_12, Other_Provider_Identifier_13, Other_Provider_Identifier_Type_Code_13, Other_Provider_Identifier_State_13, Other_Provider_Identifier_Issuer_13, Other_Provider_Identifier_14, Other_Provider_Identifier_Type_Code_14, Other_Provider_Identifier_State_14, Other_Provider_Identifier_Issuer_14, Other_Provider_Identifier_15, Other_Provider_Identifier_Type_Code_15, Other_Provider_Identifier_State_15, Other_Provider_Identifier_Issuer_15, Other_Provider_Identifier_16, Other_Provider_Identifier_Type_Code_16, Other_Provider_Identifier_State_16, Other_Provider_Identifier_Issuer_16, Other_Provider_Identifier_17, Other_Provider_Identifier_Type_Code_17, Other_Provider_Identifier_State_17, Other_Provider_Identifier_Issuer_17, Other_Provider_Identifier_18, Other_Provider_Identifier_Type_Code_18, Other_Provider_Identifier_State_18, Other_Provider_Identifier_Issuer_18, Other_Provider_Identifier_19, Other_Provider_Identifier_Type_Code_19, Other_Provider_Identifier_State_19, Other_Provider_Identifier_Issuer_19, Other_Provider_Identifier_20, Other_Provider_Identifier_Type_Code_20, Other_Provider_Identifier_State_20, Other_Provider_Identifier_Issuer_20, Other_Provider_Identifier_21, Other_Provider_Identifier_Type_Code_21, Other_Provider_Identifier_State_21, Other_Provider_Identifier_Issuer_21, Other_Provider_Identifier_22, Other_Provider_Identifier_Type_Code_22, Other_Provider_Identifier_State_22, Other_Provider_Identifier_Issuer_22, Other_Provider_Identifier_23, Other_Provider_Identifier_Type_Code_23, Other_Provider_Identifier_State_23, Other_Provider_Identifier_Issuer_23, Other_Provider_Identifier_24, Other_Provider_Identifier_Type_Code_24, Other_Provider_Identifier_State_24, Other_Provider_Identifier_Issuer_24, Other_Provider_Identifier_25, Other_Provider_Identifier_Type_Code_25, Other_Provider_Identifier_State_25, Other_Provider_Identifier_Issuer_25, Other_Provider_Identifier_26, Other_Provider_Identifier_Type_Code_26, Other_Provider_Identifier_State_26, Other_Provider_Identifier_Issuer_26, Other_Provider_Identifier_27, Other_Provider_Identifier_Type_Code_27, Other_Provider_Identifier_State_27, Other_Provider_Identifier_Issuer_27, Other_Provider_Identifier_28, Other_Provider_Identifier_Type_Code_28, Other_Provider_Identifier_State_28, Other_Provider_Identifier_Issuer_28, Other_Provider_Identifier_29, Other_Provider_Identifier_Type_Code_29, Other_Provider_Identifier_State_29, Other_Provider_Identifier_Issuer_29, Other_Provider_Identifier_30, Other_Provider_Identifier_Type_Code_30, Other_Provider_Identifier_State_30, Other_Provider_Identifier_Issuer_30, Other_Provider_Identifier_31, Other_Provider_Identifier_Type_Code_31, Other_Provider_Identifier_State_31, Other_Provider_Identifier_Issuer_31, Other_Provider_Identifier_32, Other_Provider_Identifier_Type_Code_32, Other_Provider_Identifier_State_32, Other_Provider_Identifier_Issuer_32, Other_Provider_Identifier_33, Other_Provider_Identifier_Type_Code_33, Other_Provider_Identifier_State_33, Other_Provider_Identifier_Issuer_33, Other_Provider_Identifier_34, Other_Provider_Identifier_Type_Code_34, Other_Provider_Identifier_State_34, Other_Provider_Identifier_Issuer_34, Other_Provider_Identifier_35, Other_Provider_Identifier_Type_Code_35, Other_Provider_Identifier_State_35, Other_Provider_Identifier_Issuer_35, Other_Provider_Identifier_36, Other_Provider_Identifier_ype_Code_36, Other_Provider_Identifier_State_36, Other_Provider_Identifier_Issuer_36, Other_Provider_Identifier_37, Other_Provider_Identifier_Type_Code_37, Other_Provider_Identifier_State_37, Other_Provider_Identifier_Issuer_37, Other_Provider_Identifier_38, Other_Provider_Identifier_Type_Code_38, Other_Provider_Identifier_State_38, Other_Provider_Identifier_Issuer_38, Other_Provider_Identifier_39, Other_Provider_Identifier_Type_Code_39, Other_Provider_Identifier_State_39, Other_Provider_Identifier_Issuer_39, Other_Provider_Identifier_40, Other_Provider_Identifier_Type_Code_40, Other_Provider_Identifier_State_40, Other_Provider_Identifier_Issuer_40, Other_Provider_Identifier_41, Other_Provider_Identifier_Type_Code_41, Other_Provider_Identifier_State_41, Other_Provider_Identifier_Issuer_41, Other_Provider_Identifier_42, Other_Provider_Identifier_Type_Code_42, Other_Provider_Identifier_State_42, Other_Provider_Identifier_Issuer_42, Other_Provider_Identifier_43, Other_Provider_Identifier_Type_Code_43, Other_Provider_Identifier_State_43, Other_Provider_Identifier_Issuer_43, Other_Provider_Identifier_44, Other_Provider_Identifier_Type_Code_44, Other_Provider_Identifier_State_44, Other_Provider_Identifier_Issuer_44, Other_Provider_Identifier_45, Other_Provider_Identifier_Type_Code_45, Other_Provider_Identifier_State_45, Other_Provider_Identifier_Issuer_45, Other_Provider_Identifier_46, Other_Provider_Identifier_Type_Code_46, Other_Provider_Identifier_State_46, Other_Provider_Identifier_Issuer_46, Other_Provider_Identifier_47, Other_Provider_Identifier_Type_Code_47,Other_Provider_Identifier_State_47, Other_Provider_Identifier_Issuer_47, Other_Provider_Identifier_48, Other_Provider_Identifier_Type_Code_48, Other_Provider_Identifier_State_48, Other_Provider_Identifier_Issuer_48, Other_Provider_Identifier_49, Other_Provider_Identifier_Type_Code_49, Other_Provider_Identifier_State_49, Other_Provider_Identifier_Issuer_49, Other_Provider_Identifier_50, Other_Provider_Identifier_Type_Code_50, Other_Provider_Identifier_State_50, Other_Provider_Identifier_Issuer_50, Is_Sole_Proprietor, Is_Organization_Subpart, Parent_Organization_LBN, Parent_Organization_TIN, Authorized_Official_Name_Prefix_Text, Authorized_Official_Name_Suffix_Text, Authorized_Official_Credential_Text, Healthcare_Provider_Taxonomy_Group_1, Healthcare_Provider_Taxonomy_Group_2, Healthcare_Provider_Taxonomy_Group_3, Healthcare_Provider_Taxonomy_Group_4, Healthcare_Provider_Taxonomy_Group_5, Healthcare_Provider_Taxonomy_Group_6, Healthcare_Provider_Taxonomy_Group_7, Healthcare_Provider_Taxonomy_Group_8, Healthcare_Provider_Taxonomy_Group_9, Healthcare_Provider_Taxonomy_Group_10, Healthcare_Provider_Taxonomy_Group_11,Healthcare_Provider_Taxonomy_Group_12,Healthcare_Provider_Taxonomy_Group_13, Healthcare_Provider_Taxonomy_Group_14, Healthcare_Provider_Taxonomy_Group_15, Certification_Date)
        cur.execute(query, data)
        conn.commit()

cur.close()
conn.close()