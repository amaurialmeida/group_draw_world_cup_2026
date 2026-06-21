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
# TAB 3 — BRACKET CLÁSSICO (layout igual ao print 2 - chaveamento completo)
# ══════════════════════════════════════════════════════════════════════════════
with tab3:

    qualifiers = get_group_qualifiers()
    team_info  = get_team_info()
    qual_json  = json.dumps(qualifiers)
    info_json  = json.dumps(team_info)

    BRACKET_HTML = f"""<!DOCTYPE html>
<html lang="pt-BR">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<style>
*{{box-sizing:border-box;margin:0;padding:0;}}
body{{
  background:radial-gradient(ellipse at 20% 0%,#0c1f50 0%,#06122a 60%,#020810 100%);
  color:#fff;font-family:'Segoe UI',system-ui,sans-serif;
  min-height:100vh;padding:12px 4px 40px;user-select:none;
}}
.pg-title{{text-align:center;margin-bottom:10px;}}
.pg-title h1{{
  font-size:1.5rem;font-weight:900;letter-spacing:.07em;
  background:linear-gradient(90deg,#FFD700,#fff 50%,#FFD700);
  -webkit-background-clip:text;-webkit-text-fill-color:transparent;
}}
.pg-title p{{font-size:.6rem;color:#5a80b0;letter-spacing:.1em;margin-top:2px;}}
.info-bar{{background:rgba(0,150,255,.07);border:1px solid rgba(0,150,255,.2);
  border-radius:7px;padding:5px 10px;font-size:.65rem;color:#7ab0e0;
  text-align:center;margin-bottom:12px;}}

/* ── FLAG CIRCLE ── */
.fc{{
  width:46px;height:46px;border-radius:50%;
  background:radial-gradient(circle at 35% 30%,rgba(255,255,255,.22),rgba(0,5,30,.8));
  border:2.5px solid rgba(255,255,255,.4);
  box-shadow:0 3px 12px rgba(0,0,0,.6),inset 0 1px 3px rgba(255,255,255,.15);
  display:flex;align-items:center;justify-content:center;
  font-size:1.55rem;cursor:grab;
  transition:transform .13s,box-shadow .13s,border-color .13s;
  position:relative;flex-shrink:0;
}}
.fc:hover{{transform:scale(1.14);border-color:rgba(255,215,0,.75);
  box-shadow:0 5px 20px rgba(255,215,0,.38);}}
.fc.drag{{opacity:.55;transform:scale(.9);}}
.fc .fn{{position:absolute;bottom:-14px;left:50%;transform:translateX(-50%);
  font-size:.38rem;font-weight:700;color:#a8bcd0;white-space:nowrap;
  pointer-events:none;text-shadow:0 1px 3px rgba(0,0,0,.9);}}

/* ── DROP SLOT ── */
.ds{{
  width:46px;height:46px;border-radius:50%;
  border:2px dashed rgba(255,255,255,.2);
  background:rgba(0,0,0,.4);
  display:flex;align-items:center;justify-content:center;
  font-size:.42rem;color:rgba(255,255,255,.15);
  transition:all .15s;position:relative;flex-shrink:0;
}}
.ds.over{{border-color:#FFD700;border-style:solid;
  background:rgba(255,215,0,.1);box-shadow:0 0 14px rgba(255,215,0,.3);
  font-size:.8rem;color:#FFD700;}}
.ds.filled{{border-style:solid;border-color:rgba(255,255,255,.45);
  background:radial-gradient(circle at 35% 30%,rgba(255,255,255,.22),rgba(0,5,30,.8));
  font-size:1.55rem;cursor:grab;}}
.ds.filled:hover{{border-color:rgba(255,215,0,.65);box-shadow:0 3px 14px rgba(255,215,0,.28);}}
.ds .fn{{position:absolute;bottom:-14px;left:50%;transform:translateX(-50%);
  font-size:.38rem;font-weight:700;color:#a8bcd0;white-space:nowrap;
  pointer-events:none;text-shadow:0 1px 3px rgba(0,0,0,.9);}}
.ds .del{{position:absolute;top:-4px;right:-4px;
  background:#b03020;color:#fff;border:none;border-radius:50%;
  width:14px;height:14px;font-size:.45rem;font-weight:900;
  cursor:pointer;display:flex;align-items:center;justify-content:center;
  z-index:20;padding:0;}}

/* ── BRACKET MAIN LAYOUT ── */
.bracket-outer{{
  width:100%;overflow-x:auto;padding-bottom:10px;
}}
.bracket-inner{{
  display:flex;align-items:center;
  min-width:900px;max-width:1300px;
  margin:0 auto;gap:0;
  position:relative;
}}

/* left side columns */
.left-side{{
  display:flex;flex-direction:row;align-items:center;flex:1;
}}
.right-side{{
  display:flex;flex-direction:row-reverse;align-items:center;flex:1;
}}

/* column of slots */
.b-col{{
  display:flex;flex-direction:column;
  justify-content:space-around;
  position:relative;flex-shrink:0;
  padding:4px 2px;
}}
.b-col-lbl{{
  font-size:.44rem;font-weight:900;letter-spacing:.1em;
  color:rgba(255,215,0,.6);text-transform:uppercase;
  text-align:center;margin-bottom:4px;
}}

/* slot wrapper with name */
.sw{{
  display:flex;flex-direction:column;align-items:center;
  gap:0;margin:4px 0;position:relative;
}}
.sw-lbl{{font-size:.38rem;color:#3a5060;text-align:center;
  margin-top:14px;white-space:nowrap;}}

/* connector SVG between columns */
.conn{{flex-shrink:0;}}

/* center trophy */
.center{{
  display:flex;flex-direction:column;align-items:center;
  justify-content:center;flex-shrink:0;width:130px;
  gap:6px;
}}
.trophy{{font-size:3.5rem;filter:drop-shadow(0 0 18px rgba(255,215,0,.7));
  animation:fl 3s ease-in-out infinite;}}
@keyframes fl{{0%,100%{{transform:translateY(0);}}50%{{transform:translateY(-7px);}}}}
.center-lbl{{font-size:.65rem;font-weight:900;color:#FFD700;letter-spacing:.1em;}}
.center-sub{{font-size:.45rem;color:#4a6080;text-align:center;}}

/* champ slot */
.champ-slot{{
  width:60px;height:60px;border-radius:50%;
  border:2px solid #FFD700;
  background:rgba(255,215,0,.07);
  display:flex;align-items:center;justify-content:center;
  font-size:1.8rem;cursor:grab;transition:all .15s;
  position:relative;
}}
.champ-slot.over{{box-shadow:0 0 20px rgba(255,215,0,.5);}}
.champ-slot.filled{{font-size:2rem;}}
.champ-slot .fn{{position:absolute;bottom:-15px;left:50%;transform:translateX(-50%);
  font-size:.4rem;font-weight:700;color:#FFD700;white-space:nowrap;pointer-events:none;}}
.champ-slot .del{{position:absolute;top:-4px;right:-4px;
  background:#b03020;color:#fff;border:none;border-radius:50%;
  width:14px;height:14px;font-size:.45rem;font-weight:900;
  cursor:pointer;display:flex;align-items:center;justify-content:center;z-index:20;padding:0;}}

.champ-banner{{
  text-align:center;margin:14px auto 0;max-width:280px;
  background:linear-gradient(135deg,rgba(255,215,0,.14),rgba(255,215,0,.03));
  border:2px solid #FFD700;border-radius:12px;padding:.9rem;
}}
.champ-banner h2{{font-size:1.1rem;font-weight:900;color:#FFD700;letter-spacing:.07em;}}

.reset-btn{{display:block;margin:18px auto 0;
  background:rgba(180,40,40,.14);border:1px solid rgba(180,40,40,.4);
  color:#e07070;border-radius:7px;padding:7px 20px;cursor:pointer;
  font-weight:700;font-size:.75rem;}}
.reset-btn:hover{{background:rgba(180,40,40,.28);color:#fff;}}

/* phase section titles (below bracket) */
.ph{{text-align:center;font-weight:900;font-size:.75rem;letter-spacing:.13em;
  color:#FFD700;text-transform:uppercase;margin:18px 0 8px;
  display:flex;align-items:center;gap:7px;justify-content:center;}}
.ph::before,.ph::after{{content:'';flex:1;height:1px;
  background:linear-gradient(90deg,transparent,rgba(255,215,0,.3),transparent);}}

/* avos grid */
.avos-grid{{display:grid;grid-template-columns:repeat(4,1fr);
  gap:7px;max-width:940px;margin:0 auto;}}
@media(max-width:680px){{.avos-grid{{grid-template-columns:repeat(2,1fr);}}}}
.avo-card{{background:rgba(255,255,255,.04);border:1px solid rgba(255,255,255,.09);
  border-radius:9px;padding:7px 5px;
  display:flex;flex-direction:column;align-items:center;gap:5px;}}
.avo-vs{{display:flex;align-items:center;gap:7px;justify-content:center;}}
.m-lbl{{font-size:.55rem;font-weight:900;color:#FFD700;letter-spacing:.1em;}}
.m-meta{{font-size:.42rem;color:#3a5568;text-align:center;line-height:1.4;}}
.w-lbl{{font-size:.38rem;color:#2a4050;margin-top:1px;}}

/* available chips */
.avail{{display:flex;gap:4px;justify-content:center;flex-wrap:wrap;
  border-top:1px solid rgba(255,255,255,.06);padding-top:4px;width:100%;}}
.avail-lbl{{font-size:.36rem;color:#2a4050;width:100%;text-align:center;}}
</style>
</head>
<body>
<div class="pg-title">
  <h1>WORLD CUP 2026 · CHAVEAMENTO</h1>
  <p>ARRASTE AS BANDEIRAS FASE A FASE · HORÁRIOS BRASÍLIA (BRT)</p>
</div>
<div class="info-bar">
  🖱️ <b>Arraste</b> a bandeira do vencedor para o próximo slot &nbsp;·&nbsp;
  Classificados <b>aparecem automaticamente</b> nos Avos &nbsp;·&nbsp; <b>✕</b> para remover
</div>

<!-- ════════════════════════════════════════════════
     BRACKET PRINCIPAL (layout chaveamento clássico)
════════════════════════════════════════════════ -->
<div class="bracket-outer">
<div class="bracket-inner" id="bracket-inner">

  <!-- LEFT SIDE (Avos 1-8 → Oitavas 1-4 → Quartas 1-2 → SF1) -->
  <div class="left-side" id="left-side"></div>

  <!-- CENTER TROPHY + FINAL -->
  <div class="center" id="center-col">
    <div class="trophy">🏆</div>
    <div class="center-lbl">FINAL</div>
    <div class="center-sub">19/07 · 16h BRT<br>New York</div>
    <div id="fin_A" class="ds" style="width:52px;height:52px;font-size:1.6rem;"></div>
    <div style="font-size:.55rem;color:rgba(255,215,0,.4);font-weight:900;">×</div>
    <div id="fin_B" class="ds" style="width:52px;height:52px;font-size:1.6rem;"></div>
    <div style="font-size:.38rem;color:#3a5060;margin-top:4px;">👑 Campeão:</div>
    <div id="champ_slot" class="champ-slot"></div>
    <div id="champ-name" style="font-size:.45rem;color:#FFD700;font-weight:900;text-align:center;min-height:11px;margin-top:14px;"></div>
  </div>

  <!-- RIGHT SIDE (Avos 9-16 → Oitavas 5-8 → Quartas 3-4 → SF2) -->
  <div class="right-side" id="right-side"></div>

</div>
</div>

<!-- Final available chips -->
<div id="final-avail" style="display:flex;gap:8px;justify-content:center;flex-wrap:wrap;
     margin:6px auto 8px;max-width:260px;min-height:16px;"></div>

<!-- Champ banner -->
<div id="champ-banner" class="champ-banner" style="display:none;">
  <div id="cb-flag" style="font-size:2.8rem;"></div>
  <h2>🏆 CAMPEÃO MUNDIAL 2026</h2>
  <div id="cb-name" style="font-size:.9rem;font-weight:700;color:#fff;margin-top:2px;"></div>
</div>

<!-- 3rd place -->
<div class="ph" style="color:#8aa0b8;">🥉 DISPUTA DE 3° LUGAR — 18/07 · 18h · Miami</div>
<div style="display:flex;justify-content:center;margin-bottom:8px;">
  <div class="avo-card" style="min-width:160px;">
    <div class="m-lbl" style="color:#8aa0b8;">3° LUGAR</div>
    <div class="m-meta">18/07 · 18h · Miami</div>
    <div class="avo-vs">
      <div style="display:flex;flex-direction:column;align-items:center;gap:2px;">
        <div id="ds_3PL_A" class="ds"></div>
        <span style="font-size:.34rem;color:#2a4050;">Perd.SF1</span>
      </div>
      <span style="color:rgba(255,255,255,.15);font-size:.7rem;font-weight:900;">×</span>
      <div style="display:flex;flex-direction:column;align-items:center;gap:2px;">
        <div id="ds_3PL_B" class="ds"></div>
        <span style="font-size:.34rem;color:#2a4050;">Perd.SF2</span>
      </div>
    </div>
    <div id="avail_3PL" class="avail" style="min-height:12px;"></div>
    <div class="w-lbl">3° Lugar:</div>
    <div id="ds_3PL_W" class="ds"></div>
  </div>
</div>

<button class="reset-btn" onclick="resetAll()">🗑️ Resetar Chaveamento Completo</button>

<script>
// ── DATA ──────────────────────────────────────────────────────────────────
const QUAL = {qual_json};
const TINFO = {info_json};
const T = {{}};
Object.keys(TINFO).forEach(c=>{{ T[c]={{n:TINFO[c].name,f:TINFO[c].flag}}; }});
const team = c => T[c]||{{n:c||'?',f:'🏳️'}};

// AVOS: estrutura oficial (hSlot/aSlot = [grupo, posição 0=1°,1=2°,null=3°melhor])
const AVOS_LEFT = [
  {{id:"AV01",n:1, date:"28/06",time:"16:00",venue:"Los Angeles",   hS:["A",1],aS:["B",1],lbl:"2°A × 2°B"}},
  {{id:"AV02",n:2, date:"29/06",time:"14:00",venue:"Houston",       hS:["C",0],aS:["F",1],lbl:"1°C × 2°F"}},
  {{id:"AV03",n:3, date:"29/06",time:"17:30",venue:"Boston",        hS:["E",0],aS:null,   lbl:"1°E × 3°ABCDF"}},
  {{id:"AV04",n:4, date:"29/06",time:"22:00",venue:"Monterrey",     hS:["F",0],aS:["C",1],lbl:"1°F × 2°C"}},
  {{id:"AV05",n:5, date:"30/06",time:"14:00",venue:"Toronto",       hS:["E",1],aS:["I",1],lbl:"2°E × 2°I"}},
  {{id:"AV06",n:6, date:"30/06",time:"18:00",venue:"New York",      hS:["I",0],aS:["D",2],lbl:"1°I × 3°CDFGH"}},
  {{id:"AV07",n:7, date:"30/06",time:"22:00",venue:"Seattle",       hS:["A",0],aS:["G",2],lbl:"1°A × 3°CEFHI"}},
  {{id:"AV08",n:8, date:"01/07",time:"13:00",venue:"Atlanta",       hS:["L",0],aS:["H",2],lbl:"1°L × 3°EHIJK"}},
];
const AVOS_RIGHT = [
  {{id:"AV09",n:9, date:"01/07",time:"17:00",venue:"Dallas",        hS:["G",0],aS:["E",2],lbl:"1°G × 3°AEHIJ"}},
  {{id:"AV10",n:10,date:"01/07",time:"21:00",venue:"São Francisco", hS:["D",0],aS:["B",2],lbl:"1°D × 3°BEFIJ"}},
  {{id:"AV11",n:11,date:"02/07",time:"16:00",venue:"Los Angeles",   hS:["H",0],aS:["J",1],lbl:"1°H × 2°J"}},
  {{id:"AV12",n:12,date:"02/07",time:"20:00",venue:"Philadelphia",  hS:["K",1],aS:["L",1],lbl:"2°K × 2°L"}},
  {{id:"AV13",n:13,date:"03/07",time:"00:00",venue:"Vancouver",     hS:["B",0],aS:["F",2],lbl:"1°B × 3°EFGIJ"}},
  {{id:"AV14",n:14,date:"03/07",time:"15:00",venue:"Dallas",        hS:["D",1],aS:["G",1],lbl:"2°D × 2°G"}},
  {{id:"AV15",n:15,date:"03/07",time:"19:00",venue:"Miami",         hS:["J",0],aS:["H",1],lbl:"1°J × 2°H"}},
  {{id:"AV16",n:16,date:"03/07",time:"22:30",venue:"Kansas City",   hS:["K",0],aS:["C",2],lbl:"1°K × 3°DEIJL"}},
];

// Oitavas
const OIT_LEFT = [
  {{id:"OT01",n:1,date:"04/07",time:"14:00",venue:"Houston",     fA:"AV01",fB:"AV04",lbl:"Venc.J1 × Venc.J4"}},
  {{id:"OT02",n:2,date:"04/07",time:"18:00",venue:"Philadelphia",fA:"AV03",fB:"AV06",lbl:"Venc.J3 × Venc.J6"}},
  {{id:"OT03",n:3,date:"05/07",time:"17:00",venue:"New York",    fA:"AV02",fB:"AV05",lbl:"Venc.J2 × Venc.J5"}},
  {{id:"OT04",n:4,date:"05/07",time:"21:00",venue:"Los Angeles", fA:"AV07",fB:"AV08",lbl:"Venc.J7 × Venc.J8"}},
];
const OIT_RIGHT = [
  {{id:"OT05",n:5,date:"06/07",time:"16:00",venue:"Dallas",      fA:"AV12",fB:"AV11",lbl:"Venc.J12 × Venc.J11"}},
  {{id:"OT06",n:6,date:"06/07",time:"21:00",venue:"Seattle",     fA:"AV10",fB:"AV09",lbl:"Venc.J10 × Venc.J9"}},
  {{id:"OT07",n:7,date:"07/07",time:"13:00",venue:"Atlanta",     fA:"AV15",fB:"AV14",lbl:"Venc.J15 × Venc.J14"}},
  {{id:"OT08",n:8,date:"07/07",time:"17:00",venue:"Vancouver",   fA:"AV13",fB:"AV16",lbl:"Venc.J13 × Venc.J16"}},
];

// Quartas
const QF_LEFT = [
  {{id:"QF01",n:1,date:"09/07",time:"17:00",venue:"Boston",     fA:"OT02",fB:"OT01",lbl:"Venc.O2 × Venc.O1"}},
  {{id:"QF02",n:2,date:"10/07",time:"16:00",venue:"Los Angeles",fA:"OT03",fB:"OT04",lbl:"Venc.O3 × Venc.O4"}},
];
const QF_RIGHT = [
  {{id:"QF03",n:3,date:"11/07",time:"18:00",venue:"Miami",      fA:"OT05",fB:"OT06",lbl:"Venc.O5 × Venc.O6"}},
  {{id:"QF04",n:4,date:"11/07",time:"22:00",venue:"Kansas City",fA:"OT07",fB:"OT08",lbl:"Venc.O7 × Venc.O8"}},
];

// Semis
const SF_LEFT  = {{id:"SF01",fA:"QF01",fB:"QF02",date:"14/07",time:"16:00",venue:"New York"}};
const SF_RIGHT = {{id:"SF02",fA:"QF03",fB:"QF04",date:"15/07",time:"16:00",venue:"Dallas"}};

// ── STATE ─────────────────────────────────────────────────────────────────
let slots={{}};
let dragging=null;

// ── HELPERS ───────────────────────────────────────────────────────────────
function getTeamFromSlot(hS) {{
  if(!hS) return null;
  const [g,p]=hS;
  if(p===2) return null; // 3rd place best — not auto-populated (unknown)
  const arr=QUAL[g];
  if(!arr) return null;
  return arr[p]||null;
}}

function mkFC(code,size=46,drag=true) {{
  const t=team(code);
  const d=document.createElement('div');
  d.className='fc';
  d.style.width=d.style.height=size+'px';
  d.style.fontSize=(size*0.56)+'px';
  d.innerHTML=t.f+`<span class="fn">${{t.n.length>10?t.n.slice(0,9)+'…':t.n}}</span>`;
  if(drag){{
    d.draggable=true;
    d.addEventListener('dragstart',e=>{{
      dragging=code;e.dataTransfer.setData('text',code);
      setTimeout(()=>d.classList.add('drag'),0);
    }});
    d.addEventListener('dragend',()=>d.classList.remove('drag'));
  }}
  return d;
}}

function mkDS(slotId,hint,size=46,extraClass=''){{
  const d=document.createElement('div');
  d.className='ds '+extraClass;
  d.style.width=d.style.height=size+'px';
  d.style.fontSize=(size*0.52)+'px';
  const refresh=()=>{{
    d.innerHTML='';
    const code=slots[slotId];
    if(code){{
      const t=team(code);
      d.classList.add('filled');
      d.textContent=t.f;
      d.draggable=true;
      d.ondragstart=e=>{{dragging=code;e.dataTransfer.setData('text',code);}};
      const fn=document.createElement('span');fn.className='fn';fn.textContent=t.n.length>10?t.n.slice(0,9)+'…':t.n;d.appendChild(fn);
      const del=document.createElement('button');del.className='del';del.textContent='✕';
      del.onclick=e=>{{e.stopPropagation();delete slots[slotId];refresh();onSlotChange();}};
      d.appendChild(del);
    }}else{{
      d.classList.remove('filled');d.draggable=false;
      d.innerHTML=`<span style="font-size:.36rem;color:rgba(255,255,255,.15);">${{hint}}</span>`;
    }}
  }};
  d.addEventListener('dragover',e=>{{e.preventDefault();d.classList.add('over');}});
  d.addEventListener('dragleave',()=>d.classList.remove('over'));
  d.addEventListener('drop',e=>{{
    e.preventDefault();d.classList.remove('over');
    const c=e.dataTransfer.getData('text')||dragging;
    if(c){{slots[slotId]=c;refresh();onSlotChange();}}
  }});
  refresh();
  return{{el:d,refresh}};
}}

// ── WIRE EXISTING ELEMENT AS SLOT ─────────────────────────────────────────
function wireEl(elId,slotId,hint,size=52,isChamp=false){{
  const el=document.getElementById(elId);
  if(!el)return;
  el.style.width=el.style.height=size+'px';
  const refresh=()=>{{
    el.innerHTML='';
    const code=slots[slotId];
    if(code){{
      const t=team(code);
      el.classList.add('filled');el.textContent=t.f;el.draggable=true;
      el.ondragstart=e=>{{dragging=code;e.dataTransfer.setData('text',code);}};
      const fn=document.createElement('span');fn.className='fn';fn.textContent=t.n.length>10?t.n.slice(0,9)+'…':t.n;el.appendChild(fn);
      const del=document.createElement('button');del.className='del';del.textContent='✕';
      del.onclick=e=>{{e.stopPropagation();delete slots[slotId];refresh();onSlotChange();}};
      el.appendChild(del);
      if(isChamp)showChamp(code);
    }}else{{
      el.classList.remove('filled');el.draggable=false;
      if(isChamp){{document.getElementById('champ-banner').style.display='none';}}
      el.innerHTML=`<span style="font-size:.42rem;color:rgba(255,255,255,.15);">${{hint}}</span>`;
    }}
  }};
  el.addEventListener('dragover',e=>{{e.preventDefault();el.classList.add('over');}});
  el.addEventListener('dragleave',()=>el.classList.remove('over'));
  el.addEventListener('drop',e=>{{
    e.preventDefault();el.classList.remove('over');
    const c=e.dataTransfer.getData('text')||dragging;
    if(c){{slots[slotId]=c;refresh();onSlotChange();}}
  }});
  refresh();
}}

function showChamp(code){{
  const t=team(code);
  document.getElementById('cb-flag').textContent=t.f;
  document.getElementById('cb-name').textContent=t.n;
  document.getElementById('champ-name').textContent=t.n;
  document.getElementById('champ-banner').style.display='block';
}}

// ── BUILD BRACKET SIDE ────────────────────────────────────────────────────
// Each side: COL1=Avos(8 matches) → COL2=Oitavas(4) → COL3=Quartas(2) → COL4=SF(1)
// Connected by SVG lines

function buildSide(containerId, avos, oitavas, quartas, sf, isLeft){{
  const side=document.getElementById(containerId);
  side.innerHTML='';
  const dir = isLeft ? 'row' : 'row-reverse';
  side.style.cssText='display:flex;flex-direction:'+dir+';align-items:center;flex:1;';

  // ── COL 1: AVOS (8 jogos) ──
  const col1=document.createElement('div');
  col1.className='b-col';
  col1.style.cssText='display:flex;flex-direction:column;justify-content:space-around;align-items:center;gap:6px;padding:0 2px;';

  const lbl1=document.createElement('div');lbl1.className='b-col-lbl';lbl1.textContent='16 AVOS';col1.appendChild(lbl1);

  avos.forEach(m=>{{
    const hCode=getTeamFromSlot(m.hS);
    const aCode=getTeamFromSlot(m.aS);

    const card=document.createElement('div');
    card.style.cssText=`display:flex;flex-direction:column;align-items:center;gap:3px;
      background:rgba(255,255,255,.035);border:1px solid rgba(255,255,255,.07);
      border-radius:8px;padding:5px 4px;`;

    const title=document.createElement('div');
    title.style.cssText='font-size:.42rem;font-weight:900;color:rgba(255,215,0,.8);letter-spacing:.07em;';
    title.textContent=`J${{String(m.n).padStart(2,'0')}}`;
    card.appendChild(title);

    const meta=document.createElement('div');
    meta.style.cssText='font-size:.35rem;color:#3a5060;text-align:center;line-height:1.3;';
    meta.innerHTML=`${{m.date}}<br>${{m.time}} · ${{m.venue.length>12?m.venue.slice(0,11)+'…':m.venue}}`;
    card.appendChild(meta);

    const vsRow=document.createElement('div');
    vsRow.style.cssText='display:flex;align-items:center;gap:5px;';

    // home
    const hWrap=document.createElement('div');
    hWrap.style.cssText='display:flex;flex-direction:column;align-items:center;gap:1px;';
    if(hCode){{
      const fc=mkFC(hCode,38,true);hWrap.appendChild(fc);
    }}else{{
      const ph=document.createElement('div');
      ph.className='ds';ph.style.width=ph.style.height='38px';ph.style.fontSize='1.1rem';
      const hLbl=m.hS?`${{m.hS[1]===0?'1°':m.hS[1]===1?'2°':'3°'}}${{m.hS[0]}}`:'?';
      ph.innerHTML=`<span style="font-size:.32rem;color:rgba(255,255,255,.2);">${{hLbl}}</span>`;
      hWrap.appendChild(ph);
    }}
    vsRow.appendChild(hWrap);

    const x=document.createElement('span');
    x.style.cssText='color:rgba(255,255,255,.15);font-size:.6rem;font-weight:900;';x.textContent='×';
    vsRow.appendChild(x);

    // away
    const aWrap=document.createElement('div');
    aWrap.style.cssText='display:flex;flex-direction:column;align-items:center;gap:1px;';
    if(aCode){{
      const fc=mkFC(aCode,38,true);aWrap.appendChild(fc);
    }}else{{
      const ph=document.createElement('div');
      ph.className='ds';ph.style.width=ph.style.height='38px';ph.style.fontSize='1.1rem';
      const aLbl=m.aS?`${{m.aS[1]===0?'1°':m.aS[1]===1?'2°':'3°'}}${{m.aS[0]}}`:'3°';
      ph.innerHTML=`<span style="font-size:.32rem;color:rgba(255,255,255,.2);">${{aLbl}}</span>`;
      aWrap.appendChild(ph);
    }}
    vsRow.appendChild(aWrap);

    card.appendChild(vsRow);

    // winner slot
    const wl=document.createElement('div');wl.style.cssText='font-size:.32rem;color:#2a4050;';wl.textContent='↓ Venc.';
    card.appendChild(wl);
    const ws=mkDS(`${{m.id}}_W`,'',36);
    card.appendChild(ws.el);

    col1.appendChild(card);
  }});
  side.appendChild(col1);

  // SVG connector col1→col2
  side.appendChild(buildConnectorSVG(avos.length, oitavas.length, isLeft, 'rgba(255,255,255,0.3)'));

  // ── COL 2: OITAVAS ──
  const col2=document.createElement('div');
  col2.style.cssText='display:flex;flex-direction:column;justify-content:space-around;align-items:center;gap:8px;padding:0 2px;';
  const lbl2=document.createElement('div');lbl2.className='b-col-lbl';lbl2.textContent='OITAVAS';col2.appendChild(lbl2);

  oitavas.forEach(m=>{{
    const card=buildKOCard(m,'O','rgba(50,100,200,.3)');
    col2.appendChild(card);
  }});
  side.appendChild(col2);

  // SVG connector col2→col3
  side.appendChild(buildConnectorSVG(oitavas.length, quartas.length, isLeft, 'rgba(80,160,100,.4)'));

  // ── COL 3: QUARTAS ──
  const col3=document.createElement('div');
  col3.style.cssText='display:flex;flex-direction:column;justify-content:space-around;align-items:center;gap:8px;padding:0 2px;';
  const lbl3=document.createElement('div');lbl3.className='b-col-lbl';lbl3.textContent='QUARTAS';col3.appendChild(lbl3);

  quartas.forEach(m=>{{
    const card=buildKOCard(m,'QF','rgba(200,160,0,.25)');
    col3.appendChild(card);
  }});
  side.appendChild(col3);

  // SVG connector col3→col4
  side.appendChild(buildConnectorSVG(quartas.length, 1, isLeft, 'rgba(255,140,0,.45)'));

  // ── COL 4: SEMIFINAL ──
  const col4=document.createElement('div');
  col4.style.cssText='display:flex;flex-direction:column;justify-content:center;align-items:center;gap:6px;padding:0 2px;';
  const lbl4=document.createElement('div');lbl4.className='b-col-lbl';lbl4.textContent='SEMI';col4.appendChild(lbl4);

  const sfCard=buildSFCard(sf);
  col4.appendChild(sfCard);
  side.appendChild(col4);

  // SVG connector SF → Final center
  side.appendChild(buildFinalConnector(isLeft));
}}

function buildKOCard(m,prefix,bg){{
  const card=document.createElement('div');
  card.style.cssText=`background:${{bg}};border:1px solid rgba(255,255,255,.1);
    border-radius:8px;padding:6px 5px;display:flex;flex-direction:column;
    align-items:center;gap:4px;min-width:90px;`;

  const tt=document.createElement('div');
  tt.style.cssText='font-size:.42rem;font-weight:900;color:rgba(255,215,0,.85);letter-spacing:.07em;';
  tt.textContent=`${{prefix}}${{m.n}}`;card.appendChild(tt);

  const meta=document.createElement('div');
  meta.style.cssText='font-size:.33rem;color:#3a5060;text-align:center;line-height:1.3;';
  meta.innerHTML=`${{m.date}} ${{m.time}}<br>${{m.venue.length>12?m.venue.slice(0,11)+'…':m.venue}}`;
  card.appendChild(meta);

  // avail chips from previous round
  const avDiv=document.createElement('div');
  avDiv.className='avail';avDiv.id=`avail_${{m.id}}`;avDiv.style.minHeight='12px';
  card.appendChild(avDiv);

  // slot A
  const sAw=document.createElement('div');sAw.style.cssText='display:flex;flex-direction:column;align-items:center;gap:1px;';
  const sA=mkDS(`${{m.id}}_A`,'',42);sAw.appendChild(sA.el);
  card.appendChild(sAw);

  const xEl=document.createElement('div');
  xEl.style.cssText='color:rgba(255,255,255,.15);font-weight:900;font-size:.6rem;';xEl.textContent='×';
  card.appendChild(xEl);

  // slot B
  const sBw=document.createElement('div');sBw.style.cssText='display:flex;flex-direction:column;align-items:center;gap:1px;';
  const sB=mkDS(`${{m.id}}_B`,'',42);sBw.appendChild(sB.el);
  card.appendChild(sBw);

  const wlEl=document.createElement('div');
  wlEl.style.cssText='font-size:.32rem;color:#2a4050;margin-top:2px;';wlEl.textContent='↓ Venc.';
  card.appendChild(wlEl);
  const sW=mkDS(`${{m.id}}_W`,'',38);
  card.appendChild(sW.el);

  // drag forward area
  const fwd=document.createElement('div');
  fwd.id=`fwd_${{m.id}}`;
  fwd.style.cssText='display:flex;gap:4px;justify-content:center;flex-wrap:wrap;min-height:10px;';
  card.appendChild(fwd);

  return card;
}}

function buildSFCard(sf){{
  const card=document.createElement('div');
  card.style.cssText=`background:rgba(200,140,0,.12);border:1px solid rgba(255,215,0,.3);
    border-radius:9px;padding:7px 5px;display:flex;flex-direction:column;
    align-items:center;gap:5px;min-width:95px;`;

  const tt=document.createElement('div');
  tt.style.cssText='font-size:.44rem;font-weight:900;color:rgba(255,215,0,.9);letter-spacing:.07em;';
  tt.textContent=`SEMI ${{sf.id==='SF01'?1:2}}`;card.appendChild(tt);

  const meta=document.createElement('div');
  meta.style.cssText='font-size:.34rem;color:#3a5060;text-align:center;line-height:1.3;';
  meta.innerHTML=`${{sf.date}} ${{sf.time}}<br>${{sf.venue}}`;
  card.appendChild(meta);

  const avDiv=document.createElement('div');
  avDiv.className='avail';avDiv.id=`avail_${{sf.id}}`;avDiv.style.minHeight='12px';
  card.appendChild(avDiv);

  const sA=mkDS(`${{sf.id}}_A`,'',44);
  const sB=mkDS(`${{sf.id}}_B`,'',44);
  card.appendChild(sA.el);
  const x=document.createElement('div');
  x.style.cssText='color:rgba(255,255,255,.15);font-weight:900;font-size:.6rem;';x.textContent='×';
  card.appendChild(x);
  card.appendChild(sB.el);

  const wl=document.createElement('div');
  wl.style.cssText='font-size:.34rem;color:#2a4050;margin-top:2px;';wl.textContent='↓ p/ Final:';
  card.appendChild(wl);
  const sW=mkDS(`${{sf.id}}_W`,'',40);
  card.appendChild(sW.el);

  const fwd=document.createElement('div');
  fwd.id=`fwd_${{sf.id}}`;
  fwd.style.cssText='display:flex;gap:4px;justify-content:center;flex-wrap:wrap;min-height:10px;';
  card.appendChild(fwd);

  return card;
}}

// ── SVG CONNECTORS (bracket lines) ────────────────────────────────────────
function buildConnectorSVG(fromCount, toCount, isLeft, stroke){{
  const svg=document.createElementNS('http://www.w3.org/2000/svg','svg');
  const w=30, spacing=60;
  const h=Math.max(fromCount,toCount)*spacing+40;
  svg.setAttribute('width',w);svg.setAttribute('height',h);
  svg.style.flexShrink='0';svg.style.overflow='visible';

  // from slots evenly spaced
  const fromY=(i)=>{{const step=h/fromCount;return step/2+i*step;}};
  const toY=(i)=>{{const step=h/toCount;return step/2+i*step;}};

  // pair up: every 2 from → 1 to
  for(let i=0;i<toCount;i++){{
    const y1=fromY(i*2),y2=fromY(i*2+1),ym=toY(i);
    const x1=isLeft?0:w, x2=isLeft?w/2:w/2, xOut=isLeft?w:0;
    // horizontal lines from each source
    const l1=document.createElementNS('http://www.w3.org/2000/svg','line');
    l1.setAttribute('x1',x1);l1.setAttribute('y1',y1);l1.setAttribute('x2',x2);l1.setAttribute('y2',y1);
    l1.setAttribute('stroke',stroke);l1.setAttribute('stroke-width','1.5');svg.appendChild(l1);
    const l2=document.createElementNS('http://www.w3.org/2000/svg','line');
    l2.setAttribute('x1',x1);l2.setAttribute('y1',y2);l2.setAttribute('x2',x2);l2.setAttribute('y2',y2);
    l2.setAttribute('stroke',stroke);l2.setAttribute('stroke-width','1.5');svg.appendChild(l2);
    // vertical connector
    const lv=document.createElementNS('http://www.w3.org/2000/svg','line');
    lv.setAttribute('x1',x2);lv.setAttribute('y1',y1);lv.setAttribute('x2',x2);lv.setAttribute('y2',y2);
    lv.setAttribute('stroke',stroke);lv.setAttribute('stroke-width','1.5');svg.appendChild(lv);
    // horizontal to output
    const lo=document.createElementNS('http://www.w3.org/2000/svg','line');
    lo.setAttribute('x1',x2);lo.setAttribute('y1',ym);lo.setAttribute('x2',xOut);lo.setAttribute('y2',ym);
    lo.setAttribute('stroke',stroke);lo.setAttribute('stroke-width','1.5');svg.appendChild(lo);
  }}
  return svg;
}}

function buildFinalConnector(isLeft){{
  const svg=document.createElementNS('http://www.w3.org/2000/svg','svg');
  svg.setAttribute('width','24');svg.setAttribute('height','60');
  svg.style.flexShrink='0';svg.style.overflow='visible';
  const x1=isLeft?0:24,x2=isLeft?24:0;
  const l=document.createElementNS('http://www.w3.org/2000/svg','line');
  l.setAttribute('x1',x1);l.setAttribute('y1','30');l.setAttribute('x2',x2);l.setAttribute('y2','30');
  l.setAttribute('stroke','rgba(255,215,0,0.5)');l.setAttribute('stroke-width','2');svg.appendChild(l);
  return svg;
}}

// ── REFRESH AVAILABLE CHIPS ────────────────────────────────────────────────
function refreshAvailDiv(elId, srcSlots){{
  const el=document.getElementById(elId);if(!el)return;
  el.innerHTML='';
  const codes=[];
  srcSlots.forEach(s=>{{const c=slots[s];if(c&&!codes.includes(c))codes.push(c);}});
  if(codes.length){{
    const l=document.createElement('div');l.className='avail-lbl';l.textContent='↑ Disp.:';el.appendChild(l);
    codes.forEach(c=>el.appendChild(mkFC(c,30,true)));
  }}
}}

function refreshFwdDiv(elId, srcSlots){{
  const el=document.getElementById(elId);if(!el)return;
  el.innerHTML='';
  srcSlots.forEach(s=>{{
    const c=slots[s];
    if(c){{
      const wrap=document.createElement('div');
      wrap.style.cssText='display:flex;flex-direction:column;align-items:center;gap:1px;';
      wrap.appendChild(mkFC(c,30,true));
      el.appendChild(wrap);
    }}
  }});
}}

function onSlotChange(){{
  // Oitavas: avail from Avos winners
  [...OIT_LEFT,...OIT_RIGHT].forEach(m=>{{
    refreshAvailDiv(`avail_${{m.id}}`,[`${{m.fA}}_W`,`${{m.fB}}_W`]);
    refreshFwdDiv(`fwd_${{m.id}}`,[`${{m.id}}_A`,`${{m.id}}_B`]);
  }});
  // Quartas: avail from Oitavas winners
  [...QF_LEFT,...QF_RIGHT].forEach(m=>{{
    refreshAvailDiv(`avail_${{m.id}}`,[`${{m.fA}}_W`,`${{m.fB}}_W`]);
    refreshFwdDiv(`fwd_${{m.id}}`,[`${{m.id}}_A`,`${{m.id}}_B`]);
  }});
  // Semis
  [SF_LEFT,SF_RIGHT].forEach(sf=>{{
    refreshAvailDiv(`avail_${{sf.id}}`,[`${{sf.fA}}_W`,`${{sf.fB}}_W`]);
    refreshFwdDiv(`fwd_${{sf.id}}`,[`${{sf.id}}_A`,`${{sf.id}}_B`]);
  }});
  // Final avail chips
  const fa=document.getElementById('final-avail');
  if(fa){{
    fa.innerHTML='';
    ['SF01_W','SF02_W'].forEach(s=>{{
      const c=slots[s];
      if(c){{
        const wrap=document.createElement('div');
        wrap.style.cssText='display:flex;flex-direction:column;align-items:center;gap:2px;';
        wrap.appendChild(mkFC(c,38,true));
        const l=document.createElement('span');
        l.style.cssText='font-size:.36rem;color:#3a6080;';l.textContent='↑ p/ Final';
        wrap.appendChild(l);fa.appendChild(wrap);
      }}
    }});
  }}
  // 3rd place avail (losers of semis)
  const e3=document.getElementById('avail_3PL');
  if(e3){{
    e3.innerHTML='';
    const losers=[];
    ['SF01','SF02'].forEach(sf=>{{
      const w=slots[`${{sf}}_W`];
      ['A','B'].forEach(side=>{{
        const c=slots[`${{sf}}_${{side}}`];
        if(c&&c!==w)losers.push(c);
      }});
    }});
    if(losers.length){{
      const l=document.createElement('div');l.className='avail-lbl';l.textContent='Perd. Semis:';e3.appendChild(l);
      losers.forEach(c=>e3.appendChild(mkFC(c,30,true)));
    }}
  }}
  // champ name
  document.getElementById('champ-name').textContent=slots['CHAMP']?team(slots['CHAMP']).n:'';
}}

function resetAll(){{
  if(!confirm('Resetar todo o chaveamento?'))return;
  slots={{}};
  buildSide('left-side',  AVOS_LEFT,  OIT_LEFT,  QF_LEFT,  SF_LEFT,  true);
  buildSide('right-side', AVOS_RIGHT, OIT_RIGHT, QF_RIGHT, SF_RIGHT, false);
  wireEl('fin_A',   'FIN_A',  'Venc.SF1',52);
  wireEl('fin_B',   'FIN_B',  'Venc.SF2',52);
  wireEl('champ_slot','CHAMP','👑',60,true);
  // re-wire 3PL
  ['A','B','W'].forEach(s=>{{
    const el=document.getElementById(`ds_3PL_${{s}}`);
    if(el){{
      const ws=mkDS(`3PL_${{s}}`,'',46);
      el.replaceWith(ws.el);ws.el.id=`ds_3PL_${{s}}`;
    }}
  }});
  document.getElementById('champ-banner').style.display='none';
  onSlotChange();
}}

// ── INIT ──────────────────────────────────────────────────────────────────
buildSide('left-side',  AVOS_LEFT,  OIT_LEFT,  QF_LEFT,  SF_LEFT,  true);
buildSide('right-side', AVOS_RIGHT, OIT_RIGHT, QF_RIGHT, SF_RIGHT, false);
wireEl('fin_A',    'FIN_A',  'Venc.SF1',52);
wireEl('fin_B',    'FIN_B',  'Venc.SF2',52);
wireEl('champ_slot','CHAMP', '👑',60,true);
wireEl('ds_3PL_A', '3PL_A',  'Perd.SF1',46);
wireEl('ds_3PL_B', '3PL_B',  'Perd.SF2',46);
wireEl('ds_3PL_W', '3PL_W',  '🥉',46);
onSlotChange();
</script>
</body>
</html>"""

    components.html(BRACKET_HTML, height=5400, scrolling=True)
