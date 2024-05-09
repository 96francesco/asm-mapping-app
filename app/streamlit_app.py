import streamlit as st
import folium

from streamlit_folium import st_folium
from folium.plugins import Draw
from datetime import date


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
            ('Median composite', 'Latest')
      )
      return model_option, image_type

# main function to manage the app
def main():
      st.set_page_config(page_title="ASM detection", layout="wide")
      st.title("Artisanal and Small-scale Mining (ASM) detection in the DRC")

      # get user inputs
      model_option, image_type = user_input_options()
      
      # get date range
      if image_type == 'Median composite':
            min_date = date(2020, 9, 1)
            max_date = date.today()
            start_date = st.date_input("Select start date:", min_value=min_date, max_value=max_date, value=min_date)
            end_date = st.date_input("Select end date:", min_value=min_date, max_value=max_date, value=max_date)
      else:
            # TODO: understand how to handle the last image case
            pass


      # display map and get marker
      # draw_control = map_with_marker()
      st.markdown('#### Draw a marker in the area of the map where you want to detect ASM areas and click the RUN button below.')
      st.markdown('###### Note: at the moment, only the DRC area is supported.')
      
      m = folium.Map(location=[-4.0383, 21.7587], zoom_start=5)
      tile = folium.TileLayer(
        tiles = 'https://services.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/tile/{z}/{y}/{x}',
        attr = 'Esri',
        name = 'Esri Satellite',
        overlay = True,
        control = True
       ).add_to(m)

      tile = folium.TileLayer(
            tiles = 'https://services.arcgisonline.com/ArcGIS/rest/services/Reference/World_Boundaries_and_Places/MapServer/tile/{z}/{y}/{x}',
            attr = 'Esri',
            name = 'Esri Satellite',
            overlay = True,
            control = True
            ).add_to(m)
      
      Draw(export = False, draw_options = {'polyline' : False, 'polygon': False, 'rectangle' : False, 'circle' : False, 'circlemarker' : False}).add_to(m)
      map = st_folium(m, width = 700, height = 500, returned_objects=['marker'])

      # RUN button to process the selected area and display the results
      if st.button("RUN"):

            with st.spinner('Collecting satellite imagery and searching for ASM sites with '+model_option+' model...'):
                  coordinates = list(map['marker']['geometry']['coordinates'])

# run
if __name__ == "__main__":
      main()