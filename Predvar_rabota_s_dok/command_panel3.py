import tkinter as tk
from tkinter import filedialog, messagebox

def select_file():
    # Открывает диалоговое окно для выбора файла
    filepath = filedialog.askopenfilename(
        title="Выберите PDF файл",
        filetypes=[("PDF файлы", "*.pdf")]
    )
    if filepath:
        entry_file_path.delete(0, tk.END)  # Очищает текущее содержимое поля
        entry_file_path.insert(0, filepath)  # Вставляет выбранный путь в поле

# Создание основного окна
root = tk.Tk()
root.title("Интерфейс обработки PDF")

# Поле для выбора файла через диалог
frame_file = tk.Frame(root)
frame_file.pack(pady=10)
tk.Label(frame_file, text="Выберите файл:").pack(side=tk.LEFT, padx=5)

# Текстовое поле для отображения выбранного пути
entry_file_path = tk.Entry(frame_file, width=50)
entry_file_path.pack(side=tk.LEFT, padx=5)

# Кнопка для вызова браузера файлов
btn_browse = tk.Button(frame_file, text="Обзор...", command=select_file)
btn_browse.pack(side=tk.LEFT, padx=5)

# Кнопка для демонстрации результата
def show_selected_file():
    filepath = entry_file_path.get()
    if filepath:
        messagebox.showinfo("Выбранный файл", f"Вы выбрали файл:\n{filepath}")
    else:
        messagebox.showerror("Ошибка", "Файл не выбран!")

btn_show = tk.Button(root, text="Показать выбранный файл", command=show_selected_file)
btn_show.pack(pady=20)

# Запуск интерфейса
root.mainloop()
