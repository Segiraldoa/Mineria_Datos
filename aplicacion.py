import streamlit as st
from PIL import Image
from tensorflow.keras.preprocessing.image import img_to_array


def preprocesse_image(image):
  image=image.convert("L")
  image=image.resize((28,28))
  image_array=img_to_array(image)/255.0
  image_array=np.expand_dims(image_array, axis=0)
  return image_array
  
def main():
  st.title("Clasificación de la base de datos mnist")
  st.markdown("Suba la imagen para clasificar")

  uploaded_file = st.file_uploader("Selecciona una imagen",type=["jpg","png","jpeg"])

  if uploaded_file is not None:
    image = Image.open(uploaded_file)

    st.image(image,caption="Imagen subida")
    preprocessed_image=preprocesse_image(image)
    st.image(preprocessed_image,caption="Imagen preprocesada")
  

if __name__=='__main__':
  main()
