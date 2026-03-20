import streamlit as st

# Inicialização
if "pagina" not in st.session_state:
    st.session_state.pagina = "inicio"
    st.session_state.indice = 0
    st.session_state.placar = 0
    st.session_state.tentativas = 0

# Lista de perguntas (equivalente ao seu código original)
quiz = [
    {
        "pergunta": "Em qual programa Margaret Hamilton esteve envolvida?",
        "opcoes": ["a) Sputnik", "b) Gêmeos", "c) Mercúrio", "d) Apollo"],
        "resposta": "d"
    },
    {
        "pergunta": "Em qual filme Margaret Hamilton atuou?",
        "opcoes": ["a) O Mágico de OZ", "b) Titanic", "c) Caça às Bruxas"],
        "resposta": "a"
    },
    {
        "pergunta": "Em que ano aconteceu a missão Apollo?",
        "opcoes": ["a) 2000", "b) 1969", "c) 1970"],
        "resposta": "b"
    },
    {
        "pergunta": "Em que ano Margaret Hamilton recebeu a medalha da liberdade dos Estados Unidos?",
        "opcoes": ["a) 2018", "b) 2017", "c) 2019"],
        "resposta": "c"
    },
    {
        "pergunta": "Quantos artigos Margaret Hamilton publicou?",
        "opcoes": ["a) Mais de 10", "b) Mais de 150", "c) Mais de 130"],
        "resposta": "c"
    },
    {
        "pergunta": "Qual personagem Margaret Hamilton interpretou no Mágico de OZ?",
        "opcoes": ["a) Dorothy Gale", "b) Glinda", "c) Bruxa Má do Oeste"],
        "resposta": "c"
    },
    {
        "pergunta": "Margaret Hamilton estudou no MIT?",
        "opcoes": ["a) Falso", "b) Verdadeiro"],
        "resposta": "a"
    },
    {
        "pergunta": "Em qual ano Margaret Hamilton nasceu?",
        "opcoes": ["a) 1989", "b) 1936", "c) 1990"],
        "resposta": "b"
    },
    {
        "pergunta": "Qual é o significado das siglas MIT?",
        "opcoes": ["a) Instituto de Tecnologia de Massachusetts", "b) Ministério Internacional", "c) Módulo de Inclusão de Tributos"],
        "resposta": "a"
    },
    {
        "pergunta": "Margaret Hamilton foi uma grande cientista da computação?",
        "opcoes": ["a) Verdadeiro", "b) Falso"],
        "resposta": "a"
    }
]

# ---------------- TELA INICIAL ----------------
if st.session_state.pagina == "inicio":
    st.title("INSERIR TÍTULO AQUI")

    st.write("Seja bem-vindo(a)!")
    st.write("Este é um Quiz sobre Margaret Hamilton.")
    st.write("Cada questão vale 10 pontos.")
    st.write("Erros retiram 10 pontos.")

    if st.button("Iniciar Quiz"):
        st.session_state.pagina = "quiz"
        st.rerun()

# ---------------- QUIZ ----------------
elif st.session_state.pagina == "quiz":
    i = st.session_state.indice

    if i < len(quiz):
        pergunta = quiz[i]

        st.subheader(f"Pergunta {i+1}")
        st.write(pergunta["pergunta"])

        resposta = st.radio("Escolha uma alternativa:", pergunta["opcoes"], key=i)

        if st.button("Próxima"):
            st.session_state.tentativas += 1

            if resposta.startswith(pergunta["resposta"]):
                st.session_state.placar += 10
            else:
                st.session_state.placar -= 10

            st.session_state.indice += 1
            st.rerun()
    else:
        st.session_state.pagina = "final"
        st.rerun()

# ---------------- RESULTADO FINAL ----------------
elif st.session_state.pagina == "final":
    st.title("Resultado Final")

    st.write(f"Sua pontuação foi: {st.session_state.placar}")
    st.write(f"Total de tentativas: {st.session_state.tentativas}")

    st.write("🌸 Obrigado por participar do nosso Quiz! 🌸")

    st.write("""
    Neste Dia das Mulheres, queremos lembrar o quanto cada mulher é forte,
    inteligente e capaz de transformar o mundo ao seu redor.

    Um exemplo incrível disso é Margaret Hamilton, que ajudou levar a humanidade à Lua 🚀

    Que sua jornada seja cheia de conquistas!

    Feliz Dia das Mulheres! 🌷
    """)

    if st.button("Reiniciar"):
        st.session_state.pagina = "inicio"
        st.session_state.indice = 0
        st.session_state.placar = 0
        st.session_state.tentativas = 0
        st.rerun()
