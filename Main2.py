from tkinter import Tk, Label, Button, PhotoImage, Toplevel
import tkinter as tk
import fitz
from PIL import Image, ImageTk

window = Tk()
window.iconbitmap(r'images/iconfortest.ico')
window.state('zoomed')


class MainMenu:
    def __init__(self):
        self.canvas = tk.Canvas(window, width=1920, height=1080)
        self.canvas.place(x=0, y=0)
        img = PhotoImage(file="images/zadnifon.png")
        self.canvas.create_image(0, 0, image=img, anchor='nw')
        self.main_menu()
        window.mainloop()

    def exit_app(self):
        confirm_window = Toplevel(window)
        confirm_window.grab_set()
        confirm_window.geometry("500x250+750+400")
        confirm_window.resizable(width=False, height=False)
        confirm_window.title("Выход из приложения")

        # x = (confirm_window.winfo_screenwidth() - confirm_window.winfo_reqwidth()) / 2
        # y = (confirm_window.winfo_screenheight() - confirm_window.winfo_reqheight()) / 2
        # confirm_window.wm_geometry("+%d+%d" % (x, y))

        Label(confirm_window, text="Вы уверенны, что хотите выйти?", font=("Times new Roman", 20)).place(x=50, y=10)
        Button(confirm_window, text="Выйти на рабочий стол", font=("Times new Roman", 16), bg="red",
               command=window.destroy).place(x=130, y=70)
        Button(confirm_window, text="Отмена", font=("Times new Roman", 16), bg="green",
               command=confirm_window.destroy).place(x=200, y=140)

    def main_menu(self):
        window.title("Учебник по ПДД")
        window.geometry("1920x1080+500+0")
        window.resizable(width=False, height=False)
        Button(self.canvas, text="1. Общие положения", font=("Times new Roman", 16), bg="#A2A2D0",
               command=lambda: self.start_theme("Unit_1")).place(x=20, y=150)
        Button(self.canvas, text="2. Общие обязанности водителей", font=("Times new Roman", 16), bg="#A2A2D0",
               command=lambda: self.start_theme("Unit_2")).place(x=20, y=200)
        Button(self.canvas, text="3. Применение специальных сигналов", font=("Times new Roman", 16), bg="#A2A2D0",
               command=lambda: self.start_theme("Unit_3")).place(x=20, y=250)
        Button(self.canvas, text="4. Обязанности пешеходов", font=("Times new Roman", 16), bg="#A2A2D0",
               command=lambda: self.start_theme("Unit_4")).place(x=20, y=300)
        Button(self.canvas, text="5. Обязаннсоти пассажиров", font=("Times new Roman", 16), bg="#A2A2D0",
               command=lambda: self.start_theme("Unit_5")).place(x=20, y=350)
        Button(self.canvas, text="6. Сигналы светофора и регулировщика", font=("Times new Roman", 16), bg="#A2A2D0",
               command=lambda: self.start_theme("Unit_6")).place(x=20, y=400)
        Button(self.canvas, text="7. Применение аварийной сигнализации и знака аварийной остановки",
               font=("Times new Roman", 16), bg="#A2A2D0", command=lambda: self.start_theme("Unit_7")).place(x=20,
                                                                                                             y=450)
        Button(self.canvas, text="8. Начало движения, маневрирование", font=("Times new Roman", 16), bg="#A2A2D0",
               command=lambda: self.start_theme("Unit_8")).place(x=20, y=500)
        Button(self.canvas, text="9. Расположение транспортных средств на проезжей части", font=("Times new Roman", 16),
               bg="#A2A2D0", command=lambda: self.start_theme("Unit_9")).place(x=20, y=550)
        Button(self.canvas, text="10. Скорость движения", font=("Times new Roman", 16), bg="#A2A2D0",
               command=lambda: self.start_theme("Unit_10")).place(x=20, y=600)
        Button(self.canvas, text="11. Обгон, опережение, встречный разъезд", font=("Times new Roman", 16), bg="#A2A2D0",
               command=lambda: self.start_theme("Unit_11")).place(x=20, y=650)
        Button(self.canvas, text="12. Остановка и стоянка", font=("Times new Roman", 16), bg="#A2A2D0",
               command=lambda: self.start_theme("Unit_12")).place(x=20, y=700)
        Button(self.canvas, text="13. Проезд перекрестков", font=("Times new Roman", 16), bg="#A2A2D0",
               command=lambda: self.start_theme("Unit_13")).place(x=20, y=750)
        Button(self.canvas, text="14. Пешеходные переходы и места остановок маршрутных транспортных средств",
               font=("Times new Roman", 16), bg="#A2A2D0", command=lambda: self.start_theme("Unit_14")).place(x=690,
                                                                                                              y=150)
        Button(self.canvas, text="15. Движение через железнодорожные пути", font=("Times new Roman", 16), bg="#A2A2D0",
               command=lambda: self.start_theme("Unit_15")).place(x=690, y=200)
        Button(self.canvas, text="16. Движение по автомагистралям", font=("Times new Roman", 16), bg="#A2A2D0",
               command=lambda: self.start_theme("Unit_16")).place(x=690, y=250)
        Button(self.canvas, text="17. Движение в жилых зонах", font=("Times new Roman", 16), bg="#A2A2D0",
               command=lambda: self.start_theme("Unit_17")).place(x=690, y=300)
        Button(self.canvas, text="18. Приоритет маршрутных транспортных средств", font=("Times new Roman", 16),
               bg="#A2A2D0", command=lambda: self.start_theme("Unit_18")).place(x=690, y=350)
        Button(self.canvas, text="19. Пользование внешними световыми приборами и звуковыми сигналами",
               font=("Times new Roman", 16), bg="#A2A2D0", command=lambda: self.start_theme("Unit_19")).place(x=690,
                                                                                                              y=400)
        Button(self.canvas, text="20. Буксировка механических транспортных средств", font=("Times new Roman", 16),
               bg="#A2A2D0", command=lambda: self.start_theme("Unit_20")).place(x=690, y=450)
        Button(self.canvas, text="21. Учебная езда", font=("Times new Roman", 16), bg="#A2A2D0",
               command=lambda: self.start_theme("Unit_21")).place(x=690, y=500)
        Button(self.canvas, text="22. Перевозка людей", font=("Times new Roman", 16), bg="#A2A2D0",
               command=lambda: self.start_theme("Unit_22")).place(x=690, y=550)
        Button(self.canvas, text="23. Перевозка грузов", font=("Times new Roman", 16), bg="#A2A2D0",
               command=lambda: self.start_theme("Unit_23")).place(x=690, y=600)
        Button(self.canvas, text="24. Дополнительные требования к движению велосипедистов и водителей мопедов",
               font=("Times new Roman", 16), bg="#A2A2D0", command=lambda: self.start_theme("Unit_24")).place(x=690,
                                                                                                              y=650)
        Button(self.canvas, text="25. Дополнительные требования к движению гужевых повозок, а также к прогону животных",
               font=("Times new Roman", 16), bg="#A2A2D0", command=lambda: self.start_theme("Unit_25")).place(x=690,
                                                                                                              y=700)
        Button(self.canvas, text="26. Нормы времени управления транспортным средством и отдыха",
               font=("Times new Roman", 16), bg="#A2A2D0", command=lambda: self.start_theme("Unit_26")).place(x=690,
                                                                                                              y=750)
        Button(self.canvas, text="Перейти к билетам", font=("Times new Roman", 26), bg="green",
               command=self.start_bil).place(x=830, y=850)
        Button(self.canvas, text="Выйти из приложения", font=("Times new Roman", 20), bg="red",
               command=self.exit_app).place(x=20, y=1000)

    def start_theme(self, theme):
        theme_mapping = {
            "Unit_1": "objie_polojenia.pdf",
            "Unit_2": "objie_obazannosti.pdf",
            "Unit_3": "primenenie_spec_signalov.pdf",
            # "Unit_3": "Unit_3.pdf",
            # "Unit_3": "Unit_3.pdf",
            # "Unit_3": "Unit_3.pdf",
            # "Unit_3": "Unit_3.pdf",
        }
        if theme in theme_mapping:
            destroy_canvas(self.canvas)
            pdf_file = theme_mapping[theme]
            TeachBook(theme, pdf_file)

    def start_bil(self):
        destroy_canvas(self.canvas)
        BilTest()


class BilTest:
    def __init__(self):
        window.title('Билеты')
        self.root = window
        self.canvas = tk.Canvas(self.root)
        self.canvas.pack(fill=tk.BOTH, expand=True)
        self.button_glav = tk.Button(self.canvas, text="Главное меню", command=self.glav_men)
        self.button_glav.place(x=610, y=10)

        self.padding = 40
        self.show_bil()

    def show_bil(self):
        count_bil, x = 5, 20
        Button(self.canvas,
               text=f"Билет 1",
               command=lambda: self.start_bil(f'bil_0.txt')).place(x=x, y=20 + self.padding * 0)
        Button(self.canvas,
               text=f"Билет 2",
               command=lambda: self.start_bil(f'bil_1.txt')).place(x=x, y=20 + self.padding * 1)
        Button(self.canvas,
               text=f"Билет 3",
               command=lambda: self.start_bil(f'bil_2.txt')).place(x=x, y=20 + self.padding * 2)
        Button(self.canvas,
               text=f"Билет 4",
               command=lambda: self.start_bil(f'bil_3.txt')).place(x=x, y=20 + self.padding * 3)
        Button(self.canvas,
               text=f"Билет 5",
               command=lambda: self.start_bil(f'bil_4.txt')).place(x=x, y=20 + self.padding * 4)

    def start_bil(self, bil_file):
        destroy_canvas(self.canvas)
        print(bil_file)
        Tester(bil_file)

    def glav_men(self):
        destroy_canvas(self.canvas)
        MainMenu()


class TeachBook:
    def __init__(self, theme, pdf_file):
        self.theme = theme
        self.pdf_file = pdf_file
        self.page_num = 0
        self.img_tk = tk.Image

        self.root = window
        self.canvas = tk.Canvas(self.root)
        self.canvas.pack(fill=tk.BOTH, expand=True)

        self.render_page()

        self.root.bind("<Left>", self.prev_page)
        self.root.bind("<Right>", self.next_page)

        Label(self.canvas, text="Для перелистывания страниц используйте клавиши ← и → на вашей клавиатуре",
              font=("Times new Roman", 20)).place(x=500, y=900)

        self.button = tk.Button(self.canvas, text="Тестирование", command=self.start_test)
        self.button.place(x=20, y=80)

        self.button_glav = tk.Button(self.canvas, text="Вернуться в главное меню", font=("Times new Roman", 20),
                                     command=self.glav_men)
        self.button_glav.place(x=20, y=10)

    def render_page(self):
        pdf_document = fitz.open(self.pdf_file)
        page = pdf_document[self.page_num]
        pix = page.get_pixmap()
        img = Image.frombytes("RGB", (pix.width, pix.height), pix.samples)
        img_tk = ImageTk.PhotoImage(img)
        self.canvas.create_image(650, 0, anchor=tk.NW, image=img_tk)
        self.img_tk = img_tk

    def prev_page(self, event):
        if self.page_num > 0:
            self.page_num -= 1
            self.render_page()

    def next_page(self, event):
        pdf_document = fitz.open(self.pdf_file)
        if self.page_num < pdf_document.page_count - 1:
            self.page_num += 1
            self.render_page()

    def start_test(self):
        print("Тестирование")
        destroy_canvas(self.canvas)
        Tester(self.theme)

    def glav_men(self):
        destroy_canvas(self.canvas)
        MainMenu()


theme_dict = {
    "Unit_1": "unit_1.txt",
    "Unit_2": "unit_2.txt",
    "Unit_3": "unit_3.txt",
}


class Tester:
    def __init__(self, theme):
        self.file = None
        self.root = window
        self.theme = theme
        try:
            self.questions = self.load_questions(theme_dict[self.theme])
        except KeyError:
            self.questions = self.load_questions(theme)
        self.current_question = 0
        self.score = 0
        self.false = 0
        self.load_file()
        self.setup_ui()

    def load_file(self):
        try:
            self.file = open(theme_dict[self.theme], "r")
        except KeyError:
            self.file = open(self.theme, "r")

    def load_questions(self, filename):
        questions = []
        with open(filename, "r") as file:
            lines = file.readlines()
            for i in range(0, len(lines), 6):
                question = {
                    "image": lines[i].strip(),
                    "answers": [lines[i + 1].strip(), lines[i + 2].strip(), lines[i + 3].strip(),
                                lines[i + 4].strip()],
                    "correct_answer": lines[i + 5].strip()
                }
                questions.append(question)
        return questions

    def setup_ui(self):
        self.canvas = tk.Canvas(self.root, width=1980, height=720)

        Button(self.canvas, text='Выход', command=self.exit_bilet).place(x=100, y=100)

        self.canvas.place(x=0, y=0)
        self.canvas.pack(side=tk.TOP)

        self.buttons_frame = tk.Frame(self.root)
        self.buttons_frame.pack(side=tk.TOP)

        self.image = None
        self.buttons = []
        for j in range(4):  # i поменялась на j
            button = Button(self.buttons_frame, text=f"Answer {chr(65 + j)}",  # i поменялась на j
                            command=lambda i=j: self.check_answer(chr(65 + i)))  # вторая i в i=i поменялась на j
            button.pack(side=tk.TOP, pady=10)

            self.buttons.append(button)

        self.show_question()

    def exit_bilet(self):
        confirm_window = Toplevel(window)
        confirm_window.grab_set()
        confirm_window.geometry("500x250+750+400")
        confirm_window.resizable(width=False, height=False)
        confirm_window.title("Выход из приложения")
        Label(confirm_window, text="Вы уверенны, что хотите выйти?", font=("Times new Roman", 20)).place(x=50, y=10)
        Label(confirm_window, text="Ваш прогресс будет утерян.",font=("Times new Roman", 20)).place(x=75, y=50)
        Button(confirm_window, text="Выйти в главное меню", font=("Times new Roman", 16), bg="red",
               command=lambda: self.close_test(confirm_window)).place(x=130, y=100)
        Button(confirm_window, text="Отмена", font=("Times new Roman", 16), bg="green",
               command=confirm_window.destroy).place(x=200, y=170)

    def close_test(self, confirm_window):
        destroy_canvas(self.canvas)
        self.buttons_frame.destroy()
        confirm_window.destroy()
        MainMenu()

    def show_question(self):
        self.canvas.delete("all")
        if self.current_question < len(self.questions):
            question = self.questions[self.current_question]

            self.image = PhotoImage(file=question["image"])
            self.canvas.create_image(750, 200, image=self.image)
            self.canvas.pack(pady=10)

            for i, answer in enumerate(question["answers"]):
                self.buttons[i].config(text=answer)

        else:
            self.show_results()
            self.buttons_frame.destroy()

    def show_results(self):
        self.allq = self.score + self.false
        print(int((self.score / self.allq) * 100))

        Label = tk.Label(self.canvas, text='Количество правильных ответов: '
                                           + str(self.score) + ' ', font='Arial 12')
        Label.pack()
        proc = tk.Label(self.canvas, text='Процент правильных ответов =  '
                                          + str(int((self.score / self.allq) * 100)) + ' %',
                        font='Arial 12')
        proc.pack()

        def glav_men():
            destroy_canvas(self.canvas)
            self.file.seek(0)
            MainMenu()

        def restart():
            destroy_canvas(self.canvas)
            self.file.seek(0)
            Tester(self.theme)

        Glav_menu = tk.Button(self.canvas, text='Перейти в главное меню', command=glav_men)
        Glav_menu.pack(side=tk.LEFT, padx=10)

        restart = tk.Button(self.canvas, text='Начать тест заново', command=restart)
        restart.pack(side=tk.LEFT, padx=5)

    def check_answer(self, answer):
        question = self.questions[self.current_question]
        line = self.file.readline().rstrip()
        if answer == question["correct_answer"]:
            self.score += 1
        else:
            self.false += 1
            print('Неверный ответ:', line)  # Вывод информации об ошибке

        self.current_question += 1
        self.show_question()


def destroy_canvas(canvas: tk.Canvas) -> None:
    window.unbind("<Left>")
    window.unbind("<Right>")
    canvas.destroy()


if __name__ == "__main__":
    MainMenu()
