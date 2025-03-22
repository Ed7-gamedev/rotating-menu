import flet as ft
import math
import asyncio
import random

def main(page: ft.Page):
    page.bgcolor = "white"
    page.title = "Menu Circular"
    
    def update_layout():
        width, height = page.window.width, page.window.height
        center_x, center_y = width // 2, height // 2
        radius = min(width, height) // 3
        
        for i, item in enumerate(menu_items):
            angles[i] += 0.05  # Incrementa o ângulo para rotação
            x = center_x + radius * math.cos(angles[i])
            y = center_y + radius * math.sin(angles[i])
            item.left = x - item.width // 2 if item.width else x
            item.top = y - item.height // 2 if item.height else y
            item.update()
        
        if center_button.width and center_button.height:
            center_button.left = center_x - center_button.width // 2
            center_button.top = center_y - center_button.height // 2
        else:
            center_button.left = center_x
            center_button.top = center_y
        
        center_button.update()
        
        stack.width = width
        stack.height = height
        
        stack.update()
    
    page.on_resize = lambda e: update_layout()
    
    colors = ["red", "blue", "green", "yellow", "purple", "orange"]
    icons = [
        ("Settings", ft.Icons.SETTINGS),
        ("Home", ft.Icons.HOME),
        ("News", ft.Icons.NEWSPAPER),
        ("Movies", ft.Icons.MOVIE),
        ("Sports", ft.  Icons.SPORTS_SOCCER),
        ("Music", ft.Icons.MUSIC_NOTE),
    ]
    
    menu_items = []
    angles = []
    for i, (label, icon) in enumerate(icons):
        angle = (i / len(icons)) * 2 * math.pi
        angles.append(angle)
        triangle = ft.Container(
            content=ft.Icon(name=icon, color="white", size=30),
            width=120,
            height=120,
            bgcolor=colors[i],
            border_radius=0,
            shape=ft.BoxShape.RECTANGLE,
        )
        menu_items.append(triangle)
    
    center_button = ft.IconButton(
        icon=ft.icons.MENU,
        icon_color= random.choice(colors),
        bgcolor=random.choice(colors),
        on_click=lambda e: print("Menu Clicked"),
        width= 100,
        height= 100,
        
    )
    
    stack = ft.Stack(menu_items + [center_button])
    page.add(stack)
    
    async def rotate_containers():
        while True:
            update_layout()
            await asyncio.sleep(0.05)
    
    page.run_task(rotate_containers)
    update_layout()

ft.app(target=main)
