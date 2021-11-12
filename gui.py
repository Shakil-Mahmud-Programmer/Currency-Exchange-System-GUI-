import tkinter as tk,datetime,urllib.request
import webbrowser
from tkinter import ttk
from info import Converter
import tkinter.messagebox as mb
link = 'https://api.exchangerate-api.com/v4/latest/USD'
Result=Converter(link)

def run():
    if From.get()=='' or amount.get()=='':
        mb.showwarning(title="Warning !", message="Select a option !")

    else:
        res = Result.convert(From.get(), 'USD', float(amount.get()))
        result.set(res)
        now=datetime.datetime.now()
        time.set(now.strftime('%H:%M:%S %p' ))



def go():
    webbrowser.open_new_tab('https://www.facebook.com/profile.php?id=100036971298466')
    webbrowser.open_new('https://github.com/Shakil-Mahmud-Programmer')



window=tk.Tk()
window.geometry('800x450')
window.title('Currency Exchange System')
window.iconbitmap('dollar.ico')
tk.Label(text="Currency Exchange System",fg='red',font=("jost",12,"bold")).place(x=280,y=0)

curr=["AED","AFN","ALL","AMD","ANG","AOA","ARS","AUD","AWG","AZN","BAM","BBD","BDT","BGN","BHD","BIF","BMD","BND","BOB","BRL","BSD","BTN","BWP","BYN","BZD","CAD","CDF","CHF","CLP",
      "CNY","COP","CRC","CUC","CUP","CVE","CZK","DJF","DKK","DOP","DZD","EGP","ERN","ETB","EUR","FJD","FKP","FOK","GBP","GEL","GGP","GHS","GIP","GMD","GNF","GTQ","GYD","HKD","HNL",
      "HRK","HTG","HUF","IDR","ILS","IMP","INR","IQD","IRR","ISK","JMD","JOD","JPY","KES","KGS","KHR","KID","KMF","KRW","KWD","KYD","KZT","LAK","LBP","LKR","LRD","LSL","LYD","MAD",
      "MDL","MGA","MKD","MMK","MNT","MOP","MRU","MUR","MVR","MWK","MXN","MYR","MZN","NAD","NGN","NIO","NOK","NPR","NZD","OMR","PAB","PEN","PGK","PHP","PKR","PLN","PYG","QAR","RON",
      "RSD","RUB","RWF","SAR","SBD","SCR","SDG","SEK","SGD","SHP","SLL","SOS","SRD","SSP","STN","SYP","SZL","THB","TJS","TMT","TND","TOP","TRY","TTD","TVD","TWD","TZS","UAH","UGX",
      "UYU","UZS","VES","VND","VUV","WST","XAF","XCD","XDR","XOF","XPF","YER","ZAR","ZMW"]



tk.Label(text="From ",fg="blue",font=("jost",12,"bold")).place(x=50,y=80)
From=tk.StringVar()
From_entry=ttk.Combobox(textvariable=From,values=curr,width=10).place(x=100,y=83)


tk.Label(text="To ",fg="blue",font=("jost",12,"bold")).place(x=400,y=80)
tk.Label(text="USD ",fg="blue",font=("jost",12,"bold")).place(x=430,y=80)



tk.Label(text="Amount ",fg="blue",font=("jost",12,"bold")).place(x=50,y=150)
amount=tk.StringVar()
amount_entry=tk.Entry(textvariable=amount,font='jost',fg='blue').place(x=120,y=153)


tk.Label(text="Result ",fg="blue",font=("jost",12,"bold")).place(x=400,y=150)
result=tk.StringVar()
result_entry=tk.Entry(textvariable=result,font='jost',fg='red').place(x=460,y=153)


tk.Label(text="Time ",fg="blue",font=("jost",12,"bold")).place(x=50,y=230)
time=tk.StringVar()
tk.Entry(textvariable=time,font='jost',fg='red').place(x=100,y=230)

tk.Button(text="Calculate",bg="green",fg="White",font="Bold,200",height=1,width=8,command=run).place(x=560,y=230)

tk.Button(text="Developer",bg="blue",fg="White",font="Bold,200",height=1,width=8,command=go).place(x=50,y=280)


window.mainloop()