from aiogram import Bot, Dispatcher, types
import asyncio
from datetime import datetime
from config import TOKEN

bot = Bot(token=TOKEN)
dp = Dispatcher()
ADMIN_ID = "1047421689"  # O'zingizning Telegram ID raqamingizni yozing
messages = {}  # Xabarlarni saqlash

@dp.message()
async def read_messages(message: types.Message):
    if message.chat.type in ["group", "supergroup"]:
        messages[message.message_id] = message.text  # Xabarni eslab qolamiz

@dp.edited_message()
async def edited_messages(message: types.Message):
    eski_xabar = messages.get(message.message_id)
    if eski_xabar and eski_xabar != message.text:
        vaqt = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        matn = (f"✏️ *Xabar tahrirlandi!*\n\n"
                f"👤 Kim: {message.from_user.first_name}\n"
                f"🕰 Qachon: {vaqt}\n\n"
                f"🔄 Eski xabar:\n{eski_xabar}\n\n"
                f"🆕 Yangi xabar:\n{message.text}")

        await bot.send_message(ADMIN_ID, matn, parse_mode="Markdown")
        messages[message.message_id] = message.text  # Yangi xabarni yangilaymiz

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
