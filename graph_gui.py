import PySimpleGUI as sg
import stock_analyzer as cs
import dynamic_stock as ds
from datetime import datetime
import pytz

# All the stuff inside your window.

layout_open_stocks = [  
            [sg.Text("What stocks would you like to view? (ex. AAPL, AMZN)")],
            [sg.InputText(key='-NORMAL_VIEW-')],
            [sg.Text("What stock would you like to view live? (ex. AAPL)")],
            [sg.InputText(key='-LIVE_VIEW-')],
            [sg.Button('View'), sg.Button('Live View'), sg.Button('Cancel')]   
        ]

layout_closed_stocks = [ 
            [sg.Text("Note: The stock market is closed. Live view will show most recent close price because of this.")],
            [sg.Text("What stocks would you like to view? (ex. AAPL, AMZN)")],
            [sg.InputText(key='-NORMAL_VIEW-')],
            [sg.Text("What stock would you like to view live? (ex. AAPL)")],
            [sg.InputText(key='-LIVE_VIEW-')],
            [sg.Button('View'), sg.Button('Live View'), sg.Button('Cancel')]   
        ]

# Create the Window
date = datetime.now()
newYorkTz = pytz.timezone("America/New_York") 
timeInNewYork = datetime.now(newYorkTz)
currentTimeInNewYork = timeInNewYork.strftime("%H:%M:%S")

if int(currentTimeInNewYork[:2]) >= 16 or date.weekday() >= 5:
    window = sg.Window('Stock Scout', layout_closed_stocks, size=(400, 350))
else: 
    window = sg.Window('Stock Scout', layout_open_stocks, size=(400, 350))

# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, values = window.read()

    # if user closes window or clicks cancel
    if event == sg.WIN_CLOSED or event == 'Cancel':
        break

    if event == 'View':
        tickers_value = values['-NORMAL_VIEW-']
        tickers = [ticker.strip().upper() for ticker in tickers_value.split(",")]
        
        if tickers:
            stock = cs.ChosenStock(tickers,"2015-10-01", datetime.now(), testing=False)
    
    if event == 'Live View':
        if values['-LIVE_VIEW-']:
            live_ticker = values['-LIVE_VIEW-'].strip().upper()
            stock = ds.DynamicStock(live_ticker, "1d", "1m", testing=False)

window.close()