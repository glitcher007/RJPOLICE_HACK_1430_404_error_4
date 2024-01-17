import cachetools
import cv2
import numpy as np
import os


try:
    from enum import Enum
    from io import BytesIO
    import os
    import pandas as pd
    import streamlit as st
    import shutil
except Exception as e:
    print(e)

STYLE = """
<style>
img {
    max-width: 100%;
}
</style>
"""

class FileType(Enum):
    CSV = "csv"
    PNG = "png"
    JPG = "jpg"

class FileUpload(object):

    def __init__(self):
        self.fileTypes = [FileType.PNG, FileType.JPG]
        self.uploaded_files_dir = "uploaded_imges"  # Replace with your desired directory name

    def save_uploaded_file(self, file, filename):
        os.makedirs(self.uploaded_files_dir, exist_ok=True)
        filepath = os.path.join(self.uploaded_files_dir, filename)
        with open(filepath, 'wb') as f:
            f.write(file.getvalue())
        return filepath

    def run(self):
        """
        Upload File on Streamlit Code
        :return:
        """
        st.info(__doc__)
        st.markdown(STYLE, unsafe_allow_html=True)
        file = st.file_uploader("Upload file", type=[file_type.value for file_type in self.fileTypes],accept_multiple_files=True)
        print(os.getcwd())
        #file_array=np.array(file)
       
        #parent_directory=r'C:\Users\glitcher\Desktop\Rj_hackathon_2\venv\uploaded_imges'
        file_path=os.path.join(os.getcwd(),'venv','uploaded_imges')
        #cv2.imwrite(file_path, file_array)
        
        if file is not None:
            file_details = {"FileName":file.name,"FileType":file.type}
            st.write(file_details)
            
            with open(os.path.join(file_path,file.name),"wb") as f: 
                f.write(file.getbuffer())         
                st.success("Saved File")

        show_file = st.empty()
        if not file:
            show_file.info(f"Please upload a file of type: {', '.join(file_type.value for file_type in self.fileTypes)}")
            return

        content = file.getvalue()
        if isinstance(file, BytesIO):
            show_file.image(file)

            # Save the uploaded file to the directory
            uploaded_filepath = self.save_uploaded_file(file, file.filename)
            st.success(f"File successfully uploaded and saved to: {uploaded_filepath}")

        else:
            data = pd.read_csv(file)
            st.dataframe(data.head(10))

        file.close()

if __name__ == "__main__":
    helper = FileUpload()
    helper.run()
