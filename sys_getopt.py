import sys
import getopt


def main(argv):
    FILE_NAME = argv[0]
    INSTANCE_NAME = ""
    CHANNEL_NAME = ""

    try:
        opts, etc_args = getopt.getopt(
            argv[1:], "hi:c:", ["help", "instance=", "channel="]
        )

    except getopt.GetoptError:
        print(FILE_NAME, "-i <instance name> -c <channel name>")
        sys.exit(2)

    for opt, arg in opts:
        if opt in ("-h", "--help"):
            print(FILE_NAME, "-i <instance name> -c <channel name>")
            sys.exit()
        elif opt in ("-i", "--instance"):
            INSTANCE_NAME = arg

        elif opt in ("-c", "--channel"):
            CHANNEL_NAME = arg

    if len(INSTANCE_NAME) < 1:  # 필수 항목 값이 비어있다면
        print(FILE_NAME, "-i option is mandatory")
        sys.exit(2)

    print("INSTANCE_NAME:", INSTANCE_NAME)
    print("CHANNEL_NAME:", CHANNEL_NAME)


if __name__ == "__main__":
    main(sys.argv)