from pyrogram import Client
from pyrogram import filters
from pyrogram.types import Message
import random
from time import sleep

#################################################
#################################################
#################################################

api_id = ""
api_hash = ""
admin_id = ""

#################################################
#################################################
#################################################

app = Client("robot", api_id , api_hash)

addPost = False
join_chat = False
stratAutoSend = False
EditDatabase = False
Database = None
messageIdData = 0

caption = [
"وصله ✅",
"خودم باهاش وصلم",
"سرعت عالی 🚀",
"ناب",
"شاهکار 💫",
"اثر هنری",
"متصله ✅",
"تست کنین",
"تست شده با ایرانسل و وایفای",
"تست شده با نت همراه ",
"با لایک و دیس لایک نشون بدین وصله یا نه",
"فضایی♥️",
"ناسا 🚀",
"عالیه",
"ِلذت ببرید ",
"میشه باهاش عشق بازی کرد",
"خوبه وصله ✔",
"سرعت خوب",
"برای دانلود"
]

@app.on_message(filters.text and filters.chat(admin_id))
def main(c:Client , m:Message):
    
    global addPost
    global join_chat
    global stratAutoSend
    global EditDatabase
    global messageIdData
    global Database
    global caption

    usertext = m.text

    if addPost == True:
        if m.text == "stopaddpost":
            addPost = False
            app.send_message(m.chat.id , "اد کردن پست غیر فعال شد")
            return

        postList = m.text.split('\n')
        data = ""
        for i in postList:
            data += i + "\n+|+\n"

        f = open("database.txt", "a" ,encoding="utf-8")
        f.writelines(data)
        f.close()
        app.send_message(m.chat.id , "پست به دیتا بیس اضافه شد")

    elif join_chat == True:
        if m.text == "stopjoingrupe":
            join_chat = False
            app.send_message(m.chat.id , "جوین به چت غیر فعال شد")
            return

        try:
            app.join_chat(usertext)
            app.send_message(m.chat.id , " به چت اضافه شد برای اتمام جوین به گره `stopjoingrupe` را ارسال کنید")
        except:
            try:
                app.join_chat(app.get_chat(usertext).linked_chat.id)
            except:
                app.send_message(m.chat.id , "امکان جوین شدن داخل این گروه وجود ندارد برای اتمام جوین به گره `stopjoingrupe` را ارسال کنید")

    elif EditDatabase == True:
        if m.text == "EndEditData":
            EditDatabase == False
            data = ""
            for i in Database:
                data += i + "\n+|+\n"
            f = open("database.txt", "w" , encoding="utf-8")
            f.write(data)
            f.close()
            EditDatabase = False
            app.send_message(m.chat.id , "اطلاعات دیتا بیس به روز شد")

        else:
            try:
                if Database.__len__() > 0:
                    Database.pop(int(m.text))
                    index = 0
                    data = ""
                    for i in Database:
                        data += f"{index} : {i} \n\n"
                        index += 1
                if Database.__len__() == 0:
                    c.edit_message_text(m.chat.id , messageIdData , "دیتا بیس خالی")
                else:
                    c.edit_message_text(m.chat.id , messageIdData , data)
            except:
                app.send_message(m.chat.id , "امکان حذف وجود ندارد")

    elif m.text == "editData" and EditDatabase == False:
        f = open("database.txt", "r" ,encoding="utf-8")
        txt = f.read()
        f.close()

        if txt != "":
            Database = txt.split("\n+|+\n")
            Database.pop(Database.__len__()-1)

            index = 0
            data = ""
            for i in Database:
                data += f"{index} : {i} \n\n"
                index += 1
            i = app.send_message(m.chat.id , data + "\n\nبرای حذف پست شماره ایندکس پست را ارسال کنید و برای ذخیره تعقییرات `EndEditData` را ارسال کنید")
            messageIdData = i.id
            EditDatabase = True
        else:
            app.send_message(m.chat.id , "دیتا بیس خالی است")

    elif m.text == "addpost":
        addPost = True
        app.send_message(m.chat.id , "اد کردن پست فعال شد")

    elif m.text == "joingrupe":
        join_chat = True
        app.send_message(m.chat.id , "جوین به چت فعال شد ایدی گروه را وارد کنید")

    elif m.text.lower() == "info" or m.text.lower() == "help":
        
        app.send_message(m.chat.id , """`info` or `help` -> نمایش لیست دستورات ربات
`addpost` ->  اضافه کردن پروکسی (بین پروکس ها یک اینتر بگذارید تا جدا از هم داخل دیتا بیس ذخیره شوند)
`stopaddpost` -> متوقف کردن افزودن پروکسی
`deletdata` -> حذف دیتا بیس
`joingrupe` -> جوین به گروه   
`stopjoingrupe` -> متوقف کردن جوین به چت
`send` -> ارسال پست به گروه ها
`startautosend` -> ارسال پیام به صورت خودکار به گروه ها درهر چند دقیقه
`Stopautosend` -> متوقف کردن ارسال پیام به صورت خودکار
`editData` -> نماش اطلاعات دیتا بیس و حذف پست های دلخواه
`EndEditData` -> ذخیره تعقییرات دیتا بیس
""")

    elif m.text == "deletdata":
        f = open("database.txt", "w" , encoding="utf-8")
        f.write("")
        f.close()
        app.send_message(m.chat.id , "دیتا بیس پاک شد")

    elif m.text == "startautosend":
        app.send_message(m.chat.id , "ارسال پیام خودکار اغاز شد")
        stratAutoSend = True
        while stratAutoSend:

            ListTime = [20 , 30 , 40 , 50 , 60]
            timeS = random.randint(0 , ListTime.__len__()-1)
            app.send_message(m.chat.id , f"{ListTime[timeS]} دقیقه دیگر پیام ها ارسال میشوند")
            sleep(ListTime[timeS] * 60)
            f = open("database.txt", "r" ,encoding="utf-8")
            txt = f.read()
            f.close()

            if txt != "":
                List = txt.split("\n+|+\n")
                List.pop(List.__len__()-1)
                text = List[random.randint(0 , List.__len__()-1)]

                if List.__len__() > 0:
                    for i in app.get_dialogs():
                        try:
                            if i.chat.id != m.chat.id:
                                app.send_message(i.chat.id ,f"{caption[random.randint(0 , caption.__len__()-1)]}\n" + text)
                        except:
                            pass
            else:
                print("detabase Empty")

    elif m.text == "Stopautosend":
        stratAutoSend = False
        app.send_message(m.chat.id , "ارسال پیام خودکار متوقف شد")
        pass

    elif m.text == "send":
        f = open("database.txt", "r" ,encoding="utf-8")
        txt = f.read()
        f.close()
        if txt != "":
            List = txt.split("\n+|+\n")
            List.pop(List.__len__()-1)
            text = List[random.randint(0 , List.__len__()-1)]

            if List.__len__() > 0:
                for i in app.get_dialogs():
                    try:
                        if i.chat.id != m.chat.id:
                            app.send_message(i.chat.id ,f"{caption[random.randint(0 , caption.__len__()-1)]}\n" + text)
                    except:
                        pass
            app.send_message(m.chat.id , "پیام ها ارسال شدند")
        else:
            app.send_message(m.chat.id , "دیتا بیس خالی")

    else:
        app.send_message(m.chat.id , "این دستور وجود ندارد")

app.run()
