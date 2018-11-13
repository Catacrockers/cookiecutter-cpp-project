import sys

from cookiecutter.main import cookiecutter

def clone_cookiecutter(url, name):
    print("Cloning %s from %s" % (name, url))
    cookiecutter(url, no_input=True)
    return

def clone_all_modules():
    {% for module in cookiecutter.modules.names %}
    clone_cookiecutter("https://github.com/Catacrockers/cookiecutter-helloworld.git", "{{module}}")
    {% endfor %}
    return

def clone_all_samples():
    {% for sample in cookiecutter.samples.names %}
    clone_cookiecutter("https://github.com/Catacrockers/cookiecutter-helloworld.git", "{{sample}}")
    {% endfor %}
    return

if __name__ == "__main__":
    print("Posthook for {{ cookiecutter.project_name}}")

    #clone_all_modules()
    #clone_all_samples()

    exit(0)
