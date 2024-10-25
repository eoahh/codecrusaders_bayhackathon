import streamlit as st
import plotly.graph_objects as go
import nibabel as nib
import numpy as np
from google.cloud import storage
import time

client = storage.Client()

bucket_name = 'marketplace-p115jwl6'
segmentation_paths = [
    'TotalSegmentator/98/artifactFiles/Totalsegmentator_dataset/s0000/segmentations/femur_right.nii.gz'
]

@st.cache_data
def load_segmentations():
    st.write("Starting to load segmentations...")
    bucket = client.bucket(bucket_name)
    data = []
    for path in segmentation_paths:
        blob = bucket.blob(path)
        local_filename = path.split('/')[-1]
        blob.download_to_filename(local_filename)
        st.write(f"Downloaded {local_filename}")
        img = nib.load(local_filename)
        data.append(img.get_fdata())
    st.write("Finished loading segmentations")
    return data

def visualize_segmentations_3d(data_list):
    st.write("Starting visualization...")
    fig = go.Figure()
    for i, data in enumerate(data_list):
        x, y, z = np.where(data > 0)
        fig.add_trace(go.Scatter3d(x=x, y=y, z=z, mode='markers', marker=dict(size=1), name=f"Organ {i+1}"))
    fig.update_layout(scene=dict(aspectmode='data'), title='3D Visualization of Right Femur')
    st.write("Finished visualization")
    return fig

st.title('3D Segmentation Visualization of Right Femur')
st.write('Visualizing segmented organs from the TotalSegmentator dataset.')

if st.button('Load and Visualize Segmentation'):
    st.write("Button clicked!")
    start_time_loading = time.time()
    segmentation_data = load_segmentations()
    end_time_loading = time.time()
    st.write(f"Total time taken for loading segmentation: {end_time_loading - start_time_loading:.2f} seconds")
   
    start_time_visualization = time.time()
    fig = visualize_segmentations_3d(segmentation_data)
    end_time_visualization = time.time()
    st.write(f"Total time taken for visualization: {end_time_visualization - start_time_visualization:.2f} seconds")

    st.plotly_chart(fig)


#with open("streamlit_app.py", "w") as f:
    #f.write(streamlit_code)

#print("Streamlit app code has been written to streamlit_app.py")