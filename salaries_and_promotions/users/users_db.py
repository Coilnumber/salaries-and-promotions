from .schemas import UserSchema
from datetime import date
from salaries_and_promotions.auth import utils as auth_utils

vadim_tregulov = UserSchema(
    login= "vadim",
    name = "Vadim Tregulov",
    password = auth_utils.hash_password("w"),
    salary = 60000,
    date_of_promotion = date(2025, 9, 5)
)


users_db: dict[str, UserSchema] = {
    vadim_tregulov.login: vadim_tregulov,
}