# rm-DRM

> remove DRM of your own ebook in Adobe Digital Edition

[![st-badge]][rm-drm] [![MIT-badge]][MIT-url] [![black-badge]][black-url]

## Quick Start

### Use it Online

rm-DRM on [Streamlit Community Cloud](https://rm-drm.streamlit.app)

### Run Locally

`pip install pycryptodome lxml streamlit`

Then run it with [streamlit]

`streamlit run main.py`

### Prerequisite

- Adobe Digital Edition for *macOS*
- DRM encrypted epub or pdf from `~/Documents/Digital Editions`
- activation file: `~/Library/Application Support/Adobe/Digital Editions/activation.dat`

## Privacy Statements

- this app does not store any information from the users
- all uploaded files are ephemeral and will be cleared after closing the webapp

## Credits

- decryption logic: [DeDRM_tools]

## Need Help?

[![git-logo] github issue][github issue]

[![x-logo] posts][x-post]

[rm-drm]: https://rm-drm.streamlit.app
[black-badge]: https://img.shields.io/badge/code%20style-black-000000.svg
[black-url]: https://github.com/psf/black
[DeDRM_tools]: https://github.com/noDRM/DeDRM_tools
[git-logo]: https://api.iconify.design/bi/github.svg?color=%236FD886&width=20
[github issue]: https://github.com/hoishing/rm-drm/issues
[MIT-badge]: https://img.shields.io/github/license/hoishing/ptag
[MIT-url]: https://opensource.org/licenses/MIT
[st-badge]: https://static.streamlit.io/badges/streamlit_badge_black_white.svg
[streamlit]: https://docs.streamlit.io
[x-logo]: https://api.iconify.design/ri:twitter-x-fill.svg?width=20&color=DarkGray
[x-post]: https://x.com/hoishing
