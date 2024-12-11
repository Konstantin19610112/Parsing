import tkinter as tk
from tkinter import filedialog, messagebox
from tkinter import ttk
import fitz  # PyMuPDF
import pdfplumber
from PyPDF2 import PdfReader, PdfWriter
from PyPDF4 import PdfFileReader, PdfFileWriter
from pdfminer.high_level import extract_text



def Pusk():
    # Получаем введённое имя файла и выбранный метод обработки
#    file_name = entry_file_name.get()
    file_name = entry_file_path.get()

    selected_method = combo_methods.get()
    
    # Проверяем, введено ли имя файла и выбран ли метод
    if not file_name:
        messagebox.showerror("Ошибка", "Введите имя файла!")
        return
    if not selected_method:
        messagebox.showerror("Ошибка", "Выберите метод обработки!")
        return
    
    # Выводим информацию о файле и методе обработки
    result_message = f"Имя файла: {file_name}\nМетод обработки: {selected_method}"
    messagebox.showinfo("Информация", result_message)


def select_file():
    # Открывает диалоговое окно для выбора файла
    filepath = filedialog.askopenfilename(
        title="Выберите PDF файл",
        filetypes=[("PDF файлы", "*.pdf")]
    )
    if filepath:
        entry_file_path.delete(0, tk.END)  # Очищает текущее содержимое поля
        entry_file_path.insert(0, filepath)  # Вставляет выбранный путь в поле

def show_selected_file():
    filepath = entry_file_path.get()
    if filepath:
        messagebox.showinfo("Выбранный файл", f"Вы выбрали файл:\n{filepath}")
    else:
        messagebox.showerror("Ошибка", "Файл не выбран!")


# Создание основного окна
root = tk.Tk()
root.title("Интерфейс обработки PDF")

# Поле для ввода имени файла вручную
frame_file = tk.Frame(root)
frame_file.pack(pady=10)
tk.Label(frame_file, text="Введите имя файла:").pack(side=tk.LEFT, padx=5)

# Поле для текста с дефолтным значением
entry_file_path = tk.Entry(frame_file, width=50)
entry_file_path.insert(0, "default.pdf")  # Устанавливает значение по умолчанию
entry_file_path.pack(side=tk.LEFT, padx=5)

# Кнопка для вызова браузера файлов
btn_browse = tk.Button(frame_file, text="Обзор...", command=select_file)
btn_browse.pack(side=tk.LEFT, padx=5)

# Кнопка для подтверждения выбора файла

btn_show = tk.Button(root, text="Показать выбранный файл", command=show_selected_file)
btn_show.pack(pady=20)

frame_method = tk.Frame(root)
frame_method.pack(pady=10)

tk.Label(frame_method, text="Выберите метод обработки:").pack(side=tk.LEFT, padx=5)
combo_methods = ttk.Combobox(
    frame_method, 
    values=["PyPDF2", "PyMuPDF (fitz)", "pdfplumber", "PyPDF4", "PDFMiner"],
    state="readonly",
    width=20
)
combo_methods.pack(side=tk.LEFT, padx=5)

# Кнопка для запуска программы Pusk
btn_run = tk.Button(root, text="Запуск Pusk", command=Pusk)
btn_run.pack(pady=20)



# Запуск интерфейса
root.mainloop()
