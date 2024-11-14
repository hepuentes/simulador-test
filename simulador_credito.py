import streamlit as st

# Variables modificables mensualmente
INTERES_BANCARIO_CORRIENTE = 18.6  # Cambiar este valor cada mes

# Diccionario de líneas de crédito y sus intereses mensuales (ajustables)
LINEAS_DE_CREDITO = {
    "LoansiMoto": {"descripcion": "Compra de Moto Nueva", "interes_mv": 1.7, "monto_max": 16100000},
    "LoansiFlex": {"descripcion": "Libre Inversión", "interes_mv": 1.8, "monto_max": 20000000},
    "LoansiMicroFlex": {"descripcion": "Competitivo Gota a Gota", "interes_mv": 3.0, "monto_max": 300000}
}

# Título de la aplicación
st.title("Simulador de Crédito Loansi")

# Selección del tipo de crédito
tipo_credito = st.selectbox("Selecciona la Línea de Crédito", options=list(LINEAS_DE_CREDITO.keys()))
detalles_credito = LINEAS_DE_CREDITO[tipo_credito]
descripcion = detalles_credito["descripcion"]
interes_mensual = detalles_credito["interes_mv"]

# Mostrar detalles del tipo de crédito seleccionado
st.write(f"**Descripción**: {descripcion}")
st.write(f"**Interés Mensual (M.V.)**: {interes_mensual}%")
st.write(f"**Monto Máximo Disponible**: COP {detalles_credito['monto_max']:,}")

# Entradas para el monto solicitado y el plazo
monto = st.number_input("Monto Solicitado (COP):", min_value=0, max_value=detalles_credito["monto_max"], step=100000)
plazo = st.slider("Plazo en Meses:", min_value=12, max_value=48, step=12)

# Cálculo de cuota mensual
if monto > 0:
    cuota = (monto * (interes_mensual / 100)) / (1 - (1 + (interes_mensual / 100)) ** -plazo)
    st.write("### Resultado de Simulación")
    st.write(f"**Cuota Mensual Estimada**: COP {cuota:,.2f}")
    st.write(f"**Total a Pagar en {plazo} meses**: COP {cuota * plazo:,.2f}")
else:
    st.write("Por favor ingrese un monto válido para ver la cuota estimada.")

# Información adicional de simulación
st.write("---")
st.write("**Nota**: Las tasas de interés y condiciones pueden variar según el perfil del cliente.")
st.write("**Tasa de Interés Bancario Corriente**:", INTERES_BANCARIO_CORRIENTE, "%")
