<h1 align="center">AppImage for Cisco Packet Tracer 💻</h1>
<p>
  <img alt="Version" src="https://img.shields.io/badge/version-1.0.0-blue.svg?cacheSeconds=2592000" />
  <a href="https://github.com/Avlye/PacketTracer-AppImage" target="_blank">
    <img alt="Documentation" src="https://img.shields.io/badge/documentation-yes-brightgreen.svg" />
  </a>
  <a href="https://opensource.org/licenses/MIT" target="_blank">
    <img alt="License: MIT" src="https://img.shields.io/badge/License-MIT-yellow.svg" />
  </a>
  <a href="https://twitter.com/AvlyeV" target="_blank">
    <img alt="Twitter: AvlyeV" src="https://img.shields.io/twitter/follow/AvlyeV.svg?style=social" />
  </a>
</p>

> An automated tool for building appimages with pkg2appimage for Packet Tracer.

### 🏠 [Homepage](https://avlye.github.io/PacketTracer-AppImage/)

## Download Latest Packet Tracer AppImage

[![Cisco Packet Tracer App Image](download.png)](https://github.com/Avlye/PacketTracer-AppImage/releases/download/latest/Packet_Tracer_7.3.0-.glibc2.27-x86_64.AppImage)

## Install

```sh
./Packet_Tracer_7.3.0-.glibc2.27-x86_64.AppImage
```

## Usage

```sh
Double click on Packet Tracer AppImage
```

## Motivations

Would be ideal having an automated build release for Cisco Packet Tracer, so you can always get the latest release.
Thinking about that, I decided to create this repo as an opinionated tool for building app images.

## How To Build Yourself

### Enviroment
GITHUB_TOKEN=generated_token_acess

### Requirements

- git
- wget
- desktop-file-utils

### Get Started

1. Clone this repo
  ```shell
  git clone https://github.com/Avlye/PacketTracer-AppImage
  cd PacketTracer-AppImage/
  ```

2. Download pkg2appimage tool and create a executable binary
  ```shell
   wget https://github.com/AppImage/pkg2appimage/raw/master/pkg2appimage
   chmod +x pkg2appimage
   ```
3. Build
  ```shell
   ./pkg2appimage PacketTracer.yml
   ```

4. After all this process, the appimage of Packet Tracer will be in `out/` directory.

5. To run the application, just click on the AppImage, just like any other AppImage.
  Also check if AppImage has permissions to execute the file properties. (**Right click on >> Properties**)


## Author

👤 **Gabriel Almir**

* Website: http://avlye.me
* Twitter: [@AvlyeV](https://twitter.com/AvlyeV)
* Github: [@Avlye](https://github.com/Avlye)
* LinkedIn: [@Avlye](https://linkedin.com/in/Avlye)

## 🤝 Contributing

Contributions, issues and feature requests are welcome!<br />Feel free to check [issues page](https://github.com/Avlye/PacketTracer-AppImage/issues).

## Show your support

Give a ⭐️ if this project helped you!

## 📝 License

Copyright © 2020 [Gabriel Almir](https://github.com/Avlye).<br />
This project is [MIT](https://opensource.org/licenses/MIT) licensed.

***
_This README was generated with ❤️ by [readme-md-generator](https://github.com/kefranabg/readme-md-generator)_
