import streamlit as st
import streamlit.components.v1 as components
import json

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

def get_group_qualifiers():
    """Returns dict: group -> [1st, 2nd] team codes"""
    q = {}
    for gkey in GROUPS:
        s = compute_standings(gkey)
        q[gkey] = [s[0]["code"] if len(s)>0 else None,
                   s[1]["code"] if len(s)>1 else None]
    return q

def get_team_info():
    """Returns flat dict: code -> {name, flag}"""
    info = {}
    for g in GROUPS.values():
        for t in g["teams"]:
            info[t["code"]] = {"name": t["name"], "flag": t["flag"]}
    return info

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
# HEADER
# ══════════════════════════════════════════════════════════════════════════════

st.markdown("""
<div class="wc-header">
  <h1>🏆 FIFA WORLD CUP 2026</h1>
  <p>Tabela Interativa · USA · Canadá · México · Horários de Brasília (BRT)</p>
</div>
""", unsafe_allow_html=True)

tab1, tab2, tab3 = st.tabs([
    "⚽ Fase de Grupos",
    "✏️ Inserir Resultados",
    "🏆 Bracket Mata-Mata"
])

# ══════════════════════════════════════════════════════════════════════════════
# TAB 1 — CLASSIFICAÇÃO
# ══════════════════════════════════════════════════════════════════════════════
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
                  <td class="fl"><span style="font-size:.7rem;opacity:.7;font-family:monospace;">{t['code'].lower()}</span> {t['name']}</td>
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

# ══════════════════════════════════════════════════════════════════════════════
# TAB 2 — INSERIR RESULTADOS
# ══════════════════════════════════════════════════════════════════════════════
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
            hg = st.number_input("Casa", 0, 30, ex[0], key=f"h_{key}", label_visibility="collapsed")
        with c2:
            st.markdown("<div style='text-align:center;padding-top:6px;color:#FFD700;font-weight:900;font-size:1.3rem'>×</div>", unsafe_allow_html=True)
        with c3:
            ag = st.number_input("Fora", 0, 30, ex[1], key=f"a_{key}", label_visibility="collapsed")
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

# ══════════════════════════════════════════════════════════════════════════════
# TAB 3 — BRACKET (estilo GE Globo)
# ══════════════════════════════════════════════════════════════════════════════
with tab3:

    # Compute qualifiers from group results
    qualifiers = get_group_qualifiers()
    team_info  = get_team_info()

    # Serialize to JSON to pass into JS
    qual_json = json.dumps(qualifiers)
    info_json = json.dumps(team_info)

    BRACKET_HTML = f"""<!DOCTYPE html>
<html lang="pt-BR">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<style>
*{{box-sizing:border-box;margin:0;padding:0;}}
body{{
  background:radial-gradient(ellipse at 20% 0%,#0d2a6e 0%,#061030 55%,#020810 100%);
  color:#fff;font-family:'Segoe UI',system-ui,sans-serif;
  min-height:100vh;padding:14px 6px 40px;
  user-select:none;
}}

/* ── PAGE TITLE ── */
.title{{text-align:center;margin-bottom:12px;}}
.title h1{{
  font-size:1.6rem;font-weight:900;letter-spacing:.08em;
  background:linear-gradient(90deg,#FFD700,#fff 50%,#FFD700);
  -webkit-background-clip:text;-webkit-text-fill-color:transparent;
}}
.title p{{font-size:.65rem;color:#5a80b0;letter-spacing:.12em;margin-top:2px;}}
.info-bar{{
  background:rgba(0,150,255,.07);border:1px solid rgba(0,150,255,.2);
  border-radius:8px;padding:6px 12px;font-size:.68rem;color:#7ab0e0;
  text-align:center;margin-bottom:14px;
}}

/* ── PHASE TITLE ── */
.ph{{
  text-align:center;font-weight:900;font-size:.8rem;letter-spacing:.14em;
  color:#FFD700;text-transform:uppercase;margin:16px 0 8px;
  display:flex;align-items:center;gap:8px;justify-content:center;
}}
.ph::before,.ph::after{{content:'';flex:1;height:1px;
  background:linear-gradient(90deg,transparent,rgba(255,215,0,.3),transparent);}}

/* ── AVOS GRID ── */
.avos-grid{{
  display:grid;
  grid-template-columns:repeat(4,1fr);
  gap:8px;max-width:980px;margin:0 auto 4px;
}}
@media(max-width:700px){{.avos-grid{{grid-template-columns:repeat(2,1fr);}}}}

.avo-card{{
  background:rgba(255,255,255,.045);
  border:1px solid rgba(255,255,255,.09);
  border-radius:10px;padding:8px 6px;
  display:flex;flex-direction:column;align-items:center;gap:5px;
}}
.avo-vs{{display:flex;align-items:center;gap:8px;justify-content:center;}}
.match-lbl{{
  font-size:.58rem;font-weight:900;color:#FFD700;
  letter-spacing:.1em;text-align:center;
}}
.match-meta{{font-size:.48rem;color:#4a6280;text-align:center;line-height:1.4;}}
.win-lbl{{font-size:.44rem;color:#3a5060;margin-top:1px;}}

/* ── FLAG CIRCLE ── */
.fc{{
  width:52px;height:52px;border-radius:50%;
  background:radial-gradient(circle at 35% 30%,rgba(255,255,255,.2),rgba(0,10,40,.75));
  border:2.5px solid rgba(255,255,255,.4);
  box-shadow:0 3px 14px rgba(0,0,0,.55),inset 0 1px 3px rgba(255,255,255,.15);
  display:flex;align-items:center;justify-content:center;
  font-size:1.6rem;cursor:grab;
  transition:transform .14s,box-shadow .14s,border-color .14s;
  position:relative;flex-shrink:0;
}}
.fc:hover{{
  transform:scale(1.12);border-color:rgba(255,215,0,.75);
  box-shadow:0 6px 22px rgba(255,215,0,.38);
}}
.fc.dragging{{opacity:.55;transform:scale(.92);}}
.fc .fn{{
  position:absolute;bottom:-15px;left:50%;transform:translateX(-50%);
  font-size:.42rem;font-weight:700;color:#b8cce0;
  white-space:nowrap;pointer-events:none;
  text-shadow:0 1px 3px rgba(0,0,0,.9);
}}

/* ── DROP SLOT ── */
.ds{{
  width:52px;height:52px;border-radius:50%;
  border:2px dashed rgba(255,255,255,.2);
  background:rgba(0,0,0,.35);
  display:flex;align-items:center;justify-content:center;
  font-size:.48rem;color:rgba(255,255,255,.18);
  transition:all .17s;position:relative;flex-shrink:0;
}}
.ds.over{{
  border-color:#FFD700;border-style:solid;
  background:rgba(255,215,0,.1);
  box-shadow:0 0 14px rgba(255,215,0,.3);
  color:#FFD700;font-size:.85rem;
}}
.ds.filled{{
  border-style:solid;border-color:rgba(255,255,255,.45);
  background:radial-gradient(circle at 35% 30%,rgba(255,255,255,.2),rgba(0,10,40,.75));
  font-size:1.6rem;cursor:grab;
}}
.ds.filled:hover{{border-color:rgba(255,215,0,.65);box-shadow:0 3px 14px rgba(255,215,0,.28);}}
.ds .sl{{
  position:absolute;bottom:-15px;left:50%;transform:translateX(-50%);
  font-size:.42rem;font-weight:700;color:#5a7890;
  white-space:nowrap;pointer-events:none;text-shadow:0 1px 2px rgba(0,0,0,.9);
}}
.ds .del{{
  position:absolute;top:-5px;right:-5px;
  background:#c0392b;color:#fff;border:none;border-radius:50%;
  width:15px;height:15px;font-size:.48rem;font-weight:900;
  cursor:pointer;display:flex;align-items:center;justify-content:center;
  z-index:20;padding:0;box-shadow:0 1px 4px rgba(0,0,0,.6);
}}

/* ── KO CARD ── */
.ko-grid{{
  display:flex;flex-wrap:wrap;justify-content:center;
  gap:10px;max-width:980px;margin:0 auto;
}}
.ko-card{{
  background:rgba(255,255,255,.04);
  border:1px solid rgba(255,255,255,.09);
  border-radius:10px;padding:10px 8px;
  display:flex;flex-direction:column;align-items:center;gap:6px;
  min-width:122px;
}}
.ko-card.gold{{background:rgba(255,215,0,.065);border-color:rgba(255,215,0,.35);}}
.ko-card.silver{{border-color:rgba(160,190,210,.3);}}
.avail{{
  display:flex;gap:4px;justify-content:center;flex-wrap:wrap;
  margin-top:2px;border-top:1px solid rgba(255,255,255,.06);
  padding-top:5px;width:100%;min-height:14px;
}}
.avail-lbl{{font-size:.4rem;color:#3a5060;width:100%;text-align:center;margin-bottom:1px;}}

/* ── BRACKET GE STYLE ── */
.ge-wrap{{
  max-width:1200px;margin:0 auto;overflow-x:auto;padding:10px 0 20px;
}}
.ge-bracket{{
  display:flex;align-items:center;justify-content:center;
  gap:0;min-width:700px;
}}
.ge-side{{
  display:flex;align-items:center;gap:0;
}}
.ge-col{{
  display:flex;flex-direction:column;
  align-items:center;gap:0;
  position:relative;
}}
.ge-col-label{{
  font-size:.52rem;font-weight:900;letter-spacing:.1em;
  color:rgba(255,215,0,.65);text-transform:uppercase;
  text-align:center;margin-bottom:5px;
}}

/* ── TROPHY CENTER ── */
.trophy-center{{
  display:flex;flex-direction:column;align-items:center;
  justify-content:center;padding:0 12px;flex:0 0 140px;
}}
.trophy-icon{{
  font-size:4rem;filter:drop-shadow(0 0 22px rgba(255,215,0,.7));
  animation:float 3s ease-in-out infinite;
}}
@keyframes float{{0%,100%{{transform:translateY(0);}}50%{{transform:translateY(-7px);}}}}
.trophy-title{{
  font-size:.75rem;font-weight:900;color:#FFD700;
  letter-spacing:.1em;text-align:center;margin-top:5px;
}}
.trophy-sub{{font-size:.5rem;color:#4a6080;text-align:center;margin-top:2px;}}

/* champ banner */
.champ-banner{{
  text-align:center;margin:14px auto 0;max-width:300px;
  background:linear-gradient(135deg,rgba(255,215,0,.14),rgba(255,215,0,.03));
  border:2px solid #FFD700;border-radius:14px;padding:1rem;
}}
.champ-banner h2{{font-size:1.2rem;font-weight:900;color:#FFD700;letter-spacing:.07em;}}

/* reset */
.reset-btn{{
  display:block;margin:20px auto 0;
  background:rgba(200,50,50,.14);border:1px solid rgba(200,50,50,.4);
  color:#e07070;border-radius:8px;padding:8px 22px;cursor:pointer;
  font-weight:700;font-size:.78rem;transition:all .17s;
}}
.reset-btn:hover{{background:rgba(200,50,50,.28);color:#fff;}}

/* connector lines between phases inside bracket */
.conn-v{{width:2px;background:rgba(100,200,120,.45);}}
.conn-h{{height:2px;background:rgba(100,200,120,.45);}}
</style>
</head>
<body>

<div class="title">
  <h1>WORLD CUP 2026 · BRACKET</h1>
  <p>ARRASTE AS BANDEIRAS FASE A FASE · HORÁRIOS BRASÍLIA (BRT)</p>
</div>
<div class="info-bar">
  🖱️ <b>Arraste</b> a bandeira do vencedor para o próximo slot &nbsp;·&nbsp;
  <b>✕</b> para remover &nbsp;·&nbsp;
  Bandeiras dos classificados <b>aparecem automaticamente</b> nos 16 Avos
</div>

<!-- ══════ 16 AVOS ══════ -->
<div class="ph">⚔️ 16 AVOS DE FINAL</div>
<div class="avos-grid" id="avos-grid"></div>

<!-- ══════ OITAVAS ══════ -->
<div class="ph">🔵 OITAVAS DE FINAL</div>
<div class="ko-grid" id="oitavas-grid"></div>

<!-- ══════ QUARTAS ══════ -->
<div class="ph">🟡 QUARTAS DE FINAL</div>
<div class="ko-grid" id="quartas-grid"></div>

<!-- ══════ SEMI + FINAL (estilo GE) ══════ -->
<div class="ph">🏆 SEMIFINAL · FINAL · 3° LUGAR</div>

<div class="ge-wrap">
<div class="ge-bracket" id="ge-bracket">

  <!-- SEMI LEFT -->
  <div style="display:flex;flex-direction:column;align-items:flex-end;gap:30px;flex:1;padding-right:6px;" id="semi-left-col">
    <!-- SF1 slots filled by JS -->
  </div>

  <!-- CONNECTOR LEFT SVG -->
  <svg id="svg-left" width="80" height="220" style="flex:0 0 80px;overflow:visible;">
    <line x1="0" y1="55"  x2="40" y2="55"  stroke="rgba(100,200,120,.45)" stroke-width="2"/>
    <line x1="0" y1="165" x2="40" y2="165" stroke="rgba(100,200,120,.45)" stroke-width="2"/>
    <line x1="40" y1="55"  x2="40" y2="165" stroke="rgba(100,200,120,.45)" stroke-width="2"/>
    <line x1="40" y1="110" x2="80" y2="110" stroke="rgba(100,200,120,.45)" stroke-width="2"/>
  </svg>

  <!-- CENTER COLUMN -->
  <div style="display:flex;flex-direction:column;align-items:center;gap:8px;flex:0 0 150px;">
    <!-- Final slot A -->
    <div style="display:flex;flex-direction:column;align-items:center;gap:3px;">
      <div style="font-size:.5rem;color:#5a7090;">Venc. SF1</div>
      <div id="fin_A" class="ds" style="width:58px;height:58px;font-size:1.7rem;" data-slot="FIN_A">
        <span class="sl">SF1</span>
      </div>
    </div>
    <!-- Trophy -->
    <div class="trophy-center" style="flex:0 0 auto;padding:6px 0;">
      <div class="trophy-icon">🏆</div>
      <div class="trophy-title">FINAL</div>
      <div class="trophy-sub">19/07 · 16h · New York</div>
      <!-- champion slot -->
      <div style="margin-top:7px;display:flex;flex-direction:column;align-items:center;gap:3px;">
        <div style="font-size:.48rem;color:#4a6080;">👑 Campeão:</div>
        <div id="fin_champ" class="ds" style="width:64px;height:64px;font-size:2rem;" data-slot="CHAMP">
          <span class="sl">Arraste</span>
        </div>
        <div id="champ-name" style="font-size:.58rem;color:#FFD700;font-weight:900;min-height:12px;text-align:center;"></div>
      </div>
    </div>
    <!-- Final slot B -->
    <div style="display:flex;flex-direction:column;align-items:center;gap:3px;">
      <div id="fin_B" class="ds" style="width:58px;height:58px;font-size:1.7rem;" data-slot="FIN_B">
        <span class="sl">SF2</span>
      </div>
      <div style="font-size:.5rem;color:#5a7090;">Venc. SF2</div>
    </div>
  </div>

  <!-- CONNECTOR RIGHT SVG -->
  <svg id="svg-right" width="80" height="220" style="flex:0 0 80px;overflow:visible;">
    <line x1="80" y1="55"  x2="40" y2="55"  stroke="rgba(100,200,120,.45)" stroke-width="2"/>
    <line x1="80" y1="165" x2="40" y2="165" stroke="rgba(100,200,120,.45)" stroke-width="2"/>
    <line x1="40" y1="55"  x2="40" y2="165" stroke="rgba(100,200,120,.45)" stroke-width="2"/>
    <line x1="40" y1="110" x2="0"  y2="110" stroke="rgba(100,200,120,.45)" stroke-width="2"/>
  </svg>

  <!-- SEMI RIGHT -->
  <div style="display:flex;flex-direction:column;align-items:flex-start;gap:30px;flex:1;padding-left:6px;" id="semi-right-col">
    <!-- SF2 slots filled by JS -->
  </div>

</div><!-- /ge-bracket -->
</div><!-- /ge-wrap -->

<!-- Available chips for final -->
<div id="final-avail" style="display:flex;gap:10px;justify-content:center;flex-wrap:wrap;
     margin:6px auto 12px;max-width:300px;min-height:18px;"></div>

<!-- 3rd place -->
<div class="ph" style="color:#a0b8c8;">🥉 DISPUTA DE 3° LUGAR — 18/07 · 18h · Miami</div>
<div class="ko-grid" id="terceiro-grid"></div>

<!-- Champion banner -->
<div id="champ-banner" class="champ-banner" style="display:none;">
  <div style="font-size:3rem;" id="cb-flag"></div>
  <h2>🏆 CAMPEÃO MUNDIAL 2026</h2>
  <div id="cb-name" style="font-size:1rem;font-weight:700;color:#fff;margin-top:3px;"></div>
</div>

<button class="reset-btn" onclick="resetAll()">🗑️ Resetar Bracket</button>

<script>
// ── QUALIFIERS FROM PYTHON ────────────────────────────────────────────────
const QUAL = {qual_json};   // {{A:[code1,code2], B:[...], ...}}
const TINFO = {info_json};  // {{code:{{name,flag}}, ...}}

// All 48 teams
const T = {{}};
Object.keys(TINFO).forEach(c => {{ T[c] = {{n:TINFO[c].name, f:TINFO[c].flag}}; }});
const team = c => T[c] || {{n:c||'?', f:'🏳️'}};

// ── AVOS OFFICIAL STRUCTURE ──────────────────────────────────────────────
// Each avo: hSlot = which group pos fills left, aSlot = which fills right
// Format: [group, pos] where pos=0→1st, pos=1→2nd
const AVOS = [
  {{id:"AV01",n:1, date:"28/06",time:"16:00",venue:"Los Angeles",   hSlot:["A",1],aSlot:["B",1],label:"2°A × 2°B"}},
  {{id:"AV02",n:2, date:"29/06",time:"14:00",venue:"Houston",       hSlot:["C",0],aSlot:["F",1],label:"1°C × 2°F"}},
  {{id:"AV03",n:3, date:"29/06",time:"17:30",venue:"Boston",        hSlot:["E",0],aSlot:null,   label:"1°E × 3°ABCDF"}},
  {{id:"AV04",n:4, date:"29/06",time:"22:00",venue:"Monterrey",     hSlot:["F",0],aSlot:["C",1],label:"1°F × 2°C"}},
  {{id:"AV05",n:5, date:"30/06",time:"14:00",venue:"Toronto",       hSlot:["E",1],aSlot:["I",1],label:"2°E × 2°I"}},
  {{id:"AV06",n:6, date:"30/06",time:"18:00",venue:"New York",      hSlot:["I",0],aSlot:null,   label:"1°I × 3°CDFGH"}},
  {{id:"AV07",n:7, date:"30/06",time:"22:00",venue:"Seattle",       hSlot:["A",0],aSlot:null,   label:"1°A × 3°CEFHI"}},
  {{id:"AV08",n:8, date:"01/07",time:"13:00",venue:"Atlanta",       hSlot:["L",0],aSlot:null,   label:"1°L × 3°EHIJK"}},
  {{id:"AV09",n:9, date:"01/07",time:"17:00",venue:"Dallas",        hSlot:["G",0],aSlot:null,   label:"1°G × 3°AEHIJ"}},
  {{id:"AV10",n:10,date:"01/07",time:"21:00",venue:"São Francisco", hSlot:["D",0],aSlot:null,   label:"1°D × 3°BEFIJ"}},
  {{id:"AV11",n:11,date:"02/07",time:"16:00",venue:"Los Angeles",   hSlot:["H",0],aSlot:["J",1],label:"1°H × 2°J"}},
  {{id:"AV12",n:12,date:"02/07",time:"20:00",venue:"Philadelphia",  hSlot:["K",1],aSlot:["L",1],label:"2°K × 2°L"}},
  {{id:"AV13",n:13,date:"03/07",time:"00:00",venue:"Vancouver",     hSlot:["B",0],aSlot:null,   label:"1°B × 3°EFGIJ"}},
  {{id:"AV14",n:14,date:"03/07",time:"15:00",venue:"Dallas",        hSlot:["D",1],aSlot:["G",1],label:"2°D × 2°G"}},
  {{id:"AV15",n:15,date:"03/07",time:"19:00",venue:"Miami",         hSlot:["J",0],aSlot:["H",1],label:"1°J × 2°H"}},
  {{id:"AV16",n:16,date:"03/07",time:"22:30",venue:"Kansas City",   hSlot:["K",0],aSlot:null,   label:"1°K × 3°DEIJL"}},
];

const OITAVAS = [
  {{id:"OT01",n:1,date:"04/07",time:"14:00",venue:"Houston",     fromA:"AV01",fromB:"AV04",label:"Venc. J1 × Venc. J4"}},
  {{id:"OT02",n:2,date:"04/07",time:"18:00",venue:"Philadelphia",fromA:"AV03",fromB:"AV06",label:"Venc. J3 × Venc. J6"}},
  {{id:"OT03",n:3,date:"05/07",time:"17:00",venue:"New York",    fromA:"AV02",fromB:"AV05",label:"Venc. J2 × Venc. J5"}},
  {{id:"OT04",n:4,date:"05/07",time:"21:00",venue:"Los Angeles", fromA:"AV07",fromB:"AV08",label:"Venc. J7 × Venc. J8"}},
  {{id:"OT05",n:5,date:"06/07",time:"16:00",venue:"Dallas",      fromA:"AV12",fromB:"AV11",label:"Venc. J12 × Venc. J11"}},
  {{id:"OT06",n:6,date:"06/07",time:"21:00",venue:"Seattle",     fromA:"AV10",fromB:"AV09",label:"Venc. J10 × Venc. J9"}},
  {{id:"OT07",n:7,date:"07/07",time:"13:00",venue:"Atlanta",     fromA:"AV15",fromB:"AV14",label:"Venc. J15 × Venc. J14"}},
  {{id:"OT08",n:8,date:"07/07",time:"17:00",venue:"Vancouver",   fromA:"AV13",fromB:"AV16",label:"Venc. J13 × Venc. J16"}},
];

const QUARTAS = [
  {{id:"QF01",n:1,date:"09/07",time:"17:00",venue:"Boston",     fromA:"OT02",fromB:"OT01",label:"Venc. O2 × Venc. O1"}},
  {{id:"QF02",n:2,date:"10/07",time:"16:00",venue:"Los Angeles",fromA:"OT05",fromB:"OT06",label:"Venc. O5 × Venc. O6"}},
  {{id:"QF03",n:3,date:"11/07",time:"18:00",venue:"Miami",      fromA:"OT03",fromB:"OT04",label:"Venc. O3 × Venc. O4"}},
  {{id:"QF04",n:4,date:"11/07",time:"22:00",venue:"Kansas City",fromA:"OT07",fromB:"OT08",label:"Venc. O7 × Venc. O8"}},
];

const SEMIS = [
  {{id:"SF01",n:1,date:"14/07",time:"16:00",venue:"New York",fromA:"QF01",fromB:"QF02",label:"Venc. QF1 × Venc. QF2"}},
  {{id:"SF02",n:2,date:"15/07",time:"16:00",venue:"Dallas",  fromA:"QF03",fromB:"QF04",label:"Venc. QF3 × Venc. QF4"}},
];

// ── STATE ─────────────────────────────────────────────────────────────────
let slots = {{}};
let dragging = null;

// ── MAKE FLAG CIRCLE ──────────────────────────────────────────────────────
function mkFC(code, size=52, draggable=true) {{
  const t = team(code);
  const d = document.createElement('div');
  d.className = 'fc';
  d.style.width = d.style.height = size+'px';
  d.style.fontSize = (size*0.58)+'px';
  d.innerHTML = t.f + `<span class="fn">${{t.n}}</span>`;
  if(draggable) {{
    d.draggable = true;
    d.addEventListener('dragstart', e => {{
      dragging = code; e.dataTransfer.setData('text', code);
      setTimeout(()=>d.classList.add('dragging'),0);
    }});
    d.addEventListener('dragend', ()=>d.classList.remove('dragging'));
  }}
  return d;
}}

// ── MAKE DROP SLOT ────────────────────────────────────────────────────────
function mkDS(slotId, hint, size=52, extraClass='') {{
  const d = document.createElement('div');
  d.className = 'ds ' + extraClass;
  d.style.width = d.style.height = size+'px';
  d.style.fontSize = (size*0.54)+'px';

  const refresh = () => {{
    d.innerHTML = '';
    const code = slots[slotId];
    if(code) {{
      const t = team(code);
      d.classList.add('filled');
      d.textContent = t.f;
      d.draggable = true;
      d.ondragstart = e => {{ dragging=code; e.dataTransfer.setData('text',code); }};
      const lbl = document.createElement('span');
      lbl.className='sl'; lbl.textContent=t.n; d.appendChild(lbl);
      const del = document.createElement('button');
      del.className='del'; del.textContent='✕';
      del.onclick = e => {{ e.stopPropagation(); delete slots[slotId]; refresh(); onSlotChange(); }};
      d.appendChild(del);
    }} else {{
      d.classList.remove('filled');
      d.draggable = false;
      d.innerHTML = `<span class="sl">${{hint}}</span>`;
    }}
  }};

  d.addEventListener('dragover', e => {{ e.preventDefault(); d.classList.add('over'); }});
  d.addEventListener('dragleave', ()=>d.classList.remove('over'));
  d.addEventListener('drop', e => {{
    e.preventDefault(); d.classList.remove('over');
    const code = e.dataTransfer.getData('text')||dragging;
    if(code) {{ slots[slotId]=code; refresh(); onSlotChange(); }}
  }});

  refresh();
  return {{ el:d, refresh }};
}}

// ── WIRE EXISTING SLOT (for FIN_A, FIN_B, CHAMP) ─────────────────────────
function wireSlot(elId, slotId, hint, size=58) {{
  const el = document.getElementById(elId);
  if(!el) return;
  el.style.width = el.style.height = size+'px';
  el.style.fontSize = (size*0.54)+'px';

  const refresh = () => {{
    el.innerHTML = '';
    const code = slots[slotId];
    if(code) {{
      const t = team(code);
      el.classList.add('filled'); el.classList.remove('ds');
      el.textContent = t.f; el.draggable=true;
      el.ondragstart = e => {{ dragging=code; e.dataTransfer.setData('text',code); }};
      const lbl=document.createElement('span'); lbl.className='sl'; lbl.textContent=t.n; el.appendChild(lbl);
      const del=document.createElement('button'); del.className='del'; del.textContent='✕';
      del.onclick=e=>{{ e.stopPropagation(); delete slots[slotId]; refresh(); onSlotChange(); }};
      el.appendChild(del);
      if(slotId==='CHAMP') showChamp(code);
    }} else {{
      el.classList.remove('filled'); el.classList.add('ds');
      el.draggable=false; el.innerHTML=`<span class="sl">${{hint}}</span>`;
      if(slotId==='CHAMP') {{ document.getElementById('champ-banner').style.display='none'; }}
    }}
  }};

  el.addEventListener('dragover',e=>{{e.preventDefault();el.classList.add('over');}});
  el.addEventListener('dragleave',()=>el.classList.remove('over'));
  el.addEventListener('drop',e=>{{
    e.preventDefault();el.classList.remove('over');
    const code=e.dataTransfer.getData('text')||dragging;
    if(code){{slots[slotId]=code;refresh();onSlotChange();}}
  }});
  refresh();
}}

function showChamp(code) {{
  const t = team(code);
  document.getElementById('cb-flag').textContent = t.f;
  document.getElementById('cb-name').textContent = t.n;
  document.getElementById('champ-name').textContent = t.n;
  document.getElementById('champ-banner').style.display = 'block';
}}

// ── BUILD AVOS ────────────────────────────────────────────────────────────
function buildAvos() {{
  const grid = document.getElementById('avos-grid');
  grid.innerHTML = '';

  AVOS.forEach(m => {{
    const card = document.createElement('div');
    card.className = 'avo-card';

    // get auto codes from qualifiers
    let hCode = null, aCode = null;
    if(m.hSlot) {{ const [g,p]=m.hSlot; hCode = QUAL[g]?.[p]||null; }}
    if(m.aSlot) {{ const [g,p]=m.aSlot; aCode = QUAL[g]?.[p]||null; }}

    card.innerHTML = `
      <div class="match-lbl">JOGO ${{String(m.n).padStart(2,'0')}}</div>
      <div class="match-meta">${{m.date}} · ${{m.time}} BRT<br>${{m.venue}}</div>
      <div style="font-size:.43rem;color:#2a4050;margin-bottom:1px;">${{m.label}}</div>`;

    const vs = document.createElement('div');
    vs.className = 'avo-vs';

    // home side
    const hWrap = document.createElement('div');
    hWrap.style.cssText = 'display:flex;flex-direction:column;align-items:center;gap:3px;';
    if(hCode) {{
      hWrap.appendChild(mkFC(hCode, 44));
    }} else {{
      const ph = document.createElement('div');
      ph.className='ds'; ph.style.width=ph.style.height='44px';
      ph.style.fontSize='1.3rem';
      ph.innerHTML=`<span class="sl">${{m.hSlot?m.hSlot[1]===0?'1°'+m.hSlot[0]:'2°'+m.hSlot[0]:'?'}}</span>`;
      hWrap.appendChild(ph);
    }}
    vs.appendChild(hWrap);

    const xEl = document.createElement('span');
    xEl.style.cssText='color:rgba(255,255,255,.18);font-weight:900;font-size:.75rem;';
    xEl.textContent='×'; vs.appendChild(xEl);

    // away side
    const aWrap = document.createElement('div');
    aWrap.style.cssText='display:flex;flex-direction:column;align-items:center;gap:3px;';
    if(aCode) {{
      aWrap.appendChild(mkFC(aCode, 44));
    }} else {{
      const ph=document.createElement('div');
      ph.className='ds'; ph.style.width=ph.style.height='44px'; ph.style.fontSize='1.3rem';
      ph.innerHTML=`<span class="sl">${{m.aSlot?m.aSlot[1]===0?'1°'+m.aSlot[0]:'2°'+m.aSlot[0]:'3°'}}</span>`;
      aWrap.appendChild(ph);
    }}
    vs.appendChild(aWrap);
    card.appendChild(vs);

    // winner slot
    const wl=document.createElement('div'); wl.className='win-lbl'; wl.textContent='↓ Arraste o vencedor';
    card.appendChild(wl);
    const ws=mkDS(`${{m.id}}_W`,'Venc.',42);
    // if only one team and no away, auto-populate not needed - user drags
    card.appendChild(ws.el);
    grid.appendChild(card);
  }});
}}

// ── BUILD KO PHASE ────────────────────────────────────────────────────────
function buildKO(containerId, matches, label, cardClass='') {{
  const grid=document.getElementById(containerId);
  grid.innerHTML='';
  matches.forEach(m=>{{
    const card=document.createElement('div');
    card.className='ko-card '+cardClass;
    card.innerHTML=`
      <div class="match-lbl">${{label}} ${{m.n}}</div>
      <div class="match-meta">${{m.date}} · ${{m.time}} BRT<br>${{m.venue}}</div>
      <div style="font-size:.43rem;color:#2a4050;">${{m.label}}</div>`;

    const sA=mkDS(`${{m.id}}_A`,'Lado A',46);
    card.appendChild(sA.el);
    const x=document.createElement('div');
    x.style.cssText='color:rgba(255,255,255,.16);font-weight:900;font-size:.65rem;';
    x.textContent='×'; card.appendChild(x);
    const sB=mkDS(`${{m.id}}_B`,'Lado B',46);
    card.appendChild(sB.el);

    // available chips
    const avDiv=document.createElement('div');
    avDiv.className='avail'; avDiv.id=`avail_${{m.id}}`;
    card.appendChild(avDiv);

    const wl=document.createElement('div');
    wl.className='win-lbl'; wl.textContent='↓ Vencedor avança';
    card.appendChild(wl);
    const ws=mkDS(`${{m.id}}_W`,'Venc.',42);
    card.appendChild(ws.el);
    grid.appendChild(card);
  }});
}}

// ── BUILD SEMIS (left/right columns in GE style) ──────────────────────────
function buildSemis() {{
  // SF01 → left col (top + bottom slots)
  const lCol=document.getElementById('semi-left-col');
  lCol.innerHTML='';
  [['SF01','A','QF01'],['SF01','B','QF02']].forEach(([sfId,side,src])=>{{
    const wrap=document.createElement('div');
    wrap.style.cssText='display:flex;flex-direction:column;align-items:center;gap:3px;';
    const lbl=document.createElement('div');
    lbl.style.cssText='font-size:.48rem;color:#5a7090;text-align:center;';
    lbl.textContent=side==='A'?'Venc. QF1':'Venc. QF2';
    wrap.appendChild(lbl);
    const s=mkDS(`SF01_${{side}}`,'→',46);
    wrap.appendChild(s.el);
    const avail=document.createElement('div');
    avail.className='avail'; avail.id=`avail_SF01_${{side}}`;
    wrap.appendChild(avail);
    lCol.appendChild(wrap);
  }});
  // SF01 winner label
  const wl1=document.createElement('div');
  wl1.style.cssText='font-size:.45rem;color:#3a5060;text-align:center;width:100%;';
  wl1.textContent='↑ Arraste vencedor para Final';
  lCol.appendChild(wl1);
  const ws1=mkDS('SF01_W','Venc.',42);
  lCol.appendChild(ws1.el);

  // SF02 → right col
  const rCol=document.getElementById('semi-right-col');
  rCol.innerHTML='';
  [['SF02','A','QF03'],['SF02','B','QF04']].forEach(([sfId,side,src])=>{{
    const wrap=document.createElement('div');
    wrap.style.cssText='display:flex;flex-direction:column;align-items:center;gap:3px;';
    const lbl=document.createElement('div');
    lbl.style.cssText='font-size:.48rem;color:#5a7090;text-align:center;';
    lbl.textContent=side==='A'?'Venc. QF3':'Venc. QF4';
    wrap.appendChild(lbl);
    const s=mkDS(`SF02_${{side}}`,'→',46);
    wrap.appendChild(s.el);
    const avail=document.createElement('div');
    avail.className='avail'; avail.id=`avail_SF02_${{side}}`;
    wrap.appendChild(avail);
    rCol.appendChild(wrap);
  }});
  const wl2=document.createElement('div');
  wl2.style.cssText='font-size:.45rem;color:#3a5060;text-align:center;width:100%;';
  wl2.textContent='↑ Arraste vencedor para Final';
  rCol.appendChild(wl2);
  const ws2=mkDS('SF02_W','Venc.',42);
  rCol.appendChild(ws2.el);
}}

// ── BUILD 3° LUGAR ────────────────────────────────────────────────────────
function buildTerceiro() {{
  const grid=document.getElementById('terceiro-grid');
  grid.innerHTML='';
  const card=document.createElement('div');
  card.className='ko-card silver';
  card.innerHTML=`
    <div class="match-lbl" style="color:#a0b8c8;">3° LUGAR</div>
    <div class="match-meta">18/07 · 18:00 BRT · Miami</div>
    <div style="font-size:.43rem;color:#2a4050;">Perd. SF1 × Perd. SF2</div>`;
  const sA=mkDS('3PL_A','Perd.SF1',46,'silver');
  card.appendChild(sA.el);
  const x=document.createElement('div');
  x.style.cssText='color:rgba(255,255,255,.16);font-weight:900;font-size:.65rem;';
  x.textContent='×'; card.appendChild(x);
  const sB=mkDS('3PL_B','Perd.SF2',46,'silver');
  card.appendChild(sB.el);
  const avail=document.createElement('div');
  avail.className='avail'; avail.id='avail_3PL'; card.appendChild(avail);
  const ws=mkDS('3PL_W','🥉',44,'silver');
  const wl=document.createElement('div');
  wl.className='win-lbl'; wl.style.color='#7a9ab8'; wl.textContent='3° Lugar:';
  card.appendChild(wl);
  card.appendChild(ws.el);
  grid.appendChild(card);
}}

// ── REFRESH AVAILABLE CHIPS ────────────────────────────────────────────────
function refreshAvail(elId, srcs) {{
  const el=document.getElementById(elId);
  if(!el) return;
  el.innerHTML='';
  const codes=[];
  srcs.forEach(slotId=>{{
    const c=slots[slotId]; if(c && !codes.includes(c)) codes.push(c);
  }});
  if(codes.length) {{
    const lbl=document.createElement('div');
    lbl.className='avail-lbl'; lbl.textContent='↑ Disponíveis:'; el.appendChild(lbl);
    codes.forEach(c=>{{ el.appendChild(mkFC(c,34,true)); }});
  }}
}}

function onSlotChange() {{
  // Oitavas availables from Avos winners
  OITAVAS.forEach(m=>{{
    refreshAvail(`avail_${{m.id}}`,[`${{m.fromA}}_W`,`${{m.fromB}}_W`]);
  }});
  // Quartas availables from Oitavas winners
  QUARTAS.forEach(m=>{{
    refreshAvail(`avail_${{m.id}}`,[`${{m.fromA}}_W`,`${{m.fromB}}_W`]);
  }});
  // Semis availables
  SEMIS.forEach(m=>{{
    refreshAvail(`avail_${{m.id}}_A`,[`${{m.fromA}}_W`]);
    refreshAvail(`avail_${{m.id}}_B`,[`${{m.fromB}}_W`]);
  }});
  // Final availables (SF winners)
  const favail=document.getElementById('final-avail');
  if(favail){{
    favail.innerHTML='';
    ['SF01_W','SF02_W'].forEach(sid=>{{
      const c=slots[sid];
      if(c){{
        const wrap=document.createElement('div');
        wrap.style.cssText='display:flex;flex-direction:column;align-items:center;gap:2px;';
        wrap.appendChild(mkFC(c,40,true));
        const l=document.createElement('span');
        l.style.cssText='font-size:.4rem;color:#4a7090;';
        l.textContent='↑ Arraste para Final';
        wrap.appendChild(l);
        favail.appendChild(wrap);
      }}
    }});
  }}
  // 3rd place: show losers of semis (teams in SF slots not chosen as winner)
  const e3=document.getElementById('avail_3PL');
  if(e3){{
    e3.innerHTML='';
    const losers=[];
    ['SF01','SF02'].forEach(sf=>{{
      const w=slots[`${{sf}}_W`];
      ['A','B'].forEach(side=>{{
        const c=slots[`${{sf}}_${{side}}`];
        if(c && c!==w) losers.push(c);
      }});
    }});
    if(losers.length){{
      const l=document.createElement('div'); l.className='avail-lbl';
      l.textContent='Perdedores SF:'; e3.appendChild(l);
      losers.forEach(c=>e3.appendChild(mkFC(c,34,true)));
    }}
  }}
  // Champ slot refresh via wireSlot mechanism (handled by refresh closures)
  document.getElementById('champ-name').textContent =
    slots['CHAMP'] ? team(slots['CHAMP']).n : '';
}}

function resetAll(){{
  if(!confirm('Resetar todo o bracket?')) return;
  slots={{}};
  buildAvos();
  buildKO('oitavas-grid',OITAVAS,'OITAVAS');
  buildKO('quartas-grid',QUARTAS,'QUARTAS','gold');
  buildSemis();
  buildTerceiro();
  wireSlot('fin_A','FIN_A','Venc. SF1',58);
  wireSlot('fin_B','FIN_B','Venc. SF2',58);
  wireSlot('fin_champ','CHAMP','👑 Campeão',64);
  document.getElementById('champ-banner').style.display='none';
  onSlotChange();
}}

// ── INIT ──────────────────────────────────────────────────────────────────
buildAvos();
buildKO('oitavas-grid',OITAVAS,'OITAVAS');
buildKO('quartas-grid',QUARTAS,'QUARTAS','gold');
buildSemis();
buildTerceiro();
wireSlot('fin_A','FIN_A','Venc. SF1',58);
wireSlot('fin_B','FIN_B','Venc. SF2',58);
wireSlot('fin_champ','CHAMP','👑 Campeão',64);
onSlotChange();
</script>
</body>
</html>"""

    components.html(BRACKET_HTML, height=5200, scrolling=True)
