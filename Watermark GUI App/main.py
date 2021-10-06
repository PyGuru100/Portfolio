import tkinter as tk
import tkinter.filedialog
from PIL import Image, ImageDraw, ImageFont
import os


window = tk.Tk()
window.title('Coffee-Mark')
window.geometry('500x600')

help_label = tk.Label(window, text='Use only the options you need. You don\'t need to set\n '
                                   'the font size, for example, if you\'re superimposing a watermark.')
help_label.pack()


icon_or_text = tk.IntVar()
icon_or_text.set(1)
radio_icon = tk.Radiobutton(window,
                            text='Superimpose watermark', variable=icon_or_text, value=1)
radio_text = tk.Radiobutton(window,
                            text='Add Text', variable=icon_or_text, value=2)
radio_icon.pack()
radio_text.pack()


chosen_file = ""
chosen_icon = ""


browse_var = tk.IntVar()
browse_var.set(1)
radio_browse_image = tk.Radiobutton(window, text='Browse for image',
                                    variable=browse_var, value=1)
radio_browse_icon = tk.Radiobutton(window, text='Browse for watermark',
                                   variable=browse_var, value=2)


chosen_label = tk.Label(window, text='Chosen Image: None')
chosen_label.pack()

chosen_icon_label = tk.Label(window, text='Chosen Watermark: None')
chosen_icon_label.pack()


def browse():
    file_finder = tkinter.filedialog
    global chosen_file, chosen_icon
    if browse_var.get() == 1:
        chosen_file = file_finder.askopenfilename()
        chosen_label['text'] = f'Chosen Image: {chosen_file.split("/")[-1]}'
    else:
        chosen_icon = file_finder.askopenfilename()
        chosen_icon_label['text'] = f'Chosen Icon: {chosen_icon.split("/")[-1]}'


browse_button = tk.Button(window, text='Browse', command=browse)
browse_button.pack()
# I kept the radio button pack calls right here so they'd be in the right place in the GUI
# I had to define them before the browse function since it references the variable browse_var.
radio_browse_image.pack()
radio_browse_icon.pack()

missing_info_label = tk.Label(window, text="")

text_box_label = tk.Label(window,
                          text="Text you'd like to add (e.g. Copyright © Protected): ")
text_box_label.pack()
text_box = tk.Entry(window)
text_box.pack()

font_box_label = tk.Label(window, text='Font file name (e.g. On Linux: Ramaraja-Regular.ttf | On Windows: cambria)')
font_size_label = tk.Label(window, text="Font size")
font_box = tk.Entry(window)
font_size = tk.Scale(window, from_=1, to=90, orient='horizontal')
text_color_label = tk.Label(window, text='Text color (R, G, B)')
text_color_r = tk.Entry(window)
text_color_g = tk.Entry(window)
text_color_b = tk.Entry(window)

image_name = ""


def name_handler():
    global image_name
    image_name = saved_image_entry.get() + '.png'
    if image_name == '.png':
        missing_info_label['text'] = 'No name chosen for file.'
    elif image_name in [file for file in os.listdir('.') if os.path.isfile(file)]:
        missing_info_label['text'] = 'Name already in use.'
    else:
        return True
    image_name = ""  # these two lines of code follow the if and elif scenarios.
    return False


def add_mark():
    if icon_or_text.get() == 2:
        return add_text()
    if not chosen_file:
        missing_info_label['text'] = "No image selected."
        return
    if not chosen_icon:
        missing_info_label['text'] = "No watermark selected"
        return
    old_image = Image.open(chosen_file)
    icon_image = Image.open(chosen_icon)
    width, height = old_image.size
    # now let's maintain the aspect ratio of the icon.
    i_width, i_height = icon_image.size
    icon_height_over_width = i_height / i_width
    # .resize((width, height))
    icon_image = icon_image.resize((round(0.1 * width),
                                    round(0.1 * width * icon_height_over_width)))
    # .paste(image, (x,y), mask)
    old_image.paste(icon_image, (round(0.8 * width), round(0.8 * height)), icon_image.convert('RGBA'))
    if not name_handler():
        return
    old_image.save(image_name)
    missing_info_label['text'] = ""


def add_text():
    if not chosen_file:
        missing_info_label['text'] = "No image selected."
        return
    if not text_box.get():
        missing_info_label['text'] = "No text to add."
        return
    image = Image.open(chosen_file)
    width, height = image.size
    text_image = Image.new(image.mode, (width, height), (255, 255, 255, 0))
    draw = ImageDraw.Draw(text_image)
    try:
        font = ImageFont.truetype(font_box.get(), font_size.get())
    except OSError:
        missing_info_label['text'] = 'Invalid font. Try "cambria" if you\'re using windows.'
        return
    r, g, b = [color.get() for color in (text_color_r, text_color_g, text_color_b)]
    try:
        r, g, b = [int(number) for number in (r, g, b)]
    except ValueError:
        missing_info_label['text'] = "Invalid Color."
        return
    if not (0 <= r <= 255 and 0 <= g <= 255 and 0 <= b <= 255):
        missing_info_label['text'] = "Invalid Color: values must be between 0 and 255"
        return
    for sample_width in [width//3 + _ * width // 2.5 for _ in range(0, 2)]:
        for sample_height in [height//3 + _ * height // 2.5 for _ in range(0, 2)]:
            draw.text(xy=(sample_width, sample_height),
                      text=text_box.get(), fill=(r, g, b), font=font)
    text_image = text_image.rotate(35, fillcolor='white')
    text_image.paste(image, (0, 0), text_image.convert('1'))
    if not name_handler():
        return
    text_image.save(image_name)
    missing_info_label['text'] = ""


font_box_label.pack()
font_box.pack()
font_size_label.pack()
font_size.pack()
text_color_label.pack()
text_color_r.pack()
text_color_g.pack()
text_color_b.pack()


saved_image_label = tk.Label(window, text='Marked image name: ')
saved_image_entry = tk.Entry(window)
saved_image_label.pack()
saved_image_entry.pack()

mark_button = tk.Button(window, text='Add!', command=add_mark)
mark_button.pack()
missing_info_label.pack()

window.mainloop()
