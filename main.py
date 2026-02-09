# txt_to_pdf.py (оновлена версія)
"""
Конвертер TXT → PDF з підтримкою кодування та базовим форматуванням.
"""

from fpdf import FPDF
import argparse
import os

class PDF(FPDF):
    def header(self):
        self.set_font("Arial", "B", 12)
        self.cell(0, 10, self.title, 0, 1, "C")
        self.ln(10)

def txt_to_pdf(input_file, output_file=None, title=None, encoding="utf-8"):
    if not os.path.exists(input_file):
        print(f"Файл {input_file} не знайдено")
        return

    if output_file is None:
        output_file = os.path.splitext(input_file)[0] + ".pdf"

    pdf = PDF()
    pdf.title = title or os.path.basename(input_file)
    pdf.add_page()
    pdf.set_font("Arial", size=11)

    try:
        with open(input_file, "r", encoding=encoding) as f:
            for line in f:
                pdf.multi_cell(0, 6, line.strip())
    except UnicodeDecodeError:
        print(f"Помилка кодування. Спробуйте інше кодування (наприклад cp1251)")
        return

    pdf.output(output_file)
    print(f"PDF успішно створено: {output_file}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Конвертер TXT у PDF")
    parser.add_argument("input", help="Шлях до вхідного .txt файлу")
    parser.add_argument("-o", "--output", help="Шлях до вихідного PDF (опціонально)")
    parser.add_argument("-t", "--title", help="Заголовок документа (опціонально)")
    parser.add_argument("--encoding", default="utf-8", help="Кодування файлу (default: utf-8)")
    args = parser.parse_args()

    txt_to_pdf(args.input, args.output, args.title, args.encoding)
