import sys

from cookiecutter.main import cookiecutter

def clone_cookiecutter(url, path, name):
    print("Cloning %s at path %s from %s" % (name, path, url))
    cookiecutter(url, no_input=True, output_dir=path, extra_context={'project_name': name})
    return

def clone_all_modules():
    {% for module in cookiecutter.modules.names %}
    clone_cookiecutter("https://github.com/Catacrockers/cookiecutter-cpp-module.git", "modules", "module_{{module}}")
    {% endfor %}
    return

def clone_all_samples():
    {% for sample in cookiecutter.samples.names %}
    clone_cookiecutter("https://github.com/Catacrockers/cookiecutter-cpp-module.git", "samples", "sample_{{sample}}")
    {% endfor %}
    return

if __name__ == "__main__":
    print("Posthook for {{ cookiecutter.project_name}}")

    clone_all_modules()
    clone_all_samples()

    exit(0)
