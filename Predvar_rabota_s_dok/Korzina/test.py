import os

def all_pdf():
    # Определяем путь к текущему файлу
    current_dir = os.path.dirname(os.path.abspath(__file__))

    # Указываем относительный путь к поддиректории с PDF-файлами
    pdf_dir = os.path.join(current_dir, 'PDF')

    # Проверяем, существует ли директория
    if not os.path.exists(pdf_dir):
        print(f"Директория {pdf_dir} не существует.")
    else:
        # Получаем список всех PDF-файлов в поддиректории
        pdf_files = [f for f in os.listdir(pdf_dir) if f.endswith('.pdf')]

        # Выводим список файлов
        if pdf_files:
            pass
        else:
            print("В поддиректории нет PDF-файлов.")
    return pdf_files