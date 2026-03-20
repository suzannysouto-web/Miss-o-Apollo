import streamlit as st

# Estado inicial
if "pagina" not in st.session_state:
    st.session_state.pagina = "inicio"
    st.session_state.indice = 0
    st.session_state.placar = 0
    st.session_state.tentativas = 0

# Perguntas
quiz = [
    {
        "pergunta": "Em qual programa Margaret Hamilton esteve envolvida?",
        "opcoes": ["a) Sputnik", "b) Gêmeos", "c) Mercúrio", "d) Apollo", "e) Skylab"],
        "resposta": "d"
    },
    {
        "pergunta": "Em qual filme Margaret Hamilton atuou?",
        "opcoes": ["a) O Mágico de OZ", "b) Titanic", "c) Caça às Bruxas", "d) Avatar", "e) Frozen"],
        "resposta": "a"
    },
    {
        "pergunta": "Em que ano aconteceu a missão Apollo?",
        "opcoes": ["a) 2000", "b) 1969", "c) 1970", "d) 1980", "e) 1950"],
        "resposta": "b"
    },
    {
        "pergunta": "Em que ano Margaret Hamilton recebeu a medalha da liberdade?",
        "opcoes": ["a) 2018", "b) 2017", "c) 2019", "d) 2015", "e) 2020"],
        "resposta": "c"
    },
    {
        "pergunta": "Quantos artigos Margaret Hamilton publicou?",
        "opcoes": ["a) Mais de 10", "b) Mais de 150", "c) Mais de 130", "d) Mais de 50", "e) Mais de 5"],
        "resposta": "c"
    },
    {
        "pergunta": "Qual personagem ela interpretou no Mágico de OZ?",
        "opcoes": ["a) Dorothy", "b) Glinda", "c) Bruxa Má do Oeste", "d) Espantalho", "e) Leão"],
        "resposta": "c"
    },
    {
        "pergunta": "Margaret Hamilton estudou no MIT?",
        "opcoes": ["a) Falso", "b) Verdadeiro"],
        "resposta": "a"
    },
    {
        "pergunta": "Em qual ano Margaret Hamilton nasceu?",
        "opcoes": ["a) 1989", "b) 1936", "c) 1990", "d) 1920", "e) 1945"],
        "resposta": "b"
    },
    {
        "pergunta": "Qual é o significado de MIT?",
        "opcoes": [
            "a) Instituto de Tecnologia de Massachusetts",
            "b) Ministério Internacional",
            "c) Módulo de Tributos",
            "d) Máquina Inteligente Tecnológica",
            "e) Método Internacional Técnico"
        ],
        "resposta": "a"
    },
    {
        "pergunta": "Margaret Hamilton foi uma grande cientista da computação?",
        "opcoes": ["a) Verdadeiro", "b) Falso"],
        "resposta": "a"
    }
]

# -------- TELA INICIAL --------
if st.session_state.pagina == "inicio":
    st.title("INSERIR TÍTULO AQUI")

    st.write("🌸 Seja bem-vindo(a)! 🌸")
    st.write("Este é um Quiz desenvolvido para homenagear Margaret Hamilton.")

    st.write("""
    Neste Dia das Mulheres, queremos lembrar o quanto cada mulher é forte,
    inteligente e capaz de transformar o mundo ao seu redor.

    Um exemplo incrível disso é Margaret Hamilton, que fez história na tecnologia
    e ajudou a levar a humanidade à Lua 🚀
    """)

    st.write("Cada acerto vale +10 pontos.")
    st.write("Erros retiram 10 pontos (mínimo 0).")
    st.write("Boa sorte! 🍀")

    if st.button("Iniciar Quiz"):
        st.session_state.pagina = "quiz"
        st.rerun()

# -------- QUIZ --------
elif st.session_state.pagina == "quiz":
    i = st.session_state.indice

    if i < len(quiz):
        pergunta = quiz[i]

        st.subheader(f"Pergunta {i+1}")
        st.write(pergunta["pergunta"])

        resposta = st.radio("Escolha:", pergunta["opcoes"], key=i)

        if st.button("Próxima"):
            st.session_state.tentativas += 1

            if resposta.startswith(pergunta["resposta"]):
                st.session_state.placar += 10
            else:
                st.session_state.placar -= 10

            # Evita pontuação negativa
            if st.session_state.placar < 0:
                st.session_state.placar = 0

            st.session_state.indice += 1
            st.rerun()

    else:
        st.session_state.pagina = "final"
        st.rerun()

# -------- RESULTADO --------
elif st.session_state.pagina == "final":
    st.title("Resultado Final")

    st.write(f"Pontuação: {st.session_state.placar}")
    st.write(f"Tentativas: {st.session_state.tentativas}")

    st.write("🌸 Obrigado por participar do quiz! 🌸")

    st.write("""
    Feliz Dia das Mulheres! 🌷

    Continue acreditando no seu potencial e no seu brilho!
    """)

    if st.button("Reiniciar"):
        st.session_state.pagina = "inicio"
        st.session_state.indice = 0
        st.session_state.placar = 0
        st.session_state.tentativas = 0
        st.rerun()
      
