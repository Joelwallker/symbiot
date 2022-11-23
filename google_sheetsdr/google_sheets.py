import gspread
import pandas as pd
import time


# connect got Google Sheets
gc = gspread.service_account(filename="/home/whitehercog/credentials/lookysymbiot-8bd1d380b0c4.json")
# list all available spreadsheets
sh = gc.open_by_key('1e8byu8VovhBsEc9mG5DRxayywP8zaA2DzpsAcAuboLc')

worksheet = sh.sheet1
worklist = worksheet.get_all_values()

# pandas df
Ddf = pd.DataFrame(worksheet.get_values('A2:E30'),
                   columns=['Worked_date', 'Worker', 'Start_smene', 'End_smene', 'Chat_id_worker'])
Ddf = Ddf.set_index('Worked_date')

Ndf = pd.DataFrame(worksheet.get_values('F2:J30'),
                   columns=['Worked_date', 'Worker', 'Start_smene', 'End_smene', 'Chat_id_worker'])

Ndf = Ndf.set_index('Worked_date')

# date variable
wdate = time.strftime("%d.%m.%Y")
wtime = time.strftime("%H:%M")

getdworker = Ddf.loc[wdate]['Worker']
getnworker = Ndf.loc[wdate]['Worker']
getworkerchatcatid = Ddf.loc[wdate]['Chat_id_worker']
getworkernchatcatid = Ndf.loc[wdate]['Chat_id_worker']



