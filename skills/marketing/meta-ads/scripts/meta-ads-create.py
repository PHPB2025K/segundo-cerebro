#!/usr/bin/env python3
"""
meta-ads-create.py — Criar Campanhas Completas Meta Ads
GB Importadora / KOBE.OPENCLAW

Cria estrutura completa: Campaign → Ad Set → Ad Creative → Ad

Uso:
  python3 meta-ads-create.py --name "BUDAMIX_SALES_POTES_Mar2026" --budget 15000
  python3 meta-ads-create.py --name "BUDAMIX_AWARENESS_BRAND_Mar2026" --objective OUTCOME_AWARENESS --budget 5000
  python3 meta-ads-create.py --campaign-only --name "TEST_CBO" --budget 50000
  python3 meta-ads-create.py --dry-run --name "TEST" --budget 10000
"""

import argparse
import json
import subprocess
import sys
from datetime import datetime

try:
    import requests
except ImportError:
    print("Erro: pip3 install requests")
    sys.exit(1)

# ─── Configurações ──────────────────────────────────────────────────────────
AD_ACCOUNT = "act_323534883953033"
API_VERSION = "v21.0"
BASE_URL = f"https://graph.facebook.com/{API_VERSION}"
TOKEN_OP_PATH = "op://OpenClaw/Meta Ads API - KOBE.OPENCLAW/access_token"

# IDs da GB Importadora — preencher quando disponível
DEFAULT_PAGE_ID = ""          # ID da Page do Facebook da GB/Budamix
DEFAULT_PIXEL_ID = ""         # ID do Pixel Meta da GB
DEFAULT_INSTAGRAM_ID = ""     # ID da conta Instagram

# ─── Helpers ─────────────────────────────────────────────────────────────────

def get_token():
    try:
        result = subprocess.run(
            ["op", "read", TOKEN_OP_PATH],
            capture_output=True, text=True, timeout=10
        )
        if result.returncode != 0:
            print(f"Erro 1Password: {result.stderr.strip()}")
            sys.exit(1)
        return result.stdout.strip()
    except FileNotFoundError:
        print("Erro: 'op' não encontrado. Instale 1Password CLI.")
        sys.exit(1)


def api_post(url, payload, dry_run=False):
    """POST para a API. Se dry_run, apenas imprime o payload."""
    if dry_run:
        print(f"\n[DRY RUN] POST {url}")
        print(json.dumps(payload, indent=2, ensure_ascii=False))
        return {"id": "DRY_RUN_ID", "dry_run": True}

    try:
        resp = requests.post(url, json=payload, timeout=30)
        data = resp.json()
        if "error" in data:
            print(f"\n❌ Erro da API: {data['error'].get('message', str(data['error']))}")
            print(f"   Código: {data['error'].get('code')}")
            print(f"   Subcode: {data['error'].get('error_subcode', 'N/A')}")
            return None
        return data
    except requests.exceptions.RequestException as e:
        print(f"❌ Erro de conexão: {e}")
        return None


def confirm(msg):
    """Pede confirmação do usuário."""
    resp = input(f"\n{msg} [s/N]: ").strip().lower()
    return resp in ("s", "sim", "y", "yes")


# ─── Criação de objetos ───────────────────────────────────────────────────────

def create_campaign(token, account_id, name, objective, budget_cents, bid_strategy, status, dry_run):
    """Cria uma campanha."""
    print(f"\n📋 Criando campanha: {name}")

    # Determinar se é CBO (budget na campanha)
    payload = {
        "name": name,
        "objective": objective,
        "status": status,
        "special_ad_categories": [],
        "access_token": token,
    }

    # CBO: budget na campanha
    if budget_cents > 0:
        payload["daily_budget"] = budget_cents
        payload["bid_strategy"] = bid_strategy

    result = api_post(f"{BASE_URL}/{account_id}/campaigns", payload, dry_run)
    if result:
        campaign_id = result.get("id", "DRY_RUN_ID")
        print(f"   ✅ Campanha criada: {campaign_id}")
        return campaign_id
    return None


def create_adset(token, account_id, campaign_id, name, budget_cents, bid_strategy,
                 pixel_id, targeting, status, dry_run, is_cbo=False):
    """Cria um Ad Set."""
    print(f"\n📦 Criando Ad Set: {name}")

    payload = {
        "name": name,
        "campaign_id": campaign_id,
        "billing_event": "IMPRESSIONS",
        "optimization_goal": "OFFSITE_CONVERSIONS",
        "bid_strategy": bid_strategy,
        "targeting": targeting,
        "status": status,
        "access_token": token,
    }

    # ABO: budget no adset
    if not is_cbo and budget_cents > 0:
        payload["daily_budget"] = budget_cents

    # Evento de otimização (Purchase)
    if pixel_id:
        payload["promoted_object"] = {
            "pixel_id": pixel_id,
            "custom_event_type": "PURCHASE"
        }

    result = api_post(f"{BASE_URL}/{account_id}/adsets", payload, dry_run)
    if result:
        adset_id = result.get("id", "DRY_RUN_ID")
        print(f"   ✅ Ad Set criado: {adset_id}")
        return adset_id
    return None


def create_creative(token, account_id, name, page_id, link_url, image_url, message, headline, dry_run):
    """Cria um Ad Creative básico com link."""
    print(f"\n🎨 Criando Ad Creative: {name}")

    if not page_id:
        print("   ⚠️  PAGE_ID não configurado — criativo ignorado")
        print("   Configure DEFAULT_PAGE_ID no script ou passe --page-id")
        return None

    object_story_spec = {
        "page_id": page_id,
        "link_data": {
            "link": link_url,
            "message": message,
            "name": headline,
            "call_to_action": {
                "type": "SHOP_NOW",
                "value": {"link": link_url}
            }
        }
    }

    if image_url:
        object_story_spec["link_data"]["picture"] = image_url

    payload = {
        "name": name,
        "object_story_spec": object_story_spec,
        "access_token": token,
    }

    result = api_post(f"{BASE_URL}/{account_id}/adcreatives", payload, dry_run)
    if result:
        creative_id = result.get("id", "DRY_RUN_ID")
        print(f"   ✅ Creative criado: {creative_id}")
        return creative_id
    return None


def create_ad(token, account_id, adset_id, creative_id, name, status, dry_run):
    """Cria um Ad."""
    print(f"\n📢 Criando Ad: {name}")

    payload = {
        "name": name,
        "adset_id": adset_id,
        "creative": {"creative_id": creative_id},
        "status": status,
        "access_token": token,
    }

    result = api_post(f"{BASE_URL}/{account_id}/ads", payload, dry_run)
    if result:
        ad_id = result.get("id", "DRY_RUN_ID")
        print(f"   ✅ Ad criado: {ad_id}")
        return ad_id
    return None


def get_targeting(age_min, age_max, country, broad):
    """Monta objeto de targeting."""
    targeting = {
        "geo_locations": {"countries": [country]},
        "age_min": age_min,
        "age_max": age_max,
    }
    if broad:
        # Advantage+ Audience (broad targeting)
        targeting["advantage_audience"] = 1
    return targeting


# ─── Main ─────────────────────────────────────────────────────────────────────

def main():
    parser = argparse.ArgumentParser(
        description="Meta Ads Create — GB Importadora",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Exemplos:
  # Criar campanha CBO completa (campanha + adset + criativo + ad)
  python3 meta-ads-create.py \\
    --name "BUDAMIX_SALES_POTES_Mar2026" \\
    --budget 15000 \\
    --pixel-id 123456789 \\
    --page-id 987654321 \\
    --link "https://budamix.com.br/potes" \\
    --message "Potes herméticos premium para sua cozinha" \\
    --headline "Potes Herméticos Budamix" \\
    --status PAUSED

  # Apenas criar a campanha (sem adset/ad)
  python3 meta-ads-create.py --campaign-only --name "TEST_CBO" --budget 50000

  # Dry run — ver o que seria criado sem de fato criar
  python3 meta-ads-create.py --dry-run --name "TEST" --budget 10000

  # Campanha de Awareness (sem evento de conversão)
  python3 meta-ads-create.py \\
    --name "BUDAMIX_AWARENESS_BRAND_Mar2026" \\
    --objective OUTCOME_AWARENESS \\
    --budget 5000 \\
    --campaign-only
        """
    )

    # Campos principais
    parser.add_argument("--name", required=True,
                        help="Nome da campanha (usar naming convention)")
    parser.add_argument("--budget", type=int, default=10000,
                        help="Budget diário em centavos. Ex: 15000 = R$150/dia (padrão: 10000 = R$100)")
    parser.add_argument("--objective", default="OUTCOME_SALES",
                        choices=["OUTCOME_SALES", "OUTCOME_TRAFFIC", "OUTCOME_AWARENESS",
                                 "OUTCOME_ENGAGEMENT", "OUTCOME_LEADS", "OUTCOME_APP_PROMOTION"],
                        help="Objetivo da campanha (padrão: OUTCOME_SALES)")
    parser.add_argument("--status", default="PAUSED",
                        choices=["PAUSED", "ACTIVE"],
                        help="Status inicial (padrão: PAUSED — sempre pausado por segurança)")
    parser.add_argument("--bid-strategy", default="LOWEST_COST_WITHOUT_CAP",
                        choices=["LOWEST_COST_WITHOUT_CAP", "LOWEST_COST_WITH_BID_CAP",
                                 "COST_CAP", "MINIMUM_ROAS"],
                        help="Estratégia de lance (padrão: LOWEST_COST_WITHOUT_CAP)")

    # Ad Set
    parser.add_argument("--adset-name", default=None,
                        help="Nome do Ad Set (padrão: {nome}_ADSET)")
    parser.add_argument("--age-min", type=int, default=25,
                        help="Idade mínima do público (padrão: 25)")
    parser.add_argument("--age-max", type=int, default=55,
                        help="Idade máxima do público (padrão: 55)")
    parser.add_argument("--country", default="BR",
                        help="País do targeting (padrão: BR)")
    parser.add_argument("--broad", action="store_true", default=True,
                        help="Usar Advantage+ Audience / broad targeting (padrão: True)")
    parser.add_argument("--pixel-id", default=DEFAULT_PIXEL_ID,
                        help="ID do Pixel Meta")
    parser.add_argument("--adset-budget", type=int, default=0,
                        help="Budget do Ad Set em centavos (ABO). Se 0, usa CBO da campanha.")

    # Creative / Ad
    parser.add_argument("--page-id", default=DEFAULT_PAGE_ID,
                        help="ID da Page do Facebook")
    parser.add_argument("--link", default="https://www.instagram.com/budamix",
                        help="URL de destino do anúncio")
    parser.add_argument("--message", default="Confira os produtos Budamix!",
                        help="Texto principal do anúncio")
    parser.add_argument("--headline", default="Budamix — Qualidade para sua cozinha",
                        help="Headline do anúncio")
    parser.add_argument("--image-url", default=None,
                        help="URL pública de imagem para o criativo")

    # Modos
    parser.add_argument("--account", default=AD_ACCOUNT,
                        help=f"Ad Account (padrão: {AD_ACCOUNT})")
    parser.add_argument("--campaign-only", action="store_true",
                        help="Criar apenas a campanha (sem Ad Set, Creative, Ad)")
    parser.add_argument("--dry-run", action="store_true",
                        help="Simular criação sem chamar a API")

    args = parser.parse_args()

    # Aviso de status
    if args.status == "ACTIVE" and not args.dry_run:
        print(f"⚠️  ATENÇÃO: Campanha será criada como ACTIVE (já começa gastando!)")
        if not confirm("Confirmar criação como ACTIVE?"):
            print("Abortado.")
            sys.exit(0)

    print(f"🔐 Obtendo token do 1Password...")
    token = get_token()
    print(f"✅ Token obtido")

    if args.dry_run:
        print(f"\n🔷 MODO DRY RUN — Nenhuma chamada real à API será feita\n")

    print(f"\n{'='*60}")
    print(f"  CRIANDO ESTRUTURA DE CAMPANHA")
    print(f"{'='*60}")
    print(f"  Conta: {args.account}")
    print(f"  Nome: {args.name}")
    print(f"  Objetivo: {args.objective}")
    print(f"  Budget: R${args.budget/100:.2f}/dia")
    print(f"  Status: {args.status}")
    print(f"{'='*60}")

    # 1. Criar Campaign
    is_cbo = args.adset_budget == 0
    campaign_budget = args.budget if is_cbo else 0
    campaign_id = create_campaign(
        token=token,
        account_id=args.account,
        name=args.name,
        objective=args.objective,
        budget_cents=campaign_budget,
        bid_strategy=args.bid_strategy,
        status=args.status,
        dry_run=args.dry_run
    )

    if not campaign_id:
        print("\n❌ Falha ao criar campanha. Abortando.")
        sys.exit(1)

    if args.campaign_only:
        print(f"\n✅ Campanha criada com sucesso!")
        print(f"   Campaign ID: {campaign_id}")
        print(f"\n📋 Próximos passos:")
        print(f"   1. Criar Ad Sets manualmente no Ads Manager")
        print(f"   2. Ou re-executar sem --campaign-only com --pixel-id e --page-id")
        return

    # 2. Criar Ad Set
    adset_name = args.adset_name or f"{args.name}_ADSET"
    targeting = get_targeting(args.age_min, args.age_max, args.country, args.broad)
    adset_budget = args.adset_budget if not is_cbo else 0

    adset_id = create_adset(
        token=token,
        account_id=args.account,
        campaign_id=campaign_id,
        name=adset_name,
        budget_cents=adset_budget,
        bid_strategy=args.bid_strategy,
        pixel_id=args.pixel_id,
        targeting=targeting,
        status=args.status,
        dry_run=args.dry_run,
        is_cbo=is_cbo
    )

    if not adset_id:
        print("\n❌ Falha ao criar Ad Set.")
        print(f"   Campaign ID criado: {campaign_id} (pode continuar manualmente)")
        sys.exit(1)

    # 3. Criar Creative
    creative_name = f"{args.name}_CREATIVE"
    creative_id = create_creative(
        token=token,
        account_id=args.account,
        name=creative_name,
        page_id=args.page_id,
        link_url=args.link,
        image_url=args.image_url,
        message=args.message,
        headline=args.headline,
        dry_run=args.dry_run
    )

    # 4. Criar Ad (apenas se tiver creative)
    ad_id = None
    if creative_id:
        ad_name = f"{args.name}_AD_001"
        ad_id = create_ad(
            token=token,
            account_id=args.account,
            adset_id=adset_id,
            creative_id=creative_id,
            name=ad_name,
            status=args.status,
            dry_run=args.dry_run
        )

    # Resumo
    print(f"\n{'='*60}")
    print(f"  ✅ ESTRUTURA CRIADA COM SUCESSO")
    print(f"{'='*60}")
    print(f"  Campaign ID: {campaign_id}")
    print(f"  Ad Set ID:   {adset_id}")
    print(f"  Creative ID: {creative_id or '⚠️  não criado (sem page_id)'}")
    print(f"  Ad ID:       {ad_id or '⚠️  não criado (sem creative)'}")
    print(f"  Status:      {args.status}")
    print(f"{'='*60}")

    if args.status == "PAUSED":
        print(f"\n⏸️  Campanha pausada. Para ativar:")
        print(f"   TOKEN=$(op read '{TOKEN_OP_PATH}')")
        print(f"   curl -X POST 'https://graph.facebook.com/{API_VERSION}/{campaign_id}' \\")
        print(f"     -d 'status=ACTIVE' -d 'access_token=$TOKEN'")

    if not args.pixel_id:
        print(f"\n⚠️  ATENÇÃO: Pixel não configurado!")
        print(f"   Sem Pixel, não há otimização por conversão.")
        print(f"   Configure --pixel-id ou DEFAULT_PIXEL_ID no script.")

    print(f"\n📋 Próximos passos recomendados:")
    print(f"   1. Revisar no Ads Manager antes de ativar")
    print(f"   2. Adicionar criativos de qualidade (imagens/vídeos)")
    print(f"   3. Verificar evento de Pixel configurado corretamente")
    print(f"   4. Ativar apenas quando tudo estiver revisado")
    print(f"   5. Configurar regras automáticas: python3 meta-ads-rules.py --create-essentials")


if __name__ == "__main__":
    main()
