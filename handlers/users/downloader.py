from cgitb import text
from distutils import text_file
from distutils.text_file import TextFile
from functools import cache
from os import link
from subprocess import call
from urllib import response
from aiogram import types
from aiogram.types import InlineKeyboardMarkup,InlineKeyboardButton
from loader import dp
from tiktok import tk
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher.filters.builtin import CallbackQuery
@dp.message_handler(Text(startswith='https'))
async def test(message:types.Message):
    natija = tk(message.text)

    qoshiq=natija['music']
    btn = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="Musiqasini yuklab olish",url="{}".format(qoshiq))]
             
         ]
    )

    await message.answer_audio(natija['video'],caption='<b>@savestkbot orqali yuklab olindi</b>',parse_mode='HTML',reply_markup=btn )
    @dp.callback_query_handler(Text(startswith=''))
    async def test2(call:CallbackQuery):
        await call.answer(cache_time=60)
        data = call.data[1:]
        await call.message.answer_audio(data)

