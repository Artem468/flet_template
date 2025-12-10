import flet as ft


def home_view(page: ft.Page) -> ft.View:
    return ft.View(
        route="/",
        controls=[
            ft.AppBar(title=ft.Text("Главная"), bgcolor=ft.Colors.SURFACE),
            ft.Container(
                alignment=ft.alignment.center,
                content=ft.Column(
                    [
                        ft.Text("Добро пожаловать!", size=30, weight=ft.FontWeight.BOLD),
                        ft.ElevatedButton(
                            "Управление пользователями",
                            on_click=lambda _: page.go("/users"),
                        ),
                    ],
                    alignment=ft.MainAxisAlignment.CENTER,
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                ),
                expand=True,
            ),
        ],
    )
