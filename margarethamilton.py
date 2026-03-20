import streamlit as st

# -------- ESTADO --------
if "pagina" not in st.session_state:
    st.session_state.pagina = "inicio"
    st.session_state.indice = 0
    st.session_state.placar = 0
    st.session_state.tentativas = 0
    st.session_state.acertos = 0
    st.session_state.erros = 0
    st.session_state.respondido = False

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
    st.title("INSERIR TÍTULO AQUI")

    st.write("Seja bem-vindo(a)! 🌸")
    st.write("Quiz em homenagem a Margaret Hamilton.")
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
            index=None,
            key=f"q_{i}"
        )

        # BOTÃO RESPONDER
        if st.button("Responder", key=f"resp_{i}"):

            if resposta is None:
                st.warning("Escolha uma opção antes de continuar!")
            elif not st.session_state.respondido:

                st.session_state.respondido = True
                st.session_state.tentativas += 1

                letra = resposta[0].lower()

                if letra == pergunta["resposta"]:
                    st.session_state.placar += 10
                    st.session_state.acertos += 1
                else:
                    st.session_state.placar = max(0, st.session_state.placar - 5)
                    st.session_state.erros += 1

                st.rerun()

        # BOTÃO PRÓXIMA (só depois de responder)
        if st.session_state.respondido:
            if st.button("Próxima", key=f"next_{i}"):
                st.session_state.indice += 1
                st.session_state.respondido = False
                st.rerun()

    else:
        st.session_state.pagina = "final"
        st.rerun()

# -------- RESULTADO FINAL --------
elif st.session_state.pagina == "final":
    st.title("🏆 Resultado Final")

    st.write(f"Sua pontuação foi: {st.session_state.placar}")
    st.write(f"Total de tentativas: {st.session_state.tentativas}")
    st.write(f"Acertos: {st.session_state.acertos}")
    st.write(f"Erros: {st.session_state.erros}")

    st.write("🌸 Obrigado por participar do nosso quiz! 🌸")

    st.write("Neste Dia das Mulheres, queremos lembrar o quanto cada mulher é forte, inteligente e capaz de transformar o mundo ao seu redor.")
    st.write("Um exemplo incrível disso é Margaret Hamilton, que fez história na tecnologia e ajudou a levar a humanidade à Lua. ")
    st.write("Que a sua jornada também seja cheia de conquistas, sonhos realizados e muita inspiração! ")
    st.write("Feliz Dia das Mulheres! Nunca duvide do seu brilho. 🌷")

    if st.button("Reiniciar"):
        for k in list(st.session_state.keys()):
            del st.session_state[k]
        st.rerun()
