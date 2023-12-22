from aiogram.fsm.state import StatesGroup, State


class RegisterUser(StatesGroup):
    NAME = State()
    FINAL = State()
