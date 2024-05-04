from sqladmin import ModelView
from server.models import User

class UserAdmin(ModelView, model=User):
    name = "Пользователь"
    name_plural = "Пользователи"
    icon = "fa-solid fa-user-circle"

    column_list = [User.id, User.username, User.email]
    column_details_list = [User.id, User.username, User.email]
    column_labels = {
        User.id: "ID",
        User.username: "Имя пользователя",
        User.email: "Электронная почта"
    }

    form_excluded_columns = ['devices', 'measurements', 'password']