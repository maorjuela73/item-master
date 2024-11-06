from questions.idatos import questions

from jinja2 import Template, Environment, FileSystemLoader
env = Environment(
    loader=FileSystemLoader('.'),
    trim_blocks=True,
    lstrip_blocks=True)

# Cargar la plantilla Moodle XML
with open('templates/relational_with_categories.xml', 'r') as file:
    moodle_template_str = file.read()

moodle_template = Template(moodle_template_str)

# Renderizar el XML completo
rendered_moodle_xml = moodle_template.render(questions=questions)

# Guardar en un archivo el XML con codificación UTF-8
with open('outputs/rel_questions.xml', 'w', encoding='utf-8') as file:
    file.write(rendered_moodle_xml)
