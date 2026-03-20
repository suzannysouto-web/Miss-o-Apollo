import streamlit as st

# Estado inicial
if "pagina" not in st.session_state:
    st.session_state.pagina = "inicio"
    st.session_state.indice = 0
    st.session_state.placar = 0
    st.session_state.tentativas = 0
    st.session_state.acertos = 0
    st.session_state.erros = 0
    st.session_state.respondeu = False

# Perguntas
quiz = [
    {
        "pergunta": "Em qual programa Margaret Hamilton esteve envolvida?",
        "opcoes": ["a) Sputnik", "b) Gêmeos", "c) Mercúrio", "d) Apollo", "e) Skylab"],
        "resposta": "d"
    },
    {
        "pergunta": "Em qual filme Margaret Hamilton atuou?",
        "opcoes": ["a) Caça às Bruxas", "b) Titanic", "c) O Mágico de OZ", "d) Avatar", "e) Frozen"],
        "resposta": "c"
    },
    {
        "pergunta": "Em que ano aconteceu a missão Apollo?",
        "opcoes": ["a) 2000", "b) 1969", "c) 1980", "d) 1970", "e) 1950"],
        "resposta": "b"
    },
    {
        "pergunta": "Em que ano Margaret Hamilton recebeu a medalha da liberdade?",
        "opcoes": ["a) 2018", "b) 2017", "c) 2016", "d) 2015", "e) 2020"],
        "resposta": "c"
    },
    {
        "pergunta": "Quantos artigos Margaret Hamilton publicou?",
        "opcoes": ["a) Mais de 10", "b) Mais de 150", "c) Mais de 130", "d) Mais de 50", "e) Mais de 5"],
        "resposta": "c"
    },
    {
        "pergunta": "Qual personagem ela interpretou no Mágico de OZ?",
        "opcoes": ["a) Dorothy", "b) Glinda", "c) Leão", "d) Espantalho", "e) Bruxa Má do Oeste"],
        "resposta": "e"
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
            "a) Máquina Inteligente Tecnológica",
            "b) Ministério Internacional",
            "c) Módulo de Tributos",
            "d) Instituto de Tecnologia de Massachusetts",
            "e) Método Internacional Técnico"
        ],
        "resposta": "d"
    },
    {
        "pergunta": "Margaret Hamilton foi uma grande cientista da computação.",
        "opcoes": ["a) Falso", "b) Verdadeiro"],
        "resposta": "b"
    }
]

# -------- TELA INICIAL --------
if st.session_state.pagina == "inicio":
    st.title("🚀 Margaret Hamilton e a Lua 🌕")

    st.write("🌸 Bem-vindo(a)! 🌸")
    st.write("✔ Acerto: +10 pontos")
    st.write("❌ Erro: -5 pontos (mínimo 0)")

    if st.button("Iniciar Quiz"):
        st.session_state.pagina = "quiz"
        st.rerun()

# -------- QUIZ --------
elif st.session_state.pagina == "quiz":
    i = st.session_state.indice

    st.write(f"🏆 Pontos: {st.session_state.placar}")
    st.write(f"✅ {st.session_state.acertos} | ❌ {st.session_state.erros}")

    if i < len(quiz):
        pergunta = quiz[i]

        st.subheader(f"Pergunta {i+1}")
        st.write(pergunta["pergunta"])

        resposta = st.radio("Escolha:", pergunta["opcoes"], key=i)

        if not st.session_state.respondeu:
            if st.button("Responder"):
                st.session_state.tentativas += 1

                if resposta.startswith(pergunta["resposta"]):
                    st.session_state.placar += 10
                    st.session_state.acertos += 1
                else:
                    st.session_state.placar -= 5
                    st.session_state.erros += 1

                # Impede negativo
                if st.session_state.placar < 0:
                    st.session_state.placar = 0

                st.session_state.respondeu = True
                st.rerun()

        else:
            if st.button("Próxima"):
                st.session_state.indice += 1
                st.session_state.respondeu = False
                st.rerun()

    else:
        st.session_state.pagina = "final"
        st.rerun()

# -------- RESULTADO --------
elif st.session_state.pagina == "final":
    st.title("Resultado Final")

    st.write(f"🏆 Pontuação: {st.session_state.placar}")
    st.write(f"✅ Acertos: {st.session_state.acertos}")
    st.write(f"❌ Erros: {st.session_state.erros}")

    if st.button("Reiniciar"):
        st.session_state.pagina = "inicio"
        st.session_state.indice = 0
        st.session_state.placar = 0
        st.session_state.tentativas = 0
        st.session_state.acertos = 0
        st.session_state.erros = 0
        st.session_state.respondeu = False
        st.rerun()
