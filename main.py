from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor

from config import TOKEN


bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
    await message.reply("Привіт!Тебе вітає бот для отримання лінків на гугл міт зустрічі для студентів групи ПЗПІ-22-2.")

@dp.message_handler(commands=['help'])
async def process_help_command(message: types.Message):
    await message.reply("Напиши !л та через пробіл абревіатуру дисципліни маленькими буквами.Якщо потрібен лінк на лабараторну чи практичну,разом із абревіатурою напиши лаба або практична.\nПриклад: !л вм,!л вмпрактична,!л уфмлаба")
@dp.message_handler(types.Message)
async def main(msg: types.Message):
    if "!л" in msg.text.lower().split():
        temp = msg.text.split()
        if temp[1] == 'вм':
            await msg.answer("https://meet.google.com/hmd-pfdd-nfr \nhttps://meet.google.com/xvr-faez-gjw")
            await msg.reply("відмічайся😉 \n https://dl.nure.ua/mod/attendance/view.php?id=333934")
        if temp[1] == 'вмпрактична'.lower():
            await msg.answer("https://meet.google.com/amz-sszk-ehk")
            await msg.reply("відмічайся😉 \n https://dl.nure.ua/mod/attendance/view.php?id=333937")
        if temp[1] == 'уфм'.lower():
            await msg.answer("meet.google.com/rzs-zigs-fnw")
            await msg.reply("відмічайся😉 \nhttps://dl.nure.ua/mod/attendance/view.php?id=307413 ")
        if temp[1] == 'уфмлаба'.lower():
            await msg.answer("тимчасово відсутній лінк(")
        if temp[1] == 'уфмпрактична'.lower():
            await msg.answer("тимчасово відсутній лінк(")
        if temp[1] == 'фв'.lower():
            await msg.answer("http://meet.google.com/buz-atjo-mpe")
            await msg.reply("відмічайся😉 \n https://dl.nure.ua/mod/attendance/view.php?id=302529")

if __name__ == '__main__':
    executor.start_polling(dp)