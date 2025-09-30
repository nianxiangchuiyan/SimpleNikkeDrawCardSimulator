import sys, test
from random import random, randint

from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout, QLineEdit, QMessageBox
from test import draw

draw_result =[]
ticket:int
gem:int
def get():
    global ticket, gem
    try:
        ticket = int(text_box2.text())
    except ValueError:
        ticket = 0
    try:
        gem = int(text_box.text())
    except ValueError:
        gem = 0

def update():
    global ticket, gem
    text_box2.setText(str(ticket))
    text_box.setText(str(gem))
    print(draw_result)


def show_result():
    if draw_result:
        # 从test模块获取角色池信息
        from test import CharacterPool
        character_pool = CharacterPool()

        # 定义各类型的颜色映射
        type_colors = {
            "pilgrim": "black",
            "gold": "gold",
            "up": "red",
            "purple": "purple",
            "blue": "blue"
        }

        # 创建角色到颜色的映射
        character_color_map = {}
        for type_name in character_pool.get_types():
            characters = character_pool.get_characters(type_name)
            color = type_colors.get(type_name, "black")
            for character in characters:
                character_color_map[character] = color

        # 构建带颜色的HTML文本
        colored_results = []
        for result in draw_result:
            color = character_color_map.get(result, "black")  # 默认黑色
            colored_results.append(f'<span style="color:{color};">{result}</span>')

        msg = QMessageBox()
        msg.setWindowTitle("抽卡结果")
        msg.setTextFormat(1)  # Qt.RichText
        msg.setText("<br>".join(colored_results))
        msg.exec_()


def on_click_1():
    global draw_result, ticket, gem
    get()
    if ticket > 0:
        draw_result = draw(1)
        ticket -= 1
    elif gem >= 300:
        draw_result = draw(1)
        gem -= 300
    else:
        return
    update()
    show_result()  # 显示结果弹窗

def on_click_10():
    global draw_result, ticket, gem
    get()
    if ticket > 9:
        draw_result = draw(10)
        ticket -= 10
    elif int(gem/300) + ticket >= 10:
        draw_result = draw(10)
        gem -= 300 * (10 - ticket)
        ticket = 0
    elif gem >= 3000:
        draw_result = draw(10)
        gem -= 3000
    else:
        return
    update()
    show_result()  # 显示结果弹窗



app = QApplication(sys.argv)
window = QWidget()
window.setWindowTitle("我的第一个 PyQt GUI")

layout = QVBoxLayout()

label = QLabel("简易妮姬抽卡\n")

label1 = QLabel("钻：")
label2 = QLabel("票：")
text_box = QLineEdit()
text_box.setPlaceholderText("30000")
text_box2 = QLineEdit()
text_box2.setPlaceholderText("5")


#单抽按钮
button_draw1 = QPushButton("单抽")

#十连按钮
button_draw10 = QPushButton("十连抽")
button_draw1.clicked.connect(on_click_1)
button_draw10.clicked.connect(on_click_10)

layout.addWidget(label)
layout.addWidget(label1)
layout.addWidget(text_box)
layout.addWidget(label2)
layout.addWidget(text_box2)
layout.addWidget(button_draw1)
layout.addWidget(button_draw10)
window.setLayout(layout)

window.show()
sys.exit(app.exec_())

