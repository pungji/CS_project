from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.popup import Popup
from kivy.core.text import LabelBase
from kivy.clock import Clock

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
        order_button.bind(on_press=self.show_order_confirmation)
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

    def show_order_confirmation(self, instance):
        if self.order_count == 0:
            popup = Popup(title='ALERT', content=Label(text='주문량이 0입니다. 메뉴를 선택해주세요.', font_name='NanumGothic'), size_hint=(None, None), size=(300, 200))
            popup.open()
        else:
            confirmation_text = f'주문 내역:\n'
            for item, quantity in self.order_history.items():
                if quantity > 0:
                    confirmation_text += f"{item}: {quantity}개 - {self.menu_prices[item] * quantity}원\n"
            confirmation_text += f'\n총 가격: {self.total_price}원\n\n이렇게 주문하시겠습니까?'

            confirmation_popup = Popup(title='ORDER', size_hint=(None, None), size=(400, 300))
            popup_content = BoxLayout(orientation='vertical')
            popup_content.add_widget(Label(text=confirmation_text, font_name='NanumGothic'))
            button_layout = BoxLayout(orientation='horizontal', size_hint=(1, None), height=50)
            yes_button = Button(text='예', font_name='NanumGothic', size_hint=(0.5, 1))
            yes_button.bind(on_press=self.complete_order)
            no_button = Button(text='아니요', font_name='NanumGothic', size_hint=(0.5, 1))
            no_button.bind(on_press=confirmation_popup.dismiss)
            button_layout.add_widget(yes_button)
            button_layout.add_widget(no_button)
            popup_content.add_widget(button_layout)
            confirmation_popup.content = popup_content
            confirmation_popup.open()

    def complete_order(self, instance):
        self.reset_order_count()
        complete_popup = Popup(title='ALERT', content=Label(text='주문이 완료되었습니다.', font_name='NanumGothic'), size_hint=(None, None), size=(300, 200))
        complete_popup.open()
        Clock.schedule_once(self.close_popup, 1)  # 1초 후에 팝업 닫기

    def close_popup(self, dt):
        for widget in App.get_running_app().root_window.children:
            if isinstance(widget, Popup):
                widget.dismiss()

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
