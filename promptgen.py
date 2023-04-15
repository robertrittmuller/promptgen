import re
import csv
import random
import argparse

# default filenames/paths
template_path = "templates.csv"
prompt_path = "prompts.txt"

# default options
number_of_sets = 5
base_resolutions = ['-W1600 -H1024']
base_settings = '-n 3 -s 150 -U 4 --hires_fix'
samplers = ['k_heun']
cfg = [7.5,8.5,9.5]

# command line arguments
parser = argparse.ArgumentParser(description="Command line parameters for your script.")
parser.add_argument("--template_path", default=template_path, help="Path to the templates.csv file.")
parser.add_argument("--prompt_path", default=prompt_path, help="Path to the prompts.txt file.")
parser.add_argument("--number_of_sets", type=int, default=number_of_sets, help="Number of sets.")
parser.add_argument("--base_resolutions", nargs='+', default=base_resolutions, help="Base resolutions.")
parser.add_argument("--base_settings", default=base_settings, help="Base settings.")
parser.add_argument("--samplers", nargs='+', default=samplers, help="List of samplers.")
parser.add_argument("--cfg", nargs='+', type=float, default=cfg, help="Configuration values.")

args = parser.parse_args()

# Read in the prompt templates and create a dictionary to map template names to content
templates = {}
with open(args.template_path, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_ALL, skipinitialspace=True)
    for row in csvreader:
        templates[row[0]] = row[1]

# Read in the prompts
prompts = []
with open(args.prompt_path, newline='') as promptfile:
    for row in promptfile:
        prompts.append(row.strip())

# Process each prompt for any templates
for each_prompt in prompts:
    for i in range(args.number_of_sets):
        # Replace templates using the dictionary
        final_prompt = each_prompt.format(**templates)
        
        # Handle wildcard blocks
        wildcard_blocks = re.findall(r'\(.*?\)', final_prompt)
        for block in wildcard_blocks:
            choices = block.strip('()').split('|')
            final_prompt = final_prompt.replace(block, random.choice(choices).strip())
        
        # Render final prompt with options
        for samp in args.samplers:
            for cg in args.cfg:
                for res in args.base_resolutions:
                    print(f' {final_prompt} -A{samp} -C{cg} {res} {args.base_settings}')   