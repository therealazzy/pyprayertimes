from bs4 import BeautifulSoup
import requests
import pandas as pd
import csv
import subprocess
import os
import sys
import ctypes  # An included library with Python install.
import tkinter as tk
from tkinter import messagebox
from tkinter.font import Font


page = requests.get("https://en.masjidway.com/masjid/3341/prayer")
soup = BeautifulSoup(page.text, 'html.parser')
table = soup.find('table',class_ = 'monthPrayers')
headers = [th.text.strip() for th in table.find_all('th')]
filename = "maghribtime.csv"
#body = table.find("tbody")
#days = body.find_all("tr")
#times = days.find_all("td")
#rows = table.find_all("tr")
#row = rows.find_all("td", class_ = "day")

current_day = soup.find("tr", attrs={"class":"current"})

#day = days.find("td", class_ = "day")
#subh = days.find_all("td", class_ = "subh_val")
#duhr = days.find_all("td", class_ = "duhr_val")
#asr = days.find_all("td", class_ = "asr_val")
maghreb = current_day.find("td", class_ = "maghreb_val")
#isha = days.find_all("td", class_ = "isha_val")

#print(day + "\nsubh: " + subh + "\nduhr: " + duhr + "\nasr: " + asr + " \nmasghreb: " + maghreb + "\nisha: " + isha)

headers[0] = ""

maghtime = maghreb.get_text()

maghrib = "".join(char for char in maghtime if char != ",")
#rows = []
crows = []

#output to a message box
#ctypes.windll.user32.MessageBoxW(0, maghrib, "Maghrib time today", 0)

#this writes to a csv file
#with open(filename, "w", newline="") as file:
#    writer = csv.writer(file)

#    writer.writerow([maghrib])

#os.startfile(filename)




#this for loop is for processing today's prayer times
for row in current_day.find_all('td'):
    rows = row.text
    crows.append(rows)

crows[0] = ''


combined = [x + ' ' + y for x, y in zip(headers, crows)]
formatted_combined = '\n'.join(combined)


window = tk.Tk()
window.withdraw()
font_size = 16
custom_font = Font(family="Arial", size = font_size)

dialog = tk.Toplevel(window)
dialog.title('Prayer Times Today')
dialog.option_add("*Font", custom_font)
dialog_width = 450
dialog_height = 300
dialog.update_idletasks()
dialog.geometry('{}x{}'.format(dialog_width, dialog_height))

label = tk.Label(dialog, text= formatted_combined)
label.pack(padx = 20, pady = 20)

button_style = {
    'font': custom_font, 'foreground': 'white', 'background': 'grey50', 'activeforeground': 'white', 'activebackground': 'grey60', 'highlightthickness': 0, 'borderwidth': 0, 'padx': 10, 'pady': 5}

button_ok = tk.Button(dialog, text='OK', command=dialog.destroy, **button_style)
button_ok.pack(pady=10)



window.update_idletasks()
x = window.winfo_screenwidth() // 2 - dialog.winfo_width() // 2
y = window.winfo_screenheight() // 2 - dialog.winfo_height() // 2
dialog.geometry('+{}+{}'.format(x, y))

#dialog.transient(window)
#dialog.grab_set()
#dialog.wait_window()

dialog.mainloop()

window.destroy()




#ctypes.windll.user32.MessageBoxW(0, str(formatted_combined), "Prayer times today", 0)



#this for loop is for processing the entire calendar month of prayer times
#for tr in table.find_all('tr'):
#   row = [td.text.strip() for td in tr.find_all('td')]
#   if row:
#       rows.append(row)

#pandas dataframe (for some reason using the 'rows' array doesn't pose a problem but if you're using 'crows' array then you need the square brackets
#df = pd.DataFrame([crows], columns = headers)


#print for debugging
#print(df)

#saves csv file to local directory
#df.to_csv('prayerdata.csv', index = False)

#exit
sys.exit()
