import flet as ft
import math

def main(page: ft.Page):
    page.bgcolor = "black"
    page.title = "Menu Circular"
    page.window_width = 600
    page.window_height = 600
    
    center_x, center_y = 300, 300
    radius = 150
    icons = [
        ("Settings", ft.icons.SETTINGS),
        ("Home", ft.icons.HOME),
        ("News", ft.icons.NEWSPAPER),
        ("Movies", ft.icons.MOVIE),
        ("Sports", ft.icons.SPORTS_SOCCER),
        ("Music", ft.icons.MUSIC_NOTE),
    ]
    
    menu_items = []
    for i, (label, icon) in enumerate(icons):
        angle = (i / len(icons)) * 2 * math.pi
        x = center_x + radius * math.cos(angle)
        y = center_y + radius * math.sin(angle)
        
        btn = ft.IconButton(icon=icon, icon_color="white", bgcolor="black", on_click=lambda e, lbl=label: print(lbl))
        btn.left = x - 24
        btn.top = y - 24
        menu_items.append(btn)
    
    center_button = ft.IconButton(
        icon=ft.icons.MENU,
        icon_color="black",
        bgcolor="white",
        on_click=lambda e: print("Menu Clicked")
    )
    center_button.left = center_x - 24
    center_button.top = center_y - 24
    
    stack = ft.Stack(menu_items + [center_button], width=600, height=600)
    page.add(stack)

ft.app(target=main)
