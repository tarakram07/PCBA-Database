

# Inserting parameters into a pcb table inside the Database
def InsertPcbDetailsInto_DB():
    return "insert into pcba(PCBA_ID, MAT_NUMBER, FS, MANUFACTURER, MANUFACTURER_YEAR, MANUFACTURER_MONTH, " \
           "SERIAL_NUMBER, ADDED_BY, PCBA_STATUS) values(?,?,?,?,?,?,?,?,?)"

#  Retrieving the data from a pcb table inside the Database
def GetPcbRecordsFrom_DB():
    return "Select * from pcba WHERE PCBA_ID = ? "

# update the status of a pcb in the database
def change_status_query():
    return f"UPDATE pcba SET PCBA_STATUS = ? WHERE PCBA_ID = ?"

def get_status_query():
    return f"SELECT PCBA_STATUS FROM pcba WHERE PCBA_ID = ?"
