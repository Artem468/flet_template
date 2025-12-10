import flet as ft
from tables.database import SessionLocal
from tables.models.user import User


def users_view(page: ft.Page) -> ft.View:
    username_input = ft.TextField(label="Имя", width=250)
    password_input = ft.TextField(label="Пароль", width=250, password=True)
    users_column = ft.Column(scroll=ft.ScrollMode.AUTO)

    def load_users():
        users_column.controls.clear()
        db = SessionLocal()
        try:
            for user in db.query(User).order_by(User.id).all():
                users_column.controls.append(
                    ft.Row(
                        [
                            ft.Text(f"{user.id}: {user.username}", expand=True),
                            ft.IconButton(
                                icon=ft.Icons.DELETE,
                                icon_color="red",
                                tooltip="Удалить",
                                on_click=lambda e, uid=user.id: delete_user(uid),
                            ),
                        ]
                    )
                )
        finally:
            db.close()
        page.update()

    def add_user(e):
        username = username_input.value.strip()
        password = password_input.value.strip()
        if not username or not password:
            return
        db = SessionLocal()
        try:
            db_user = User(username=username, password=password)
            db.add(db_user)
            db.commit()
            username_input.value = ""
            password_input.value = ""
        finally:
            db.close()
        load_users()

    def delete_user(user_id: int):
        db = SessionLocal()
        try:
            user = db.query(User).filter(User.id == user_id).first()
            if user:
                db.delete(user)
                db.commit()
        finally:
            db.close()
        load_users()

    add_button = ft.ElevatedButton("Добавить", on_click=add_user)

    view = ft.View(
        route="/users",
        controls=[
            ft.AppBar(
                title=ft.Text("Пользователи"),
                bgcolor=ft.Colors.SURFACE,
                leading=ft.IconButton(
                    icon=ft.Icons.ARROW_BACK,
                    on_click=lambda _: page.go("/"),
                ),
            ),
            ft.Container(
                content=ft.Column(
                    [
                        ft.Row([username_input, password_input, add_button]),
                        ft.Divider(),
                        ft.Text("Список пользователей:", size=18, weight=ft.FontWeight.BOLD),
                        users_column,
                    ],
                    expand=True,
                ),
                padding=20,
                expand=True,
            ),
        ],
    )

    load_users()
    return view
