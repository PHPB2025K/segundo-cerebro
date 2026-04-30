#!/usr/bin/env python3
"""
Override mensal do banco de horas do Mateus E. L. Santos.

Motivo: jornada reduzida acordada (08:30-17:00) durante Tiro de Guerra.
Sem este override, o sistema calcula o saldo dele com jornada padrão 8h30/dia,
gerando déficit estrutural de ~18h/mês. O override compensa esse déficit pra
que ele opere em condição idêntica aos outros funcionários: bônus + extras
reais - débito mensal padrão de -10h.

Uso:
    python3 mateus-override-mensal.py 2026-05    # cria override de maio
    python3 mateus-override-mensal.py            # mês corrente

Quando rodar: dia 31 do mês ou dia 1 do mês seguinte ANTES de 00:00 BRT
(antes do cron reset-banco-horas executar).

Autor: CC local — 30/04/2026
Documentação: openclaw/agents/kobe/shared/rh/knowledge/jornadas-individuais.md
"""
import sys, os, json, urllib.request, urllib.parse
from datetime import datetime, date, time, timedelta
from collections import defaultdict
from zoneinfo import ZoneInfo

MATEUS_USER_ID = "1edae654-065c-4d3d-8516-ca5267d2a47b"
TZ = ZoneInfo("America/Sao_Paulo")

# Jornada acordada do Mateus (08:30-17:00 com 1h almoço = 7h30/dia)
JORNADA_ACORDADA_SEG_QUI = timedelta(hours=7, minutes=30)
JORNADA_ACORDADA_SEX = timedelta(hours=7, minutes=30)

# Jornada padrão do sistema (pra calcular o "déficit estrutural" a compensar)
JORNADA_PADRAO_SEG_QUI = timedelta(hours=8, minutes=30)
JORNADA_PADRAO_SEX = timedelta(hours=8)

def get_credentials():
    """Lê credenciais do config canônico do RH."""
    path = os.path.expanduser(
        "~/segundo-cerebro/openclaw/agents/kobe/shared/rh/config/ponto-certo.json"
    )
    return json.load(open(path))

def http(method, url, headers, body=None):
    data = json.dumps(body).encode() if body else None
    req = urllib.request.Request(url, data=data, method=method, headers=headers)
    with urllib.request.urlopen(req, timeout=30) as r:
        txt = r.read().decode()
        return json.loads(txt) if txt else None

def main(mes_str=None):
    if mes_str:
        ano, mes = map(int, mes_str.split("-"))
    else:
        hoje = datetime.now(TZ).date()
        ano, mes = hoje.year, hoje.month
    primeiro_dia = date(ano, mes, 1)
    if mes == 12:
        prox = date(ano+1, 1, 1)
    else:
        prox = date(ano, mes+1, 1)
    print(f"Mês de referência: {primeiro_dia} → {prox - timedelta(days=1)}")

    cred = get_credentials()
    sr = cred["supabase_service_role_key"]
    base = cred["supabase_url"]
    headers = {
        "apikey": sr,
        "Authorization": f"Bearer {sr}",
        "Content-Type": "application/json",
        "Prefer": "return=representation",
    }

    # 1) Pegar batidas do Mateus do mês
    qs = urllib.parse.urlencode([
        ("select", "*"),
        ("user_id", f"eq.{MATEUS_USER_ID}"),
        ("recorded_at", f"gte.{primeiro_dia.isoformat()}T00:00:00"),
        ("recorded_at", f"lt.{prox.isoformat()}T00:00:00"),
        ("order", "recorded_at"),
    ])
    trs = http("GET", f"{base}/rest/v1/time_records?{qs}", headers)
    print(f"Batidas no mês: {len(trs)}")

    # 2) Indexar por dia
    by_day = defaultdict(dict)
    for r in trs:
        rec = datetime.fromisoformat(r["recorded_at"].replace("Z","+00:00")).astimezone(TZ)
        by_day[rec.date()][r["record_type"]] = rec

    # 3) Calcular tempo trabalhado real por dia (tempo entre clock_in e clock_out menos almoço)
    tempo_real_total = timedelta()
    jornada_acordada_total = timedelta()
    jornada_padrao_total = timedelta()
    dias_completos = 0
    dias_incompletos = []

    for d, recs in sorted(by_day.items()):
        if d.weekday() >= 5:
            continue  # ignora sábado/domingo (pago à parte conforme política)
        ci = recs.get("clock_in")
        co = recs.get("clock_out")
        bs = recs.get("break_start")
        be = recs.get("break_end")
        if not (ci and co):
            dias_incompletos.append(d)
            continue
        trabalhado = co - ci
        if bs and be:
            trabalhado -= (be - bs)
        tempo_real_total += trabalhado
        if d.weekday() < 4:
            jornada_acordada_total += JORNADA_ACORDADA_SEG_QUI
            jornada_padrao_total += JORNADA_PADRAO_SEG_QUI
        else:
            jornada_acordada_total += JORNADA_ACORDADA_SEX
            jornada_padrao_total += JORNADA_PADRAO_SEX
        dias_completos += 1

    extras_acordada = tempo_real_total - jornada_acordada_total
    deficit_estrutural = jornada_padrao_total - jornada_acordada_total

    # horas_extras_override = extras_reais (versus jornada acordada) + déficit_estrutural a compensar
    # racional: zerar o "trabalhou menos que jornada padrão" pra ele operar como os outros
    horas_extras_override = extras_acordada + deficit_estrutural

    print(f"\nDias completos: {dias_completos}")
    print(f"Dias incompletos (ignorados): {dias_incompletos}")
    print(f"Tempo real trabalhado: {tempo_real_total}")
    print(f"Jornada acordada total: {jornada_acordada_total}")
    print(f"Jornada padrão total: {jornada_padrao_total}")
    print(f"Extras vs jornada acordada: {extras_acordada}")
    print(f"Déficit estrutural a compensar: {deficit_estrutural}")
    print(f"horas_extras_override final: {horas_extras_override}")

    # Garantir que horas_extras_override seja diferente de zero (regra do sistema)
    if horas_extras_override == timedelta():
        horas_extras_override = timedelta(seconds=1)
        print(f"  ⚠️ Ajustado pra +1s pra forçar uso do override (regra do sistema)")

    # 4) Verificar se já existe override pro mês
    qs2 = urllib.parse.urlencode([
        ("select", "*"),
        ("user_id", f"eq.{MATEUS_USER_ID}"),
        ("mes_referencia", f"eq.{primeiro_dia.isoformat()}"),
    ])
    existing = http("GET", f"{base}/rest/v1/banco_horas?{qs2}", headers)

    def fmt(td):
        total = int(td.total_seconds())
        sign = "-" if total < 0 else ""
        total = abs(total)
        h, rem = divmod(total, 3600)
        m, s = divmod(rem, 60)
        return f"{sign}{h:02d}:{m:02d}:{s:02d}"

    payload = {
        "user_id": MATEUS_USER_ID,
        "mes_referencia": primeiro_dia.isoformat(),
        "horas_extras": fmt(horas_extras_override),
    }

    print(f"\nPayload override:")
    print(json.dumps(payload, indent=2))

    if "--dry-run" in sys.argv:
        print("\n(dry-run, não vou gravar)")
        return

    if existing:
        print(f"\nJá existe override (id={existing[0]['id']}) — atualizando...")
        url = f"{base}/rest/v1/banco_horas?id=eq.{existing[0]['id']}"
        result = http("PATCH", url, headers, payload)
    else:
        print(f"\nCriando novo override...")
        url = f"{base}/rest/v1/banco_horas"
        result = http("POST", url, headers, payload)
    print(f"✅ Override registrado:")
    print(json.dumps(result, indent=2, default=str))

if __name__ == "__main__":
    arg = sys.argv[1] if len(sys.argv) > 1 and not sys.argv[1].startswith("--") else None
    main(arg)
