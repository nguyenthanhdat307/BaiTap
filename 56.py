import shutil

def get_console_size():
    size = shutil.get_terminal_size()
    return size.columns, size.lines
if __name__ == "__main__":
    width, height = get_console_size()
    print(width , height)
