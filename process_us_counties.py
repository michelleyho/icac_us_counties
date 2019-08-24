import sqlite3

conn = sqlite3.connect('icac_centers.db')
#CREATE TABLE center_info ( AGENCY text NOT NULL, STATE text NOT NULL, PHONE text, EMAIL text, WEBSITE text
with open("us_county_list.csv") as fIn:
    with conn:
        cur = conn.cursor()
        for line in fIn:
            results = line.split(",")
            results = [x.strip() for x in results]
            insert_cmd = ''' INSERT INTO state_counties (COUNTY, STATE) VALUES(?,?)'''
            county = unicode(results[0].replace(" County",""),"utf-8")
            state = unicode(results[1],"utf-8")
            print "{}({}) -> {}({})".format(county, type(county),state, type(state))
            cur.execute(insert_cmd,(county, state))

