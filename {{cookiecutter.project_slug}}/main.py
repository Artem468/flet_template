import flet as ft
from tables.database import init_db
from routes import setup_routes


def main(page: ft.Page):
    page.title = "Main"
    page.horizontal_alignment = "center"
    page.vertical_alignment = "start"

    init_db()

    setup_routes(page)


if __name__ == "__main__":
    ft.app(target=main)
