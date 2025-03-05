from aiogram import Bot, Dispatcher, types
from aiogram.types import Message
import asyncio
from datetime import datetime
from config import TOKEN

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)
ADMIN_ID = "1047421689"  # O'zingizning Telegram ID raqamingizni yozing
messages = {}  # Xabarlarni saqlash

@dp.message_handler(content_types=types.ContentType.TEXT)
async def read_messages(message: Message):
    if message.chat.type in ["group", "supergroup"]:
        messages[message.message_id] = message.text  # Xabarni saqlash

@dp.edited_message_handler(content_types=types.ContentType.TEXT)
async def edited_messages(message: Message):
    eski_xabar = messages.get(message.message_id)
    if eski_xabar and eski_xabar != message.text:
        vaqt = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        matn = (f"✏️ *Xabar tahrirlandi!*\n\n"
                f"👤 Kim: {message.from_user.first_name}\n"
                f"🕰 Qachon: {vaqt}\n\n"
                f"🔄 Eski xabar:\n{eski_xabar}\n\n"
                f"🆕 Yangi xabar:\n{message.text}")

        await bot.send_message(ADMIN_ID, matn, parse_mode="Markdown")
        messages[message.message_id] = message.text  # Xabarni yangilash

async def main():
    print("Bot ishga tushdi...")
    await dp.start_polling()

if __name__ == "__main__":
    asyncio.run(main())
