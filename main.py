import PyPDF2
import os

# Función para dividir el PDF
def split_pdf(input_pdf, start_page, end_page, output_pdf):
    with open(input_pdf, 'rb') as pdf_file:
        reader = PyPDF2.PdfReader(pdf_file)
        
        # Crear un nuevo PDF para almacenar las páginas seleccionadas
        writer = PyPDF2.PdfWriter()

        # Asegurarnos de que las páginas están dentro del rango
        total_pages = len(reader.pages)
        if start_page < 0 or end_page >= total_pages:
            print(f"Error: El rango de páginas debe estar entre 1 y {total_pages}.")
            return

        # Extraer páginas del PDF original
        for page_num in range(start_page, end_page + 1):
            page = reader.pages[page_num]
            writer.add_page(page)
        
        # Guardar el nuevo archivo PDF
        with open(output_pdf, 'wb') as new_pdf_file:
            writer.write(new_pdf_file)

        print(f"Nuevo archivo PDF guardado como: {output_pdf}")


# Inputs del usuario
input_pdf = 'AWS-CERTIFIED-DEVELOPER-SLICES.pdf'  # remplaza por el nombre de tu archivo pdf

start_page = int(input("Ingresa el número de página de inicio: ")) - 1  # Convertir a índice 0
end_page = int(input("Ingresa el número de página final/corte: ")) - 1  # Convertir a índice 0

# Automatizamos el nombre del nuevo archivo PDF en la carpeta Sections
section_number = input("Ingresa el número de sección: ")  # Para darle nombre al archivo, ej: "1", "2"
section_name = input("Ingresa el nombre de la sección (sin espacios): ")  # Nombre de la sección, ej: "getting_started_with_AWS"
output_pdf = f'Sections/{section_number}_{section_name}.pdf'

# Verificar si la carpeta Sections existe, si no, crearla
if not os.path.exists('Sections'):
    os.makedirs('Sections')

# Ejecutar la función
split_pdf(input_pdf, start_page, end_page, output_pdf)
