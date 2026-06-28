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
    </style>
""", unsafe_allow_html=True)

# --- SIDEBAR ESQUERDO ---
with st.sidebar:
    st.markdown("<h2 style='text-align: center; margin-bottom: 0;'>🏆 WC 2026 ARENA</h2>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; font-size: 0.8rem; color: #888;'>Fase Final Corrigida (28/06/2026)</p>", unsafe_allow_html=True)
    
    st.markdown("### 🔥 ARTILHARIA OFICIAL")
    st.markdown("""
    <div class='metric-card'>
        <div style='display: flex; justify-content: space-between; align-items: center;'>
            <span style='font-size: 1.1rem;'>🥇 <b>Lionel Messi</b> (ARG)</span>
            <span class='gold-text' style='font-size: 1.3rem;'>6 Gols</span>
        </div>
        <small style='color: #aaa;'>Mais um gol hoje contra a Jordânia (3x1)!</small>
    </div>
    """, unsafe_allow_html=True)

# --- PAINEL CENTRAL ---
st.markdown("<h1 style='text-align: center; margin-top: -20px;'>CHAVEAMENTO OFICIAL - FIFA WORLD CUP 2026</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #aaa;'>Estrutura idêntica à imagem oficial. Clique ou arraste para avançar as seleções.</p>", unsafe_allow_html=True)

# HTML/JS Estruturado idêntico ao posicionamento das bandeiras de 23985.jpg
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
        }
        .bracket-container {
            display: flex;
            gap: 15px;
            align-items: center;
            background: #111;
            padding: 20px;
            border-radius: 15px;
            border: 1px solid #ffd70022;
            width: 100%;
            overflow-x: auto;
            justify-content: space-between;
        }
        .column {
            display: flex;
            flex-direction: column;
            justify-content: space-around;
            height: 950px;
            min-width: 150px;
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
            gap: 8px;
            padding: 6px 8px;
            background: #252525;
            border-radius: 4px;
            cursor: grab;
            transition: all 0.2s;
            user-select: none;
            font-size: 0.78rem;
            font-weight: 600;
        }
        .team:hover {
            background: #ffd70022;
            border-color: #ffd700;
        }
        .target {
            border: 1px dashed #ffd70055;
            background: #151515;
            min-height: 32px;
            border-radius: 4px;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 0.75rem;
            color: #555;
        }
        .title-stage {
            text-align: center;
            font-family: 'Bebas Neue', sans-serif;
            color: #ffd700;
            font-size: 1.1rem;
            margin-bottom: 5px;
        }
    </style>
</head>
<body>

<div class="bracket-container">
    
    <!-- LADO ESQUERDO: 1/16 AVOS -->
    <div class="column">
        <div class="title-stage">1/16 AVOS</div>
        <div class="matchup">
            <div class="team" draggable="true" ondragstart="drag(event)" id="le1" onclick="advance('le1', 'o_le1')">🇩🇪 Alemanha</div>
            <div class="team" draggable="true" ondragstart="drag(event)" id="le2" onclick="advance('le2', 'o_le1')">🇵🇾 Paraguai</div>
        </div>
        <div class="matchup">
            <div class="team" draggable="true" ondragstart="drag(event)" id="le3" onclick="advance('le3', 'o_le2')">🇳🇱 Holanda</div>
            <div class="team" draggable="true" ondragstart="drag(event)" id="le4" onclick="advance('le4', 'o_le2')">🇲🇦 Marrocos</div>
        </div>
        <div class="matchup">
            <div class="team" draggable="true" ondragstart="drag(event)" id="le5" onclick="advance('le5', 'o_le3')">🇿🇦 África do Sul</div>
            <div class="team" draggable="true" ondragstart="drag(event)" id="le6" onclick="advance('le6', 'o_le3')">🇨🇦 Canadá</div>
        </div>
        <div class="matchup">
            <div class="team" draggable="true" ondragstart="drag(event)" id="le7" onclick="advance('le7', 'o_le4')">🇨🇮 C. do Marfim</div>
            <div class="team" draggable="true" ondragstart="drag(event)" id="le8" onclick="advance('le8', 'o_le4')">🇳🇴 Noruega</div>
        </div>
        <div class="matchup">
            <div class="team" draggable="true" ondragstart="drag(event)" id="le9" onclick="advance('le9', 'o_le5')">🇵🇹 Portugal</div>
            <div class="team" draggable="true" ondragstart="drag(event)" id="le10" onclick="advance('le10', 'o_le5')">🇭🇷 Croácia</div>
        </div>
        <div class="matchup">
            <div class="team" draggable="true" ondragstart="drag(event)" id="le11" onclick="advance('le11', 'o_le6')">🇪🇸 Espanha</div>
            <div class="team" draggable="true" ondragstart="drag(event)" id="le12" onclick="advance('le12', 'o_le6')">🇦🇹 Áustria</div>
        </div>
        <div class="matchup">
            <div class="team" draggable="true" ondragstart="drag(event)" id="le13" onclick="advance('le13', 'o_le7')">🇺🇸 Estados Unidos</div>
            <div class="team" draggable="true" ondragstart="drag(event)" id="le14" onclick="advance('le14', 'o_le7')">🇧🇦 Bósnia</div>
        </div>
        <div class="matchup">
            <div class="team" draggable="true" ondragstart="drag(event)" id="le15" onclick="advance('le15', 'o_le8')">🇧🇪 Bélgica</div>
            <div class="team" draggable="true" ondragstart="drag(event)" id="le16" onclick="advance('le16', 'o_le8')">🇸🇳 Senegal</div>
        </div>
    </div>

    <!-- LADO ESQUERDO: OITAVAS -->
    <div class="column">
        <div class="title-stage">OITAVAS</div>
        <div class="matchup">
            <div class="target team" id="o_le1" ondrop="drop(event)" ondragover="allowDrop(event)" draggable="true" ondragstart="drag(event)" onclick="advance(this.id, 'q_le1')">?</div>
            <div class="target team" id="o_le2" ondrop="drop(event)" ondragover="allowDrop(event)" draggable="true" ondragstart="drag(event)" onclick="advance(this.id, 'q_le1')">?</div>
        </div>
        <div class="matchup">
            <div class="target team" id="o_le3" ondrop="drop(event)" ondragover="allowDrop(event)" draggable="true" ondragstart="drag(event)" onclick="advance(this.id, 'q_le2')">?</div>
            <div class="target team" id="o_le4" ondrop="drop(event)" ondragover="allowDrop(event)" draggable="true" ondragstart="drag(event)" onclick="advance(this.id, 'q_le2')">?</div>
        </div>
        <div class="matchup">
            <div class="target team" id="o_le5" ondrop="drop(event)" ondragover="allowDrop(event)" draggable="true" ondragstart="drag(event)" onclick="advance(this.id, 'q_le3')">?</div>
            <div class="target team" id="o_le6" ondrop="drop(event)" ondragover="allowDrop(event)" draggable="true" ondragstart="drag(event)" onclick="advance(this.id, 'q_le3')">?</div>
        </div>
        <div class="matchup">
            <div class="target team" id="o_le7" ondrop="drop(event)" ondragover="allowDrop(event)" draggable="true" ondragstart="drag(event)" onclick="advance(this.id, 'q_le4')">?</div>
            <div class="target team" id="o_le8" ondrop="drop(event)" ondragover="allowDrop(event)" draggable="true" ondragstart="drag(event)" onclick="advance(this.id, 'q_le4')">?</div>
        </div>
    </div>

    <!-- LADO ESQUERDO: QUARTAS -->
    <div class="column">
        <div class="title-stage">QUARTAS</div>
        <div class="matchup">
            <div class="target team" id="q_le1" ondrop="drop(event)" ondragover="allowDrop(event)" draggable="true" ondragstart="drag(event)" onclick="advance(this.id, 'sf_le')">?</div>
            <div class="target team" id="q_le2" ondrop="drop(event)" ondragover="allowDrop(event)" draggable="true" ondragstart="drag(event)" onclick="advance(this.id, 'sf_le')">?</div>
        </div>
        <div class="matchup">
            <div class="target team" id="q_le3" ondrop="drop(event)" ondragover="allowDrop(event)" draggable="true" ondragstart="drag(event)" onclick="advance(this.id, 'sf_le2')">?</div>
            <div class="target team" id="q_le4" ondrop="drop(event)" ondragover="allowDrop(event)" draggable="true" ondragstart="drag(event)" onclick="advance(this.id, 'sf_le2')">?</div>
        </div>
    </div>

    <!-- PAINEL CENTRAL: SEMIFINAIS, FINAL, BRONZE E CAMPEÃO -->
    <div class="column" style="min-width: 180px;">
        <div class="title-stage">SEMIFINAL</div>
        <div class="matchup">
            <div class="target team" id="sf_le" ondrop="drop(event)" ondragover="allowDrop(event)" draggable="true" ondragstart="drag(event)" onclick="advance(this.id, 'f_1')">?</div>
            <div class="target team" id="sf_le2" ondrop="drop(event)" ondragover="allowDrop(event)" draggable="true" ondragstart="drag(event)" onclick="advance(this.id, 'f_1')">?</div>
        </div>
        
        <div style="margin: 20px 0; text-align: center;">
            <div class="title-stage" style="color: #ffd700; font-size: 1.3rem;">WORLD CHAMPION</div>
            <div class="matchup" style="border: 2px solid #ffd700; background: #000;">
                <div class="target" id="champion" ondrop="drop(event)" ondragover="allowDrop(event)" style="height: 50px; font-weight: bold; color: #ffd700;">?</div>
            </div>
        </div>

        <div style="text-align: center; margin-bottom: 20px;">
            <div style="font-size: 0.7rem; color: #aaa; text-transform: uppercase;">Bronze Final</div>
            <div class="matchup" style="flex-direction: row; gap: 10px;">
                <div class="target" id="b1" ondrop="drop(event)" ondragover="allowDrop(event)" style="width: 50%;">?</div>
                <div class="target" id="b2" ondrop="drop(event)" ondragover="allowDrop(event)" style="width: 50%;">?</div>
            </div>
        </div>

        <div class="matchup">
            <div class="target team" id="sf_ld" ondrop="drop(event)" ondragover="allowDrop(event)" draggable="true" ondragstart="drag(event)" onclick="advance(this.id, 'f_2')">?</div>
            <div class="target team" id="sf_ld2" ondrop="drop(event)" ondragover="allowDrop(event)" draggable="true" ondragstart="drag(event)" onclick="advance(this.id, 'f_2')">?</div>
        </div>
    </div>

    <!-- LADO DIREITO: QUARTAS -->
    <div class="column">
        <div class="title-stage">QUARTAS</div>
        <div class="matchup">
            <div class="target team" id="q_ld1" ondrop="drop(event)" ondragover="allowDrop(event)" draggable="true" ondragstart="drag(event)" onclick="advance(this.id, 'sf_ld')">?</div>
            <div class="target team" id="q_ld2" ondrop="drop(event)" ondragover="allowDrop(event)" draggable="true" ondragstart="drag(event)" onclick="advance(this.id, 'sf_ld')">?</div>
        </div>
        <div class="matchup">
            <div class="target team" id="q_ld3" ondrop="drop(event)" ondragover="allowDrop(event)" draggable="true" ondragstart="drag(event)" onclick="advance(this.id, 'sf_ld2')">?</div>
            <div class="target team" id="q_ld4" ondrop="drop(event)" ondragover="allowDrop(event)" draggable="true" ondragstart="drag(event)" onclick="advance(this.id, 'sf_ld2')">?</div>
        </div>
    </div>

    <!-- LADO DIREITO: OITAVAS -->
    <div class="column">
        <div class="title-stage">OITAVAS</div>
        <div class="matchup">
            <div class="target team" id="o_ld1" ondrop="drop(event)" ondragover="allowDrop(event)" draggable="true" ondragstart="drag(event)" onclick="advance(this.id, 'q_ld1')">?</div>
            <div class="target team" id="o_ld2" ondrop="drop(event)" ondragover="allowDrop(event)" draggable="true" ondragstart="drag(event)" onclick="advance(this.id, 'q_ld1')">?</div>
        </div>
        <div class="matchup">
            <div class="target team" id="o_ld3" ondrop="drop(event)" ondragover="allowDrop(event)" draggable="true" ondragstart="drag(event)" onclick="advance(this.id, 'q_ld2')">?</div>
            <div class="target team" id="o_ld4" ondrop="drop(event)" ondragover="allowDrop(event)" draggable="true" ondragstart="drag(event)" onclick="advance(this.id, 'q_ld2')">?</div>
        </div>
        <div class="matchup">
            <div class="target team" id="o_ld5" ondrop="drop(event)" ondragover="allowDrop(event)" draggable="true" ondragstart="drag(event)" onclick="advance(this.id, 'q_ld3')">?</div>
            <div class="target team" id="o_ld6" ondrop="drop(event)" ondragover="allowDrop(event)" draggable="true" ondragstart="drag(event)" onclick="advance(this.id, 'q_ld3')">?</div>
        </div>
        <div class="matchup">
            <div class="target team" id="o_ld7" ondrop="drop(event)" ondragover="allowDrop(event)" draggable="true" ondragstart="drag(event)" onclick="advance(this.id, 'q_ld4')">?</div>
            <div class="target team" id="o_ld8" ondrop="drop(event)" ondragover="allowDrop(event)" draggable="true" ondragstart="drag(event)" onclick="advance(this.id, 'q_ld4')">?</div>
        </div>
    </div>

    <!-- LADO DIREITO: 1/16 AVOS -->
    <div class="column">
        <div class="title-stage">1/16 AVOS</div>
        <div class="matchup">
            <div class="team" draggable="true" ondragstart="drag(event)" id="ld1" onclick="advance('ld1', 'o_ld1')">🇧🇷 Brasil</div>
            <div class="team" draggable="true" ondragstart="drag(event)" id="ld2" onclick="advance('ld2', 'o_ld1')">🇯🇵 Japão</div>
        </div>
        <div class="matchup">
            <div class="team" draggable="true" ondragstart="drag(event)" id="ld3" onclick="advance('ld3', 'o_ld2')">🇮🇪 Irlanda</div>
            <div class="team" draggable="true" ondragstart="drag(event)" id="ld4" onclick="advance('ld4', 'o_ld2')">🏴󠁧󠁢󠁥󠁮󠁧󠁿 Inglaterra</div>
        </div>
        <div class="matchup">
            <div class="team" draggable="true" ondragstart="drag(event)" id="ld5" onclick="advance('ld5', 'o_ld3')">🇲🇽 México</div>
            <div class="team" draggable="true" ondragstart="drag(event)" id="ld6" onclick="advance('ld6', 'o_ld3')">🇪🇨 Equador</div>
        </div>
        <div class="matchup">
            <div class="team" draggable="true" ondragstart="drag(event)" id="ld7" onclick="advance('ld7', 'o_ld4')">🇨🇴 Colômbia</div>
            <div class="team" draggable="true" ondragstart="drag(event)" id="ld8" onclick="advance('ld8', 'o_ld4')">🇬🇭 Gana</div>
        </div>
        <div class="matchup">
            <div class="team" draggable="true" ondragstart="drag(event)" id="ld9" onclick="advance('ld9', 'o_ld5')">🇦🇷 Argentina</div>
            <div class="team" draggable="true" ondragstart="drag(event)" id="ld10" onclick="advance('ld10', 'o_ld5')">🇨🇻 Cabo Verde</div>
        </div>
        <div class="matchup">
            <div class="team" draggable="true" ondragstart="drag(event)" id="ld11" onclick="advance('ld11', 'o_ld6')">🇦🇺 Austrália</div>
            <div class="team" draggable="true" ondragstart="drag(event)" id="ld12" onclick="advance('ld12', 'o_ld6')">🇪🇬 Egito</div>
        </div>
        <div class="matchup">
            <div class="team" draggable="true" ondragstart="drag(event)" id="ld13" onclick="advance('ld13', 'o_ld7')">🇨🇭 Suíça</div>
            <div class="team" draggable="true" ondragstart="drag(event)" id="ld14" onclick="advance('ld14', 'o_ld7')">🇩🇿 Argélia</div>
        </div>
        <div class="matchup">
            <div class="team" draggable="true" ondragstart="drag(event)" id="ld15" onclick="advance('ld15', 'o_ld8')">🇫🇷 França</div>
            <div class="team" draggable="true" ondragstart="drag(event)" id="ld16" onclick="advance('ld16', 'o_ld8')">🇸🇪 Suécia</div>
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
        
        if (draggedEl) {
            var content = draggedEl.textContent || draggedEl.innerText;
            if (content.trim() !== "?" && content.trim() !== "") {
                ev.target.innerHTML = content;
                ev.target.style.background = "#2a2a2a";
                ev.target.style.borderColor = "#ffd700";
            }
        }
    }

    // Suporta o clique simples para avançar para a caixa de destino mapeada
    function advance(sourceId, targetId) {
        var sourceEl = document.getElementById(sourceId);
        var targetEl = document.getElementById(targetId);
        if(sourceEl && targetEl) {
            var content = sourceEl.textContent || sourceEl.innerText;
            if(content.trim() !== "?" && content.trim() !== "") {
                targetEl.innerHTML = content;
                targetEl.style.background = "#2a2a2a";
                targetEl.style.borderColor = "#ffd700";
            }
        }
    }
</script>

</body>
</html>
"""

components.html(bracket_html, height=980, scrolling=True)
st.info("Chaveamento totalmente alinhado com o print 23985.jpg!")
