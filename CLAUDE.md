# Nortiq: repositório de design

- Protótipo navegável do Nortiq CRM (`index.html`, `ds/`), publicado no GitHub Pages. `PENDENCIAS.md` registra o que foi decidido e o que falta.
- O sistema de verdade (API, telas, site e banco) fica no repositório privado `phchris95/nortiq-crm-api`.

## Verificação do Google: perguntar antes de mudar

O Google aprovou em 10/10/2026 o acesso do Nortiq CRM ao Google Agenda (`calendar.events`). Mudar a configuração da tela de permissão do Google pede uma verificação nova, com vídeo e dias ou semanas de espera. Antes de mexer nas permissões pedidas ao Google, no nome "Nortiq CRM", no logo ou e-mail da tela de permissão, nos endereços da página inicial, da privacidade e dos termos (`nortiqtec.com.br`, `/privacidade`, `/termos`) ou no domínio autorizado, avise o dono do projeto disso e pergunte se ele quer seguir, sim ou não. Os detalhes estão no `CLAUDE.md` do `nortiq-crm-api`.

## Vídeos

O padrão de vídeo aprovado está em `video/ESTILO.md`: identidade, roteiro, ritmo, trilha, efeitos, os formatos 16:9 (site) e 9:16 (Instagram) e como renderizar. Para qualquer vídeo novo do Nortiq, parta de `video/site-16x9/` e `video/instagram-9x16/` e siga esse guia, sem refazer a configuração do zero. Prepare a máquina com `source video/ambiente.sh` e renderize com `bash video/renderizar.sh`.
