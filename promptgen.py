import re
import csv
import random

# default filenames/paths
template_path = "templates.csv"
prompt_path = "prompts.txt"

# default options
number_of_sets = 5
base_resolutions = ['-W1600 -H1024']
base_settings = '-n 3 -s 150 -U 4 --hires_fix'
samplers = ['k_heun']
cfg = [7.5,8.5,9.5]

# read in the prompt templates
templates = []
with open(template_path, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_ALL, skipinitialspace=True)
    for row in csvreader:
        templates.append(row)

# read in the prompts
prompts = []
with open(prompt_path, newline='') as promptfile:
    for row in promptfile:
        prompts.append(row.strip())

# process each prompt for any templates
for each_prompt in prompts:
    for i in range(number_of_sets):
        final_prompt = each_prompt
        for each_template in templates:
            search_text = '{' + each_template[0] + '}'
            final_prompt = final_prompt.replace(search_text, each_template[1])
        
        # now we need to generate all of the varients if there are any wildcard blocks
        wildcard_blocks = re.findall(r'\(.*?\)', final_prompt)
        
        for each_wildcard_block in wildcard_blocks:
            # decompose each block down to individual elements based on the pipe | delimiter
            this_wildcard_block = each_wildcard_block.replace('(', '')
            this_wildcard_block = this_wildcard_block.replace(')', '')
            block_elements = this_wildcard_block.split('|')
            
            # choose one random element to use for this prompt
            this_element = random.choice(block_elements)

            # drop in the selected element
            final_prompt = final_prompt.replace(each_wildcard_block, this_element.strip())
        
        # now render the final prompt with options
        for samp in samplers:
            for cg in cfg:
                for res in base_resolutions:
                    print(f' {final_prompt} -A{samp} -C{cg} {res} {base_settings}')
    