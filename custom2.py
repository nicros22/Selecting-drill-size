import tkinter
from tkinter import *
import customtkinter
from PIL import ImageTk, Image, ImageDraw
from data import dict

customtkinter.set_appearance_mode("System")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"
material_options = ['Сталь', 'Латунь', 'Алюминий', 'Чугун', 'Бронза', 'Пластмасса']
diameter_options = dict.keys()

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        # configure window
        self.title("Расчёт сверла")
        self.geometry(f"{1100}x{580}")

        # configure grid layout (3x3)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure((2, 3), weight=0)
        self.grid_rowconfigure((0, 1, 2), weight=1)
        self.selection1 = None
        self.selection2 = None

        # create sidebar frame with widgets
        self.sidebar_frame = customtkinter.CTkFrame(self, width=140, corner_radius=0)
        self.sidebar_frame.grid(row=0, column=0, rowspan=4, sticky="nsew")
        self.sidebar_frame.grid_rowconfigure(4, weight=1)
        self.logo_label = customtkinter.CTkLabel(self.sidebar_frame, text="Расчёт сверла", font=customtkinter.CTkFont(size=20, weight="bold"))
        self.logo_label.grid(row=0, column=0, padx=20, pady=(20, 10))
        self.sidebar_button_1 = customtkinter.CTkButton(self.sidebar_frame, command=self.material_button, text='Материал')
        self.sidebar_button_1.grid(row=1, column=0, padx=20, pady=10)
        self.sidebar_button_2 = customtkinter.CTkButton(self.sidebar_frame, command=self.diameter_button, text='Диаметр резьбы')
        self.sidebar_button_2.grid(row=2, column=0, padx=20, pady=10)
        self.sidebar_button_3 = customtkinter.CTkButton(self.sidebar_frame, command=self.step_button, text='Шаг резьбы')
        self.sidebar_button_3.grid(row=3, column=0, padx=20, pady=10)
        self.appearance_mode_label = customtkinter.CTkLabel(self.sidebar_frame, text="Режим вида:", anchor="w")
        self.appearance_mode_label.grid(row=5, column=0, padx=20, pady=(10, 0))
        self.appearance_mode_optionemenu = customtkinter.CTkOptionMenu(self.sidebar_frame, values=["Светлый", "Тёмный", "Системный"],
                                                                       command=self.change_appearance_mode_event)
        self.appearance_mode_optionemenu.grid(row=6, column=0, padx=20, pady=(10, 10))
        self.scaling_label = customtkinter.CTkLabel(self.sidebar_frame, text="Масштаб интерфейса:", anchor="w")
        self.scaling_label.grid(row=7, column=0, padx=20, pady=(10, 0))
        self.scaling_optionemenu = customtkinter.CTkOptionMenu(self.sidebar_frame, values=["80%", "90%", "100%", "110%", "120%"],
                                                               command=self.change_scaling_event)
        self.scaling_optionemenu.grid(row=8, column=0, padx=20, pady=(10, 20))

        # create main entry and button
        self.entry = customtkinter.CTkEntry(self, placeholder_text="CTkEntry")
        self.entry.grid(row=3, column=1, columnspan=1, padx=(20, 0), pady=(20, 20), sticky="nsew")

        self.main_button_1 = customtkinter.CTkButton(master=self, fg_color="transparent", border_width=2, text="Подсчитать", command=self.print_selections, text_color=("gray10", "#DCE4EE"))
        self.main_button_1.grid(row=3, column=2, padx=(20, 20), pady=(20, 20), sticky="nsew")

        # create textbox
        # create choose frame
        self.parameter_frame = customtkinter.CTkFrame(self, width=50, corner_radius=0)
        self.parameter_frame.grid(row=0, column=2, rowspan=3, sticky="nsew")
        self.parameter_frame.grid_rowconfigure(4, weight=1)
        self.logo_label = customtkinter.CTkLabel(self.sidebar_frame, text="Расчёт сверла",
                                                 font=customtkinter.CTkFont(size=20, weight="bold"))
        self.parameter_label = customtkinter.CTkLabel(self.parameter_frame, text="Параметры",
                                                      font=customtkinter.CTkFont(size=20, weight="bold"))
        self.parameter_label.grid(row=0, column=2, padx=20, pady=(20, 10), sticky="n")
        # set image
        img = Image.open("hi.png")
        photo = ImageTk.PhotoImage(img)
        # создаем фрейм для фото и размещаем его слева
        # создаем метку с фото и размещаем ее внутри фрейма
        photo_label = Label(self, image=photo)
        photo_label.image = photo
        photo_label.grid(row=0, column=1)

        # for option in material_options:
        #     self.diameter_listbox.insert(tkinter.END, option)
        # self.parameter_listbox.grid(row=1, column=2, pady=10, padx=20, sticky="nsew")
        # self.parameter_listbox.grid_remove()
        #
        # self.parameter_listbox = tkinter.Listbox(self.parameter_frame, bg="#242424", border=0,
        #                                          highlightbackground='black', fg="white")
        # for option in material_options:
        #     self.parameter_listbox.insert(tkinter.END, option)
        # self.parameter_listbox.grid(row=1, column=2, pady=10, padx=20, sticky="nsew")
        # self.parameter_listbox.grid_remove()

        self.material_listbox = tkinter.Listbox(self.parameter_frame, bg="#242424", border=0,
                                                 highlightbackground='black', fg="white")
        self.diameter_listbox = tkinter.Listbox(self.parameter_frame, bg="#242424", border=0,
                                                 highlightbackground='black', fg="white")
        self.step_listbox = tkinter.Listbox(self.parameter_frame, bg="#242424", border=0,
                                                 highlightbackground='black', fg="white")

        self.material_listbox.bind("<<ListboxSelect>>", self.update_steplistbox)
        self.diameter_listbox.bind("<<ListboxSelect>>", self.update_steplistbox)
        self.step_listbox.bind("<<ListboxSelect>>", self.update_steplistbox)



        for option in material_options:
            self.material_listbox.insert(tkinter.END, option)

        for option in diameter_options:
            self.diameter_listbox.insert(tkinter.END, option)


        self.appearance_mode_optionemenu.set("Тёмный")
        self.scaling_optionemenu.set("100%")

    def material_button(self):
        self.sidebar_button_1.configure(fg_color='#c20020', hover_color='#8f0018')
        self.sidebar_button_2.configure(fg_color='#1F6AA5', hover_color='#144870')
        self.sidebar_button_3.configure(fg_color='#1F6AA5', hover_color='#144870')
        self.hide_listboxes()
        self.material_listbox.grid(row=1, column=2, rowspan=10, pady=10, padx=20, sticky="nsew")


    def diameter_button(self):
        self.sidebar_button_2.configure(fg_color='#c20020', hover_color='#8f0018')
        self.sidebar_button_1.configure(fg_color='#1F6AA5', hover_color='#144870')
        self.sidebar_button_3.configure(fg_color='#1F6AA5', hover_color='#144870')
        self.hide_listboxes()
        self.diameter_listbox.grid(row=1, column=2, rowspan=10, pady=10, padx=20, sticky="nsew")


    def step_button(self):
        self.sidebar_button_3.configure(fg_color='#c20020', hover_color='#8f0018')
        self.sidebar_button_2.configure(fg_color='#1F6AA5', hover_color='#144870')
        self.sidebar_button_1.configure(fg_color='#1F6AA5', hover_color='#144870')
        self.hide_listboxes()
        self.step_listbox.grid(row=1, column=2, rowspan=10, pady=10, padx=20, sticky="nsew")

    def update_steplistbox(self, event):
        selection = self.diameter_listbox.curselection()
        if len(selection) > 0:
            self.selection2 = self.diameter_listbox.get(selection[0])
        else:
            self.selection2 = None

        selection = self.material_listbox.curselection()
        if len(selection) > 0:
            index = selection[0]
            self.selection1 = self.material_listbox.get(index)
        else:
            self.selection1 = None

    def print_selections(self):
        if self.selection1 is not None:
            print('Selection 1:', self.selection1)
        if self.selection2 is not None:
            print('Selection 2:', self.selection2)

    def hide_listboxes(self):
        self.material_listbox.grid_forget()
        self.diameter_listbox.grid_forget()
        self.step_listbox.grid_forget()


    def change_appearance_mode_event(self, new_appearance_mode: str):
        if new_appearance_mode == "Светлый":
            new_appearance_mode = "Light"
        elif new_appearance_mode == "Тёмный":
            new_appearance_mode = "Dark"
        elif new_appearance_mode == "Системный":
            new_appearance_mode = "System"
        customtkinter.set_appearance_mode(new_appearance_mode)

    def change_scaling_event(self, new_scaling: str):
        new_scaling_float = int(new_scaling.replace("%", "")) / 100
        customtkinter.set_widget_scaling(new_scaling_float)

    def sidebar_button_event(self):
        print("sidebar_button click")



if __name__ == "__main__":
    app = App()
    app.mainloop()
