import streamlit as st

# Inicialização dos estados
if "pagina" not in st.session_state:
    st.session_state.pagina = "inicio"
    st.session_state.pergunta_atual = 0
    st.session_state.pontuacao = 0
    st.session_state.acertos = 0
    st.session_state.erros = 0

# Lista de perguntas
perguntas = [
    {
        "pergunta": "1) Em qual programa espacial Margaret Hamilton esteve envolvida?",
        "opcoes": ["Sputnik", "Gêmeos (Gemini)", "Mercúrio", "Apollo", "Artemis", "Voyager"],
        "resposta": 3
    },
    {
        "pergunta": "2) Em qual filme clássico Margaret Hamilton atuou?",
        "opcoes": ["O Mágico de Oz", "Titanic", "E o Vento Levou", "Casablanca", "Caça as Bruxas", "Cantando na Chuva"],
        "resposta": 0
    },
    {
        "pergunta": "3) Em que ano aconteceu o primeiro pouso na Lua?",
        "opcoes": ["2000", "1968", "1970", "1955", "1945", "1969"],
        "resposta": 5
    },
    {
        "pergunta": "4) Em que ano Margaret Hamilton recebeu a Medalha Presidencial da Liberdade?",
        "opcoes": ["2018", "2019", "2016", "2020", "2010", "2014"],
        "resposta": 2
    },
    {
        "pergunta": "5) Quantos artigos Margaret Hamilton publicou aproximadamente?",
        "opcoes": ["Mais de 10", "Mais de 150", "Menos de 5", "Mais de 50", "Mais de 130", "Exatos 100"],
        "resposta": 4
    },
    {
        "pergunta": "6) Qual personagem ela interpretou no Mágico de Oz?",
        "opcoes": ["Dorothy", "Glinda", "Bruxa Má do Oeste", "Tia Em", "Leão", "Espantalho"],
        "resposta": 2
    },
    {
        "pergunta": "7) Margaret Hamilton estudou no MIT?",
        "opcoes": ["Falso", "Verdadeiro"],
        "resposta": 0
    },
    {
        "pergunta": "8) Em qual ano ela nasceu?",
        "opcoes": ["1939", "1989", "1936", "1990", "1920", "1950"],
        "resposta": 2
    },
    {
        "pergunta": "9) Ela criou qual termo?",
        "opcoes": ["Hardware", "Engenharia de Software", "IA", "Ciência de Dados", "Internet", "Algoritmo"],
        "resposta": 1
    },
    {
        "pergunta": "10) O que significa MIT?",
        "opcoes": [
            "Instituto de Tecnologia de Massachusetts",
            "Missão internacional de tecnologia",
            "Ministério internacional do trabalhador",
            "Módulo de inclusão de tributos",
            "Manutenção Industrial Técnica",
            "Marca de Inovação Tecnológica"
        ],
        "resposta": 0
    }
]

# ===== TELA INICIAL =====
if st.session_state.pagina == "inicio":
    st.title("🚀Margaret Elaine Hamilton,a Mulher que Levou a Humanidade à Lua.🌕")

    st.write("Bem-vindo(a) ao Quiz em homenagem a Margaret Hamilton!")
    st.write("🎯 Total: 100 pontos")
    st.write("❌ Erro: -5 pontos")

    if st.button("Iniciar Quiz"):
        st.session_state.pagina = "quiz"
        st.rerun()

# ===== QUIZ =====
elif st.session_state.pagina == "quiz":
    i = st.session_state.pergunta_atual
    pergunta = perguntas[i]

    st.subheader(pergunta["pergunta"])

    resposta = st.radio(
        "Escolha uma opção:",
        pergunta["opcoes"],
        key=i
    )

    if st.button("Próxima"):
        if pergunta["opcoes"].index(resposta) == pergunta["resposta"]:
            st.session_state.pontuacao += 10
            st.session_state.acertos += 1
        else:
            st.session_state.pontuacao -= 5
            st.session_state.erros += 1

        st.session_state.pergunta_atual += 1

        if st.session_state.pergunta_atual >= len(perguntas):
            st.session_state.pagina = "resultado"

        st.rerun()

# ===== RESULTADO FINAL =====
elif st.session_state.pagina == "resultado":
    if st.session_state.pontuacao < 0:
        st.session_state.pontuacao = 0

    st.title("🏆 RESULTADO FINAL")

    st.write(f"Pontuação: {st.session_state.pontuacao} de 100")
    st.write(f"✅ Acertos: {st.session_state.acertos}")
    st.write(f"❌ Erros: {st.session_state.erros}")
    st.write(f"📊 Total de perguntas: {len(perguntas)}")

    st.markdown("---")

    st.write("🌸 Obrigado por participar do nosso quiz! 🌸")
    st.write("Neste Dia das Mulheres, celebramos a força e a inteligência de todas as mulheres!")
    st.write("✨ Nunca duvide do seu brilho! ✨")

    if st.button("Reiniciar"):
        for key in st.session_state.keys():
            del st.session_state[key]
        st.rerun()
