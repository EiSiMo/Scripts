from PIL import Image
import time
import argparse


def print_info(time_start, quiet, msg):
    if not quiet:
        time_offset = str(round(time.time() - time_start, 3)).ljust(5, '0')
        print(f"[{time_offset}] {msg}")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("filename_input", type=str, help="name of the file to read from")
    parser.add_argument("filename_output", type=str, help="name of the file to write to")
    parser.add_argument("-q", "--quiet", action="store_true", help="don't print information")

    args = parser.parse_args()
    start = time.time()

    try:
        image = Image.open(args.filename_input)
        print_info(start, args.quiet, "File opened")
    except FileNotFoundError:
        print_info(start, args.quiet, "File not found")
    else:
        pixels = list(image.getdata())
        print_info(start, args.quiet, "Pixel values read")
        image = Image.new(image.mode, image.size)
        image.putdata(pixels)
        print_info(start, args.quiet, "New image created")
        image.save(args.filename_output)
        print_info(start, args.quiet, "Image saved")


if __name__ == "__main__":
    main()
