from questions.prnopr import questions

from jinja2 import Template, Environment, FileSystemLoader
env = Environment(
    loader=FileSystemLoader('.'),
    trim_blocks=True,
    lstrip_blocks=True)

# Cargar la plantilla Moodle XML
with open('templates/python_questions.xml', 'r') as file:
    moodle_template_str = file.read()

moodle_template = Template(moodle_template_str)

# Renderizar el XML completo
rendered_moodle_xml = moodle_template.render(questions=questions)

# Guardar en un archivo
with open('outputs/questions.xml', 'w') as file:
    file.write(rendered_moodle_xml)
