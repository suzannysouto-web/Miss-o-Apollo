import streamlit as st

# -------- ESTADO INICIAL --------
if "pagina" not in st.session_state:
    st.session_state.pagina = "inicio"
    st.session_state.indice = 0
    st.session_state.placar = 0
    st.session_state.tentativas = 0
    st.session_state.acertos = 0
    st.session_state.erros = 0

# -------- PERGUNTAS --------
quiz = [
    {"pergunta": "Em qual programa Margaret Hamilton esteve envolvida?",
     "opcoes": ["a) Sputnik", "b) Gêmeos", "c) Mercúrio", "d) Apollo"], "resposta": "d"},

    {"pergunta": "Em qual filme Margaret Hamilton atuou?",
     "opcoes": ["a) O Mágico de OZ", "b) Titanic", "c) Caça às Bruxas"], "resposta": "a"},

    {"pergunta": "Em que ano aconteceu a missão Apollo?",
     "opcoes": ["a) 2000", "b) 1969", "c) 1970"], "resposta": "b"},

    {"pergunta": "Em que ano Margaret Hamilton recebeu a medalha da liberdade?",
     "opcoes": ["a) 2018", "b) 2017", "c) 2019"], "resposta": "c"},

    {"pergunta": "Quantos artigos Margaret Hamilton publicou?",
     "opcoes": ["a) Mais de 10", "b) Mais de 150", "c) Mais de 130"], "resposta": "c"},

    {"pergunta": "Qual personagem ela interpretou no Mágico de OZ?",
     "opcoes": ["a) Dorothy", "b) Glinda", "c) Bruxa Má do Oeste"], "resposta": "c"},

    {"pergunta": "Margaret Hamilton estudou no MIT?",
     "opcoes": ["a) Falso", "b) Verdadeiro"], "resposta": "a"},

    {"pergunta": "Em qual ano Margaret Hamilton nasceu?",
     "opcoes": ["a) 1989", "b) 1936", "c) 1990"], "resposta": "b"},

    {"pergunta": "Qual é o significado de MIT?",
     "opcoes": ["a) Instituto de Tecnologia de Massachusetts",
                "b) Ministério Internacional do Trabalhador",
                "c) Módulo de Inclusão de Tributos"], "resposta": "a"},

    {"pergunta": "Margaret Hamilton foi uma grande cientista da computação?",
     "opcoes": ["a) Verdadeiro", "b) Falso"], "resposta": "a"}
]

# -------- TELA INICIAL --------
if st.session_state.pagina == "inicio":
    st.title("Margaret Elaine Hamilton,a mulher que levou a humanidade à lua.")

    st.write("Seja bem-vindo(a)! 🌸")
    st.write("✔ Acerto: +10 pontos")
    st.write("❌ Erro: -5 pontos")

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

        resposta = st.radio(
            "Escolha uma opção:",
            pergunta["opcoes"],
            index=None,  # 👈 evita resposta automática
            key=f"q_{i}"
        )

        if st.button("Próxima", key=f"btn_{i}"):

            if resposta is None:
                st.warning("⚠️ Escolha uma opção antes de continuar!")
            else:
                st.session_state.tentativas += 1
                letra = resposta[0].lower()

                if letra == pergunta["resposta"]:
                    st.session_state.placar += 10
                    st.session_state.acertos += 1
                else:
                    st.session_state.placar = max(0, st.session_state.placar - 5)
                    st.session_state.erros += 1

                st.session_state.indice += 1
                st.rerun()
    else:
        st.session_state.pagina = "final"
        st.rerun()

# -------- RESULTADO FINAL --------
elif st.session_state.pagina == "final":
    st.title("🏆 Resultado Final")

    st.write(f"🏆 Pontuação: {st.session_state.placar}")
    st.write(f"🔁 Tentativas: {st.session_state.tentativas}")
    st.write(f"✅ Acertos: {st.session_state.acertos}")
    st.write(f"❌ Erros: {st.session_state.erros}")

    # Mensagem inteligente baseada no desempenho
    if st.session_state.acertos >= 8:
        st.success("🌟 Incrível! Você domina o assunto!")
    elif st.session_state.acertos >= 5:
        st.info("👏 Muito bem! Você foi muito bem!")
    else:
        st.warning("💡 Continue tentando, você vai melhorar!")

    if st.button("Reiniciar"):
        for key in st.session_state.keys():
            del st.session_state[key]
        st.rerun()
