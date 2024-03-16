from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.popup import Popup
from kivy.core.text import LabelBase
from kivy.clock import Clock
import requests  # Importing the requests library

class MyKiosk(App):
    def build(self):
        # 한글 폰트 설정
        LabelBase.register(name='NanumGothic', fn_regular='fonts/NanumGothic.ttf')

        # 메뉴별 가격 정보
        self.menu_prices = {'타코야끼': 6000, '문꼬치': 5000}

        self.order_count = 0
        self.order_history = {'타코야끼': 0, '문꼬치': 0}
        self.total_price = 0
        
        layout = BoxLayout(orientation='vertical')

        title_label = Label(text='풍지네 닭꼬치', font_name='NanumGothic', font_size=30)
        layout.add_widget(title_label)

        # 주문 내역 표시 레이블 추가
        self.order_history_label = Label(text='', font_name='NanumGothic')
        layout.add_widget(self.order_history_label)

        # 주문량과 합계 가격 표시 레이블 추가
        self.order_label = Label(text=f'주문량: {self.order_count}\n합계 가격: {self.total_price}원', font_name='NanumGothic')
        layout.add_widget(self.order_label)

        takoyaki_button = Button(text='타코야끼 - 6000원', font_name='NanumGothic')
        takoyaki_button.bind(on_press=self.order_takoyaki)
        layout.add_widget(takoyaki_button)

        skewer_button = Button(text='문꼬치 - 5000원', font_name='NanumGothic')
        skewer_button.bind(on_press=self.order_skewer)
        layout.add_widget(skewer_button)

        order_button = Button(text='주문하기', font_name='NanumGothic')
        order_button.bind(on_press=self.send_order_to_server)  # Change binding to send_order_to_server
        layout.add_widget(order_button)

        reset_button = Button(text='주문 초기화', font_name='NanumGothic')
        reset_button.bind(on_press=self.reset_order_count)
        layout.add_widget(reset_button)

        return layout

    def order_takoyaki(self, instance):
        self.order_count += 1
        self.order_history['타코야끼'] += 1
        self.total_price += self.menu_prices['타코야끼']
        self.update_order_label()

    def order_skewer(self, instance):
        self.order_count += 1
        self.order_history['문꼬치'] += 1
        self.total_price += self.menu_prices['문꼬치']
        self.update_order_label()

    def send_order_to_server(self, instance):  # New method to send order data to the server
        order_data = {'order_count': self.order_count, 'order_history': self.order_history, 'total_price': self.total_price}
        response = requests.post('http://your-server-url.com/order', json=order_data)
        if response.status_code == 200:
            popup = Popup(title='Order Sent', content=Label(text='주문이 성공적으로 전송되었습니다.', font_name='NanumGothic'), size_hint=(None, None), size=(300, 200))
            popup.open()
        else:
            popup = Popup(title='Order Failed', content=Label(text='주문 전송에 실패했습니다.', font_name='NanumGothic'), size_hint=(None, None), size=(300, 200))
            popup.open()

    def reset_order_count(self, instance=None):
        self.order_count = 0
        self.order_history = {'타코야끼': 0, '문꼬치': 0}
        self.total_price = 0
        self.update_order_label()

    def update_order_label(self):
        order_text = f'주문 내역:\n'
        for item, quantity in self.order_history.items():
            if quantity > 0:
                order_text += f"{item}: {quantity}개 - {self.menu_prices[item] * quantity}원\n"
        self.order_history_label.text = order_text
        self.order_label.text = f'주문량: {self.order_count}\n합계 가격: {self.total_price}원'
        

if __name__ == '__main__':
    MyKiosk().run()
