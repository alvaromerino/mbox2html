#!/usr/bin/python3
import os
import mailbox
import jinja2


def ask_mbox_file_path():
    path_exists = False
    is_mbox_file = False
    while not path_exists or not is_mbox_file:
        path_mbox_file = input("Enter the mbox file path: ")
        path_exists = os.path.exists(path_mbox_file)
        filename, file_extension = os.path.splitext(path_mbox_file)
        is_mbox_file = file_extension.lower() == ".mbox"

    return path_mbox_file


def ask_output_html_file_path():
    file = None
    while file is None:
        try:
            output_html_file_path = input("Enter the path of output html file: ")
            file = open(output_html_file_path, "w")
        except Exception as ex:
            print(ex)

    file.close()
    return output_html_file_path


if __name__ == "__main__":
    template_env = jinja2.Environment(loader=jinja2.FileSystemLoader("./"))
    TEMPLATE_FILE = "template.html"
    template = template_env.get_template(TEMPLATE_FILE)

    mbox_file_path = ask_mbox_file_path()
    output_html_file_path = ask_output_html_file_path()

    mbox_file = mailbox.mbox(mbox_file_path)
    title = os.path.basename(output_html_file_path)

    template.stream(mbox=mbox_file, title=title).dump(output_html_file_path)
