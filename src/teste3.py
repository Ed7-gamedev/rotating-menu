import flet as ft
import math
import asyncio

def main(page: ft.Page):
    page.bgcolor = "black"
    page.title = "Menu Circular"
    page.window_width = 600
    page.window_height = 600
    
    center_x, center_y = 300, 300
    radius = 150
    colors = ["red", "blue", "green", "yellow", "purple", "orange"]
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
        
        triangle = ft.Container(
            content=ft.Icon(name=icon, color="white", size=30),
            width=120,
            height=120,
            bgcolor=colors[i],
            border_radius=0,
            shape=ft.BoxShape.RECTANGLE,
            left=x - 60,
            top=y - 60,
            rotate=ft.Rotate(angle, alignment=ft.alignment.center)
        )
        menu_items.append(triangle)
    
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
    
    async def rotate_containers():
        while True:
            for item in menu_items:
                item.rotate.angle += 0.1
                item.update()
            await asyncio.sleep(0.05)
    
    page.run_task(rotate_containers)

ft.app(target=main)