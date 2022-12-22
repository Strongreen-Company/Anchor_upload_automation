import sys

from pytube import YouTube

from banner import print_banner


def main():
    try:
        if sys.argv[1] and sys.argv[1] == "-path":
            print("initiating download")
            with open(sys.argv[2], "r") as file:
                for i, line in enumerate(file):
                    yt = YouTube(line)
                    print(f" {int(i) + 1} - Downloading {yt.title}")
                    names.append(yt.title)
                    yt.streams.filter(only_audio=True).first().download(
                        output_path="audio"
                    )
        print("Download complete")
        sys.exit()
    except (IndexError):
        print_banner()
    except (FileNotFoundError):
        print("arquivo não encontrado")
    except KeyboardInterrupt:
        print("\nsaindo do programa ...")
        sys.exit()


if __name__ == "__main__":
    main()
