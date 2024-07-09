filename = input("input the filename: ")
dot_position = filename.rfind('.')
extension = filename[dot_position +1:]
print(f"The extension of the file is: {extension}")