#!/usr/bin/python
import sqlite3

exclude_states = ["California", "Florida", "Illinois", "New York", "Texas", "Virginia"]

def add_new_icac_centers(conn):
    cur = conn.cursor()
    cmd = "select state_counties.county, state_counties.state, center_info.agency, center_info.phone, center_info.website from state_counties, center_info where state_counties.state = center_info.state"
    cur.execute(cmd)
    results = cur.fetchall()
    for county, state, agency, phone, website in results:
        if state not in exclude_states:
            print county, state, agency
            insert_cmd = ''' INSERT INTO icac_centers (COUNTY, STATE, AGENCY) VALUES(?,?,?)'''
            cur.execute(insert_cmd,(county, state, agency))
            conn.commit()

def add_icac_centers(conn):
    cur = conn.cursor()
    cur.execute("select * from state_counties")
    all_counties = cur.fetchall()
    errorCount = 0
    for county in all_counties:
        print county
        if county[1] not in exclude_states:
            cmd = "select state_counties.county, state_counties.state, center_info.agency, center_info.phone, center_info.website from state_counties, center_info where state_counties.state = center_info.state and state_counties.state='Hawaii'"
            cur.execute(cmd)
            results = cur.fetchall()

if __name__ == "__main__":
    conn = sqlite3.connect("icac_centers.db")
    #add_icac_centers(conn)
    add_new_icac_centers(conn)
