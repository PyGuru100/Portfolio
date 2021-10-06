from html_generator import loop_range

for j in range(loop_range):
    print(f'#h1-letter{j} {{animation-delay: {25 * j}ms;}}')
