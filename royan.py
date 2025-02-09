import streamlit as st
import pandas as pd

# Cargar datos desde un CSV (simulado aquí)
data = pd.DataFrame({
    'Imagen': [
        'images/WhatsApp Image 2025-02-09 at 13.35.23.jpeg',
        'images/WhatsApp Image 2025-02-09 at 13.35.24.jpeg',
        'images/WhatsApp Image 2025-02-09 at 13.35.24 (1).jpeg',
        'images/WhatsApp Image 2025-02-09 at 13.35.24 (2).jpeg',
        'images/WhatsApp Image 2025-02-09 at 13.35.24 (3).jpeg',
        'images/WhatsApp Image 2025-02-09 at 13.35.24 (4).jpeg'
    ],
    'Nombre': [
        'Pendientes Pandora', 'Pulsera Guess', 'Collar con cruz', 
        'Anillo Te Quiero Mamá', 'Pendientes Tous negros', 'Pendientes Tous verdes'
    ],
    'Precio': [
        '49.99€', '39.99€', '29.99€', '19.99€', '24.99€', '27.99€'
    ]
})

# Configuración de la página
st.title("Tienda de Joyería")
st.write("Explora nuestra colección de joyería exclusiva")

# Mostrar productos
for index, row in data.iterrows():
    st.image(row['Imagen'], caption=row['Nombre'], use_column_width=True)
    st.write(f"**{row['Nombre']}**")
    st.write(f"Precio: {row['Precio']}")
    st.button(f"Comprar {row['Nombre']}", key=index)
