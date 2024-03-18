from nicegui import ui

ui.label('Hello NiceGUI!')
ui.button('BUTTON', on_click=lambda: ui.notify('button was pressed'))

ui.run(title="Hello! NiceGUI")

# 三角形の面積
def calc_tri(base, height):
    return base*height/2

calc_tri_lambda = lambda base, height: base*height/2
print(calc_tri(3, 10))
print(calc_tri_lambda(3, 10))