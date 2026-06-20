import argparse

from .hashing import hash_text, hash_file, algorithms
from importlib.metadata import version


__version__ = version("PyHashKit")


def main():
    parser = argparse.ArgumentParser(
        prog="pyhashkit",
        description="PyHashKit - Hash text and files using various algorithms",
    )

    parser.add_argument(
        "-v",
        "-V",
        "--version",
        action="store_true",
        help="Show PyHashKit version",
    )

    subparsers = parser.add_subparsers(
        dest="command",
        help="Available commands",
    )

    text_parser = subparsers.add_parser(
        "text",
        help="Hash a text string",
    )

    text_parser.add_argument(
        "text",
        help="Text to hash",
    )


    text_parser.add_argument(
        "-a",
        "--algorithm",
        default="sha256",
        help="Hash algorithm (default: sha256)",
    )

    text_parser.add_argument(
        "-d",
        "--digest-size",
        type=int,
        default=32,
        help=(
            "Digest size for SHAKE algorithms "
            "(default: 32)"
        ),
    )


    file_parser = subparsers.add_parser(
        "file",
        help="Hash a file",
    )

    file_parser.add_argument(
        "path",
        help="Path to file",
    )

    file_parser.add_argument(
        "-a",
        "--algorithm",
        default="sha256",
        help="Hash algorithm (default: sha256)",
    )

    file_parser.add_argument(
        "-d",
        "--digest-size",
        type=int,
        default=32,
        help=(
            "Digest size for SHAKE algorithms "
            "(default: 32)"
        ),
    )   

    

    subparsers.add_parser(
        "commands",
        help="List all available commands",
    )

    subparsers.add_parser(
        "algorithms",
        help="List all available hashing algorithms",
    )

    args = parser.parse_args()

    if args.version:
        print(f"PyHashKit v{__version__}")
        return

    try:
        if args.command == "text":
            print(
                hash_text(
                    args.text,
                    args.algorithm,
                    args.digest_size
                )
            )       
        
        elif args.command in "algorithms":
            print("Available Algorithms:")

            for alg in algorithms():
                print(f"  - {alg}")

        elif args.command == "file":
            print(
                hash_file(
                    args.path,
                    args.algorithm,
                    args.digest_size
                )
            )

        elif args.command == "commands":
            print("""
Available Commands:

  text         Hash a text string
  file         Hash a file
  commands     Show all commands
  algorithms   Show all available algorithms

Flags:

  -v, -V,
  --version    Show version information

Options:

  -a, --algorithm
               Specify hashing algorithm
               (default: sha256)

  -d, --digest-size
               Digest size for SHAKE algorithms
               (default: 32)

Examples:

  pyhashkit text "Hello World"

  pyhashkit text "Hello World" -a md5

  pyhashkit text "Hello World" -a shake_128 -d 64

  pyhashkit file example.txt

  pyhashkit file example.txt -a sha512

  pyhashkit file example.txt -a shake_256 -d 128

  pyhashkit algorithms

  pyhashkit -v
""")
        else:
            parser.print_help()

    except FileNotFoundError:
        print(f"Error: File not found: {args.path}")

    except PermissionError:
        print(f"Error: Permission denied: {args.path}")

    except ValueError as e:
        print(f"Error: {e}")

    except Exception as e:
        print(f"Unexpected error: {e}")


if __name__ == "__main__":
    main()