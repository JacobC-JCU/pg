import sys

# definice úvodních binárních sekvencí obrázkových souborů
jpeg_header = b'\xff\xd8'
gif_header1 = b'GIF87a'
gif_header2 = b'GIF89a'
png_header = b'\x89PNG\r\n\x1a\n'


def read_header(file_name, header_length):
    with open(file_name, "rb") as header:
        hlavicka = header.read(header_length)
        return hlavicka


def is_jpeg(file_name):
    header = read_header(file_name, len(jpeg_header))
    if header == jpeg_header:
        return True


def is_gif(file_name):
    header1 = read_header(file_name, len(gif_header1))
    if header1 == gif_header1:
        return True

    header2 = read_header(file_name, len(gif_header2))
    if header2 == gif_header2:
        return True


def is_png(file_name):
    header = read_header(file_name, len(png_header))
    if header == png_header:
        return True


def print_file_type(file_name):
    if is_jpeg(file_name):
        print(f'Soubor {file_name} je typu jpeg')
    elif is_gif(file_name):
        print(f'Soubor {file_name} je typu gif')
    elif is_png(file_name):
        print(f'Soubor {file_name} je typu png')
    else:
        print(f'Soubor {file_name} je neznámého typu')


if __name__ == '__main__':
    try:
        file_name = sys.argv[1]
        print_file_type(file_name)

    except FileNotFoundError:
        print(f'Soubor {sys.argv[1]} nebyl nalezen.')
    except Exception:
        print("Neznámá chyba..")
