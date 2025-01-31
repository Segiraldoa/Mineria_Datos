import streamlit as st

def main():
  st.title("Clasificación de la base de datos mnist")
  st.markdown("Suba la imagen para clasificar")

  uploaded_file = st.file_uploader("Selecciona una imagen",type=["jpg","png","jpeg"])

if __name__=='__main__':
  main()
