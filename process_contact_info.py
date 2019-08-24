#!/usr/bin/python
import sqlite3

conn = sqlite3.connect('icac_centers.db')
#CREATE TABLE center_info ( AGENCY text NOT NULL, STATE text NOT NULL, PHONE text, EMAIL text, WEBSITE text
with open("icac_contact_info.csv") as fIn:
    with conn:
        cur = conn.cursor()
        for line in fIn:
            results = line.strip("\n").replace(";","").split(",")
            state = results[0].strip('"')
            agency = results[1].strip('"')
            phone = results[2].strip('"')
            email = ""
            website = results[4].strip('"')
            print "{} in {} --> {} --> {}".format(agency,state, phone,website)
            insert_cmd = ''' INSERT INTO center_info (AGENCY, STATE, PHONE, WEBSITE, EMAIL) VALUES(?,?,?,?,?)'''
            cur.execute(insert_cmd,(agency, state, phone, website, email))
