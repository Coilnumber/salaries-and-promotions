from .schemas import UserSchema
from datetime import date
from salaries_and_promotions.auth import utils as auth_utils

vadim_tregulov = UserSchema(
    login= "vadim.t",
    name = "Vadim Tregulov",
    password = auth_utils.hash_password("welcome"),
    salary = 60000,
    date_of_promotion = date(2025, 9, 5)
)

zakk_wylde = UserSchema(
    login= "zakk",
    name = "Zakk Wylde",
    password = auth_utils.hash_password("gibson"),
    salary = 9900000,
    date_of_promotion = date(2025, 12, 14)
)

sazonova_irina = UserSchema(
    login= "sazonova.irina",
    name = "Sazonova Irina",
    password = auth_utils.hash_password("1937"),
    salary = 75000,
    date_of_promotion = date(2025, 7, 19)
)




users_db: dict[str, UserSchema] = {
    vadim_tregulov.login: vadim_tregulov,
    zakk_wylde.login: zakk_wylde,
    sazonova_irina.login: sazonova_irina,
}