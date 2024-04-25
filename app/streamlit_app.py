import streamlit as st
import geemap.foliumap as geemap

from streamlit_folium import folium_static
from folium.plugins import Draw

def map_with_marker():
      """
      Handle the map and marker
      """
      m = geemap.Map(center=[-6.369028, 34.888822], zoom=6)
      draw = Draw(export=True)
      draw.add_to(m)
      folium_static(m)
      return m

def user_input_options():
      """
      Get user input options for model and image type
      """
      model_option = st.radio(
            "Choose a model for prediction:",
            ('Planet-NICFI standalone', 'Sentinel-1 standalone', 'Late Fusion')
      )
      
      image_type = st.radio(
            "Choose the type of image:",
            ('Composite', 'Latest')
      )
      return model_option, image_type

# main function to manage the app
def main():
      st.set_page_config(page_title="Satellite Imagery Segmentation", layout="wide")
      st.title("Satellite Imagery Segmentation")

      # get user inputs
      model_option, image_type = user_input_options()

      # display map and get marker
      draw_control = map_with_marker()

      # RUN button to process the selected area and display the results
      if st.button("RUN"):
            # extract coordinates from the draw object here
            # PLACEHOLDER coordinates = extract_coordinates(draw_control)
            coordinates = [-6.369028, 34.888822]  

            # PLACEHOLDER prediction = perform_prediction(model_option, image_type, coordinates)

            # PLACEHOLDER tif_bytes = convert_to_tif(prediction)
            tif_bytes = b"TIFF_placeholder"  # Placeholder bytes

            # use download button to download the prediction result
            st.download_button(label="Download Prediction as TIFF",
                              data=tif_bytes,
                              file_name="prediction.tif",
                              mime="image/tiff")

            # display the prediction result below the map (placeholder)
            st.image(tif_bytes, caption='Prediction', use_column_width=True)

# run
if __name__ == "__main__":
      main()