---
title: video-use — editor de vídeo conversacional via Claude Code
created: 2026-05-02
type: reference
status: active
tags:
  - skill
  - video
  - claude-code
  - browser-use
---

# video-use

> Skill instalada. Não duplicar conteúdo upstream — é um repositório Python clonado, atualiza via `git pull`.

## O que é

Skill da [browser-use](https://github.com/browser-use/video-use) (mesma org do `browser-use` original) que transforma Claude Code em editor de vídeo conversacional. Você joga raw footage em uma pasta, conversa com o agente ("edit these into a launch video"), ele transcreve via ElevenLabs Scribe, propõe estratégia, gera EDL, renderiza com cortes/grading/subtitles/animações, faz self-eval e devolve `final.mp4` em `<videos_dir>/edit/`.

**Stars no momento da install:** 6.042. **Default branch:** `main`. **Linguagem:** Python.

## Como funciona

A LLM **não assiste** o vídeo. Lê via duas camadas:
1. **Audio transcript** (sempre carregado) — ElevenLabs Scribe gera word-level timestamps + diarização + tags `(laughter)`. Empacotado em `takes_packed.md` (~12KB).
2. **Visual composite** (sob demanda) — `timeline_view.py` produz filmstrip + waveform + word labels PNG só nos pontos de decisão.

Compara com abordagem naive: 30k frames × 1.5k tokens = 45M tokens de ruído.

## Instalação local (02/05/2026)

| Item | Path / Status |
|------|---------------|
| Repo clonado | `~/Developer/video-use/` |
| Symlink Claude Code | `~/.claude/skills/video-use → ~/Developer/video-use` |
| Venv (deps isoladas) | `~/Developer/video-use/.venv/` (criado via `uv sync`) |
| API key | `~/Developer/video-use/.env` (chmod 600, ELEVENLABS_API_KEY) |
| Última verificação | helpers OK, ffprobe OK, libs OK |

## CRÍTICO — invocação dos helpers

Python 3.14 do Homebrew tem PEP 668 ativo. Deps (librosa, scipy, scikit-learn, pillow, matplotlib, requests, soundfile, numpy) ficam **só no venv** do repo.

**SEMPRE invocar helpers via venv:**
```bash
~/Developer/video-use/.venv/bin/python ~/Developer/video-use/helpers/X.py [args]
```

Ou ativar o venv antes:
```bash
source ~/Developer/video-use/.venv/bin/activate
python helpers/X.py [args]
```

Ver também memória local em `~/.claude/projects/.../memory/video_use_install.md`.

## Helpers principais

| Helper | Uso |
|--------|-----|
| `transcribe.py <video>` | Single-file Scribe call. `--num-speakers N` opcional. Cached. |
| `transcribe_batch.py <dir>` | 4-worker parallel. Multi-take. |
| `pack_transcripts.py --edit-dir <dir>` | `transcripts/*.json` → `takes_packed.md` |
| `timeline_view.py <video> <start> <end>` | Filmstrip + waveform PNG (drill-down em decisões) |
| `render.py <edl.json> -o <out>` | Per-segment extract → concat → overlays → subtitles |
| `grade.py <in> -o <out>` | ffmpeg filter chain grade (presets + custom) |

## Pré-requisitos

- ✅ ffmpeg + ffprobe (brew, hard-req)
- ✅ Python ≥ 3.10 + venv com librosa/scipy/etc.
- ✅ ElevenLabs API key — Scribe é o único custo recorrente
- ⚠️ yt-dlp (opcional, só pra baixar fontes de URL)
- ⚠️ manim, Remotion (lazy install — só na primeira animação)

## Fluxo de uso

```bash
cd /path/to/your/videos
claude
> edit these into a launch video
```

Ou:
```bash
> inventory these takes and propose a strategy
```

Outputs sempre em `<videos_dir>/edit/`. O repo `video-use` fica intocado.

## Hard rules (correctness, não taste)

A skill tem 12 regras invioláveis no SKILL.md. As mais críticas:

1. Subtitles aplicados POR ÚLTIMO no filter chain (senão overlays escondem)
2. Per-segment extract → lossless `-c copy` concat (evita re-encode em cascata)
3. Fade de áudio 30ms em cada cut boundary (sem isso = pop audível)
4. `setpts=PTS-STARTPTS+T/TB` em overlays
5. SRT master usa offsets da timeline final, não do source
6. Nunca corta dentro de uma palavra — snap pra word boundary
7. Padding 30–200ms em cada cut edge (Scribe drift de 50–100ms)

## Custo

| Plano ElevenLabs | Chars/mês | ~Áudio | Preço |
|------------------|-----------|--------|-------|
| Free | 10k | ~10min | $0 |
| Creator | 250k | ~4h | $22/mês |
| Pro | 1.1M | ~18h | $99/mês |

Cache: transcript por source nunca é refeito (a menos que arquivo mude). Logo, mesmo vídeo editado 10× = 1× transcrição.

## Atualizações

```bash
cd ~/Developer/video-use && git pull --ff-only && uv sync
```

Symlink pega automático. Se `pyproject.toml` mudar, `uv sync` aplica.

## Histórico

- **02/05/2026** — Instalada por Pedro durante sessão de import-planning. API key inicial circulou em texto-claro no transcript (ambas inválidas no momento da instalação — 401). Aguardando key correta pra ativar transcrição. Skill estruturalmente OK (helpers + venv + ffprobe verificados).

## Links

- Upstream: https://github.com/browser-use/video-use
- Issues: https://github.com/browser-use/video-use/issues
- ElevenLabs API keys: https://elevenlabs.io/app/settings/api-keys
- [[knowledge/concepts/claude-code-skills-inventario]] — inventário geral
