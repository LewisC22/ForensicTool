import sqlite3
import csv
from datetime import datetime, timedelta



class HP():

    def HistParser(self):

        HistStatement = 'SELECT url FROM urls'

#Basic HistoryParser pulling only urls

        with sqlite3.connect('C:\Users\Lewis Collins\AppData\Local\Google\Chrome\User Data\Default\History') as conn:
            conn.text_factory = str
            c = conn.cursor()
            output_file_path = 'ChromeCode/Chrome_Hist.csv'
            with open(output_file_path, 'wb') as output_file:
                csv_writer = csv.writer(output_file, quoting=csv.QUOTE_ALL)
                headers = []
                csv_writer.writerow(headers)
                epoch = datetime(1601, 1, 1)
                for row in (c.execute(HistStatement)):
                    row = list(row)
                    csv_writer.writerow(row)
