from jinja2 import Environment, FileSystemLoader
import re

from questions.cppobjetos import questions


# Define el filtro personalizado
def regex_replace(s, pattern, replacement=""):
    return re.sub(pattern, replacement, s)


# Expresión regular para eliminar signos de interrogación y truncar
# en el primer punto o signo de cierre de interrogación
def clean_and_truncate(text):
    # Eliminamos todos los signos de apertura y cierre de interrogación, comas, slash y asteriscos
    text = re.sub(r"[¿?¡!.,/*]", "", text)
    # Eliminar los tags HTML
    text = re.sub(r"<[^>]*>", "", text)
    # Truncamos hasta el primer punto o signo de cierre de interrogación
    match = re.search(r"[.]", text)
    if match:
        text = text[: match.start() + 1]  # Incluye el punto en el truncado
    # Truncar a 85 caracteres
    if len(text) > 85:
        text = text[:85] + "..."
    return text


env = Environment(
    loader=FileSystemLoader("."), trim_blocks=True, lstrip_blocks=True
)

env.filters["regex_replace"] = regex_replace
env.filters["clean_and_truncate"] = clean_and_truncate

# Cargar la plantilla Moodle XML
with open("templates/cpp.xml", "r") as file:
    moodle_template_str = file.read()

moodle_template = env.from_string(moodle_template_str)

# Renderizar el XML completo
rendered_moodle_xml = moodle_template.render(questions=questions)

# Guardar en un archivo el XML con codificación UTF-8
with open("outputs/cpp_questions.xml", "w", encoding="utf-8") as file:
    file.write(rendered_moodle_xml)
