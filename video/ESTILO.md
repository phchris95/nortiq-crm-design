# Vídeos do Nortiq: o padrão aprovado

Este é o estilo aprovado em 03/10/2026 para os vídeos de apresentação do Nortiq. Ele vale para o site, para o Instagram e para os próximos vídeos. Para um vídeo novo, parta destas pastas e deste guia: não comece do zero.

| Pasta ou arquivo | O que é |
|---|---|
| `site-16x9/` | Versão do site, 1920×1080, composição HyperFrames (`index.html`) com fontes, logo, trilha e efeitos em `assets/`. |
| `instagram-9x16/` | Versão do Instagram (Reels), 1080×1920, com o layout refeito para o celular. Usa os mesmos tempos e a mesma trilha. |
| `trilha/trilha.py` | Gera a trilha instrumental original e grava `assets/trilha.wav` nas duas versões. |
| `ambiente.sh` | Prepara a máquina: ffmpeg, numpy/scipy e o navegador do HyperFrames. |
| `renderizar.sh` | Confere, renderiza e finaliza as duas versões em `finais/`. |
| `finalizar.sh` | Ajusta o volume final do som para -16 LUFS. |
| `finais/` | Os vídeos prontos e a comparação com a primeira versão. |

## Identidade (não mudar)

- **Cores:**
  - azul Nortiq `#0e2a47`, e os tons `#1c4770`, `#38689b`, `#8faac8` e `#dce4ee`;
  - fundo claro `#f7f8fa`;
  - textos `#0a1826` e `#4b5563`;
  - verde de "venda fechada" e do WhatsApp `#157347`.
- **Fontes:** Space Grotesk 700 nos títulos e nos números, IBM Plex Sans no resto. As fontes ficam em `assets/fonts` e não vêm da internet.
- **Logo:** o selo azul com o logo (`assets/logo.png`) e o nome "Nortiq" ao lado.
- **Telas:** cartões brancos com cantos arredondados e sombra leve, iguais aos do sistema. Use as telas e os dados de exemplo que já existem: Juliana Prado, Marta Oliveira, os técnicos Jefferson, Bruno e Diego. **Nunca mostre uma função que o sistema não tem.**
- **Visual:** limpo e profissional. Fundo claro com duas manchas suaves de azul, sem exagero futurista.

## Roteiro: problema → organização → controle → resultado

| Tempo | Cena | Texto (título com o final em azul, depois a frase de apoio) | Tela |
|---|---|---|---|
| 0 a 2,2 s | Abertura (painel azul) | **Nortiq**. "**Gestão inteligente** para lojas de aquecedores e hidráulica." + os módulos | Logo, frase, módulos e uma prévia da tela de Orçamentos subindo por baixo |
| 2,2 a 5,6 s | Orçamentos | "Do orçamento à instalação, *tudo em um só lugar.*" Apoio: "Sem papel, planilha ou conversa perdida: cada orçamento na sua etapa." | Funil; a Juliana passa de Enviado para Negociando e para Venda fechada, com os totais contando |
| 5,6 a 8,9 s | Clientes | "Não perca o cliente *depois da venda.*" Apoio: "O histórico de cada cliente organizado, e o aviso da manutenção pronto no WhatsApp." | Ficha da Marta: equipamento, histórico, revisão em 5 dias, depois "Avisar no WhatsApp" e a mensagem |
| 8,9 a 11,1 s | Agenda | "Organize sua agenda. *Cada técnico sabe onde ir.*" Apoio: "Saiba exatamente o que precisa ser feito, com lembrete no celular." | Semana com os técnicos e o lembrete do Google Agenda no celular |
| 11,1 a 13,3 s | Metas | "Clareza sobre os *resultados da sua loja.*" Apoio: "Vendas, conversão e a meta do mês: quanto entrou e quanto falta." | Receita, conversão, instalações e a barra da meta |
| 13,3 a 16 s | Encerramento (painel azul) | **Nortiq**. "Gestão inteligente para sua loja." "CONHEÇA A NORTIQ" + `nortiqtec.com.br` | Logo e endereço |

**Regras do texto:**
- Fale do benefício para o lojista, não da função.
- A marca não fica presa ao ramo de hidráulica: o fim diz "para sua loja".
- No título, a parte do benefício aparece em azul (`<em>` no HTML).

## Ritmo e movimento

- **Duração e tempo:** 16 s em 108 BPM; um tempo da música dura 0,5556 s.
- **Cortes no tempo da música:** em 2,222, 5,556, 8,889, 11,111 e 13,333 s. Cenas novas ou outra duração pedem os cortes recalculados no novo tempo.
- **Abertura e fim:** o painel azul sobe para abrir a primeira cena e desce para o encerramento.
- **Entre as cenas claras:** a cena que sai desliza para a esquerda e some; a que entra vem da direita (no 9:16, de baixo).
- **Títulos:** entram palavra por palavra. Use `text-wrap: balance` para nenhuma linha ficar com uma palavra sozinha.
- **Telas:** cada uma tem um zoom lento de 3,5% a 4% durante a cena.
- **Números:** contam a partir do tempo do vídeo (funciona em qualquer quadro).
- **Ações no tempo da música:** o cartão pousa, o botão é tocado, a notificação chega.

## Som

- **Trilha:** original, gerada pelo `trilha/trilha.py`, sem direitos de terceiros.
  - Estilo "modern corporate / upbeat tech", 108 BPM, sem vocal.
  - Instrumentos: batida leve, baixo, arpejo discreto e um fundo suave.
  - A abertura não tem bateria; a batida entra no corte para Orçamentos e o fim resolve em Dó e some.
  - Volume no vídeo: `data-volume="0.22"`.
- **Efeitos:** biblioteca que vem com o HyperFrames (licença Pixabay, uso comercial livre).
  - **impact:** na abertura.
  - **whoosh:** em cada troca de cena.
  - **click:** ao pegar e soltar o cartão e no botão do WhatsApp.
  - **pop:** na "venda fechada" e na mensagem.
  - **notification:** no lembrete.
  - **sparkle:** na meta.
  - **chime:** no endereço.
  - Volumes entre 0,07 e 0,3: os efeitos ficam só um pouco acima da trilha.
  - Cada efeito começa um pouco antes do momento, para o pico cair na ação: whoosh 0,165 s antes, click 0,053 s, pop 0,122 s, notification 0,232 s, chime 0,421 s.
- **Final:** `finalizar.sh` leva o vídeo pronto a -16 LUFS.

## Formatos

- **Site (16:9):** o texto fica à esquerda (a partir de x 120, 680 px de largura) e a tela à direita (x 860 a 1800).
- **Instagram (9:16):**
  - **Zona segura:** o essencial fica entre y 250 e y 1600; em cima e embaixo ficam os botões e a legenda do Instagram.
  - **Distribuição:** o texto fica em cima (até y 700) e a tela embaixo (y 735 a 1600), com letras e cartões maiores.
  - **Ajustes:** o funil mostra três etapas, e o celular da agenda sobe por baixo.
  - **Primeiros segundos:** no primeiro quadro a marca já aparece, e a frase da abertura está inteira antes de 1 s.

## Como montar um vídeo novo

1. Prepare a máquina com `source video/ambiente.sh`.
2. Copie `site-16x9/` e `instagram-9x16/` para pastas novas, ou edite as atuais. Troque os textos e as telas no `index.html`, mantendo as classes e o sistema de tempos do fim do arquivo (`entra`, `sai`, `camera`).
3. Se mudar a duração ou o tempo da música, ajuste `BPM`, `DUR` e a harmonia em `trilha/trilha.py`. Depois rode `python3 video/trilha/trilha.py` e reposicione os efeitos (`<audio>` no fim da composição).
4. Confira cada versão:
   - `$HF check`, dentro da pasta, tem que dar 0 erros;
   - `$HF snapshot --at 1,3,6,9.5,12,15` gera os quadros para olhar.
5. Renderize e finalize as duas versões com `bash video/renderizar.sh`.
6. Compare com o vídeo anterior em `finais/` antes de mostrar.

**Cuidados que já resolvemos:**
- `gsap.min.js` e as fontes ficam locais, porque o CDN pode estar bloqueado.
- O catálogo de músicas do HyperFrames precisa de conta na HeyGen, por isso a trilha é gerada.
- Elementos que se sobrepõem de propósito (a conversa do WhatsApp por cima do botão) levam `data-layout-allow-overlap`.
