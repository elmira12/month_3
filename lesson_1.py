# from aiogram import Bot, Dispatcher, types, executor
# from config import token

# bot = Bot(token=token)
# dp = Dispatcher(bot)

# @dp.message_handler(commands='start')
# async def start(message:types.Message):
#     await message.answer("Привет мир")

# @dp.message_handler(commands='help')
# async def help(message:types.Message):
#     await message.answer("Чем могу помочь? ")

# @dp.message_handler(text="Привет")
# async def hello(message:types.Message):
#     await message.answer("Привет, как дела?")

# @dp.message_handler(commands='test')
# async def test(message:types.Message):
#     await message.answer("Тестовой ответ")
#     await message.answer_location(40.51931846586533, 72.80297788183063)
#     await message.answer_photo('https://geeks.kg/back_media/main_block/2023/06/22/96425634-e4e2-44ae-8f86-243519f735f3.webp')
#     with open('мирбек.mp3','rb') as music:
#         await message.answer_audio(music)
#     await message.answer_contact('996507646420', 'Moldosakova', 'Elmira')
#     await message.answer_dice()
#     print(message)
#     await message.answer(f"Здраствуйте {message.from_user.full_name}")

# @dp.message_handler()
# async def not_found(message:types.Message):
#     await message.reply("Я вас не понял, введите /help")
    
# executor.start_polling(dp)