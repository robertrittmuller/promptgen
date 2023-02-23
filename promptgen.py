pre_prompt = 'Photorealistic close-up portrait photo of a abstract sculpture with'
post_prompt = 'surreal, fog, epic cybercity background, wet pavement, soft focus, moody lighting, neon lights, neon signs, cyberpunk, depth of field'
base_negative_prompt = 'art, cartoon, painting, oil, trending on artstation, render, octane'
base_resolution = ['-W1280 -H1024', '-W1024 -H1280']
base_settings = '-n 5 -s 75 -G .75 -U 4 --hires_fix'
adjectives = ['black shiny surface','red dimpled surface','multicolor surface, with potmarks','purple textured surface']
samplers = ['k_lms','k_euler_a','k_heun']
cfg = [7.5, 8.5, 9, 11]

for adj in adjectives:
    for samp in samplers:
        for cg in cfg:
            for res in base_resolution:
                print(f'{pre_prompt}, {adj}, {post_prompt}, [{base_negative_prompt}] -A{samp} -C{cg} {res} {base_settings}')