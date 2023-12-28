# thumbnail-resizer-tool
Tool to resize icon to its very small version made in Python 3.87 with PIL library and pyqt6.

## ui example:
<p align="middle">
  <img src="https://github.com/piotrekgelert/thumbnail-resizer-tool/blob/main/images/app_view.png" width="400"/>
</p>

## notes:
- [x] It checks if resized icon already exists, if yes adds to name number
- [x] Name is taken from original icon and to resized icon name '_thumb' is added
- [x] Saves files with original extention
- [x] Sizes to select are: 16px, 32px, 64px, 128px, 256px, 512px
- [x] You can select only sizes smaller than size of orginal icon

### icons created by:
- [juicy_fish](https://www.flaticon.com/authors/juicy-fish)
- [AbtoCreative](https://www.flaticon.com/authors/abtocreative)
- [Freepik](https://www.flaticon.com/authors/freepik)
- [Gregor Cresnar](https://www.flaticon.com/authors/gregor-cresnar)


### used packages
- [PIL 10.1.0](https://python-pillow.org/)
- [PyQt6 6.6.1](https://www.riverbankcomputing.com/software/pyqt/)
- [pyinstaller 6.3.0](https://www.pyinstaller.org/)
- [auto-py-to-exe 2.42.0](https://github.com/brentvollebregt/auto-py-to-exe)


### running the project
App opens from `App_main/main.py` file


### licence
This project is licensed under the [MIT] License - see [Licence.md](LICENSE) file for details.