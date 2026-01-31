from fpdf import FPDF
import os

def txt_to_pdf(input_file: str, output_file: str = None):
    if not os.path.exists(input_file):
        print(f"Файл {input_file} не знайдено!")
        return

    if output_file is None:
        output_file = input_file.rsplit(".", 1)[0] + ".pdf"

    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)

    with open(input_file, encoding="utf-8") as f:
        for line in f:
            pdf.cell(200, 10, txt=line.strip(), ln=True)

    pdf.output(output_file)
    print(f"PDF створено: {output_file}")


if __name__ == "__main__":
    file_path = input("Шлях до .txt файлу: ").strip()
    txt_to_pdf(file_path)
