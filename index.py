import sys
import os
from pytube import YouTube
import shutil
from banner import print_banner
from uploadSelenium import upload_file


def downloadAndUpload(link, index=1):
    yt = YouTube(link)
    print(f" {int(index) + 1} - Downloading {yt.title}")
    download = (
        yt.streams.filter(only_audio=True)
        .first()
        .download(output_path="audio")
    )
    base, ext = os.path.splitext(download)
    print(base)
    print(ext)
    os.rename(download, base + ".mp3")
    upload_file(
        f"{base}.mp3",
        {"title": yt.title, "description": yt.description},
    )


def main(link=None):
    try:
        if link is not None:
            downloadAndUpload(link)
            shutil.rmtree("audio")
        elif sys.argv[1] and sys.argv[1] == "-path":
            print("initiating download")
            with open(sys.argv[2], "r") as file:
                for i, line in enumerate(file):
                    downloadAndUpload(line, i)
            shutil.rmtree("audio")

        sys.exit()
    except (IndexError):
        print_banner()
    except (FileNotFoundError):
        print("arquivo não encontrado")
    except KeyboardInterrupt:
        print("\nsaindo do programa ...")
        shutil.rmtree("audio")
        sys.exit()


if __name__ == "__main__":
    main()
