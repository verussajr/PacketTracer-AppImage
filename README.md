# AppImage for Cisco Packet Tracer

*🎶I'm already Tracer🎶*

A configuration tool for building appimages with [pkg2appimage](https://github.com/AppImage/pkg2appimage) for Packet Tracer.

This repo is a fork from [Diolinux/PacketTracer-AppImage](https://github.com/Diolinux/PacketTracer-AppImage).

## Motivations

Would be ideal having an automated build release for Cisco Packet Tracer, so you can always get the latest release.
Thinking about that, I decided to create this repo as an opinionated tool for building app images.

## How to contribute?

### Requirements
- git
- wget

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
