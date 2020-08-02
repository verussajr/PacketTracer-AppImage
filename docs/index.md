# AppImage for Cisco Packet Tracer

[![Build Status](https://travis-ci.org/Avlye/PacketTracer-AppImage.svg?branch=master)](https://travis-ci.org/Avlye/PacketTracer-AppImage)

*🎶I'm already Tracer🎶*

An automated tool for building appimages with [pkg2appimage](https://github.com/AppImage/pkg2appimage) for Packet Tracer. 

This repo is a fork from [Diolinux/PacketTracer-AppImage](https://github.com/Diolinux/PacketTracer-AppImage).

# Latest Release

Download now the lastest release on [Avlye/PacketTracer-AppImage](https://github.com/Avlye/PacketTracer-AppImage/releases/tag/latest).

## Motivations

Would be ideal having an automated build release for Cisco Packet Tracer, so you can always get the latest release.
Thinking about that, I decided to create this repo as an opinionated tool for building app images.

## How to contribute?
### Enviroment
```
GITHUB_TOKEN=generated_token_acess
```

### Requirements
- git
- wget
- desktop-file-utils
- build-essential (optional & recommended)

```zsh
# Example On Ubuntu
sudo apt install build-essential git wget desktop-file-utils -y
```

### Get Started

1. Clone this repo
  ```zsh
  git clone https://github.com/Avlye/PacketTracer-AppImage
  cd PacketTracer-AppImage/
  ```

2. Download pkg2appimage tool and create a executable binary
  ```zsh
   wget https://github.com/AppImage/pkg2appimage/raw/master/pkg2appimage
   chmod +x pkg2appimage
   ```
3. Build
  ```zsh
   ./pkg2appimage PacketTracer.yml
   ```

4. After all this process, the appimage of Packet Tracer will be in `out/` directory.

5. To run the application, just click on the AppImage, just like any other AppImage.
  Also check if AppImage has permissions to execute the file properties. (**Right click on >> Properties**)
