from aiogram.dispatcher.filters.state import StatesGroup, State


class ProductState(StatesGroup):
    title = State()
    photo = State()
    description = State()
    price = State()