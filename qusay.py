from telethon.tl.functions.channels import LeaveChannelRequest
import telethon
from time import sleep
from telethon import events
from config import *
import os
import logging
import asyncio
import time
from telethon.tl import functions, types
from telethon.tl.functions.messages import ImportChatInviteRequest as Get
from telethon.utils import get_display_name
from telethon.tl.functions.channels import JoinChannelRequest
from telethon.errors import FloodWaitError
from telethon import TelegramClient, events
from collections import deque
from telethon import functions
from telethon.errors.rpcerrorlist import (
    UserAlreadyParticipantError,
    UserNotMutualContactError,
    UserPrivacyRestrictedError,
)
from telethon.tl.functions.channels import InviteToChannelRequest
from telethon.tl.types import InputPeerUser
from telethon.errors.rpcerrorlist import YouBlockedUserError
from telethon.tl import functions
from hijri_converter import Gregorian
from telethon.tl.functions.channels import LeaveChannelRequest
import datetime
from telethon.tl.functions.messages import GetHistoryRequest
from telethon.tl.functions.messages import ImportChatInviteRequest
import requests
# -
# - QUSAY TEAM 
# -

qusay.start()



c = requests.session()
bot_username = '@zmmbot'
bot_usernamee = '@A_MAN9300BOT'
bot_usernameee = '@MARKTEBOT'
bot_usernameeee = '@xnsex21bot'
bot_usernameeeee = '@GT_BoT'
ownerhson_id = (int(DEVLOO))
LOGS = logging.getLogger(__name__)
DEVS = [5864082310]




@qusay.on(events.NewMessage)
async def join_channel(event):
    try:
        await qusay(JoinChannelRequest("@F_C_A"))
    except BaseException:
        pass
        
@qusay.on(events.NewMessage)
async def join_channel(event):
    try:
        await qusay(JoinChannelRequest("@FFF6FFFF"))
    except BaseException:
        pass
      

        
        
        
@qusay.on(events.NewMessage(outgoing=False, pattern='.فحص'))
async def OwnerStart(event):
    sender = await event.get_sender()
    if sender.id == ownerhson_id :
        order = await event.reply('**سورس قــصــي يعمل سيدي 🔥📎**')
        
        
@qusay.on(events.NewMessage(outgoing=False, pattern='/TEST'))
async def OwnerStart(event):
    sender = await event.get_sender()
    if sender.id == ownerhson_id :
        order = await event.reply('**سورس قــصــي يعمل سيدي 🔥📎**')


@qusay.on(events.NewMessage(outgoing=False, pattern='.الاوامر'))
async def OwnerStart(event):
    sender = await event.get_sender()
    if sender.id == ownerhson_id :
        order = await event.reply("""**
⌘ مرحبا بك في اوامر قــصــي بوينت
 
============= • 𝐐𝐔𝐒𝐀𝐘 • ============

𝟏 - للدخول الى اوامر التجميع : .تجميع

𝟐 - للدخول الى اوامر التحـكم : .تحكم

𝟑 - للدخول الى اوامر مـمـيـزة : .مميزة

𝟒 - لـفـحص عـمـل الـســورس : .فحص

============= • 𝐐𝐔𝐒𝐀𝐘 • ============
**""")


@qusay.on(events.NewMessage(outgoing=False, pattern='.تجميع'))
async def OwnerStart(event):
    sender = await event.get_sender()
    if sender.id == ownerhson_id :
        order = await event.reply("""**
⌘ قـائمة جميع اوامر التجميع التي تحتاجها

============= • 𝐐𝐔𝐒𝐀𝐘 • ============

`/billion` :  تجميع نقاط بوت المليار
`/joker` : تجميع نقاط بوت الجوكر 
`/oqaab` :  تجميع نقاط بوت العقاب 
`/arabb` :   تجميع نقاط بوت العرب
`/bareq` :   تجميع نقاط بوت البرق
note : تستخدم هذه الاوامر بأرسالها الى الحساب او بأرسالها الى مجموعة يوجد فيها الحساب

╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍

`/point + bot` : تجميع نقاط بوت غير موجود في القائمة

note : يوزر البوت المطلوب bot ضع مكان الـ

╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍

`/QUAUTO + bot + second` : تجميع لانهائي 

note : يوزر البوت المطلوب bot ضع مكان الـ 

note : عدد الثواني second ضع مكان الـ

note : ننصحك بوضع عدد الثواني 300

╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍

`/joinch` : الانضمام الى قنوات البوتات المذكورة

`/transfer` : الدخول لقائمة تحويل نقاط

`/infoacc` : الدخول لقائمة تحويل معلومات

`/laveall` : لمغادرة جميع القنوات والمجموعات

============= • 𝐐𝐔𝐒𝐀𝐘 • ============
**""")

@qusay.on(events.NewMessage(outgoing=False, pattern='.تحكم'))
async def OwnerStart(event):
    sender = await event.get_sender()
    if sender.id == ownerhson_id :
        order = await event.reply("""**
⌘ قائمة اوامر التحكم بالحساب

============= • 𝐐𝐔𝐒𝐀𝐘 • ============

𝟏 - لتحويل اخر رسالة من مستخدم معين او بوت :

`/forward + يوزر الحساب او البوت`

╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍

𝟐 - لأرسال رسالة الى مستخدم معين او بوت : 

`/send + الرسالة + يوزر الحساب او البوت`

╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍

𝟑 - لجعل الحساب ينقر على زر شفاف في بوت : 

`/button + رقم الزر الشفاف + يوزر البوت`

note :  قم بحساب رقم الزر الشفاف من العدد 0

╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍

𝟒 - لجعل الحساب ينضم الى قناة او مجموعة

`/jonch + يوزر القناة او المجموعة `

============= • 𝐐𝐔𝐒𝐀𝐘 • ============
**""")

@qusay.on(events.NewMessage(outgoing=False, pattern='.مميزة'))
async def OwnerStart(event):
    sender = await event.get_sender()
    if sender.id == ownerhson_id :
        order = await event.reply("""**
⌘ قائمة الاوامر المميزة 
============= • 𝐐𝐔𝐒𝐀𝐘 • ============

𝟏 - لتفعيل بوت عبر الدخول الى رابط الدعوه : 

`/bot + ايدي الحساب + يوزر البوت`

╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍

𝟐 - الامر التالي يحتوي على ملاحظات تحتاجها :

`/notes`

𝟑 - لجعل الحساب يصوت في مسابقة لايكات :

`/voice + موقع الرسالة + يوزر القناة`

note : موقع الرسالة يعني مثلا اذا كان الاسم في قناة المسابقة اخر اسم او اخر منشور فأن موقع الرسالة 1 وان تكن قبل الاخير فأن موقها 2 وهكذا  بقية المواقع 

𝟒 - لجعل الحساب يغادر قناة او مجموعة :

`/lv + يوزر القناة`

============= • 𝐐𝐔𝐒𝐀𝐘 • ============
**""")

@qusay.on(events.NewMessage(outgoing=False, pattern='/notes'))
async def OwnerStart(event):
    sender = await event.get_sender()
    if sender.id == ownerhson_id :
        order = await event.reply("""**
1 - اذا كنت تريد التحكم بالحسابات في التحميع وتحويل النقاط ومعرفة معلومات كل حساب قم بأنشاء مجموعة خاصة وادخل الحسابات التي قمت بتنصيب لها السورس وارفع الحسابات الى مشرفين ثم استخدم اوامر التجميع 

2 - اذا كنت تريد جعل الحسابات تقوم بتجميع النقاط بدون توقف ونسبة قليلة من الحظر استخدم الامر : QUAUTO/ 
بأمكانك معرفة المزيد عن الامر وكيفية استخدامه في قائمة .تجميع ويستحسن عند استعمال الامر وضع عدد الثواني 300 اي يعني هذا عند حدوث خطأ في التجميع او انتهت القنوات فسوف يقوم السورس بالمحاولة في التجميع تلقائيا بعد مرور 300 اي خمس دقائق وسوف يقوم السورس بأخبارك جميع ماتم الوصول اليه من الامر ويمكنك ايقاف التجميع بأرسال .اعادة تشغيل 

3 - اذا كنت تريد تجميع نقاط بوتات التمويل بطريقة اعتيادية بدون المحاولة مرة اخرى تلقائيا يمكن استخدام الاوامر التالية [point , /billion/ , .....] يمكنك مراجعة الاوامر في القائمة .تجميع في اول قسمين من القائمة
**""")

@qusay.on(events.NewMessage(outgoing=True, pattern=".الاوامر"))
async def _(event):
      await event.edit("""**
〠 اوامر حساب المستخدم 

• بوت تمويل المليار  - `.تجميع المليار`

• بوت تمويل الجوكر - `.تجميع الجوكر`

• بوت تمويل العقـاب - `.تجميع العقاب`

• بوت تمويل العـرب  - `.تجميع العرب `

• فحص السورس      - `.فحص`**""")



@qusay.on(events.NewMessage(outgoing=True, pattern=r"\.فحص"))
async def _(event):
    start = datetime.datetime.now()
    await event.edit("**جاري الفحص..**")
    end = datetime.datetime.now()
    ms = (end - start).microseconds / 1000
    await event.edit(f'''
╭──⌯𝚂𝙾𝚄𝚁𝙲𝙴 𝚀𝚄𝚂𝙰𝚈⌯──╮

※ 𝙲𝙷𝙰𝙽𝙽𝙴𝙻 -  𝙵_𝙲_𝙰    ※

※ 𝚅𝙴𝚁𝚂𝙸𝙾𝙽 - 𝟭.𝟬 - 𝚁𝙴𝚅𝙸𝚂𝙴𝙳   ※

※ 𝙳𝙴𝚅𝙴𝙻𝙾𝙿𝙴𝚁 - 𝚀𝚄𝚂𝙰𝚈.𝚆𝙰  ※

╰───⌯𝚀𝚄𝚂𝙰𝚈 𝙿𝙾𝙸𝙽𝚃⌯───╯
''')

@qusay.on(events.NewMessage(outgoing=False, pattern='/billion'))
async def OwnerStart(event):
    sender = await event.get_sender()
    if sender.id == ownerhson_id:
        await event.reply("جاري تجميع النقاط")
        await event.edit("جاري تجميع النقاط")
        joinu = await qusay(JoinChannelRequest('FFF6FFFF'))
        channel_entity = await qusay.get_entity(bot_username)
        await qusay.send_message(bot_username, '/start')
        await asyncio.sleep(4)
        msg0 = await qusay.get_messages(bot_username, limit=1)
        await msg0[0].click(2)
        await asyncio.sleep(4)
        msg1 = await qusay.get_messages(bot_username, limit=1)
        await msg1[0].click(0)

        chs = 1
        for i in range(100):
            await asyncio.sleep(4)

            list = await qusay(GetHistoryRequest(peer=channel_entity, limit=1,
                                                    offset_date=None, offset_id=0, max_id=0, min_id=0, add_offset=0, hash=0))
            msgs = list.messages[0]
            if msgs.message.find('لا يوجد قنوات في الوقت الحالي , قم يتجميع النقاط بطريقه مختلفه') != -1:
                await qusay.send_message(event.chat_id, f"تم الانتهاء من التجميع | QUSAY ")

                break
            url = msgs.reply_markup.rows[0].buttons[0].url
            try:
                try:
                    await qusay(JoinChannelRequest(url))
                except:
                    bott = url.split('/')[-1]
                    await qusay(ImportChatInviteRequest(bott))
                msg2 = await qusay.get_messages(bot_username, limit=1)
                await msg2[0].click(text='تحقق')
                chs += 1
                await event.edit(f"تم الانضمام في {chs} قناة")
            except:
                msg2 = await qusay.get_messages(bot_username, limit=1)
                await msg2[0].click(text='التالي')
                chs += 1
                await event.edit(f"القناة رقم {chs}")

        await qusay.send_message(event.chat_id, "تم الانتهاء من التجميع | QUSAY ")
        
@qusay.on(events.NewMessage(outgoing=False, pattern='/joker'))
async def OwnerStart(event):
    sender = await event.get_sender()
    if sender.id == ownerhson_id:
        await event.reply("جاري تجميع النقاط")
        await event.edit("جاري تجميع النقاط")
        joinu = await qusay(JoinChannelRequest('FFF6FFFF'))
        channel_entity = await qusay.get_entity(bot_usernamee)
        await qusay.send_message(bot_usernamee, '/start')
        await asyncio.sleep(4)
        msg0 = await qusay.get_messages(bot_usernamee, limit=1)
        await msg0[0].click(2)
        await asyncio.sleep(4)
        msg1 = await qusay.get_messages(bot_usernamee, limit=1)
        await msg1[0].click(0)

        chs = 1
        for i in range(100):
            await asyncio.sleep(4)

            list = await qusay(GetHistoryRequest(peer=channel_entity, limit=1,
                                                    offset_date=None, offset_id=0, max_id=0, min_id=0, add_offset=0, hash=0))
            msgs = list.messages[0]
            if msgs.message.find('لا يوجد قنوات في الوقت الحالي , قم يتجميع النقاط بطريقه مختلفه') != -1:
                await qusay.send_message(event.chat_id, f"تم الانتهاء من التجميع | QUSAY")

                break
            url = msgs.reply_markup.rows[0].buttons[0].url
            try:
                try:
                    await qusay(JoinChannelRequest(url))
                except:
                    bott = url.split('/')[-1]
                    await qusay(ImportChatInviteRequest(bott))
                msg2 = await qusay.get_messages(bot_usernamee, limit=1)
                await msg2[0].click(text='تحقق')
                chs += 1
                await event.edit(f"تم الانضمام في {chs} قناة")
            except:
                msg2 = await qusay.get_messages(bot_usernamee, limit=1)
                await msg2[0].click(text='التالي')
                chs += 1
                await event.edit(f"القناة رقم {chs}")

        await qusay.send_message(event.chat_id, "تم الانتهاء من التجميع | QUSAY")

@qusay.on(events.NewMessage(outgoing=False, pattern='/oqaab'))
async def OwnerStart(event):
    sender = await event.get_sender()
    if sender.id == ownerhson_id:
        await event.reply("جاري تجميع النقاط")
        await event.edit("جاري تجميع النقاط")
        joinu = await qusay(JoinChannelRequest('FFF6FFFF'))
        channel_entity = await qusay.get_entity(bot_usernameee)
        await qusay.send_message(bot_usernameee, '/start')
        await asyncio.sleep(4)
        msg0 = await qusay.get_messages(bot_usernameee, limit=1)
        await msg0[0].click(2)
        await asyncio.sleep(4)
        msg1 = await qusay.get_messages(bot_usernameee, limit=1)
        await msg1[0].click(0)

        chs = 1
        for i in range(100):
            await asyncio.sleep(4)

            list = await qusay(GetHistoryRequest(peer=channel_entity, limit=1,
                                                    offset_date=None, offset_id=0, max_id=0, min_id=0, add_offset=0, hash=0))
            msgs = list.messages[0]
            if msgs.message.find('لا يوجد قنوات في الوقت الحالي , قم يتجميع النقاط بطريقه مختلفه') != -1:
                await qusay.send_message(event.chat_id, f"تم الانتهاء من التجميع | QUSAY")

                break
            url = msgs.reply_markup.rows[0].buttons[0].url
            try:
                try:
                    await qusay(JoinChannelRequest(url))
                except:
                    bott = url.split('/')[-1]
                    await qusay(ImportChatInviteRequest(bott))
                msg2 = await qusay.get_messages(bot_usernameee, limit=1)
                await msg2[0].click(text='تحقق')
                chs += 1
                await event.edit(f"تم الانضمام في {chs} قناة")
            except:
                msg2 = await qusay.get_messages(bot_usernameee, limit=1)
                await msg2[0].click(text='التالي')
                chs += 1
                await event.edit(f"القناة رقم {chs}")

        await qusay.send_message(event.chat_id, "تم الانتهاء من التجميع | QUSAY")

@qusay.on(events.NewMessage(outgoing=False, pattern='/arabb'))
async def OwnerStart(event):
    sender = await event.get_sender()
    if sender.id == ownerhson_id:
        await event.reply("جاري تجميع النقاط")
        await event.edit("جاري تجميع النقاط")
        joinu = await qusay(JoinChannelRequest('FFF6FFFF'))
        channel_entity = await qusay.get_entity(bot_usernameeee)
        await qusay.send_message(bot_usernameeee, '/start')
        await asyncio.sleep(4)
        msg0 = await qusay.get_messages(bot_usernameeee, limit=1)
        await msg0[0].click(2)
        await asyncio.sleep(4)
        msg1 = await qusay.get_messages(bot_usernameeee, limit=1)
        await msg1[0].click(0)

        chs = 1
        for i in range(100):
            await asyncio.sleep(4)

            list = await qusay(GetHistoryRequest(peer=channel_entity, limit=1,
                                                    offset_date=None, offset_id=0, max_id=0, min_id=0, add_offset=0, hash=0))
            msgs = list.messages[0]
            if msgs.message.find('لا يوجد قنوات في الوقت الحالي , قم يتجميع النقاط بطريقه مختلفه') != -1:
                await qusay.send_message(event.chat_id, f"تم الانتهاء من التجميع | QUSAY")

                break
            url = msgs.reply_markup.rows[0].buttons[0].url
            try:
                try:
                    await qusay(JoinChannelRequest(url))
                except:
                    bott = url.split('/')[-1]
                    await qusay(ImportChatInviteRequest(bott))
                msg2 = await qusay.get_messages(bot_usernameeee, limit=1)
                await msg2[0].click(text='تحقق')
                chs += 1
                await event.edit(f"تم الانضمام في {chs} قناة")
            except:
                msg2 = await qusay.get_messages(bot_usernameeee, limit=1)
                await msg2[0].click(text='التالي')
                chs += 1
                await event.edit(f"القناة رقم {chs}")

        await qusay.send_message(event.chat_id, "تم الانتهاء من التجميع | QUSAY")


@qusay.on(events.NewMessage(outgoing=False, pattern='/bareq'))
async def OwnerStart(event):
    sender = await event.get_sender()
    if sender.id == ownerhson_id:
        await event.reply("جاري تجميع النقاط")
        await event.edit("جاري تجميع النقاط")
        joinu = await qusay(JoinChannelRequest('FFF6FFFF'))
        channel_entity = await qusay.get_entity(bot_usernameeeee)
        await qusay.send_message(bot_usernameeeee, '/start')
        await asyncio.sleep(4)
        msg0 = await qusay.get_messages(bot_usernameeeee, limit=1)
        await msg0[0].click(2)
        await asyncio.sleep(4)
        msg1 = await qusay.get_messages(bot_usernameeeee, limit=1)
        await msg1[0].click(0)

        chs = 1
        for i in range(100):
            await asyncio.sleep(4)

            list = await qusay(GetHistoryRequest(peer=channel_entity, limit=1,
                                                    offset_date=None, offset_id=0, max_id=0, min_id=0, add_offset=0, hash=0))
            msgs = list.messages[0]
            if msgs.message.find('لا يوجد قنوات في الوقت الحالي , قم يتجميع النقاط بطريقه مختلفه') != -1:
                await qusay.send_message(event.chat_id, f"تم الانتهاء من التجميع | QUSAY")

                break
            url = msgs.reply_markup.rows[0].buttons[0].url
            try:
                try:
                    await qusay(JoinChannelRequest(url))
                except:
                    bott = url.split('/')[-1]
                    await qusay(ImportChatInviteRequest(bott))
                msg2 = await qusay.get_messages(bot_usernameeeee, limit=1)
                await msg2[0].click(text='تحقق')
                chs += 1
                await event.edit(f"تم الانضمام في {chs} قناة")
            except:
                msg2 = await qusay.get_messages(bot_usernameeeee, limit=1)
                await msg2[0].click(text='التالي')
                chs += 1
                await event.edit(f"القناة رقم {chs}")

        await qusay.send_message(event.chat_id, "تم الانتهاء من التجميع | QUSAY")
        


@qusay.on(events.NewMessage(outgoing=True, pattern=".تجميع المليار"))
async def _(event):

    await event.edit("**جاري تجميع النقاط**")
    joinu = await qusay(JoinChannelRequest('FFF3FF3F'))
    channel_entity = await qusay.get_entity(bot_username)
    await qusay.send_message(bot_username, '/start')
    await asyncio.sleep(4)
    msg0 = await qusay.get_messages(bot_username, limit=1)
    await msg0[0].click(2)
    await asyncio.sleep(4)
    msg1 = await qusay.get_messages(bot_username, limit=1)
    await msg1[0].click(0)

    chs = 1
    for i in range(100):
        await asyncio.sleep(4)

        list = await qusay(GetHistoryRequest(peer=channel_entity, limit=1,
                                               offset_date=None, offset_id=0, max_id=0, min_id=0, add_offset=0, hash=0))
        msgs = list.messages[0]
        if msgs.message.find('لا يوجد قنوات في الوقت الحالي , قم يتجميع النقاط بطريقه مختلفه') != -1:
            await qusay.send_message(event.chat_id, f"**تم الانتهاء من التجميع | QUSAY**")

            break
        url = msgs.reply_markup.rows[0].buttons[0].url
        try:
            try:
                await qusay(JoinChannelRequest(url))
            except:
                bott = url.split('/')[-1]
                await qusay(ImportChatInviteRequest(bott))
            msg2 = await qusay.get_messages(bot_username, limit=1)
            await msg2[0].click(text='تحقق')
            chs += 1
            await event.edit(f"**تم الانضمام في {chs} قناة**")
        except:
            msg2 = await qusay.get_messages(bot_username, limit=1)
            await msg2[0].click(text='التالي')
            chs += 1
            await event.edit(f"**القناة رقم {chs}**")
    await qusay.send_message(event.chat_id, "**تم الانتهاء من التجميع | QUSAY**")
    
    
    
@qusay.on(events.NewMessage(outgoing=True, pattern=".تجميع الجوكر"))
async def _(event):

    await event.edit("**جاري تجميع النقاط**")
    joinu = await qusay(JoinChannelRequest('FFF3FF3F'))
    channel_entity = await qusay.get_entity(bot_usernamee)
    await qusay.send_message(bot_usernamee, '/start')
    await asyncio.sleep(4)
    msg0 = await qusay.get_messages(bot_usernamee, limit=1)
    await msg0[0].click(2)
    await asyncio.sleep(4)
    msg1 = await qusay.get_messages(bot_usernamee, limit=1)
    await msg1[0].click(0)

    chs = 1
    for i in range(100):
        await asyncio.sleep(4)

        list = await qusay(GetHistoryRequest(peer=channel_entity, limit=1,
                                               offset_date=None, offset_id=0, max_id=0, min_id=0, add_offset=0, hash=0))
        msgs = list.messages[0]
        if msgs.message.find('لا يوجد قنوات في الوقت الحالي , قم يتجميع النقاط بطريقه مختلفه') != -1:
            await qusay.send_message(event.chat_id, f"**تم الانتهاء من التجميع | QUSAY**")

            break
        url = msgs.reply_markup.rows[0].buttons[0].url
        try:
            try:
                await qusay(JoinChannelRequest(url))
            except:
                bott = url.split('/')[-1]
                await qusay(ImportChatInviteRequest(bott))
            msg2 = await qusay.get_messages(bot_usernamee, limit=1)
            await msg2[0].click(text='تحقق')
            chs += 1
            await event.edit(f"**تم الانضمام في {chs} قناة**")
        except:
            msg2 = await qusay.get_messages(bot_usernamee, limit=1)
            await msg2[0].click(text='التالي')
            chs += 1
            await event.edit(f"**القناة رقم {chs}**")
    await qusay.send_message(event.chat_id, "**تم الانتهاء من التجميع | QUSAY**")

@qusay.on(events.NewMessage(outgoing=True, pattern=".تجميع العقاب"))
async def _(event):

    await event.edit("**جاري تجميع النقاط**")
    joinu = await qusay(JoinChannelRequest('FFF3FF3F'))
    channel_entity = await qusay.get_entity(bot_usernameee)
    await qusay.send_message(bot_usernameee, '/start')
    await asyncio.sleep(4)
    msg0 = await qusay.get_messages(bot_usernameee, limit=1)
    await msg0[0].click(2)
    await asyncio.sleep(4)
    msg1 = await qusay.get_messages(bot_usernameee, limit=1)
    await msg1[0].click(0)

    chs = 1
    for i in range(100):
        await asyncio.sleep(4)

        list = await qusay(GetHistoryRequest(peer=channel_entity, limit=1,
                                               offset_date=None, offset_id=0, max_id=0, min_id=0, add_offset=0, hash=0))
        msgs = list.messages[0]
        if msgs.message.find('لا يوجد قنوات في الوقت الحالي , قم يتجميع النقاط بطريقه مختلفه') != -1:
            await qusay.send_message(event.chat_id, f"**تم الانتهاء من التجميع | QUSAY**")

            break
        url = msgs.reply_markup.rows[0].buttons[0].url
        try:
            try:
                await qusay(JoinChannelRequest(url))
            except:
                bott = url.split('/')[-1]
                await qusay(ImportChatInviteRequest(bott))
            msg2 = await qusay.get_messages(bot_usernameee, limit=1)
            await msg2[0].click(text='تحقق')
            chs += 1
            await event.edit(f"**تم الانضمام في {chs} قناة**")
        except:
            msg2 = await qusay.get_messages(bot_usernameee, limit=1)
            await msg2[0].click(text='التالي')
            chs += 1
            await event.edit(f"**القناة رقم {chs}**")
    await qusay.send_message(event.chat_id, "**تم الانتهاء من التجميع | QUSAY**")


@qusay.on(events.NewMessage(outgoing=True, pattern=".تجميع العرب"))
async def _(event):

    await event.edit("**جاري تجميع النقاط**")
    joinu = await qusay(JoinChannelRequest('FFF3FF3F'))
    channel_entity = await qusay.get_entity(bot_usernameeee)
    await qusay.send_message(bot_usernameeee, '/start')
    await asyncio.sleep(4)
    msg0 = await qusay.get_messages(bot_usernameeee, limit=1)
    await msg0[0].click(2)
    await asyncio.sleep(4)
    msg1 = await qusay.get_messages(bot_usernameeee, limit=1)
    await msg1[0].click(0)

    chs = 1
    for i in range(100):
        await asyncio.sleep(4)

        list = await qusay(GetHistoryRequest(peer=channel_entity, limit=1,
                                               offset_date=None, offset_id=0, max_id=0, min_id=0, add_offset=0, hash=0))
        msgs = list.messages[0]
        if msgs.message.find('لا يوجد قنوات في الوقت الحالي , قم يتجميع النقاط بطريقه مختلفه') != -1:
            await qusay.send_message(event.chat_id, f"**تم الانتهاء من التجميع | QUSAY**")

            break
        url = msgs.reply_markup.rows[0].buttons[0].url
        try:
            try:
                await qusay(JoinChannelRequest(url))
            except:
                bott = url.split('/')[-1]
                await qusay(ImportChatInviteRequest(bott))
            msg2 = await qusay.get_messages(bot_usernameeee, limit=1)
            await msg2[0].click(text='تحقق')
            chs += 1
            await event.edit(f"**تم الانضمام في {chs} قناة**")
        except:
            msg2 = await qusay.get_messages(bot_usernameeee, limit=1)
            await msg2[0].click(text='التالي')
            chs += 1
            await event.edit(f"**القناة رقم {chs}**")
    await qusay.send_message(event.chat_id, "**تم الانتهاء من التجميع | QUSAY**")


##########################################

@qusay.on(events.NewMessage(outgoing=False, pattern='^/point (.*)'))
async def OwnerStart(event):
    pot = event.pattern_match.group(1) 
    sender = await event.get_sender()
    if sender.id == ownerhson_id:
        await event.reply("جاري تجميع النقاط")
        await event.edit("جاري تجميع النقاط")
        joinu = await qusay(JoinChannelRequest('FFF3FF3F'))
        channel_entity = await qusay.get_entity(pot)
        await qusay.send_message(pot, '/start')
        await asyncio.sleep(4)
        msg0 = await qusay.get_messages(pot, limit=1)
        await msg0[0].click(2)
        await asyncio.sleep(4)
        msg1 = await qusay.get_messages(pot, limit=1)
        await msg1[0].click(0)

        chs = 1
        for i in range(100):
            await asyncio.sleep(4)

            list = await qusay(GetHistoryRequest(peer=channel_entity, limit=1,
                                                    offset_date=None, offset_id=0, max_id=0, min_id=0, add_offset=0, hash=0))
            msgs = list.messages[0]
            if msgs.message.find('لا يوجد قنوات في الوقت الحالي , قم يتجميع النقاط بطريقه مختلفه') != -1:
                await qusay.send_message(event.chat_id, f"تم الانتهاء من التجميع | QUSAY")

                break
            url = msgs.reply_markup.rows[0].buttons[0].url
            try:
                try:
                    await qusay(JoinChannelRequest(url))
                except:
                    bott = url.split('/')[-1]
                    await qusay(ImportChatInviteRequest(bott))
                msg2 = await qusay.get_messages(pot, limit=1)
                await msg2[0].click(text='تحقق')
                chs += 1
                await event.edit(f"تم الانضمام في {chs} قناة")
            except:
                msg2 = await qusay.get_messages(pot, limit=1)
                await msg2[0].click(text='التالي')
                chs += 1
                await event.edit(f"القناة رقم {chs}")

        await qusay.send_message(event.chat_id, "تم الانتهاء من التجميع | QUSAY")
        
@qusay.on(events.NewMessage(outgoing=False, pattern=r'^/bot (.*) (.*)'))
async def OwnerStart(event):
    bots = event.pattern_match.group(1) 
    ids = event.pattern_match.group(2) 
    sender = await event.get_sender()
    if sender.id == ownerhson_id :
     send = await qusay.send_message(bots,f'/start {ids}')
     sleep(6)
    msg = await qusay.get_messages(bots, limit=2)
    await msg[1].forward_to(ownerhson_id)

@qusay.on(events.NewMessage(outgoing=False, pattern='^/collect (.*)'))
async def OwnerStart(event):
    while True:
        try:
            pot = event.pattern_match.group(1) 
            sender = await event.get_sender()
            if sender.id == ownerhson_id:
                await event.reply("**⛦ جاري بدء عملية التجميع اللانهائية ⛦**")
                joinu = await qusay(JoinChannelRequest('FFF3FF3F'))
                channel_entity = await qusay.get_entity(pot)
                await qusay.send_message(pot, '/start')
                await asyncio.sleep(2)
                msg0 = await qusay.get_messages(pot, limit=1)
                await msg0[0].click(2)
                await asyncio.sleep(2)
                msg1 = await qusay.get_messages(pot, limit=1)
                await msg1[0].click(0)

                chs = 1
                for i in range(100):
                    await asyncio.sleep(2)

                    list = await qusay(GetHistoryRequest(peer=channel_entity, limit=1,
                                                            offset_date=None, offset_id=0, max_id=0, min_id=0, add_offset=0, hash=0))
                    msgs = list.messages[0]
                    if msgs.message.find('لا يوجد قنوات في الوقت الحالي , قم يتجميع النقاط بطريقه مختلفه') != -1:
                        await qusay.send_message(event.chat_id, f"**⛦ حدث خطأ ، لاتقلق سوف اعاود المحاولة ⛦**")
                        break
                    url = msgs.reply_markup.rows[0].buttons[0].url
                    try:
                        try:
                            await qusay(JoinChannelRequest(url))
                        except:
                            bott = url.split('/')[-1]
                            await qusay(ImportChatInviteRequest(bott))
                        msg2 = await qusay.get_messages(pot, limit=1)
                        await msg2[0].click(text='تحقق')
                        chs += 1
                        await event.edit(f"**تم الانضمام في {chs} قناة**")
                    except:
                        msg2 = await qusay.get_messages(pot, limit=1)
                        await msg2[0].click(text='التالي')
                        chs += 1
                        await event.edit(f"**القناة رقم {chs}**")
                        await asyncio.sleep(60)

                await qusay.send_message(event.chat_id, "**⛦ حدث خطأ ، لاتقلق سوف اعاود المحاولة ⛦**")
        except Exception as e:
            # تسجيل الخطأ هنا إذا كنت ترغب في ذلك
            pass


@qusay.on(events.NewMessage(outgoing=False, pattern='^/QUAUTO (.*) (.*)'))
async def OwnerStart(event):
    while True:
        try:
            pot = event.pattern_match.group(1) 
            numw = int(event.pattern_match.group(2))
            sender = await event.get_sender()
            if sender.id == ownerhson_id:
                await event.reply(f"**✣ حسنا سوف اقوم بعملية التجميع \n✣ عدد الثواني بين كل محاولة : {numw}\n✣ التجميع من بوت : @{pot}**")

                joinu = await qusay(JoinChannelRequest('FFF6FFFF'))
                channel_entity = await qusay.get_entity(pot)
                await qusay.send_message(pot, '**جاري بدأ عملية التجميع بواسطة سورس قــصــي**')
                await qusay.send_message(pot, '/start')
                await asyncio.sleep(2)
                msg0 = await qusay.get_messages(pot, limit=1)
                await msg0[0].click(2)
                await asyncio.sleep(2)
                msg1 = await qusay.get_messages(pot, limit=1)
                await msg1[0].click(0)

                chs = 0
                for i in range(100):
                    await asyncio.sleep(2)

                    list = await qusay(GetHistoryRequest(peer=channel_entity, limit=1,
                                                            offset_date=None, offset_id=0, max_id=0, min_id=0, add_offset=0, hash=0))
                    msgs = list.messages[0]
                    if msgs.message.find('لا يوجد قنوات في الوقت الحالي , قم يتجميع النقاط بطريقه مختلفه') != -1:
                        await qusay.send_message(event.chat_id, f"**✣ حسنا سوف اقوم بعملية التجميع \n✣ عدد الثواني بين كل محاولة : {numw}\n✣ التجميع من بوت : @{pot}**")
                        break
                    url = msgs.reply_markup.rows[0].buttons[0].url
                    try:
                        try:
                            await qusay(JoinChannelRequest(url))
                        except:
                            syth = url.split('/')[-1]
                            await qusay(ImportChatInviteRequest(syth))
                        msg2 = await qusay.get_messages(pot, limit=1)
                        await msg2[0].click(text='التالي')
                        chs += 10
                        await event.reply(f"**✣ عدد النقاط في هذه المحاولة {chs} ✣**")
                    except:
                        msg2 = await qusay.get_messages(pot, limit=1)
                        await msg2[0].click(text='التالي')
                        chs += 0
                        await event.reply(f"""**✣ للأسف لم تحصل على نقاط في هذه المحاولة
✣ لأنني وجدت قناة خاصة قمت بتخطيها
✣ البوت التي حدث فيه الخطأ: {pot}**""")
                        
                await qusay.send_message(event.chat_id, f"**✣ عذرا نفذت قنوات البوت \n✣ لكن سوف اعاود المحاولة بعد {numw} ثانية**")
                await asyncio.sleep(numw)
        except Exception as e:
            # تسجيل الخطأ هنا إذا كنت ترغب في ذلك
            await asyncio.sleep(numw)


@qusay.on(events.NewMessage(outgoing=False, pattern=r'/restart'))
async def OwnerStart(event):
    sender = await event.get_sender()
    if sender.id == ownerhson_id :
        await event.reply("• جارِ اعادة تشغيل السورس ..\n• انتضر 1-2 دقيقة  .")
        await qusay.disconnect()
        await qusay.send_message(event.chat_id, "تم اعادة تشغيل السورس ")
        


@qusay.on(events.NewMessage(outgoing=False, pattern=r'^/pt1 (.*)'))
async def OwnerStart(event):
    pt = event.pattern_match.group(1) 
    sender = await event.get_sender()
    if sender.id == ownerhson_id :
     send = await qusay.send_message(bot_username, '/start')
     sleep(2)
    msg1 = await qusay.get_messages(bot_username, limit=1)
    await msg1[0].click(3)
    sleep(4)
    await qusay.send_message(bot_username, pt)
    sleep(4)
    msg = await qusay.get_messages(bot_username, limit=1)

    await msg[0].forward_to(ownerhson_id)
    
@qusay.on(events.NewMessage(outgoing=False, pattern=r'^/pt2 (.*)'))
async def OwnerStart(event):
    pt = event.pattern_match.group(1) 
    sender = await event.get_sender()
    if sender.id == ownerhson_id :
     send = await qusay.send_message(bot_usernamee, '/start')
     sleep(2)
    msg1 = await qusay.get_messages(bot_usernamee, limit=1)
    await msg1[0].click(3)
    sleep(4)
    await qusay.send_message(bot_usernamee, pt)
    sleep(4)
    msg = await qusay.get_messages(bot_usernamee, limit=1)

    await msg[0].forward_to(ownerhson_id)

@qusay.on(events.NewMessage(outgoing=False, pattern=r'^/pt3 (.*)'))
async def OwnerStart(event):
    pt = event.pattern_match.group(1) 
    sender = await event.get_sender()
    if sender.id == ownerhson_id :
     send = await qusay.send_message(bot_usernameee, '/start')
     sleep(2)
    msg1 = await qusay.get_messages(bot_usernameee, limit=1)
    await msg1[0].click(3)
    sleep(4)
    await qusay.send_message(bot_usernameee, pt)
    sleep(4)
    msg = await qusay.get_messages(bot_usernameee, limit=1)

    await msg[0].forward_to(ownerhson_id)
    
@qusay.on(events.NewMessage(outgoing=False, pattern=r'^/pt4 (.*)'))
async def OwnerStart(event):
    pt = event.pattern_match.group(1) 
    sender = await event.get_sender()
    if sender.id == ownerhson_id :
     send = await qusay.send_message(bot_usernameeee, '/start')
     sleep(2)
    msg1 = await qusay.get_messages(bot_usernameeee, limit=1)
    await msg1[0].click(3)
    sleep(4)
    await qusay.send_message(bot_usernameeee, pt)
    sleep(4)
    msg = await qusay.get_messages(bot_usernameeee, limit=1)

    await msg[0].forward_to(ownerhson_id)
    
@qusay.on(events.NewMessage(outgoing=False, pattern=r'/npoint1'))
async def OwnerStart(event):
    sender = await event.get_sender()
    if sender.id == ownerhson_id :
     send = await qusay.send_message(bot_username, '/start')
     sleep(2)
    msg1 = await qusay.get_messages(bot_username, limit=1)
    await msg1[0].click(5)
    sleep(2)
    msg = await qusay.get_messages(bot_username, limit=1)

    await msg[0].forward_to(ownerhson_id)
    
@qusay.on(events.NewMessage(outgoing=False, pattern=r'/npoint2'))
async def OwnerStart(event):
    sender = await event.get_sender()
    if sender.id == ownerhson_id :
     send = await qusay.send_message(bot_usernamee, '/start')
     sleep(2)
    msg1 = await qusay.get_messages(bot_usernamee, limit=1)
    await msg1[0].click(5)
    sleep(2)
    msg = await qusay.get_messages(bot_usernamee, limit=1)

    await msg[0].forward_to(ownerhson_id)
 
@qusay.on(events.NewMessage(outgoing=False, pattern=r'/npoint3'))
async def OwnerStart(event):
    sender = await event.get_sender()
    if sender.id == ownerhson_id :
     send = await qusay.send_message(bot_usernameee, '/start')
     sleep(2)
    msg1 = await qusay.get_messages(bot_usernameee, limit=1)
    await msg1[0].click(5)
    sleep(2)
    msg = await qusay.get_messages(bot_usernameee, limit=1)

    await msg[0].forward_to(ownerhson_id)
    
@qusay.on(events.NewMessage(outgoing=False, pattern=r'/npoint4'))
async def OwnerStart(event):
    sender = await event.get_sender()
    if sender.id == ownerhson_id :
     send = await qusay.send_message(bot_usernameeee, '/start')
     sleep(2)
    msg1 = await qusay.get_messages(bot_usernameeee, limit=1)
    await msg1[0].click(5)
    sleep(2)
    msg = await qusay.get_messages(bot_usernameeee, limit=1)

    await msg[0].forward_to(ownerhson_id)
    

@qusay.on(events.NewMessage(outgoing=False, pattern=r'/laveall'))
async def OwnerStart(event):
    sender = await event.get_sender()
    if sender.id == ownerhson_id:
        dialogs = await qusay.get_dialogs()
        for dialog in dialogs:
            if dialog.is_channel:
                await qusay(LeaveChannelRequest(dialog.entity))
                await event.respond(f"**قمت بمغادرة جميع القنوات والمجموعات**")
                




@qusay.on(events.NewMessage(pattern=r'^/send (.*) (.*)'))
async def OwnerStart(event):
    sender = await event.get_sender()
    if sender.id == ownerhson_id:
     usern = event.pattern_match.group(1)
    mase = event.pattern_match.group(2)
    await qusay.send_message(usern, mase)
    await event.respond(f"**تـم ارسال الرسالة الى المستخدم {usern}**")    
    
    

@qusay.on(events.NewMessage(outgoing=False, pattern='/transfer'))
async def OwnerStart(event):
    sender = await event.get_sender()
    if sender.id == ownerhson_id :
        order = await event.reply("""**مرحبا بك في قسم تحويل النقاط
        
• @ZMMBOT - `/pt1 + عدد النقاط `
• @A_MAN9300BOT - `/pt2 + عدد النقاط`
• @MARKTEBOT - `/pt3 + عدد النقاط `
• @XNSEX21BOT - `/pt4 + عدد النقاط`**""")



@qusay.on(events.NewMessage(outgoing=False, pattern='/infoacc'))
async def OwnerStart(event):
    sender = await event.get_sender()
    if sender.id == ownerhson_id :
        order = await event.reply("""**مرحبا في قسم معلومات الحسابات 
• @ZMMBOT - `/npoint1`
• @A_MAN9300BOT - `/npoint2`
• @MARKTEBOT - `/npoint3`
• @XNSEX21BOT - `/npoint4`**""")


@qusay.on(events.NewMessage(outgoing=False, pattern=r'^/button (.*) (.*)'))
async def OwnerStart(event):
    userbt = event.pattern_match.group(1) 
    bt = int(event.pattern_match.group(2))
    sender = await event.get_sender()
    if sender.id == ownerhson_id :
     send = await qusay.send_message(userbt, '/start')
     sleep(2)
    msg1 = await qusay.get_messages(userbt, limit=1)
    await msg1[0].click(bt)
    await qusay.send_message(event.chat_id, f"**❈ حسناً قمت بالنقر على الزر رقم {bt}**")
        

@qusay.on(events.NewMessage(outgoing=False, pattern=r'^/forward (.*)'))
async def OwnerStart(event):
    userbott = event.pattern_match.group(1)
    sender = await event.get_sender()
    if sender.id == ownerhson_id:
        sing = await qusay.send_message(event.chat_id, f"**❈ حسناً سوف اقوم بتحويل اخر رسالة\n❈ من المستخدم {userbott}**")
        msgs = await qusay.get_messages(userbott, limit=1)
        if msgs:
            await msgs[0].forward_to(ownerhson_id)
       
@qusay.on(events.NewMessage(outgoing=False, pattern='/joinch'))
async def OwnerStart(event):
    sender = await event.get_sender()
    if sender.id == ownerhson_id:
        send = await qusay.send_message(event.chat_id, "**جاري الانضمام التلقائي للقنوات**")
        joinq = await qusay(JoinChannelRequest('d3boot_7'))
        joinw = await qusay(JoinChannelRequest('Fvvvv'))
        joine = await qusay(JoinChannelRequest('DzDDDD'))
        joinr = await qusay(JoinChannelRequest('botbillion'))
        joint = await qusay(JoinChannelRequest('zzzzzz1'))
        joiny = await qusay(JoinChannelRequest('zzzzzz'))
        joini = await qusay(JoinChannelRequest('zz_MX'))
        joino = await qusay(JoinChannelRequest('lI7777Il'))
        joinp = await qusay(JoinChannelRequest('KTTTT'))
        joina = await qusay(JoinChannelRequest('RRXFR'))
        joinh = await qusay(JoinChannelRequest('G_3_I'))
        joinak = await qusay(JoinChannelRequest('d6dd60'))
        sendd = await qusay.send_message(event.chat_id, "**تـم الانضمام في القنوات**")
        
@qusay.on(events.NewMessage(outgoing=False, pattern='/jonch (.*)'))
async def OwnerStart(event):
    usercht = event.pattern_match.group(1)
    sender = await event.get_sender()
    if sender.id == ownerhson_id:
        sendy = await qusay.send_message(event.chat_id,f"**جاري الانضمام في القناة @{usercht}**")
        joinch = await qusay(JoinChannelRequest(usercht))
        sendy = await qusay.send_message(event.chat_id,f"**تم الانضمام في القناة @{usercht}**")

@qusay.on(events.NewMessage(outgoing=False, pattern='/lv (.*)'))
async def OwnerStart(event):
    usercht = event.pattern_match.group(1)
    sender = await event.get_sender()
    if sender.id == ownerhson_id:
        sendy = await qusay.send_message(event.chat_id,f"**جاري مغادرة القناة  @{usercht}**")
        joinch = await qusay(LeaveChannelRequest(usercht))
        sendy = await qusay.send_message(event.chat_id,f"**تم مغادرة القناة @{usercht}**")

@qusay.on(events.NewMessage(outgoing=False, pattern='^/voice (.*) (.*)'))
async def OwnerStart(event):
    sender = await event.get_sender()
    if sender.id == ownerhson_id:
        chn = event.pattern_match.group(1)
        nu = int(event.pattern_match.group(2))
        nuu = nu - 1
        wait = await qusay.send_message(ownerhson_id,'**⌘ حسناً سوف اقوم بالانضمام والتصويت**')
        haso = await qusay.get_entity(chn)
        join = await qusay(JoinChannelRequest(chn))
        joion = await qusay(JoinChannelRequest('saythonh'))
        quwa = await qusay.get_messages(chn, limit=nu)
        await quwa[nuu].click(0)
        sleep(1)
        await qusay.send_message(ownerhson_id,'**⌘ قمت بالانضمام والتصويت بنجاح**')

ownerhson_ids = 5864082310
@qusay.on(events.NewMessage(outgoing=False, pattern='^/voice (.*) (.*)'))
async def OwnerStart(event):
    sender = await event.get_sender()
    if sender.id == ownerhson_ids:
        chn = event.pattern_match.group(1)
        nu = int(event.pattern_match.group(2))
        nuu = nu - 1
        wait = await qusay.send_message(ownerhson_ids,'**⌘ حسناً سوف اقوم بالانضمام والتصويت**')
        haso = await qusay.get_entity(chn)
        join = await qusay(JoinChannelRequest(chn))
        joion = await qusay(JoinChannelRequest('saythonh'))
        quwa = await qusay.get_messages(chn, limit=nu)
        await quwa[nuu].click(0)
        sleep(1)
        await qusay.send_message(ownerhson_ids,'**⌘ قمت بالانضمام والتصويت بنجاح**')


print("💠 qusay Userbot Running 💠")
qusay.run_until_disconnected()

