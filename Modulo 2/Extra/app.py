import streamlit as st
st.title("IsaGomes RH---envie suas informações")
nome = st.text_input("Digite o nome do funcionário")
idade = st.text_input("Digite a idade do funcionário")
email = st.text_input("Digite o email do funcionário")
salario = st.text_input("Digite o salario do funcionário")
cargo = st.text_input("Digite o cardo do do seu funcionário")



if st.button("Cadastrar informações"):
    st.success(f"O funcionário {nome}, foi cadastrado com sucesso!!!")
    st.balloons()
    st.image('https://thispersondoesnotexist.com/')
    if st.button("Novo cadastro"):
        st.rerun()