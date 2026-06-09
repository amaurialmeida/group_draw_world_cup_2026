import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="FIFA World Cup 2026",
    page_icon="🏆",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ══════════════════════════════════════════════════════════════════════════════
# DADOS DOS GRUPOS
# ══════════════════════════════════════════════════════════════════════════════

GROUPS = {
    "A": {
        "teams": [
            {"code":"MEX","name":"México","flag":"🇲🇽"},
            {"code":"RSA","name":"África do Sul","flag":"🇿🇦"},
            {"code":"KOR","name":"Coreia do Sul","flag":"🇰🇷"},
            {"code":"CZE","name":"Tchéquia","flag":"🇨🇿"},
        ],
        "matches": [
            {"id":"A1","home":"MEX","away":"RSA","date":"11/06 Qua","time":"16:00","venue":"Cidade do México","tv":"SporTV/SBT/Cazé TV"},
            {"id":"A2","home":"KOR","away":"CZE","date":"11/06 Qua","time":"23:00","venue":"Guadalajara","tv":"Cazé TV"},
            {"id":"A3","home":"CZE","away":"RSA","date":"18/06 Qua","time":"13:00","venue":"Atlanta","tv":"Cazé TV"},
            {"id":"A4","home":"MEX","away":"KOR","date":"18/06 Qua","time":"22:00","venue":"Guadalajara","tv":"SporTV/Cazé TV"},
            {"id":"A5","home":"CZE","away":"MEX","date":"24/06 Ter","time":"22:00","venue":"Cidade do México","tv":"Cazé TV"},
            {"id":"A6","home":"RSA","away":"KOR","date":"24/06 Ter","time":"22:00","venue":"Monterrey","tv":"Cazé TV"},
        ]
    },
    "B": {
        "teams": [
            {"code":"CAN","name":"Canadá","flag":"🇨🇦"},
            {"code":"BIH","name":"Bósnia","flag":"🇧🇦"},
            {"code":"QAT","name":"Catar","flag":"🇶🇦"},
            {"code":"SUI","name":"Suíça","flag":"🇨🇭"},
        ],
        "matches": [
            {"id":"B1","home":"CAN","away":"BIH","date":"12/06 Qui","time":"16:00","venue":"Toronto","tv":"Cazé TV"},
            {"id":"B2","home":"QAT","away":"SUI","date":"13/06 Sex","time":"16:00","venue":"San Francisco","tv":"Cazé TV"},
            {"id":"B3","home":"SUI","away":"BIH","date":"18/06 Qua","time":"16:00","venue":"Los Angeles","tv":"SporTV/Cazé TV"},
            {"id":"B4","home":"CAN","away":"QAT","date":"18/06 Qua","time":"19:00","venue":"Vancouver","tv":"Cazé TV"},
            {"id":"B5","home":"SUI","away":"CAN","date":"24/06 Ter","time":"16:00","venue":"Vancouver","tv":"Cazé TV"},
            {"id":"B6","home":"BIH","away":"QAT","date":"24/06 Ter","time":"16:00","venue":"Seattle","tv":"Cazé TV"},
        ]
    },
    "C": {
        "teams": [
            {"code":"BRA","name":"Brasil","flag":"🇧🇷"},
            {"code":"MAR","name":"Marrocos","flag":"🇲🇦"},
            {"code":"HAI","name":"Haiti","flag":"🇭🇹"},
            {"code":"SCO","name":"Escócia","flag":"🏴󠁧󠁢󠁳󠁣󠁴󠁿"},
        ],
        "matches": [
            {"id":"C1","home":"BRA","away":"MAR","date":"13/06 Sex","time":"19:00","venue":"Los Angeles","tv":"SporTV/SBT/Cazé TV"},
            {"id":"C2","home":"HAI","away":"SCO","date":"13/06 Sex","time":"22:00","venue":"Vancouver","tv":"Cazé TV"},
            {"id":"C3","home":"SCO","away":"MAR","date":"19/06 Qui","time":"19:00","venue":"Seattle","tv":"Cazé TV"},
            {"id":"C4","home":"BRA","away":"HAI","date":"19/06 Qui","time":"21:30","venue":"San Francisco","tv":"SporTV/SBT/Cazé TV"},
            {"id":"C5","home":"SCO","away":"BRA","date":"24/06 Ter","time":"19:00","venue":"Los Angeles","tv":"SporTV/Cazé TV"},
            {"id":"C6","home":"MAR","away":"HAI","date":"24/06 Ter","time":"19:00","venue":"San Francisco","tv":"Cazé TV"},
        ]
    },
    "D": {
        "teams": [
            {"code":"USA","name":"Estados Unidos","flag":"🇺🇸"},
            {"code":"PAR","name":"Paraguai","flag":"🇵🇾"},
            {"code":"AUS","name":"Austrália","flag":"🇦🇺"},
            {"code":"TUR","name":"Turquia","flag":"🇹🇷"},
        ],
        "matches": [
            {"id":"D1","home":"USA","away":"PAR","date":"12/06 Qui","time":"22:00","venue":"Houston","tv":"SporTV/SBT/Cazé TV"},
            {"id":"D2","home":"AUS","away":"TUR","date":"14/06 Sab","time":"01:00","venue":"Philadelphia","tv":"SporTV/Cazé TV"},
            {"id":"D3","home":"USA","away":"AUS","date":"19/06 Qui","time":"16:00","venue":"Toronto","tv":"Cazé TV"},
            {"id":"D4","home":"TUR","away":"PAR","date":"20/06 Sex","time":"00:00","venue":"Kansas City","tv":"SporTV/Cazé TV"},
            {"id":"D5","home":"TUR","away":"USA","date":"25/06 Qua","time":"23:00","venue":"Philadelphia","tv":"Cazé TV"},
            {"id":"D6","home":"PAR","away":"AUS","date":"25/06 Qua","time":"23:00","venue":"New York","tv":"Cazé TV"},
        ]
    },
    "E": {
        "teams": [
            {"code":"GER","name":"Alemanha","flag":"🇩🇪"},
            {"code":"CIV","name":"Costa do Marfim","flag":"🇨🇮"},
            {"code":"CUW","name":"Curaçao","flag":"🇨🇼"},
            {"code":"ECU","name":"Equador","flag":"🇪🇨"},
        ],
        "matches": [
            {"id":"E1","home":"GER","away":"CUW","date":"14/06 Sab","time":"14:00","venue":"Dallas","tv":"Cazé TV"},
            {"id":"E2","home":"CIV","away":"ECU","date":"14/06 Sab","time":"20:00","venue":"Monterrey","tv":"SporTV/Cazé TV"},
            {"id":"E3","home":"GER","away":"CIV","date":"20/06 Sex","time":"17:00","venue":"Houston","tv":"SporTV/Cazé TV"},
            {"id":"E4","home":"ECU","away":"CUW","date":"20/06 Sex","time":"21:00","venue":"Monterrey","tv":"Cazé TV"},
            {"id":"E5","home":"CUW","away":"CIV","date":"25/06 Qua","time":"17:00","venue":"Vancouver","tv":"Cazé TV"},
            {"id":"E6","home":"ECU","away":"GER","date":"25/06 Qua","time":"17:00","venue":"Seattle","tv":"Cazé TV"},
        ]
    },
    "F": {
        "teams": [
            {"code":"NED","name":"Holanda","flag":"🇳🇱"},
            {"code":"SWE","name":"Suécia","flag":"🇸🇪"},
            {"code":"JPN","name":"Japão","flag":"🇯🇵"},
            {"code":"TUN","name":"Tunísia","flag":"🇹🇳"},
        ],
        "matches": [
            {"id":"F1","home":"NED","away":"JPN","date":"14/06 Sab","time":"17:00","venue":"Seattle","tv":"SporTV/Cazé TV"},
            {"id":"F2","home":"SWE","away":"TUN","date":"14/06 Sab","time":"23:00","venue":"Los Angeles","tv":"SporTV/Cazé TV"},
            {"id":"F3","home":"NED","away":"SWE","date":"20/06 Sex","time":"14:00","venue":"Los Angeles","tv":"Cazé TV"},
            {"id":"F4","home":"TUN","away":"JPN","date":"21/06 Sab","time":"01:00","venue":"Vancouver","tv":"SporTV/Cazé TV"},
            {"id":"F5","home":"JPN","away":"SWE","date":"25/06 Qua","time":"20:00","venue":"Kansas City","tv":"Cazé TV"},
            {"id":"F6","home":"TUN","away":"NED","date":"25/06 Qua","time":"20:00","venue":"Dallas","tv":"Cazé TV"},
        ]
    },
    "G": {
        "teams": [
            {"code":"BEL","name":"Bélgica","flag":"🇧🇪"},
            {"code":"IRN","name":"Irã","flag":"🇮🇷"},
            {"code":"EGY","name":"Egito","flag":"🇪🇬"},
            {"code":"NZL","name":"Nova Zelândia","flag":"🇳🇿"},
        ],
        "matches": [
            {"id":"G1","home":"BEL","away":"EGY","date":"15/06 Dom","time":"16:00","venue":"Atlanta","tv":"SporTV/Cazé TV"},
            {"id":"G2","home":"IRN","away":"NZL","date":"15/06 Dom","time":"22:00","venue":"Miami","tv":"Cazé TV"},
            {"id":"G3","home":"BEL","away":"IRN","date":"21/06 Sab","time":"16:00","venue":"Atlanta","tv":"Cazé TV"},
            {"id":"G4","home":"NZL","away":"EGY","date":"21/06 Sab","time":"22:00","venue":"Miami","tv":"SporTV/Cazé TV"},
            {"id":"G5","home":"EGY","away":"IRN","date":"27/06 Sab","time":"00:00","venue":"Houston","tv":"Cazé TV"},
            {"id":"G6","home":"NZL","away":"BEL","date":"27/06 Sab","time":"00:00","venue":"Guadalajara","tv":"Cazé TV"},
        ]
    },
    "H": {
        "teams": [
            {"code":"ESP","name":"Espanha","flag":"🇪🇸"},
            {"code":"KSA","name":"Arábia Saudita","flag":"🇸🇦"},
            {"code":"CPV","name":"Cabo Verde","flag":"🇨🇻"},
            {"code":"URU","name":"Uruguai","flag":"🇺🇾"},
        ],
        "matches": [
            {"id":"H1","home":"ESP","away":"CPV","date":"15/06 Dom","time":"13:00","venue":"New York","tv":"Cazé TV"},
            {"id":"H2","home":"KSA","away":"URU","date":"15/06 Dom","time":"19:00","venue":"Boston","tv":"SporTV/Cazé TV"},
            {"id":"H3","home":"ESP","away":"KSA","date":"21/06 Sab","time":"13:00","venue":"Philadelphia","tv":"Cazé TV"},
            {"id":"H4","home":"URU","away":"CPV","date":"21/06 Sab","time":"19:00","venue":"New York","tv":"SporTV/Cazé TV"},
            {"id":"H5","home":"URU","away":"ESP","date":"26/06 Sex","time":"21:00","venue":"Boston","tv":"Cazé TV"},
            {"id":"H6","home":"CPV","away":"KSA","date":"26/06 Sex","time":"21:00","venue":"Toronto","tv":"Cazé TV"},
        ]
    },
    "I": {
        "teams": [
            {"code":"FRA","name":"França","flag":"🇫🇷"},
            {"code":"SEN","name":"Senegal","flag":"🇸🇳"},
            {"code":"IRQ","name":"Iraque","flag":"🇮🇶"},
            {"code":"NOR","name":"Noruega","flag":"🇳🇴"},
        ],
        "matches": [
            {"id":"I1","home":"FRA","away":"SEN","date":"16/06 Seg","time":"16:00","venue":"Kansas City","tv":"SporTV/Cazé TV"},
            {"id":"I2","home":"IRQ","away":"NOR","date":"16/06 Seg","time":"19:00","venue":"San Francisco","tv":"Cazé TV"},
            {"id":"I3","home":"FRA","away":"IRQ","date":"22/06 Dom","time":"18:00","venue":"Dallas","tv":"Cazé TV"},
            {"id":"I4","home":"NOR","away":"SEN","date":"22/06 Dom","time":"21:00","venue":"San Francisco","tv":"SporTV/Cazé TV"},
            {"id":"I5","home":"NOR","away":"FRA","date":"26/06 Sex","time":"16:00","venue":"New York","tv":"Cazé TV"},
            {"id":"I6","home":"SEN","away":"IRQ","date":"26/06 Sex","time":"16:00","venue":"Philadelphia","tv":"Cazé TV"},
        ]
    },
    "J": {
        "teams": [
            {"code":"ARG","name":"Argentina","flag":"🇦🇷"},
            {"code":"AUT","name":"Áustria","flag":"🇦🇹"},
            {"code":"ALG","name":"Argélia","flag":"🇩🇿"},
            {"code":"JOR","name":"Jordânia","flag":"🇯🇴"},
        ],
        "matches": [
            {"id":"J1","home":"ARG","away":"ALG","date":"16/06 Seg","time":"22:00","venue":"Houston","tv":"Cazé TV"},
            {"id":"J2","home":"AUT","away":"JOR","date":"17/06 Ter","time":"01:00","venue":"Cidade do México","tv":"SporTV/Cazé TV"},
            {"id":"J3","home":"ARG","away":"AUT","date":"22/06 Dom","time":"14:00","venue":"Houston","tv":"SporTV/Cazé TV"},
            {"id":"J4","home":"JOR","away":"ALG","date":"23/06 Seg","time":"00:00","venue":"Guadalajara","tv":"SporTV/Cazé TV"},
            {"id":"J5","home":"ALG","away":"AUT","date":"27/06 Sab","time":"23:00","venue":"Miami","tv":"Cazé TV"},
            {"id":"J6","home":"JOR","away":"ARG","date":"27/06 Sab","time":"23:00","venue":"Atlanta","tv":"Cazé TV"},
        ]
    },
    "K": {
        "teams": [
            {"code":"POR","name":"Portugal","flag":"🇵🇹"},
            {"code":"UZB","name":"Uzbequistão","flag":"🇺🇿"},
            {"code":"COD","name":"RD Congo","flag":"🇨🇩"},
            {"code":"COL","name":"Colômbia","flag":"🇨🇴"},
        ],
        "matches": [
            {"id":"K1","home":"POR","away":"COD","date":"17/06 Ter","time":"14:00","venue":"Dallas","tv":"Cazé TV"},
            {"id":"K2","home":"UZB","away":"COL","date":"17/06 Ter","time":"23:00","venue":"Toronto","tv":"SporTV/Cazé TV"},
            {"id":"K3","home":"POR","away":"UZB","date":"23/06 Seg","time":"14:00","venue":"Boston","tv":"Cazé TV"},
            {"id":"K4","home":"COL","away":"COD","date":"23/06 Seg","time":"23:00","venue":"Toronto","tv":"SporTV/Cazé TV"},
            {"id":"K5","home":"COL","away":"POR","date":"27/06 Sab","time":"20:30","venue":"Kansas City","tv":"Cazé TV"},
            {"id":"K6","home":"COD","away":"UZB","date":"27/06 Sab","time":"20:30","venue":"Dallas","tv":"Cazé TV"},
        ]
    },
    "L": {
        "teams": [
            {"code":"ENG","name":"Inglaterra","flag":"🏴󠁧󠁢󠁥󠁮󠁧󠁿"},
            {"code":"GHA","name":"Gana","flag":"🇬🇭"},
            {"code":"CRO","name":"Croácia","flag":"🇭🇷"},
            {"code":"PAN","name":"Panamá","flag":"🇵🇦"},
        ],
        "matches": [
            {"id":"L1","home":"ENG","away":"CRO","date":"17/06 Ter","time":"17:00","venue":"Atlanta","tv":"SporTV/Cazé TV"},
            {"id":"L2","home":"GHA","away":"PAN","date":"17/06 Ter","time":"20:00","venue":"Guadalajara","tv":"Cazé TV"},
            {"id":"L3","home":"ENG","away":"GHA","date":"23/06 Seg","time":"17:00","venue":"Vancouver","tv":"SporTV/Cazé TV"},
            {"id":"L4","home":"PAN","away":"CRO","date":"23/06 Seg","time":"20:00","venue":"Seattle","tv":"Cazé TV"},
            {"id":"L5","home":"PAN","away":"ENG","date":"27/06 Sab","time":"18:00","venue":"Miami","tv":"Cazé TV"},
            {"id":"L6","home":"CRO","away":"GHA","date":"27/06 Sab","time":"18:00","venue":"Atlanta","tv":"Cazé TV"},
        ]
    },
}

# ══════════════════════════════════════════════════════════════════════════════
# CSS
# ══════════════════════════════════════════════════════════════════════════════

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Barlow+Condensed:wght@400;600;700;900&family=Barlow:wght@400;500;600&display=swap');
html,body,[class*="css"]{font-family:'Barlow',sans-serif;}
.stApp{background:linear-gradient(160deg,#07111f 0%,#0b1c38 50%,#060e1a 100%);color:#e8edf5;}
.wc-header{text-align:center;padding:1.5rem 1rem 1rem;
  background:linear-gradient(180deg,rgba(255,215,0,0.09) 0%,transparent 100%);
  border-bottom:1px solid rgba(255,215,0,0.18);margin-bottom:1.2rem;}
.wc-header h1{font-family:'Barlow Condensed',sans-serif;font-size:2.8rem;font-weight:900;
  letter-spacing:0.08em;color:#FFD700;text-shadow:0 0 40px rgba(255,215,0,0.4);margin:0;}
.wc-header p{color:#7a97bc;font-size:0.8rem;margin-top:4px;letter-spacing:0.15em;text-transform:uppercase;}
.group-card{background:rgba(255,255,255,0.035);border:1px solid rgba(255,255,255,0.07);
  border-radius:12px;padding:1rem;margin-bottom:1rem;}
.group-title{font-family:'Barlow Condensed',sans-serif;font-size:1.2rem;font-weight:900;
  color:#FFD700;letter-spacing:0.1em;border-bottom:1px solid rgba(255,215,0,0.18);
  padding-bottom:5px;margin-bottom:8px;}
.stbl{width:100%;border-collapse:collapse;font-size:0.8rem;}
.stbl th{color:#6a88b0;font-weight:600;text-align:center;padding:3px 4px;font-size:0.7rem;letter-spacing:0.04em;}
.stbl td{padding:4px 5px;text-align:center;border-bottom:1px solid rgba(255,255,255,0.04);}
.stbl tr:last-child td{border-bottom:none;}
.fl{text-align:left !important;font-weight:600;}
.pts{font-weight:900;color:#FFD700;}
.q1{background:rgba(0,200,100,0.1);border-left:3px solid #00c864;}
.q2{background:rgba(0,150,255,0.07);border-left:3px solid #0096ff;}
.mrow{background:rgba(0,0,0,0.18);border-radius:7px;padding:6px 9px;
  margin-bottom:5px;border:1px solid rgba(255,255,255,0.04);}
.minfo{font-size:0.7rem;color:#7a97bc;margin-bottom:3px;}
.tv-b{background:rgba(255,100,0,0.14);color:#ff9060;border-radius:4px;
  padding:1px 5px;font-size:0.62rem;font-weight:700;}
.sec-hdr{font-family:'Barlow Condensed',sans-serif;font-size:1.6rem;font-weight:900;
  color:#FFD700;letter-spacing:0.1em;text-align:center;
  padding:1rem 0 0.6rem;border-bottom:1px solid rgba(255,215,0,0.14);
  margin-bottom:1rem;text-transform:uppercase;}
</style>
""", unsafe_allow_html=True)

# ══════════════════════════════════════════════════════════════════════════════
# SESSION STATE
# ══════════════════════════════════════════════════════════════════════════════

if "scores" not in st.session_state:
    st.session_state.scores = {}

# ══════════════════════════════════════════════════════════════════════════════
# HELPERS
# ══════════════════════════════════════════════════════════════════════════════

def compute_standings(gkey):
    g = GROUPS[gkey]
    T = {t["code"]: {**t, "pts":0,"gf":0,"ga":0,"gd":0,"mp":0,"w":0,"d":0,"l":0}
         for t in g["teams"]}
    for m in g["matches"]:
        s = st.session_state.scores.get(m["id"])
        if not s: continue
        hg, ag = s
        h, a = T[m["home"]], T[m["away"]]
        h["mp"]+=1; a["mp"]+=1
        h["gf"]+=hg; h["ga"]+=ag; h["gd"]=h["gf"]-h["ga"]
        a["gf"]+=ag; a["ga"]+=hg; a["gd"]=a["gf"]-a["ga"]
        if hg > ag:   h["pts"]+=3; h["w"]+=1; a["l"]+=1
        elif hg < ag: a["pts"]+=3; a["w"]+=1; h["l"]+=1
        else:         h["pts"]+=1; a["pts"]+=1; h["d"]+=1; a["d"]+=1
    return sorted(T.values(), key=lambda x: (-x["pts"], -x["gd"], -x["gf"]))

# ══════════════════════════════════════════════════════════════════════════════
# HEADER
# ══════════════════════════════════════════════════════════════════════════════

st.markdown("""
<div class="wc-header">
  <h1>🏆 FIFA WORLD CUP 2026</h1>
  <p>Tabela Interativa · USA · Canadá · México · Horários de Brasília (BRT)</p>
</div>
""", unsafe_allow_html=True)

# ══════════════════════════════════════════════════════════════════════════════
# TABS
# ══════════════════════════════════════════════════════════════════════════════

tab1, tab2, tab3 = st.tabs([
    "⚽ Fase de Grupos",
    "✏️ Inserir Resultados",
    "🏆 Bracket Mata-Mata"
])

# ─────────────────────────────────────────────────────────────────────────────
# TAB 1 — CLASSIFICAÇÃO
# ─────────────────────────────────────────────────────────────────────────────
with tab1:
    st.markdown("<div class='sec-hdr'>Classificação por Grupo</div>", unsafe_allow_html=True)
    cols = st.columns(3)
    for gi, gkey in enumerate(GROUPS):
        with cols[gi % 3]:
            s = compute_standings(gkey)
            rows = ""
            for r, t in enumerate(s):
                cls = "q1" if r < 2 else ("q2" if r == 2 else "")
                rows += f"""<tr class="{cls}">
                  <td class="fl">{t['flag']} {t['name']}</td>
                  <td>{t['mp']}</td><td>{t['w']}</td><td>{t['d']}</td><td>{t['l']}</td>
                  <td>{t['gd']:+d}</td><td class="pts">{t['pts']}</td></tr>"""
            st.markdown(f"""
            <div class="group-card">
              <div class="group-title">⬡ GRUPO {gkey}</div>
              <table class="stbl">
                <thead><tr>
                  <th style="text-align:left">País</th>
                  <th>J</th><th>V</th><th>E</th><th>D</th><th>SG</th>
                  <th style="color:#FFD700">PTS</th>
                </tr></thead>
                <tbody>{rows}</tbody>
              </table>
              <div style="font-size:0.6rem;color:#3a5070;margin-top:5px;">
                🟢 Top 2 avançam · 🔵 Melhor 3° pode avançar
              </div>
            </div>""", unsafe_allow_html=True)

# ─────────────────────────────────────────────────────────────────────────────
# TAB 2 — RESULTADOS
# ─────────────────────────────────────────────────────────────────────────────
with tab2:
    st.markdown("<div class='sec-hdr'>Inserir Resultados – Fase de Grupos</div>", unsafe_allow_html=True)
    sel = st.selectbox("Grupo", list(GROUPS.keys()), format_func=lambda g: f"Grupo {g}")
    g = GROUPS[sel]
    tm = {t["code"]: t for t in g["teams"]}
    for m in g["matches"]:
        ht, at = tm[m["home"]], tm[m["away"]]
        key = m["id"]
        ex = st.session_state.scores.get(key, (0, 0))
        st.markdown(f"""
        <div class="mrow">
          <div class="minfo">📅 {m['date']} · ⏰ {m['time']} (BRT) · 📍 {m['venue']}
            &nbsp;<span class="tv-b">📺 {m['tv']}</span></div>
          <div style="text-align:center;font-weight:700;font-size:0.95rem;margin-bottom:4px;">
            {ht['flag']} {ht['name']} &nbsp;×&nbsp; {at['flag']} {at['name']}
          </div>
        </div>""", unsafe_allow_html=True)
        c1, c2, c3, c4 = st.columns([3, 1, 1, 3])
        with c1:
            hg = st.number_input(f"Casa", 0, 30, ex[0], key=f"h_{key}", label_visibility="collapsed")
        with c2:
            st.markdown("<div style='text-align:center;padding-top:6px;color:#FFD700;font-weight:900;font-size:1.3rem'>×</div>", unsafe_allow_html=True)
        with c3:
            ag = st.number_input(f"Fora", 0, 30, ex[1], key=f"a_{key}", label_visibility="collapsed")
        with c4:
            if st.button("✅ Salvar", key=f"sv_{key}"):
                st.session_state.scores[key] = (hg, ag)
                res = (f"{ht['flag']} {ht['name']} venceu!" if hg > ag
                       else f"{at['flag']} {at['name']} venceu!" if hg < ag
                       else "Empate!")
                st.success(f"Salvo: {hg} × {ag} — {res}")
    st.markdown("---")
    if st.button(f"🗑️ Limpar resultados do Grupo {sel}"):
        for m in g["matches"]:
            st.session_state.scores.pop(m["id"], None)
        st.rerun()

# ─────────────────────────────────────────────────────────────────────────────
# TAB 3 — BRACKET MATA-MATA (HTML visual igual ao print)
# ─────────────────────────────────────────────────────────────────────────────
with tab3:

    BRACKET_HTML = r"""
<!DOCTYPE html>
<html lang="pt-BR">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<style>
*{box-sizing:border-box;margin:0;padding:0;}
body{
  background:radial-gradient(ellipse at 20% 0%, #0d2a6e 0%, #061030 55%, #020810 100%);
  color:#fff;
  font-family:'Segoe UI',system-ui,sans-serif;
  min-height:100vh;
  padding:16px 8px 40px;
  user-select:none;
}

/* ── TITLE ── */
.title{text-align:center;margin-bottom:18px;}
.title h1{font-size:1.8rem;font-weight:900;letter-spacing:.06em;
  background:linear-gradient(90deg,#FFD700,#fff 50%,#FFD700);
  -webkit-background-clip:text;-webkit-text-fill-color:transparent;
  text-shadow:none;}
.title p{font-size:.7rem;color:#5a80b0;letter-spacing:.12em;margin-top:3px;}

/* ── INFO BOX ── */
.info{background:rgba(0,150,255,.07);border:1px solid rgba(0,150,255,.25);
  border-radius:8px;padding:7px 14px;font-size:.7rem;color:#7ab0e0;
  text-align:center;margin-bottom:16px;}

/* ── PHASE TITLE ── */
.ph-title{
  text-align:center;font-weight:900;font-size:.85rem;letter-spacing:.14em;
  color:#FFD700;text-transform:uppercase;margin:20px 0 10px;
  display:flex;align-items:center;gap:8px;justify-content:center;
}
.ph-title::before,.ph-title::after{
  content:'';flex:1;height:1px;
  background:linear-gradient(90deg,transparent,rgba(255,215,0,.3),transparent);
}

/* ── BRACKET GRID ── */
.bracket-wrap{
  display:flex;
  align-items:stretch;
  gap:0;
  width:100%;
  max-width:1100px;
  margin:0 auto;
  position:relative;
}

/* ── COLUMN ── */
.col{
  display:flex;
  flex-direction:column;
  justify-content:space-around;
  align-items:center;
  flex:1;
  position:relative;
  gap:0;
  padding:4px 2px;
}
.col-label{
  font-size:.58rem;font-weight:900;letter-spacing:.1em;color:#FFD700;
  text-align:center;margin-bottom:6px;text-transform:uppercase;
  opacity:.8;
}

/* ── MATCH PAIR (two teams + connector) ── */
.match-pair{
  display:flex;
  flex-direction:column;
  align-items:center;
  position:relative;
  width:80px;
  margin:4px 0;
}
.match-pair .line-right{
  position:absolute;right:-50%;top:50%;
  width:50%;height:2px;
  background:rgba(255,255,255,.35);
  transform:translateY(-50%);
}
.match-pair .line-left{
  position:absolute;left:-50%;top:50%;
  width:50%;height:2px;
  background:rgba(255,255,255,.35);
  transform:translateY(-50%);
}

/* ── CONNECTOR LINES (SVG overlay) ── */
.bracket-svg{
  position:absolute;top:0;left:0;width:100%;height:100%;
  pointer-events:none;overflow:visible;
}

/* ── FLAG CIRCLE ── */
.flag-circle{
  width:52px;height:52px;border-radius:50%;
  background:radial-gradient(circle at 35% 30%, rgba(255,255,255,.2), rgba(0,10,40,.7));
  border:2.5px solid rgba(255,255,255,.4);
  box-shadow:0 4px 16px rgba(0,0,0,.6),inset 0 1px 3px rgba(255,255,255,.15);
  display:flex;align-items:center;justify-content:center;
  font-size:1.65rem;
  cursor:grab;
  transition:transform .15s,box-shadow .15s,border-color .15s;
  position:relative;
  flex-shrink:0;
}
.flag-circle:hover{
  transform:scale(1.12);
  box-shadow:0 6px 24px rgba(255,215,0,.4),inset 0 1px 3px rgba(255,255,255,.2);
  border-color:rgba(255,215,0,.7);
}
.flag-circle.dragging{opacity:.6;transform:scale(.95);}
.flag-circle .fname{
  position:absolute;bottom:-16px;left:50%;transform:translateX(-50%);
  font-size:.45rem;font-weight:700;color:#c8d8f0;
  white-space:nowrap;letter-spacing:.02em;
  text-shadow:0 1px 3px rgba(0,0,0,.8);
  pointer-events:none;
}

/* ── DROP SLOT ── */
.drop-slot{
  width:52px;height:52px;border-radius:50%;
  border:2.5px dashed rgba(255,255,255,.22);
  background:rgba(0,0,0,.35);
  display:flex;align-items:center;justify-content:center;
  font-size:.5rem;color:rgba(255,255,255,.2);
  transition:all .18s;
  position:relative;
  flex-shrink:0;
}
.drop-slot.over{
  border-color:#FFD700;border-style:solid;
  background:rgba(255,215,0,.1);
  box-shadow:0 0 16px rgba(255,215,0,.35);
  color:#FFD700;font-size:.9rem;
}
.drop-slot.filled{
  border-style:solid;border-color:rgba(255,255,255,.5);
  background:radial-gradient(circle at 35% 30%,rgba(255,255,255,.2),rgba(0,10,40,.7));
  font-size:1.65rem;cursor:grab;
}
.drop-slot.filled:hover{
  border-color:rgba(255,215,0,.7);
  box-shadow:0 4px 16px rgba(255,215,0,.3);
}
.drop-slot .del{
  position:absolute;top:-5px;right:-5px;
  background:#c0392b;color:#fff;border:none;border-radius:50%;
  width:15px;height:15px;font-size:.5rem;font-weight:900;
  cursor:pointer;display:flex;align-items:center;justify-content:center;
  line-height:1;z-index:20;padding:0;
  box-shadow:0 1px 4px rgba(0,0,0,.6);
}
.slot-label{
  position:absolute;bottom:-16px;left:50%;transform:translateX(-50%);
  font-size:.45rem;font-weight:700;color:#7a9ab8;
  white-space:nowrap;pointer-events:none;
  text-shadow:0 1px 2px rgba(0,0,0,.8);
}

/* ── PAIR ROW ── two teams stacked with mid-line ── */
.pair{
  display:flex;flex-direction:column;align-items:center;
  gap:6px;position:relative;
  margin:5px 0;
}
.pair-connector{
  width:2px;height:10px;
  background:rgba(255,255,255,.3);
}
.match-label{
  font-size:.48rem;font-weight:900;color:rgba(255,215,0,.7);
  letter-spacing:.06em;text-align:center;margin-bottom:2px;
  line-height:1.1;
}
.match-meta{
  font-size:.42rem;color:rgba(100,150,180,.8);
  text-align:center;line-height:1.3;margin-bottom:3px;
}

/* ── TROPHY CENTER ── */
.trophy-col{
  display:flex;flex-direction:column;align-items:center;
  justify-content:center;padding:0 8px;
  flex:0 0 100px;
}
.trophy-img{font-size:4rem;text-align:center;
  filter:drop-shadow(0 0 20px rgba(255,215,0,.7));
  animation:float 3s ease-in-out infinite;}
@keyframes float{0%,100%{transform:translateY(0);}50%{transform:translateY(-8px);}}
.trophy-title{text-align:center;margin-top:6px;}
.trophy-title h2{
  font-size:.9rem;font-weight:900;letter-spacing:.1em;
  background:linear-gradient(90deg,#FFD700,#fff);
  -webkit-background-clip:text;-webkit-text-fill-color:transparent;
}
.trophy-title p{font-size:.52rem;color:#5a7090;letter-spacing:.08em;margin-top:1px;}

/* champion banner */
.champ-banner{
  text-align:center;margin:16px auto;max-width:320px;
  background:linear-gradient(135deg,rgba(255,215,0,.15),rgba(255,215,0,.03));
  border:2px solid #FFD700;border-radius:14px;padding:1.2rem;
}
.champ-banner h2{
  font-size:1.3rem;font-weight:900;color:#FFD700;letter-spacing:.08em;
}

/* reset */
.reset-btn{
  display:block;margin:20px auto 0;
  background:rgba(200,50,50,.15);border:1px solid rgba(200,50,50,.4);
  color:#e07070;border-radius:8px;padding:8px 22px;cursor:pointer;
  font-weight:700;font-size:.8rem;transition:all .18s;
}
.reset-btn:hover{background:rgba(200,50,50,.3);color:#fff;}

/* phase sections */
.phase-section{margin-bottom:24px;}
.avos-grid{
  display:grid;
  grid-template-columns:repeat(4,1fr);
  gap:10px;
  max-width:900px;margin:0 auto;
}
@media(max-width:700px){.avos-grid{grid-template-columns:repeat(2,1fr);}}

.avo-card{
  background:rgba(255,255,255,.04);
  border:1px solid rgba(255,255,255,.09);
  border-radius:10px;padding:8px;
  display:flex;flex-direction:column;align-items:center;gap:5px;
}
.avo-vs{
  display:flex;align-items:center;gap:8px;
  justify-content:center;
}

/* KO phases */
.ko-grid{
  display:flex;flex-wrap:wrap;justify-content:center;gap:10px;
  max-width:900px;margin:0 auto;
}
.ko-card{
  background:rgba(255,255,255,.04);
  border:1px solid rgba(255,255,255,.09);
  border-radius:10px;padding:10px;
  display:flex;flex-direction:column;align-items:center;gap:6px;
  min-width:120px;
}
.ko-card.gold{
  background:rgba(255,215,0,.07);
  border-color:rgba(255,215,0,.4);
}
.ko-card.silver{
  border-color:rgba(180,200,220,.3);
}

/* available chips below each ko card */
.avail-chips{
  display:flex;gap:5px;justify-content:center;flex-wrap:wrap;
  margin-top:2px;border-top:1px solid rgba(255,255,255,.06);
  padding-top:5px;width:100%;
}
</style>
</head>
<body>

<div class="title">
  <h1>WORLD CUP 2026 · BRACKET</h1>
  <p>ARRASTE AS BANDEIRAS FASE A FASE · HORÁRIOS BRASÍLIA (BRT)</p>
</div>

<div class="info">
  🖱️ <b>Arraste</b> a bandeira do vencedor para o slot da próxima fase &nbsp;·&nbsp;
  <b>✕</b> para remover &nbsp;·&nbsp; Bandeiras ficam ativas enquanto o time avança
</div>

<!-- ══════════════ 16 AVOS ══════════════ -->
<div class="ph-title">⚔️ 16 AVOS DE FINAL</div>
<div class="avos-grid" id="avos-grid"></div>

<!-- ══════════════ OITAVAS ══════════════ -->
<div class="ph-title">🔵 OITAVAS DE FINAL</div>
<div class="ko-grid" id="oitavas-grid"></div>

<!-- ══════════════ QUARTAS ══════════════ -->
<div class="ph-title">🟡 QUARTAS DE FINAL</div>
<div class="ko-grid" id="quartas-grid"></div>

<!-- ══════════════ SEMIFINAIS ══════════════ -->
<div class="ph-title">🔶 SEMIFINAIS</div>
<div class="ko-grid" id="semis-grid"></div>

<!-- ══════════════ BRACKET VISUAL (SEMIS → FINAL) ══════════════ -->
<div class="ph-title">🏆 FINAL — 19/07 · 16:00 BRT · New York MetLife</div>

<div style="display:flex;justify-content:center;align-items:center;gap:0;
            max-width:700px;margin:0 auto;padding:10px 0 20px;">

  <!-- LEFT: SF1 winners → Final -->
  <div style="display:flex;flex-direction:column;align-items:flex-end;gap:24px;flex:1;">
    <div style="display:flex;flex-direction:column;align-items:center;gap:4px;">
      <div class="match-label">SF1 – Lado A</div>
      <div id="fin_A" class="drop-slot" data-slot="FIN_A"><span class="slot-label">Venc. SF1</span></div>
    </div>
  </div>

  <!-- CONNECTOR LEFT -->
  <div style="display:flex;flex-direction:column;align-items:center;justify-content:center;
              height:120px;position:relative;flex:0 0 60px;">
    <svg width="60" height="120" style="overflow:visible;">
      <!-- top horizontal line to center -->
      <line x1="0" y1="28" x2="30" y2="28" stroke="rgba(255,255,255,0.4)" stroke-width="2"/>
      <!-- bottom horizontal line to center -->
      <line x1="0" y1="92" x2="30" y2="92" stroke="rgba(255,255,255,0.4)" stroke-width="2"/>
      <!-- vertical connector -->
      <line x1="30" y1="28" x2="30" y2="92" stroke="rgba(255,255,255,0.4)" stroke-width="2"/>
      <!-- line to trophy -->
      <line x1="30" y1="60" x2="60" y2="60" stroke="rgba(255,255,255,0.4)" stroke-width="2"/>
    </svg>
  </div>

  <!-- TROPHY + FINAL SLOT -->
  <div style="display:flex;flex-direction:column;align-items:center;gap:8px;flex:0 0 120px;">
    <div style="font-size:3.5rem;filter:drop-shadow(0 0 20px rgba(255,215,0,.7));
                animation:float 3s ease-in-out infinite;">🏆</div>
    <div style="font-size:.65rem;font-weight:900;color:#FFD700;letter-spacing:.1em;">FINAL</div>
    <div style="font-size:.55rem;color:#4a6080;text-align:center;">19/07 · 16h BRT<br>New York</div>
    <div id="fin_champion" class="drop-slot" style="width:60px;height:60px;font-size:2rem;"
         data-slot="CHAMP">
      <span class="slot-label">Campeão</span>
    </div>
    <div id="champ-name" style="font-size:.6rem;color:#FFD700;font-weight:900;text-align:center;min-height:14px;"></div>
  </div>

  <!-- CONNECTOR RIGHT -->
  <div style="display:flex;flex-direction:column;align-items:center;justify-content:center;
              height:120px;position:relative;flex:0 0 60px;">
    <svg width="60" height="120" style="overflow:visible;">
      <line x1="60" y1="28" x2="30" y2="28" stroke="rgba(255,255,255,0.4)" stroke-width="2"/>
      <line x1="60" y1="92" x2="30" y2="92" stroke="rgba(255,255,255,0.4)" stroke-width="2"/>
      <line x1="30" y1="28" x2="30" y2="92" stroke="rgba(255,255,255,0.4)" stroke-width="2"/>
      <line x1="30" y1="60" x2="0" y2="60" stroke="rgba(255,255,255,0.4)" stroke-width="2"/>
    </svg>
  </div>

  <!-- RIGHT: SF2 winners → Final -->
  <div style="display:flex;flex-direction:column;align-items:flex-start;gap:24px;flex:1;">
    <div style="display:flex;flex-direction:column;align-items:center;gap:4px;">
      <div class="match-label">SF2 – Lado B</div>
      <div id="fin_B" class="drop-slot" data-slot="FIN_B"><span class="slot-label">Venc. SF2</span></div>
    </div>
  </div>
</div>

<!-- Available to drag to final -->
<div id="final-avail" style="display:flex;gap:8px;justify-content:center;flex-wrap:wrap;
     margin:0 auto 10px;max-width:400px;min-height:20px;"></div>

<!-- 3rd place -->
<div class="ph-title" style="color:#a0b8c8;">🥉 DISPUTA DE 3º LUGAR — 18/07 · 18:00 BRT · Miami</div>
<div class="ko-grid" id="terceiro-grid"></div>

<!-- Champion banner -->
<div id="champ-banner" class="champ-banner" style="display:none;">
  <div style="font-size:3rem;" id="champ-flag"></div>
  <h2 id="champ-text">🏆 CAMPEÃO MUNDIAL 2026</h2>
  <div id="champ-subname" style="font-size:1rem;font-weight:700;margin-top:4px;color:#fff;"></div>
</div>

<button class="reset-btn" onclick="resetAll()">🗑️ Resetar Bracket Completo</button>

<style>@keyframes float{0%,100%{transform:translateY(0);}50%{transform:translateY(-8px);}}</style>

<script>
// ── TIMES ─────────────────────────────────────────────────────────────────
const T={
  MEX:{n:"México",f:"🇲🇽"},RSA:{n:"África do Sul",f:"🇿🇦"},KOR:{n:"Coreia do Sul",f:"🇰🇷"},CZE:{n:"Tchéquia",f:"🇨🇿"},
  CAN:{n:"Canadá",f:"🇨🇦"},BIH:{n:"Bósnia",f:"🇧🇦"},QAT:{n:"Catar",f:"🇶🇦"},SUI:{n:"Suíça",f:"🇨🇭"},
  BRA:{n:"Brasil",f:"🇧🇷"},MAR:{n:"Marrocos",f:"🇲🇦"},HAI:{n:"Haiti",f:"🇭🇹"},SCO:{n:"Escócia",f:"🏴󠁧󠁢󠁳󠁣󠁴󠁿"},
  USA:{n:"EUA",f:"🇺🇸"},PAR:{n:"Paraguai",f:"🇵🇾"},AUS:{n:"Austrália",f:"🇦🇺"},TUR:{n:"Turquia",f:"🇹🇷"},
  GER:{n:"Alemanha",f:"🇩🇪"},CIV:{n:"C.Marfim",f:"🇨🇮"},CUW:{n:"Curaçao",f:"🇨🇼"},ECU:{n:"Equador",f:"🇪🇨"},
  NED:{n:"Holanda",f:"🇳🇱"},SWE:{n:"Suécia",f:"🇸🇪"},JPN:{n:"Japão",f:"🇯🇵"},TUN:{n:"Tunísia",f:"🇹🇳"},
  BEL:{n:"Bélgica",f:"🇧🇪"},IRN:{n:"Irã",f:"🇮🇷"},EGY:{n:"Egito",f:"🇪🇬"},NZL:{n:"N.Zelândia",f:"🇳🇿"},
  ESP:{n:"Espanha",f:"🇪🇸"},KSA:{n:"Ar.Saudita",f:"🇸🇦"},CPV:{n:"Cabo Verde",f:"🇨🇻"},URU:{n:"Uruguai",f:"🇺🇾"},
  FRA:{n:"França",f:"🇫🇷"},SEN:{n:"Senegal",f:"🇸🇳"},IRQ:{n:"Iraque",f:"🇮🇶"},NOR:{n:"Noruega",f:"🇳🇴"},
  ARG:{n:"Argentina",f:"🇦🇷"},AUT:{n:"Áustria",f:"🇦🇹"},ALG:{n:"Argélia",f:"🇩🇿"},JOR:{n:"Jordânia",f:"🇯🇴"},
  POR:{n:"Portugal",f:"🇵🇹"},UZB:{n:"Uzbequistão",f:"🇺🇿"},COD:{n:"RD Congo",f:"🇨🇩"},COL:{n:"Colômbia",f:"🇨🇴"},
  ENG:{n:"Inglaterra",f:"🏴󠁧󠁢󠁥󠁮󠁧󠁿"},GHA:{n:"Gana",f:"🇬🇭"},CRO:{n:"Croácia",f:"🇭🇷"},PAN:{n:"Panamá",f:"🇵🇦"},
};

// ── ESTRUTURA OFICIAL (conforme prints) ──────────────────────────────────
const AVOS=[
  {id:"AV01",n:1, date:"28/06",time:"16:00",venue:"Los Angeles",   hc:"MEX",ac:"CAN",label:"2°A × 2°B"},
  {id:"AV02",n:2, date:"29/06",time:"14:00",venue:"Houston",       hc:"BRA",ac:"NED",label:"1°C × 2°F"},
  {id:"AV03",n:3, date:"29/06",time:"17:30",venue:"Boston",        hc:"GER",ac:"ARG",label:"1°E × 3°ABCDF"},
  {id:"AV04",n:4, date:"29/06",time:"22:00",venue:"Monterrey",     hc:"FRA",ac:"ESP",label:"1°F × 2°C"},
  {id:"AV05",n:5, date:"30/06",time:"14:00",venue:"Toronto",       hc:"ENG",ac:"POR",label:"2°E × 2°I"},
  {id:"AV06",n:6, date:"30/06",time:"18:00",venue:"New York",      hc:"URU",ac:"BEL",label:"1°I × 3°CDFGH"},
  {id:"AV07",n:7, date:"30/06",time:"22:00",venue:"Seattle",       hc:"USA",ac:"JPN",label:"1°A × 3°CEFHI"},
  {id:"AV08",n:8, date:"01/07",time:"13:00",venue:"Atlanta",       hc:"COL",ac:"CRO",label:"1°L × 3°EHIJK"},
  {id:"AV09",n:9, date:"01/07",time:"17:00",venue:"Dallas",        hc:"MAR",ac:"SUI",label:"1°G × 3°AEHIJ"},
  {id:"AV10",n:10,date:"01/07",time:"21:00",venue:"São Francisco", hc:"SEN",ac:"NOR",label:"1°D × 3°BEFIJ"},
  {id:"AV11",n:11,date:"02/07",time:"16:00",venue:"Los Angeles",   hc:"KOR",ac:"IRN",label:"1°H × 2°J"},
  {id:"AV12",n:12,date:"02/07",time:"20:00",venue:"Philadelphia",  hc:"AUS",ac:"ECU",label:"2°K × 2°L"},
  {id:"AV13",n:13,date:"03/07",time:"00:00",venue:"Vancouver",     hc:"TUR",ac:"SCO",label:"1°B × 3°EFGIJ"},
  {id:"AV14",n:14,date:"03/07",time:"15:00",venue:"Dallas",        hc:"SWE",ac:"GHA",label:"2°D × 2°G"},
  {id:"AV15",n:15,date:"03/07",time:"19:00",venue:"Miami",         hc:"PAR",ac:"CPV",label:"1°J × 2°H"},
  {id:"AV16",n:16,date:"03/07",time:"22:30",venue:"Kansas City",   hc:"CZE",ac:"ALG",label:"1°K × 3°DEIJL"},
];

// Oitavas: Venc. Jogo X vs Venc. Jogo Y (conforme print)
const OITAVAS=[
  {id:"OT01",n:1,date:"04/07",time:"14:00",venue:"Houston",     fromA:"AV01",fromB:"AV04",label:"Venc. J1 × Venc. J4"},
  {id:"OT02",n:2,date:"04/07",time:"18:00",venue:"Philadelphia",fromA:"AV03",fromB:"AV06",label:"Venc. J3 × Venc. J6"},
  {id:"OT03",n:3,date:"05/07",time:"17:00",venue:"New York",    fromA:"AV02",fromB:"AV05",label:"Venc. J2 × Venc. J5"},
  {id:"OT04",n:4,date:"05/07",time:"21:00",venue:"Los Angeles", fromA:"AV07",fromB:"AV08",label:"Venc. J7 × Venc. J8"},
  {id:"OT05",n:5,date:"06/07",time:"16:00",venue:"Dallas",      fromA:"AV12",fromB:"AV11",label:"Venc. J12 × Venc. J11"},
  {id:"OT06",n:6,date:"06/07",time:"21:00",venue:"Seattle",     fromA:"AV10",fromB:"AV09",label:"Venc. J10 × Venc. J9"},
  {id:"OT07",n:7,date:"07/07",time:"13:00",venue:"Atlanta",     fromA:"AV15",fromB:"AV14",label:"Venc. J15 × Venc. J14"},
  {id:"OT08",n:8,date:"07/07",time:"17:00",venue:"Vancouver",   fromA:"AV13",fromB:"AV16",label:"Venc. J13 × Venc. J16"},
];

// Quartas: Venc. Oitava X vs Venc. Oitava Y (conforme print)
const QUARTAS=[
  {id:"QF01",n:1,date:"09/07",time:"17:00",venue:"Boston",     fromA:"OT02",fromB:"OT01",label:"Venc. O2 × Venc. O1"},
  {id:"QF02",n:2,date:"10/07",time:"16:00",venue:"Los Angeles",fromA:"OT05",fromB:"OT06",label:"Venc. O5 × Venc. O6"},
  {id:"QF03",n:3,date:"11/07",time:"18:00",venue:"Miami",      fromA:"OT03",fromB:"OT04",label:"Venc. O3 × Venc. O4"},
  {id:"QF04",n:4,date:"11/07",time:"22:00",venue:"Kansas City",fromA:"OT07",fromB:"OT08",label:"Venc. O7 × Venc. O8"},
];

// Semifinais
const SEMIS=[
  {id:"SF01",n:1,date:"14/07",time:"16:00",venue:"New York",fromA:"QF01",fromB:"QF02",label:"Venc. QF1 × Venc. QF2"},
  {id:"SF02",n:2,date:"15/07",time:"16:00",venue:"Dallas",  fromA:"QF03",fromB:"QF04",label:"Venc. QF3 × Venc. QF4"},
];

// 3º Lugar
const TERCEIRO=[
  {id:"3PL",date:"18/07",time:"18:00",venue:"Miami",label:"Perdedor SF1 × Perdedor SF2"},
];

// ── STATE ─────────────────────────────────────────────────────────────────
let slots={}; // slotId → teamCode
let dragging=null;

// ── HELPERS ───────────────────────────────────────────────────────────────
const team=c=>T[c]||{n:c,f:"🏳️"};

function makeCircle(code,size=52,draggable=true){
  const t=team(code);
  const d=document.createElement('div');
  d.className='flag-circle';
  d.style.width=d.style.height=size+'px';
  d.style.fontSize=(size*0.6)+'px';
  d.innerHTML=t.f+`<span class="fname">${t.n}</span>`;
  if(draggable){
    d.draggable=true;
    d.addEventListener('dragstart',e=>{
      dragging=code; e.dataTransfer.setData('text',code);
      d.classList.add('dragging');
    });
    d.addEventListener('dragend',()=>d.classList.remove('dragging'));
  }
  return d;
}

function makeSlot(slotId,hint,size=52,extraClass=''){
  const d=document.createElement('div');
  d.className='drop-slot '+extraClass;
  d.dataset.slot=slotId;
  d.style.width=d.style.height=size+'px';
  d.style.fontSize=(size*0.55)+'px';

  const refresh=()=>{
    d.innerHTML='';
    const code=slots[slotId];
    if(code){
      const t=team(code);
      d.classList.add('filled');
      d.textContent=t.f;
      d.draggable=true;
      d.ondragstart=e=>{dragging=code;e.dataTransfer.setData('text',code);};
      // name label
      const lbl=document.createElement('span');
      lbl.className='slot-label'; lbl.textContent=t.n; d.appendChild(lbl);
      // delete btn
      const del=document.createElement('button');
      del.className='del'; del.textContent='✕';
      del.onclick=e=>{e.stopPropagation();delete slots[slotId];refresh();onSlotChange();};
      d.appendChild(del);
    } else {
      d.classList.remove('filled');
      d.draggable=false;
      d.innerHTML=`<span class="slot-label">${hint}</span>`;
    }
  };

  d.addEventListener('dragover',e=>{e.preventDefault();d.classList.add('over');});
  d.addEventListener('dragleave',()=>d.classList.remove('over'));
  d.addEventListener('drop',e=>{
    e.preventDefault();d.classList.remove('over');
    const code=e.dataTransfer.getData('text')||dragging;
    if(code){slots[slotId]=code;refresh();onSlotChange();}
  });

  refresh();
  return {el:d,refresh};
}

// ── BUILD AVOS ────────────────────────────────────────────────────────────
function buildAvos(){
  const grid=document.getElementById('avos-grid');
  grid.innerHTML='';
  AVOS.forEach(m=>{
    const card=document.createElement('div');
    card.className='avo-card';
    card.innerHTML=`
      <div class="match-label">JOGO ${String(m.n).padStart(2,'0')}</div>
      <div class="match-meta">${m.date} · ${m.time} BRT<br>${m.venue}</div>
      <div style="font-size:.5rem;color:#3a5568;margin-bottom:2px;">${m.label}</div>`;
    // two teams
    const vs=document.createElement('div');
    vs.className='avo-vs';
    // home
    const hDiv=document.createElement('div');
    hDiv.style.cssText='display:flex;flex-direction:column;align-items:center;gap:3px;';
    hDiv.appendChild(makeCircle(m.hc,44));
    vs.appendChild(hDiv);
    const x=document.createElement('span');
    x.style.cssText='color:rgba(255,255,255,.2);font-weight:900;font-size:.8rem;';
    x.textContent='×';
    vs.appendChild(x);
    // away
    const aDiv=document.createElement('div');
    aDiv.style.cssText='display:flex;flex-direction:column;align-items:center;gap:3px;';
    aDiv.appendChild(makeCircle(m.ac,44));
    vs.appendChild(aDiv);
    card.appendChild(vs);
    // winner slot
    const wLabel=document.createElement('div');
    wLabel.style.cssText='font-size:.45rem;color:#3a5060;margin-top:2px;';
    wLabel.textContent='↓ Arraste o vencedor';
    card.appendChild(wLabel);
    const ws=makeSlot(`${m.id}_W`,'Venc.',40);
    card.appendChild(ws.el);
    grid.appendChild(card);
  });
}

// ── BUILD KO PHASE ────────────────────────────────────────────────────────
function buildKOPhase(containerId, matches, phaseLabel, extraCardClass=''){
  const grid=document.getElementById(containerId);
  grid.innerHTML='';
  matches.forEach(m=>{
    const card=document.createElement('div');
    card.className='ko-card '+extraCardClass;
    card.innerHTML=`
      <div class="match-label">${phaseLabel} ${m.n||''}</div>
      <div class="match-meta">${m.date} · ${m.time} BRT<br>${m.venue}</div>
      <div style="font-size:.45rem;color:#3a5060;margin-bottom:2px;">${m.label}</div>`;

    // slot A
    const sA=makeSlot(`${m.id}_A`,m.fromA?'Arraste aqui':'Lado A',44);
    card.appendChild(sA.el);
    const xEl=document.createElement('div');
    xEl.style.cssText='color:rgba(255,255,255,.18);font-weight:900;font-size:.7rem;';
    xEl.textContent='×';
    card.appendChild(xEl);
    // slot B
    const sB=makeSlot(`${m.id}_B`,m.fromB?'Arraste aqui':'Lado B',44);
    card.appendChild(sB.el);

    // chips available from previous phase
    if(m.fromA||m.fromB){
      const avail=document.createElement('div');
      avail.className='avail-chips';
      avail.id=`avail_${m.id}`;
      card.appendChild(avail);
    }

    // winner slot label + slot
    const wLbl=document.createElement('div');
    wLbl.style.cssText='font-size:.45rem;color:#3a5060;margin-top:3px;';
    wLbl.textContent='↓ Vencedor avança';
    card.appendChild(wLbl);
    const ws=makeSlot(`${m.id}_W`,'Venc.',40);
    card.appendChild(ws.el);

    grid.appendChild(card);
  });
}

// ── BUILD TERCEIRO ────────────────────────────────────────────────────────
function buildTerceiro(){
  const grid=document.getElementById('terceiro-grid');
  grid.innerHTML='';
  const m=TERCEIRO[0];
  const card=document.createElement('div');
  card.className='ko-card silver';
  card.innerHTML=`
    <div class="match-label" style="color:#a0b8c8;">3° LUGAR</div>
    <div class="match-meta">${m.date} · ${m.time} BRT · ${m.venue}</div>
    <div style="font-size:.45rem;color:#3a5060;margin-bottom:2px;">${m.label}</div>`;
  const sA=makeSlot('3PL_A','Perd. SF1',44);
  card.appendChild(sA.el);
  const x=document.createElement('div');
  x.style.cssText='color:rgba(255,255,255,.18);font-weight:900;font-size:.7rem;';
  x.textContent='×';
  card.appendChild(x);
  const sB=makeSlot('3PL_B','Perd. SF2',44);
  card.appendChild(sB.el);
  // winner
  const wl=document.createElement('div');
  wl.style.cssText='font-size:.45rem;color:#3a5060;margin-top:3px;';
  wl.textContent='3° Lugar:';
  card.appendChild(wl);
  const ws=makeSlot('3PL_W','🥉',44,'silver');
  card.appendChild(ws.el);
  grid.appendChild(card);
}

// ── HOOK UP FINAL SLOTS ───────────────────────────────────────────────────
function setupFinalSlots(){
  // FIN_A, FIN_B, CHAMP are already in HTML
  // wire up drop on existing elements
  ['FIN_A','FIN_B','CHAMP'].forEach(slotId=>{
    const el=document.getElementById(
      slotId==='FIN_A'?'fin_A':slotId==='FIN_B'?'fin_B':'fin_champion'
    );
    if(!el) return;
    const refresh=()=>{
      el.innerHTML='';
      const code=slots[slotId];
      if(code){
        const t=team(code);
        el.classList.add('filled');
        el.textContent=t.f;
        el.draggable=true;
        el.ondragstart=e=>{dragging=code;e.dataTransfer.setData('text',code);};
        const lbl=document.createElement('span');
        lbl.className='slot-label'; lbl.textContent=t.n; el.appendChild(lbl);
        const del=document.createElement('button');
        del.className='del'; del.textContent='✕';
        del.onclick=e=>{e.stopPropagation();delete slots[slotId];refresh();onSlotChange();};
        el.appendChild(del);
        if(slotId==='CHAMP'){
          document.getElementById('champ-name').textContent=t.n;
          showChampBanner(code);
        }
      } else {
        el.classList.remove('filled');
        el.draggable=false;
        const hint=slotId==='FIN_A'?'Venc. SF1':slotId==='FIN_B'?'Venc. SF2':'Campeão';
        el.innerHTML=`<span class="slot-label">${hint}</span>`;
        if(slotId==='CHAMP'){
          document.getElementById('champ-name').textContent='';
          document.getElementById('champ-banner').style.display='none';
        }
      }
    };
    el.addEventListener('dragover',e=>{e.preventDefault();el.classList.add('over');});
    el.addEventListener('dragleave',()=>el.classList.remove('over'));
    el.addEventListener('drop',e=>{
      e.preventDefault();el.classList.remove('over');
      const code=e.dataTransfer.getData('text')||dragging;
      if(code){slots[slotId]=code;refresh();onSlotChange();}
    });
    refresh();
  });
}

function showChampBanner(code){
  const t=team(code);
  document.getElementById('champ-flag').textContent=t.f;
  document.getElementById('champ-subname').textContent=t.n;
  document.getElementById('champ-banner').style.display='block';
}

// ── UPDATE AVAILABLE CHIPS ────────────────────────────────────────────────
// After each slot change, refresh "available to drag" sections
function onSlotChange(){
  // For each Oitavas match, show chips from winners of the two source Avos
  OITAVAS.forEach(m=>{
    const el=document.getElementById(`avail_${m.id}`);
    if(!el) return;
    el.innerHTML='';
    [m.fromA,m.fromB].forEach(src=>{
      const code=slots[`${src}_W`];
      if(code){
        const chip=makeCircle(code,36,true);
        el.appendChild(chip);
      }
    });
    if(el.children.length>0){
      const lbl=document.createElement('div');
      lbl.style.cssText='font-size:.42rem;color:#3a5060;width:100%;text-align:center;margin-bottom:2px;';
      lbl.textContent='Disponíveis ↑';
      el.prepend(lbl);
    }
  });

  // For each Quartas match, show chips from winners of source Oitavas
  QUARTAS.forEach(m=>{
    const el=document.getElementById(`avail_${m.id}`);
    if(!el) return;
    el.innerHTML='';
    [m.fromA,m.fromB].forEach(src=>{
      const code=slots[`${src}_W`];
      if(code){
        const chip=makeCircle(code,36,true);
        el.appendChild(chip);
      }
    });
    if(el.children.length>0){
      const lbl=document.createElement('div');
      lbl.style.cssText='font-size:.42rem;color:#3a5060;width:100%;text-align:center;margin-bottom:2px;';
      lbl.textContent='Disponíveis ↑';
      el.prepend(lbl);
    }
  });

  // For each Semis match
  SEMIS.forEach(m=>{
    const el=document.getElementById(`avail_${m.id}`);
    if(!el) return;
    el.innerHTML='';
    [m.fromA,m.fromB].forEach(src=>{
      const code=slots[`${src}_W`];
      if(code){
        const chip=makeCircle(code,36,true);
        el.appendChild(chip);
      }
    });
    if(el.children.length>0){
      const lbl=document.createElement('div');
      lbl.style.cssText='font-size:.42rem;color:#3a5060;width:100%;text-align:center;margin-bottom:2px;';
      lbl.textContent='Disponíveis ↑';
      el.prepend(lbl);
    }
  });

  // Final available chips (from SF winners)
  const favail=document.getElementById('final-avail');
  if(favail){
    favail.innerHTML='';
    ['SF01','SF02'].forEach(src=>{
      const code=slots[`${src}_W`];
      if(code){
        const chip=makeCircle(code,40,true);
        const wrap=document.createElement('div');
        wrap.style.cssText='display:flex;flex-direction:column;align-items:center;gap:2px;';
        const lbl=document.createElement('span');
        lbl.style.cssText='font-size:.42rem;color:#5a8090;';
        lbl.textContent='↑ Arraste para Final';
        wrap.appendChild(chip);
        wrap.appendChild(lbl);
        favail.appendChild(wrap);
      }
    });
  }

  // 3rd place available (losers of semis = teams in SF slots that DIDN'T win)
  // We show both SF slot teams as available for 3rd place
  const tGrid=document.getElementById('terceiro-grid');
  if(tGrid){
    // just refresh avail inside terceiro card
    const el3=document.getElementById('avail_3PL');
    if(!el3){
      // create it
      const tCard=tGrid.querySelector('.ko-card');
      if(tCard){
        const avail=document.createElement('div');
        avail.className='avail-chips'; avail.id='avail_3PL';
        tCard.insertBefore(avail,tCard.querySelector('.match-label').nextSibling);
      }
    }
    const e3=document.getElementById('avail_3PL');
    if(e3){
      e3.innerHTML='';
      ['SF01','SF02'].forEach(src=>{
        ['A','B'].forEach(side=>{
          const code=slots[`${src}_${side}`];
          if(code && code!==slots[`${src}_W`]){
            const chip=makeCircle(code,34,true);
            e3.appendChild(chip);
          }
        });
      });
    }
  }
}

// ── RESET ─────────────────────────────────────────────────────────────────
function resetAll(){
  if(!confirm('Resetar todo o bracket?')) return;
  slots={};
  init();
}

// ── INIT ──────────────────────────────────────────────────────────────────
function init(){
  buildAvos();
  buildKOPhase('oitavas-grid', OITAVAS, 'OITAVAS');
  buildKOPhase('quartas-grid', QUARTAS, 'QUARTAS', 'gold');
  buildKOPhase('semis-grid',   SEMIS,   'SEMI',    'gold');
  buildTerceiro();
  setupFinalSlots();
  onSlotChange();
}

init();
</script>
</body>
</html>
"""

    components.html(BRACKET_HTML, height=5000, scrolling=True)
