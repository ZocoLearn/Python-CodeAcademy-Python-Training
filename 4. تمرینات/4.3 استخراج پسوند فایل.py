def get_file_extension(file_name):
    index=file_name.index(".")+1
    return file_name[index:]
print(get_file_extension("ali.pdf"))


def get_file_extension2(file_name):
    index=len(file_name)-3
    return file_name[index:]
print(get_file_extension2("ali.png"))