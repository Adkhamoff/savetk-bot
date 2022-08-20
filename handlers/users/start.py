from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart

from loader import dp


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    await message.answer(f"<b>Salom, ushbu bot TikTok dan videoni suv belgisiz va audio holda yuklab olishi mumkin havolani yuboring</b>", parse_mode='HTML')
#{message.from_user.full_name}