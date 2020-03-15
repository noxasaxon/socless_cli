import sys
from socli.cli import cli


def main():
    print("\nMAIN:")
    args = sys.argv[1:]
    print("count of args :: {}".format(len(args)))
    for arg in args:
        print("passed argument :: {}".format(arg))

    cli.start()


if __name__ == "__main__":
    main()
