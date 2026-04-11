---
name: shopee-budamix-brand-id
description: Brand ID da Budamix na Shopee é 5014011. Usar sempre ao criar anúncios via API.
type: feedback
---

Sempre usar brand_id=5014011 ao criar anúncios Shopee via API para a marca Budamix.

**Why:** A API da Shopee não tem busca por nome de marca — o get_brand_list só pagina sem filtro. Descobrir o ID exigiu varrer items existentes. Sem o ID correto, o produto fica como "NoBrand".

**How to apply:** No payload de `add_item`, usar `"brand": {"brand_id": 5014011, "original_brand_name": "Budamix"}` em vez de `brand_id: 0`.
