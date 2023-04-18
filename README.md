# InvokeAI Automated Prompt Generation
Automated prompt generation for Stable Diffusion. Focused on integration with <a href="https://github.com/invoke-ai/InvokeAI">InvokeAI</a>.

## Overview

The purpose of the `promptgen.py` script generates multiple variations of prompts with specific options. The generated prompts can then be passed to the InvokeAI `invoke.py` script to automate the execution of these prompts. This guide provides instructions on how to use the promptgen.py script with InvokeAI.

It reads prompt templates and prompts from separate input files (`templates.csv` and `prompts.txt`), and then generates different combinations of prompts based on the templates and options specified. The script allows users to customize the number of sets, base resolutions, base settings, samplers, and configuration values.

## Usage

### Command Line Arguments

The script accepts the following command line arguments:

- `--template_path`: Path to the `templates.csv` file. (default: `"templates.csv"`)
- `--prompt_path`: Path to the `prompts.txt` file. (default: `"prompts.txt"`)
- `--number_of_sets`: Number of sets. (default: `5`)
- `--base_resolutions`: Base resolutions. Accepts multiple values. (default: `['-W1600 -H1024']`)
- `--base_settings`: Base settings. (default: `'-n 3 -s 150 -U 4 --hires_fix'`)
- `--samplers`: List of samplers. Accepts multiple values. (default: `['k_heun']`)
- `--cfg`: Configuration values. Accepts multiple float values. (default: `[7.5, 8.5, 9.5]`)

### Input Files

The script requires two input files:

1. `templates.csv`: A CSV file containing the prompt templates. Each row in the file represents a template with two columns: the template name and the template content. The template name will be enclosed in curly braces `{}` in the prompts and will be replaced with the template content when generating the final prompts. Please note that this implementation expects the templates in templates.csv to be in the format `{template_name},template_content`, so that the template names can be directly used in the format function. 

2. `prompts.txt`: A plain text file containing the prompts. Each line in the file represents a prompt. The script will read the prompts and use the templates to generate multiple variations of each prompt.

### Wildcard Blocks

In the prompts, wildcard blocks can be specified using parentheses `()` and the pipe `|` delimiter. For example, the wildcard block `(option A|option B)` can be used in a prompt, and the script will randomly select one of the options for each generated prompt.

### Output

The script generates and prints the final prompts with options to the console. The output format for each prompt is as follows:

```
{final_prompt} -A{samp} -C{cg} {res} {base_settings}
```

Where `{final_prompt}` is the generated prompt, `{samp}` is the sampler, `{cg}` is the configuration value, `{res}` is the base resolution, and `{base_settings}` are the base settings.

## Simple Example

To run the script with the default values:
```
python promptgen.py --template_path custom_templates.csv --prompt_path custom_prompts.txt --number_of_sets 3 --base_resolutions "-W800 -H600" "-W1024 -H768" --base_settings "-n 2 -s 100 -U 3" --samplers "k_huen" --cfg 6.5 7.0 7.5
```

## Usage with InvokeAI
Save the output of the `promptgen.py` script to a text file. The file should contain one prompt per line. Each line should look like what you would type at the `invoke>` prompt. Here's an example of how to save the output to a file named `generated_prompts.txt`:
```
python promptgen.py > generated_prompts.txt

python scripts/invoke.py --from_file "/path/to/generated_prompts.txt"
```
#
Distributed under the <a href="LICENSE">MIT License</a>