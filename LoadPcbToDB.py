import getpass as gt
import sqlite3
import time
import sys

from MonthYearFormat import *
from colorama import Fore
from QueriesPcb import *


def LOAD_PCB_TO_DB(PCB_ID, mydb, logger):
    # Name of the user
    SIGN = gt.getuser()
    # Splitting the QRCode
    split_PCB_ID = PCB_ID.split("_")

    # Storing the material number by removing Data Identifiers (1P)
    MAT_NUMBER = split_PCB_ID[0]
    # Storing the function stand
    FS = split_PCB_ID[1]
    # Storing the manufacturer by removing the Identifier "S"
    MANUFACTURER = split_PCB_ID[2][1:]
    # Storing the Manufacturer year and month
    MANUFACTURER_DATE = split_PCB_ID[3]
    MANUFACTURER_YEAR = MANU_YEAR(str(MANUFACTURER_DATE[:1]))
    MANUFACTURER_MONTH = MANU_MONTH(str(MANUFACTURER_DATE[1:2]))
    # Storing the Serial Number
    SERIAL_NUMBER = split_PCB_ID[4]
    # Condition for Status after is Raw(1), Tested(2) and Broken(3)
    STATUS = "Raw"

    try:

        # To create, modify and insert data into the tables inside Database we need cursor
        myCursor = mydb.cursor()
        # Inserting parameters into a table inside the Database
        query = InsertPcbDetailsInto_DB()
        # Calling the function and Passing the values
        val = (PCB_ID, MAT_NUMBER, FS, MANUFACTURER, MANUFACTURER_YEAR, MANUFACTURER_MONTH, SERIAL_NUMBER, SIGN, STATUS)
        # Inserting data into Table
        myCursor.execute(query, val)

        # save data into the database
        mydb.commit()
        logger.info(PCB_ID + " - performed by " + SIGN)
        print(Fore.GREEN + "Data Saved. \n")
        mydb.close()
        return True

    except sqlite3.OperationalError as e:
        print(Fore.RED + f"{e}: Database Access is Denied, Please close Database ASM_PCBA.db")
        time.sleep(5)
        sys.exit(0)

    except sqlite3.IntegrityError as e:
        print(Fore.RED + f"PCBA already exist in Database.")
        return None