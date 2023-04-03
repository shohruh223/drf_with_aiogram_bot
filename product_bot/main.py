import logging
from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.types import ReplyKeyboardRemove
from aiogram.utils import executor

from db import all_product, db_start, add_product
from keyboard import get_product, get_inline_product
from product_bot.api import product_list, create_product
from state import ProductState

API_TOKEN = '6052543163:AAFe-jpzas6mcCjZLIR_MW02GyuLosi_OCM'

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
storage = MemoryStorage()
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot, storage=storage)


@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    await message.answer("welcome to my bot",
                         reply_markup=get_product())


@dp.message_handler(commands=['product'])
async def start(message: types.Message):
    await message.answer("products",
                         reply_markup=ReplyKeyboardRemove())
    await message.answer(text="📦📦📦📦📦📦",
                         reply_markup=get_inline_product())


@dp.callback_query_handler()
async def callback_product(callback: types.CallbackQuery):
    if callback.data == "all product":
        products = product_list()
        if not products:
            await callback.message.answer("Hali productlar mavjud emas")
            await callback.answer()
            return await callback.answer()
        await callback.message.answer(products)
    elif callback.data == "add product":
        await callback.message.answer("Productni nomini kiriting")
        await ProductState.title.set()


@dp.message_handler(state=ProductState.title)
async def load_title(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['title'] = message.text

    await message.answer("rasmni kiriting")
    await ProductState.next()


@dp.message_handler(state=ProductState.photo, content_types=['photo'])
async def load_photo(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['photo'] = message.photo[0].file_id

    await message.answer("product haqida izoh qoldiring")
    await ProductState.next()


@dp.message_handler(state=ProductState.description)
async def load_description(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['description'] = message.text

    await message.answer("product narxini kiriting")
    await ProductState.next()


@dp.message_handler(state=ProductState.price)
async def load_price(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['price'] = message.text
        await bot.send_photo(chat_id=message.from_user.id,
                             photo=data['photo'],
                             caption=f"Mahsulotni nomi {data['title']},"
                                     f"mahsulot haqida: {data['description']},"
                                     f"narxi {data['price']}")
        # await bot.send_message(chat_id=message.from_user.id,
        #                        text=f"{data['title']}")

    await message.answer("mahsulot saqlandi")
    await create_product(title=data['title'],
                         photo=data['photo'],
                         description=data['description'],
                         price=data['price'])
    await state.finish()


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)