import csv
import ast
from jinja2 import Environment, FileSystemLoader

# Configurar el entorno de Jinja2
env = Environment(loader=FileSystemLoader('.'), trim_blocks=True, lstrip_blocks=True)
template = env.get_template('template_banco.xml')

# Leer los datos del CSV
preguntas = []
with open('items.csv', newline='', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile, quotechar='"')
    for row in reader:

        # if len(preguntas) == 10:
        #     break

        # Parsear el campo 'contenido' que es una cadena de diccionario
        contenido_dict = ast.literal_eval(row['contenido'])
        
        # Crear el diccionario de la pregunta
        pregunta = {
            'item_id': contenido_dict['item_id'],
            'contenido': contenido_dict['contenido'],
            'opciones': []
        }

        # Añadir la respuesta correcta con fracción de 100
        pregunta['opciones'].append({
            'texto': contenido_dict['clave_correcta'],
            'fraction': '100'
        })

        # Añadir los distractores con fracción de 0
        for distractor in contenido_dict['distractores']:
            pregunta['opciones'].append({
                'texto': distractor,
                'fraction': '0'
            })

        # Añadir la pregunta a la lista de preguntas
        preguntas.append(pregunta)

# Renderizar el template con los datos
output = template.render(preguntas=preguntas)

# Guardar el archivo XML generado
with open('moodle_items/banco_preguntas.xml', 'w', encoding='utf-8') as f:
    f.write(output)

print("Archivo XML generado exitosamente.")
