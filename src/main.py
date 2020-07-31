#!/usr/bin/python3

import sys
from pathlib import Path


class Tracer:
    def __init__(self):
        self.HOME = str(Path.home())
        self.instalation_path = Path.joinpath(self.HOME, "PacketTracer")

        self.current_directory = Path.cwd()
        self.settings_path = Path.joinpath(self.HOME, ".ptappimage00")

    def recall(self):
        with open(self.settings_path, "wb") as settings_file:
            file_header = bytearray([0x00, 0x00, 0x00, 0x01, 0x00, 0x00, 0x00])
            path_start = bytearray(">", "utf16")[2:]
            path_separator = bytearray([0x00, 0x00, 0x00, 0x32, 0x00])

            apppath = Path.joinpath(self.current_directory, "opt", "pt")
            apppath_saves = Path.joinpath(apppath, "saves")

            Path(apppath_saves).mkdir(parents=True, exist_ok=True)

            apppath_encoded = bytearray(apppath, "utf16")[2:-1]

            instalation_path_enconded = bytearray(self.instalation_path, "utf16")[2:-1]

            encodedPaths = (
                path_start
                + apppath_encoded
                + path_separator
                + instalation_path_enconded
            )

            bytes_to_write = file_header + encodedPaths
            settings_file.write(bytes_to_write)


if __name__ == "__main__":
    tracer = Tracer()
    tracer.recall()
