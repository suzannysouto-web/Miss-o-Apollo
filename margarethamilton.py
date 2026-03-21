import streamlit as st

# -------- ESTADO INICIAL --------
# Inicializamos as variáveis apenas se elas não existirem
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
     "opcoes": ["a) 2018", "b) 2017", "c) 2016"], "resposta": "c"}, # Corrigido: Foi em 2016

    {"pergunta": "Quantos artigos Margaret Hamilton publicou?",
     "opcoes": ["a) Mais de 10", "b) Mais de 150", "c) Mais de 130"], "resposta": "c"},

    {"pergunta": "Qual personagem ela interpretou no Mágico de OZ?",
     "opcoes": ["a) Dorothy", "b) Glinda", "c) Bruxa Má do Oeste"], "resposta": "c"},

    {"pergunta": "Margaret Hamilton estudou no MIT?",
     "opcoes": ["a) Falso", "b) Verdadeiro"], "resposta": "b"}, # Corrigido: Ela trabalhou/liderou o lab no MIT

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
    st.title("🚀 Quiz Margaret Hamilton")
    st.write("Seja bem-vindo(a)! 🌸")
    st.write("Teste seus conhecimentos sobre a mulher que cunhou o termo 'Engenharia de Software'.")
    st.info("✔ Acerto: +10 pontos | ❌ Erro: -5 pontos")

    if st.button("Iniciar Quiz"):
        st.session_state.pagina = "quiz"
        st.rerun()

# -------- QUIZ --------
elif st.session_state.pagina == "quiz":
    idx = st.session_state.indice

    if idx < len(quiz):
        st.subheader(f"Pergunta {idx + 1} de {len(quiz)}")
        item = quiz[idx]
        
        st.write(item["pergunta"])
        
        # Usamos o index da pergunta para garantir que o rádio mude a cada rodada
        escolha = st.radio("Selecione a opção correta:", item["opcoes"], key=f"p_{idx}")

        if st.button("Confirmar Resposta"):
            # Lógica de validação
            letra_escolhida = escolha[0].lower()
            st.session_state.tentativas += 1
            
            if letra_escolhida == item["resposta"]:
                st.session_state.placar += 10
                st.session_state.acertos += 1
                st.success("Resposta Correta!")
            else:
                st.session_state.placar = max(0, st.session_state.placar - 5)
                st.session_state.erros += 1
                st.error(f"Resposta Incorreta! A correta era a letra {item['resposta']}")

            # Avançar o índice
            st.session_state.indice += 1
            st.rerun()
    else:
        st.session_state.pagina = "final"
        st.rerun()

# -------- RESULTADO FINAL --------
elif st.session_state.pagina == "final":
    st.title("🏆 Resultado Final")
    
    col1, col2 = st.columns(2)
    col1.metric("Pontuação Total", f"{st.session_state.placar} pts")
    col2.metric("Aproveitamento", f"{(st.session_state.acertos / len(quiz)) * 100:.0f}%")

    st.write(f"✅ **Acertos:** {st.session_state.acertos}")
    st.write(f"❌ **Erros:** {st.session_state.erros}")
    st.write(f"🔁 **Tentativas:** {st.session_state.tentativas}")

    st.divider()
    st.write("### Feliz Dia das Mulheres! 🌸")
    st.write("Margaret Hamilton não apenas escreveu o código para a Apollo 11, mas provou que o lugar da mulher é onde ela quiser — inclusive na Lua.")

    if st.button("Jogar Novamente"):
        # Limpa tudo e volta ao início
        for key in st.session_state.keys():
            del st.session_state[key]
        st.rerun()
