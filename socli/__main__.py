import sys
from socli.cli import cli
from fire import Fire


def main():
    # print("\nMAIN:")
    # args = sys.argv[1:]
    # print("count of args :: {}".format(len(args)))
    # for arg in args:
    #     print("passed argument :: {}".format(arg))

    # cli.start()
    print("")
    Fire(cli.Cli())


if __name__ == "__main__":
    main()
