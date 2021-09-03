from pyrogram import Client, Filters, StopPropagation, InlineKeyboardButton, InlineKeyboardMarkup


@Client.on_message(Filters.command(["start"]), group=-2)
async def start(client, message):
    # return
    Alpha = InlineKeyboardMarkup([
        
        [InlineKeyboardButton("My Dev ⚡️", url="https://t.me/invisible_einstein")],
        [InlineKeyboardButton("Telegram Channel⚡️ ", url="https://t.me/coobydoobots")]

    ])
    thumbnail_url = "https://telegra.ph/file/35ba0a85f0e7f346e99ce.jpg"
    await message.reply_photo(thumbnail_url, caption=f"**🙂 Hi <b>{message.from_user.first_name}**</b>\n\n<br>__😇 I Can Download YT Videos For You ✨️__</br>\n\n<b>• **🗂️ Instructions for use...🚨**</b>\n• **⚙ Type /help to get instructins...**\n \n───── ❝ **Lets Play** ❞ ─────\n ", reply_markup=Alpha)
    raise StopPropagation
