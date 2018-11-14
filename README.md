# cookiecutter-cpp-project

This cookiecutter template create a CPP project (compatible with C) that support several modules (or libraries) and examples

Note: This is the template README, this will not appear in the final project.

# Install

Install the latest Cookiecutter if you haven't installed it yet (this requires Cookiecutter 1.4.0 or higher):

```
pip install -U cookiecutter
```

# Usage

## Project generation

Go to path where you want to generate a project and execute:

```
cookiecutter $(path_to_basic_folder)
```

* Note: It is possible to avoid set up input, using default values with ```--no-input``` option.
* Note II: It is possible to provide variables though command using ```$(key)=$(value)``` syntax with the command.
* Note III: It is possible to use a yaml with a configuration using option ```--config-file $(config_file).yaml```

Example using config file by default:

```
cookiecutter $(path_to_basic_folder) --config-file $(config_file).yaml --no-input
```

Example using from Github:

```
cookiecutter https://github.com/Catacrockers/cookiecutter-cpp-project.git
```

## Adding modules and binaries

Use the module variable to generate libraries automatically. Exist 3 ways to do this:

### By terminal

Provide by terminal in module option an JSON object with names field containing a list of strings.

The pattern example is:

```
modules [default]: { "names" : [ "module1", "module2" ] }
samples [default]: { "names" : [ "sample1", "sample2" ] }
```

### By configuration

Use the YAML. **TODO** I couldnt to provide a valid data to do this.

### Manually

Use variable `extra_content` to achieve it.

* Using python: ```cookiecutter(url, no_input=True, output_dir=path, extra_context={'project_name': name})```
* Using executable: ```cookiecutter(url, no_input=True, output_dir=path, extra_context={'project_name': name}) -o "test_output" ```

## Setting the option without input

**TODO**

# More ideas **TODO**

* Support a list to add find_package.
* Support add libraries and include path from config.
