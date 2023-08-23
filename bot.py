import telebot
import os
import pyrogram
import random
from pyrogram import *
from telebot import *
user ='iqheiqji39nxz9ne9k2j'
bot =telebot.TeleBot('6499250484:AAF88llUBQ2RNLgjIX8B37lev6dfb7_RAR8')
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message,'''
    هلا بيك مطوري اجازه
  ارسل /user + اليوزر ليتم اضافته
  ارسل /st + السيزن ليبدء اضافه الحساب للقناه
  ارسل /v ليرس اليك ملف الحسابات
    ''')
@bot.message_handler(func=lambda mssage:True)
def echo_message(message):
    message=message.text
    if "/user" in message and "@"in message:
        a=message.replace("/user","")
        o=a.replace(" ","")
        ccc=open('mk.txt','a')
        ccc.write(str(o))
    elif "/st" in message:
        e=message.replace("/st","")
        s=e.replace(" ","")
        r=str(''.join(random.choice(user)for i in range(119)))
        vcd=open('acc.txt','a')  
        vcd.write(str(s)+'\n')
        file=open("mk.txt","+r")
        api_id='15372008'
        api_hash='ed85c35370cffb1e2cf050e44e635d26'
        mm=Client(f'nis{r}',api_id=api_id,api_hash=api_hash,session_string=s)
        for cc in file.readlines():
          cc=cc.replace('\n','')
          try:
            mm.join_chat(cc)
          except:
            pass
        bot.reply_to(message,'''
    done
    
    ''')
    elif "/v" in message:
        do=open('acc.txt','rb')
        mn=len(open('acc.txt').readlines())
        bot.send_document(message.chat.id,do,caption=f'the nuber {mn}')
bot.infinity_polling()
