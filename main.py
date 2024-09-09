import streamlit as st
from io import BytesIO
from deDRM.adobekey import extract_adobe_key
from deDRM.ineptpdf import decryptBook as decrypt_pdf
from deDRM.ineptepub import decryptBook as decrypt_epub
from streamlit.runtime.uploaded_file_manager import UploadedFile


def decrypt_file(encrypted_file: UploadedFile, dat_file: UploadedFile) -> BytesIO:
    # Extract the Adobe key
    adobe_key = extract_adobe_key(dat_file.getvalue())
    
    if encrypted_file.name.lower().endswith('.pdf'):
        return decrypt_pdf(adobe_key, encrypted_file)
    elif encrypted_file.name.lower().endswith('.epub'):
        return decrypt_epub(adobe_key, encrypted_file)
    else:
        raise ValueError("Unsupported file type")


st.set_page_config(
    page_title="rm-DRM",
    page_icon="🔑",
)

st.markdown(
    """
    ### 🔑 &nbsp; rm-DRM 

    > remove DRM of your own ebook in Adobe Digital Edition

    ![github](https://api.iconify.design/bi/github.svg?color=%236FD886&width=20) &nbsp;
    [source code](https://github.com/hoishing/rm-drm)
    """
)
st.write("")

st.write("#### Remove DRM ")

mime_types = {"pdf": "application/pdf", "epub": "application/epub+zip"}
book_data = file_name = ""
mime = mime_types["epub"]

key_file = st.file_uploader(
    "Activation file",
    type="dat",
    help="~/Library/Application Support/Adobe/Digital Editions/activation.dat\n\nOnly Digital Edition for macOS is supported",
)

encrypted_file = st.file_uploader("epub or pdf file", type=["epub", "pdf"])

if encrypted_file and key_file:
    book_data = decrypt_file(encrypted_file, key_file)
    file_name = encrypted_file.name
    mime = mime_types[encrypted_file.name.split(".")[-1]]

st.write("")

st.download_button(
    label="Download",
    data=book_data,
    file_name=file_name,
    mime=mime,
    disabled=not book_data,
)
