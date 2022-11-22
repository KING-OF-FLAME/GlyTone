

import asyncio

from pyrogram import filters
from pyrogram.types import (InlineKeyboardButton,
                            InlineKeyboardMarkup, Message)
from youtubesearchpython.__future__ import VideosSearch

import config
from config import BANNED_USERS
from config.config import OWNER_ID
from strings import get_command, get_string
from YukkiMusic import Telegram, YouTube, app
from YukkiMusic.misc import SUDOERS
from YukkiMusic.plugins.play.playlist import del_plist_msg
from YukkiMusic.plugins.sudo.sudoers import sudoers_list
from YukkiMusic.utils.database import (add_served_chat,
                                       add_served_user,
                                       blacklisted_chats,
                                       get_assistant, get_lang,
                                       get_userss, is_on_off,
                                       is_served_private_chat)
from YukkiMusic.utils.decorators.language import LanguageStart
from YukkiMusic.utils.inline import (help_pannel, private_panel,
                                     start_pannel)

loop = asyncio.get_running_loop()



@app.on_message(
    filters.command("donate")
    & filters.private
    & ~filters.edited
    & ~BANNED_USERS
)
@LanguageStart
async def donate_handler(client, message: Message, _):
    await message.reply_text("""🎉 So you want to donate? Amazing!
❇️ You can donate on **PayPal**, or **Buy Me a Coffee**""",reply_markup=InlineKeyboardMarkup( [ 
    [InlineKeyboardButton("PayPal",url="https://www.paypal.me/08pankaj"),InlineKeyboardButton("Buy Me Coffee",url="https://www.buymeacoffee.com/GlyTone")]
]))
   


@app.on_message(
    filters.command("donate")
    & filters.group
    & ~filters.edited
    & ~BANNED_USERS
)
@LanguageStart
async def donate_handler(client, message: Message, _):
    await message.reply_text("""🎉 So you want to donate? Amazing!
❇️ You can donate on **PayPal**, or **Buy Me a Coffee**""",reply_markup=InlineKeyboardMarkup( [ 
    [InlineKeyboardButton("PayPal",url="https://www.paypal.me/08pankaj"),InlineKeyboardButton("Buy Me Coffee",url="https://www.buymeacoffee.com/GlyTone")]
]))
   