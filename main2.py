import tkinter as tk
from tkinter import PhotoImage
from integral import (
    PolynomialIntegral, ExponentialIntegral, PowerIntegral,
    SinIntegral, CosIntegral ,sec_sqare_Integral ,csc_square_Integral,sec_u_tan_u,csc_u_cot_u,
    tanu_integral,cotu_integral,sec_u_integral,csc_u_integral,a_square_plus_u_square,
    cossquareu,sqrt_asquare_minus_usquare
)

def add_to_input(function):
    current_text = input_field.get()  # Получаем текущий текст
    input_field.delete(0, tk.END)  # Очищаем поле ввода
    input_field.insert(tk.END, current_text + function)  # Добавляем к старому тексту новую функцию

# Функция для получения результата интеграла
def calculate_integral():
    integral_type = integral_var.get()  # Получаем выбранный тип интеграла
    coefficient = int(coefficient_entry.get())  # Получаем коэффициент
    
    # Проверяем, существует ли l1_entry для полиномиальных интегралов
    if integral_type == "Polynomyal":
        l1_value = int(l1_entry.get())  # Получаем коэффициент l1
    else:
        l1_value = None  # Для других типов интегралов l1 не используется
    
    result = ""
    if integral_type == "Polynomyal":
        power = coefficient  # Считаем коэффициент как степень полинома
        integral = PolynomialIntegral(power, l1_value)  # Передаем power и l1
        result = integral.indefinite_integral()

    elif integral_type == "Exponential":
        integral = ExponentialIntegral(coefficient)
        result = integral.indefinite_integral()

    elif integral_type == "Power":
        integral = PowerIntegral(coefficient)
        result = integral.indefinite_integral()

    elif integral_type == "Sin(u)":
        integral = SinIntegral(coefficient)
        result = integral.indefinite_integral()

    elif integral_type == "Cos(u)":
        integral = CosIntegral(coefficient)
        result = integral.indefinite_integral()

    elif integral_type == "sec^2(u)":
        integral = sec_sqare_Integral(coefficient)
        result = integral.indefinite_integral()

    elif integral_type == "csc^2(u)":
        integral = csc_square_Integral(coefficient)
        result = integral.indefinite_integral()

    elif integral_type == "sec(u)*tan(u)":
        integral = sec_u_tan_u(coefficient)
        result = integral.indefinite_integral()

    elif integral_type == "csc(u)*cot(u)":
        integral = csc_u_cot_u(coefficient)
        result = integral.indefinite_integral()
    
    elif integral_type == "tan(u)":
        integral = tanu_integral(coefficient)
        result = integral.indefinite_integral()
    
    elif integral_type == "cot(u)":
        integral = cotu_integral(coefficient)
        result = integral.indefinite_integral()
    
    elif integral_type == "sec(u)":
        integral = sec_u_integral(coefficient)
        result = integral.indefinite_integral()
        
    elif integral_type == "csc(u)":
        integral = csc_u_integral(coefficient)
        result = integral.indefinite_integral()

    elif integral_type == "du/(a^2+u^2)":
        integral = a_square_plus_u_square(coefficient)
        result = integral.indefinite_integral()
    
    elif integral_type == "cos^2(u)":
        integral = cossquareu(coefficient)
        result = integral.indefinite_integral()

    elif integral_type == "du/sqrt(a^2-u^2)":
        integral = sqrt_asquare_minus_usquare(coefficient)
        result = integral.indefinite_integral()

    result_label.config(text=f"Результат: {result}")

root = tk.Tk()
root.title("Интегралы с функциями")

# Поле ввода для выражения
input_label = tk.Label(root, text="Введите выражение для интеграла:")
input_label.pack()

input_field = tk.Entry(root, width=50)
input_field.pack()

# Поле для ввода коэффициента
coefficient_label = tk.Label(root, text="Введите коэффициент для x:")
coefficient_label.pack()

coefficient_entry = tk.Entry(root, width=10)
coefficient_entry.pack()

# Поле для ввода коэффициента l1 для полиномиальных интегралов
l1_label = tk.Label(root, text="Введите степень x (для полиномиальных интегралов):")
l1_label.pack()

l1_entry = tk.Entry(root, width=10)
l1_entry.pack()

# Поле для выбора типа интеграла
integral_var = tk.StringVar()
integral_var.set("Polynomyal")  # Значение по умолчанию

integral_options = ["Polynomyal", "Exponential", "Power", "Sin(u)", "Cos(u)", "sec^2(u)", "csc^2(u)", "sec(u)*tan(u)", "csc(u)*cot(u)", "tan(u)", "cot(u)", "sec(u)", "csc(u)", "du/a^2+x^2", "cos^2(u)", "du/sqrt(a^2-x^2)"]
integral_menu = tk.OptionMenu(root, integral_var, *integral_options)
integral_menu.pack()

# Добавляем иконки для каждой функции (путь к вашим иконкам .png)
polynomial_icon = PhotoImage(r"C:\Users\Aitzh\OneDrive\Рабочий стол\midterm\polinom.png")
exponential_icon = PhotoImage(r"C:\Users\Aitzh\OneDrive\Рабочий стол\midterm\icon_e.png")
power_icon = PhotoImage(r"C:\Users\Aitzh\OneDrive\Рабочий стол\midterm\power.png")
sin_icon = PhotoImage(r"C:\Users\Aitzh\OneDrive\Рабочий стол\midterm\icon_sin.png")
cos_icon = PhotoImage(r"C:\Users\Aitzh\OneDrive\Рабочий стол\midterm\icon_cos.png")
sec_square_icon = PhotoImage(r"C:\Users\Aitzh\OneDrive\Рабочий стол\midterm\sec_square.png")
csc_square_icon = PhotoImage(r"C:\Users\Aitzh\OneDrive\Рабочий стол\midterm\csc_square.png")
sec_tan_icon = PhotoImage(r"C:\Users\Aitzh\OneDrive\Рабочий стол\midterm\sec_tan.png")
csc_cot_icon = PhotoImage(r"C:\Users\Aitzh\OneDrive\Рабочий стол\midterm\csc_cot.png")
tan_icon = PhotoImage(r"C:\Users\Aitzh\OneDrive\Рабочий стол\midterm\tan.png")
cot_icon = PhotoImage(r"C:\Users\Aitzh\OneDrive\Рабочий стол\midterm\cot.png")
sec_icon = PhotoImage(r"C:\Users\Aitzh\OneDrive\Рабочий стол\midterm\sec.png")
csc_icon = PhotoImage(r"C:\Users\Aitzh\OneDrive\Рабочий стол\midterm\csc.png")
a_square_plus_u_square_icon = PhotoImage(r"C:\Users\Aitzh\OneDrive\Рабочий стол\midterm\a_square_plus_u.png")
cos_square_icon = PhotoImage(r"C:\Users\Aitzh\OneDrive\Рабочий стол\midterm\cos_square.png")
sqrt_asquare_minus_usquare_icon = PhotoImage(r"C:\Users\Aitzh\OneDrive\Рабочий стол\midterm\a_square_plus_x.png")


# Создаем фрейм для кнопок, чтобы их сгруппировать слева
button_frame = tk.Frame(root)
button_frame.pack(side=tk.LEFT, fill=tk.Y)
# Кнопки с иконками
tk.Button(button_frame, text="Polynomyal", image=polynomial_icon, compound=tk.LEFT, command=lambda: add_to_input("x")).pack(pady=5)
tk.Button(button_frame, text="Exponential", image=exponential_icon, compound=tk.LEFT, command=lambda: add_to_input("e")).pack(pady=5)
tk.Button(button_frame, text="Power", image=power_icon, compound=tk.LEFT, command=lambda: add_to_input("a")).pack(pady=5)
tk.Button(button_frame, text="Sin(u)", image=sin_icon, compound=tk.LEFT, command=lambda: add_to_input("sin(x)")).pack(pady=5)
tk.Button(button_frame, text="Cos(u)", image=cos_icon, compound=tk.LEFT, command=lambda: add_to_input("cos(x)")).pack(pady=5)
tk.Button(button_frame, text="sec^2(u)", image=sec_square_icon, compound=tk.LEFT, command=lambda: add_to_input("sec^2(x)")).pack(pady=5)
tk.Button(button_frame, text="csc^2(u)", image=csc_square_icon, compound=tk.LEFT, command=lambda: add_to_input("csc^2(x)")).pack(pady=5)
tk.Button(button_frame, text="sec(u)*tan(u)", image=sec_tan_icon, compound=tk.LEFT, command=lambda: add_to_input("sec(x)*tan(x)")).pack(pady=5)
tk.Button(button_frame, text="csc(u)*cot(u)", image=csc_cot_icon, compound=tk.LEFT, command=lambda: add_to_input("csc(x)*cot(x)")).pack(pady=5)
tk.Button(button_frame, text="tan(u)", image=tan_icon, compound=tk.LEFT, command=lambda: add_to_input("tan(x)")).pack(pady=5)
tk.Button(button_frame, text="cot(u)", image=cot_icon, compound=tk.LEFT, command=lambda: add_to_input("cot(x)")).pack(pady=5)
tk.Button(button_frame, text="sec(u)", image=sec_icon, compound=tk.LEFT, command=lambda: add_to_input("sec(x)")).pack(pady=5)
tk.Button(button_frame, text="csc(u)", image=csc_icon, compound=tk.LEFT, command=lambda: add_to_input("csc(x)")).pack(pady=5)
tk.Button(button_frame, text="du/(a^2+x^2)", image=a_square_plus_u_square_icon, compound=tk.LEFT, command=lambda: add_to_input("du/(a^2+x^2)")).pack(pady=5)
tk.Button(button_frame, text="cos^2(u)", image=cos_square_icon, compound=tk.LEFT, command=lambda: add_to_input("cos^2(x)")).pack(pady=5)
tk.Button(button_frame, text="du/sqrt(a^2-x^2)", image=sqrt_asquare_minus_usquare_icon, compound=tk.LEFT, command=lambda: add_to_input("du/sqrt(a^2-x^2)")).pack(pady=5)

# Кнопка для вычисления интеграла
calculate_button = tk.Button(root, text="Вычислить интеграл", command=calculate_integral)
calculate_button.pack(pady=10)

# Метка для отображения результата
result_label = tk.Label(root, text="Результат:")
result_label.pack()

# Запуск главного цикла
root.mainloop()
