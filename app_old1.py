import streamlit as st
import streamlit.components.v1 as components

# Configurações da página
st.set_page_config(
    page_title="FIFA World Cup 2026 - Hub Arena",
    page_icon="⚽",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Estilização global com CSS personalizado para a "Dynamic Tournament Arena"
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Bebas+Neue&family=Poppins:wght@300;400;600&display=swap');
    
    /* Configurações Globais de Tema Escuro e Ouro */
    .stApp {
        background-color: #0d0d0d;
        color: #f5f5f5;
        font-family: 'Poppins', sans-serif;
    }
    
    html, body, [data-testid="stSidebar"] {
        background-color: #050505 !important;
    }
    
    h1, h2, h3 {
        font-family: 'Bebas Neue', sans-serif !important;
        letter-spacing: 1.5px;
        color: #ffd700 !important;
    }
    
    /* Estilo dos Cards Laterais */
    .metric-card {
        background: linear-gradient(145deg, #151515, #222222);
        border: 1px solid #ffd70033;
        border-radius: 10px;
        padding: 15px;
        margin-bottom: 12px;
        box-shadow: 0 4px 15px rgba(0,0,0,0.5);
    }
    
    .gold-text {
        color: #ffd700;
        font-weight: bold;
    }
    
    /* Tabelas personalizadas */
    .custom-table {
        width: 100%;
        border-collapse: collapse;
        margin-top: 10px;
    }
    .custom-table th {
        background-color: #1a1a1a;
        color: #ffd700;
        font-family: 'Bebas Neue', sans-serif;
        font-size: 1.1rem;
        padding: 8px;
        text-align: center;
        border-bottom: 2px solid #ffd700;
    }
    .custom-table td {
        padding: 8px;
        text-align: center;
        border-bottom: 1px solid #333;
        font-size: 0.9rem;
    }
    .custom-table tr:hover {
        background-color: #222;
    }
    </style>
""", unsafe_allow_html=True)

# --- SIDEBAR ESQUERDO: Classificação & Artilharia ---
with st.sidebar:
    st.markdown("<h2 style='text-align: center; margin-bottom: 0;'>🏆 WC 2026 ARENA</h2>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; font-size: 0.8rem; color: #888;'>Dados atualizados em: 28/06/2026</p>", unsafe_allow_html=True)
    
    st.markdown("### 🔥 ARTILHARIA OFICIAL")
    st.markdown("""
    <div class='metric-card'>
        <div style='display: flex; justify-content: space-between; align-items: center;'>
            <span style='font-size: 1.1rem;'>🥇 <b>Lionel Messi</b> (ARG)</span>
            <span class='gold-text' style='font-size: 1.3rem;'>6 Gols</span>
        </div>
        <small style='color: #aaa;'>Marcou +1 hoje contra a Jordânia!</small>
    </div>
    <div class='metric-card'>
        <div style='display: flex; justify-content: space-between; align-items: center;'>
            <span>🥈 Ousmane Dembélé (FRA)</span>
            <span style='color: #fff; font-weight: bold;'>4 Gols</span>
        </div>
    </div>
    <div class='metric-card'>
        <div style='display: flex; justify-content: space-between; align-items: center;'>
            <span>🥉 Erling Haaland (NOR)</span>
            <span style='color: #fff; font-weight: bold;'>3 Gols</span>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("### 📊 RESUMO DOS GRUPOS (FIM DA 1ª FASE)")
    
    grupo_sel = st.selectbox("Visualizar Classificação:", ["Grupo A", "Grupo B", "Grupo H"])
    
    if grupo_sel == "Grupo A":
        st.markdown("""
        <table class='custom-table'>
            <tr><th>Pos</th><th>Seleção</th><th>Pts</th><th>SG</th></tr>
            <tr style='background-color: #ffd7001a;'><td>1</td><td>🇦🇷 Argentina</td><td>9</td><td>+6</td></tr>
            <tr style='background-color: #ffd7001a;'><td>2</td><td>🇨🇦 Canadá</td><td>4</td><td>+1</td></tr>
            <tr><td>3</td><td>🇯🇴 Jordânia</td><td>3</td><td>-2</td></tr>
            <tr><td>4</td><td>🇳🇿 Nova Zelândia</td><td>1</td><td>-5</td></tr>
        </table>
        """, unsafe_allow_html=True)
    elif grupo_sel == "Grupo B":
        st.markdown("""
        <table class='custom-table'>
            <tr><th>Pos</th><th>Seleção</th><th>Pts</th><th>SG</th></tr>
            <tr style='background-color: #ffd7001a;'><td>1</td><td>🇫🇷 França</td><td>9</td><td>+7</td></tr>
            <tr style='background-color: #ffd7001a;'><td>2</td><td>🇸🇪 Suécia</td><td>4</td><td>0</td></tr>
            <tr><td>3</td><td>🇳🇴 Noruega</td><td>3</td><td>-1</td></tr>
            <tr><td>4</td><td>🇿🇦 África do Sul</td><td>1</td><td>-6</td></tr>
        </table>
        """, unsafe_allow_html=True)
    else:
        st.markdown("""
        <table class='custom-table'>
            <tr><th>Pos</th><th>Seleção</th><th>Pts</th><th>SG</th></tr>
            <tr style='background-color: #ffd7001a;'><td>1</td><td>🇧🇷 Brasil</td><td>9</td><td>+8</td></tr>
            <tr style='background-color: #ffd7001a;'><td>2</td><td>🇯🇵 Japão</td><td>6</td><td>+2</td></tr>
            <tr><td>3</td><td>🇩🇿 Argélia</td><td>1</td><td>-4</td></tr>
            <tr><td>4</td><td>🇦🇹 Áustria</td><td>1</td><td>-6</td></tr>
        </table>
        """, unsafe_allow_html=True)

# --- PAINEL CENTRAL: Chaveamento Interativo Drag & Drop / Click ---
st.markdown("<h1 style='text-align: center; margin-top: -20px;'>CHAVEAMENTO COPA DO MUNDO 2026</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #aaa;'>Clique na bandeira ou arraste para avançá-la para a próxima fase!</p>", unsafe_allow_html=True)

# HTML/JS do Bracket baseado na imagem IMG-20260628-WA0048.jpg
bracket_html = """
<!DOCTYPE html>
<html lang="pt">
<head>
    <meta charset="UTF-8">
    <style>
        body {
            background-color: #0d0d0d;
            color: #fff;
            font-family: 'Poppins', sans-serif;
            margin: 0;
            padding: 10px;
            display: flex;
            justify-content: center;
        }
        .bracket-container {
            display: flex;
            gap: 20px;
            align-items: center;
            background: #111;
            padding: 30px;
            border-radius: 15px;
            border: 1px solid #ffd70022;
            width: 100%;
            overflow-x: auto;
        }
        .column {
            display: flex;
            flex-direction: column;
            justify-content: space-around;
            height: 650px;
            min-width: 165px;
        }
        .matchup {
            background: #1a1a1a;
            border: 1px solid #333;
            border-radius: 8px;
            padding: 6px;
            display: flex;
            flex-direction: column;
            gap: 4px;
            box-shadow: 0 4px 6px rgba(0,0,0,0.3);
        }
        .team {
            display: flex;
            align-items: center;
            gap: 10px;
            padding: 6px 10px;
            background: #252525;
            border-radius: 4px;
            cursor: grab;
            transition: all 0.2s;
            user-select: none;
            font-size: 0.85rem;
            font-weight: 600;
        }
        .team:hover {
            background: #ffd70022;
            border-color: #ffd700;
        }
        .target {
            border: 1px dashed #ffd70088;
            background: #151515;
            min-height: 34px;
            border-radius: 4px;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 0.75rem;
            color: #666;
        }
        .title-stage {
            text-align: center;
            font-family: 'Bebas Neue', sans-serif;
            color: #ffd700;
            font-size: 1.2rem;
            margin-bottom: 5px;
        }
    </style>
</head>
<body>

<div class="bracket-container">
    <!-- DEZASSEIS-AVOS / OITAVAS ESQUERDA -->
    <div class="column">
        <div class="title-stage">1/16 AVOS</div>
        <div class="matchup">
            <div class="team" draggable="true" ondragstart="drag(event)" id="t1" onclick="advance('t1', 'r1_1')">🇩🇪 Alemanha</div>
            <div class="team" draggable="true" ondragstart="drag(event)" id="t2" onclick="advance('t2', 'r1_1')">🇦🇹 Áustria</div>
        </div>
        <div class="matchup">
            <div class="team" draggable="true" ondragstart="drag(event)" id="t3" onclick="advance('t3', 'r1_2')">🇫🇷 França</div>
            <div class="team" draggable="true" ondragstart="drag(event)" id="t4" onclick="advance('t4', 'r1_2')">🇸🇪 Suécia</div>
        </div>
        <div class="matchup">
            <div class="team" draggable="true" ondragstart="drag(event)" id="t5" onclick="advance('t5', 'r1_3')">🇺🇾 Uruguai</div>
            <div class="team" draggable="true" ondragstart="drag(event)" id="t6" onclick="advance('t6', 'r1_3')">🇨🇦 Canadá</div>
        </div>
        <div class="matchup">
            <div class="team" draggable="true" ondragstart="drag(event)" id="t7" onclick="advance('t7', 'r1_4')">🇲🇦 Marrocos</div>
            <div class="team" draggable="true" ondragstart="drag(event)" id="t8" onclick="advance('t8', 'r1_4')">🇭🇷 Croácia</div>
        </div>
    </div>

    <!-- OITAVAS DE FINAL ESQUERDA -->
    <div class="column">
        <div class="title-stage">OITAVAS</div>
        <div class="matchup">
            <div class="target" id="r1_1" ondrop="drop(event)" ondragover="allowDrop(event)">Arrastar Aqui</div>
            <div class="target" id="r1_2" ondrop="drop(event)" ondragover="allowDrop(event)">Arrastar Aqui</div>
        </div>
        <div class="matchup">
            <div class="target" id="r1_3" ondrop="drop(event)" ondragover="allowDrop(event)">Arrastar Aqui</div>
            <div class="target" id="r1_4" ondrop="drop(event)" ondragover="allowDrop(event)">Arrastar Aqui</div>
        </div>
    </div>

    <!-- QUARTAS DE FINAL -->
    <div class="column">
        <div class="title-stage">QUARTAS</div>
        <div class="matchup" style="height: 120px; justify-content: center; gap: 20px;">
            <div class="target" id="q1" ondrop="drop(event)" ondragover="allowDrop(event)" style="width:100%">Quartas 1</div>
            <div class="target" id="q2" ondrop="drop(event)" ondragover="allowDrop(event)" style="width:100%">Quartas 2</div>
        </div>
    </div>

    <!-- GRANDE CAMPEÃO -->
    <div class="column" style="min-width: 200px;">
        <div class="title-stage" style="font-size: 1.5rem; color: #ffd700;">🏆 CAMPEÃO</div>
        <div class="matchup" style="border: 2px solid #ffd700; background: radial-gradient(circle, #222 0%, #000 100%); padding: 20px;">
            <div class="target" id="champion" ondrop="drop(event)" ondragover="allowDrop(event)" style="height: 60px; font-weight: bold; color: #ffd700;">
                SOLTE O CAMPEÃO AQUI
            </div>
        </div>
    </div>

    <!-- OITAVAS DE FINAL DIREITA -->
    <div class="column">
        <div class="title-stage">OITAVAS</div>
        <div class="matchup">
            <div class="target" id="r1_5" ondrop="drop(event)" ondragover="allowDrop(event)">Arrastar Aqui</div>
            <div class="target" id="r1_6" ondrop="drop(event)" ondragover="allowDrop(event)">Arrastar Aqui</div>
        </div>
        <div class="matchup">
            <div class="target" id="r1_7" ondrop="drop(event)" ondragover="allowDrop(event)">Arrastar Aqui</div>
            <div class="target" id="r1_8" ondrop="drop(event)" ondragover="allowDrop(event)">Arrastar Aqui</div>
        </div>
    </div>

    <!-- DEZASSEIS-AVOS / OITAVAS DIREITA -->
    <div class="column">
        <div class="title-stage">1/16 AVOS</div>
        <div class="matchup">
            <div class="team" draggable="true" ondragstart="drag(event)" id="t9" onclick="advance('t9', 'r1_5')">🇧🇷 Brasil</div>
            <div class="team" draggable="true" ondragstart="drag(event)" id="t10" onclick="advance('t10', 'r1_5')">🇯🇵 Japão</div>
        </div>
        <div class="matchup">
            <div class="team" draggable="true" ondragstart="drag(event)" id="t11" onclick="advance('t11', 'r1_6')">🏴󠁧󠁢󠁥󠁮󠁧󠁿 Inglaterra</div>
            <div class="team" draggable="true" ondragstart="drag(event)" id="t12" onclick="advance('t12', 'r1_6')">🇳🇱 Holanda</div>
        </div>
        <div class="matchup">
            <div class="team" draggable="true" ondragstart="drag(event)" id="t13" onclick="advance('t13', 'r1_7')">🇦🇷 Argentina</div>
            <div class="team" draggable="true" ondragstart="drag(event)" id="t14" onclick="advance('t14', 'r1_7')">🇯🇴 Jordânia</div>
        </div>
        <div class="matchup">
            <div class="team" draggable="true" ondragstart="drag(event)" id="t15" onclick="advance('t15', 'r1_8')">🇨🇭 Suíça</div>
            <div class="team" draggable="true" ondragstart="drag(event)" id="t16" onclick="advance('t16', 'r1_8')">🇪🇸 Espanha</div>
        </div>
    </div>
</div>

<script>
    function allowDrop(ev) {
        ev.preventDefault();
    }

    function drag(ev) {
        ev.dataTransfer.setData("text", ev.target.id);
    }

    function drop(ev) {
        ev.preventDefault();
        var data = ev.dataTransfer.getData("text");
        var draggedEl = document.getElementById(data);
        
        var clone = draggedEl.cloneNode(true);
        clone.id = data + "_clone_" + Math.random().toString(36).substr(2, 4);
        clone.style.cursor = "pointer";
        
        ev.target.innerHTML = "";
        ev.target.appendChild(clone);
    }

    function advance(teamId, targetId) {
        var teamEl = document.getElementById(teamId);
        var targetEl = document.getElementById(targetId);
        if(targetEl) {
            var clone = teamEl.cloneNode(true);
            clone.id = teamId + "_click_" + Math.random().toString(36).substr(2, 4);
            targetEl.innerHTML = "";
            targetEl.appendChild(clone);
        }
    }
</script>

</body>
</html>
"""

components.html(bracket_html, height=720, scrolling=True)

# --- ABAIXO: Resultados Recentes & Resumos ---
st.markdown("---")
col1, col2 = st.columns(2)

with col1:
    st.markdown("### 📅 ÚLTIMOS RESULTADOS OFICIAIS (28/06/2026)")
    st.markdown("""
    <div class='metric-card' style='border-left: 5px solid #ffd700;'>
        <div style='display: flex; justify-content: space-between;'>
            <b>🇦🇷 Argentina</b> <span><b>3</b> x 1</span> <span>🇯🇴 Jordânia</span>
        </div>
        <small style='color: #888;'>Fim da fase de grupos. Messi garantiu a artilharia provisória.</small>
    </div>
    <div class='metric-card'>
        <div style='display: flex; justify-content: space-between;'>
            <b>🇫🇷 França</b> <span><b>4</b> x 1</span> <span>🇳🇴 Noruega</span>
        </div>
    </div>
    <div class='metric-card'>
        <div style='display: flex; justify-content: space-between;'>
            <b>🇦🇹 Áustria</b> <span><b>3</b> x 3</span> <span>🇩🇿 Argélia</span>
        </div>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("### 💡 INTERATIVIDADE DA ARENA")
    st.info("Para avançar de fase, basta arrastar a caixa do país desejado até a próxima etapa pontilhada ou simplesmente clicar sobre o nome dele! Monte sua simulação até a grande final.")
