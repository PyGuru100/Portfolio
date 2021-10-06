WORD = 'We Are a Community'
loop_range = len(WORD)

if __name__ == '__main__':  # because the css generator inherits from dis bad boy.
    for i in range(loop_range):
        thing_to_print = WORD[i]
        if thing_to_print == ' ':  # a space
            thing_to_print = '&nbsp;'
        print(f'<span id="h1-letter{i}" class="h1-letter"> {thing_to_print} </span>')
