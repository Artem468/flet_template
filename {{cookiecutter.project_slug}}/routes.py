import flet as ft
from views.home import home_view
from views.users import users_view


def setup_routes(page: ft.Page):
    def route_change(e):
        page.views.clear()

        if page.route == "/":
            page.views.append(home_view(page))
        elif page.route == "/users":
            page.views.append(users_view(page))
        else:
            page.views.append(home_view(page))

        page.update()

    def view_pop(e):
        page.views.pop()
        top_view = page.views[-1]
        page.go(top_view.route)

    page.on_route_change = route_change
    page.on_view_pop = view_pop

    page.go(page.route)
