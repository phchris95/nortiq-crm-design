# Nortiq Design System

**Nortiq Tecnologia** builds a management system / CRM for Brazilian retailers and technical service providers. The first audience is the owner-operator who sells **aquecedores** (gas, electric and solar water heaters) and **material hidráulico** — tubes, fittings, registros, pumps, reservoirs — and who also buys stock, quotes installers and closes the month. The product is meant to widen to general retail later, so this system is a general retail/CRM vocabulary with a heaters-and-plumbing accent, not a one-off.

The brand brief is explicit about the register: **profissional, direto, técnico, confiável** — a serious work tool, not an effervescent startup and not a colourful marketing agency. The user is a shop owner or a technical service provider, *not* a growth team. Clarity and big, direct numbers come before decorative charts. Combined with the product brief (*limpa, moderna e intuitiva… fluida mesmo para usuários com pouca familiaridade com tecnologia*), that gives the two rules everything else follows from: **44px controls, always-labelled fields, plain-Portuguese copy** and **one accent per screen, never more**.

Product UI language: **Portuguese (pt-BR)**. Documentation language: English, so any agent or developer can consume it.

---

## Sources given to me (and what they are)

| Source | What it actually is | How I used it |
|---|---|---|
| **`uploads/Nortiq_Identidade_Visual.md`** | **The official brand sheet** — palette (7 named colours with hexes), typography (Space Grotesk + IBM Plex Sans with weights), logo description and versions, application rules, and tone. | **Ground truth.** Every colour token, both type families and the "max 2 backgrounds / 1 accent per screen, no gradients, no heavy shadows" rule come from here verbatim. |
| 13 WhatsApp screenshots in `uploads/` (2026-09-22) | Phone screenshots of a **third-party Behance case study** for a product called *Fynix* — an AI finance dashboard by another designer (green palette, bird mark). | **Structure only**, and only where it doesn't conflict with the brand sheet: 248px grouped sidebar, one accent hero KPI tile, soft rounded cards on a tinted app background, pill filters, donut + grouped-bar pairing, thin-stroke icon chips, uppercase micro table headers. |
| Written brief | Company description; "clean, modern, intuitive, clear hierarchy, simple navigation, professional, responsive, fluid for low-tech users". | Control sizing, information density, copy strategy. |

**Nothing from the Fynix identity was reproduced** — not its green, not its bird mark, not its copy. That case study belongs to another designer and another company.

> **Palette history:** an earlier revision of this system used a warm copper/sand palette, built before the brand sheet arrived. It has been fully replaced by Azul Nortiq. No warm tokens remain — if you see copper or sand anywhere, it's stale cache.

### Not provided (and therefore absent)
- **No logo files.** The brand sheet *describes* the symbol (overlapping arcs/peaks converging on a point, thin geometric stroke; positive/negative/monochrome versions) but no artwork was supplied. **Nothing was drawn.** Wherever a mark would go, the wordmark is set in Space Grotesk 700 at `-0.03em`, and the reduced mark is the letter **N** in a navy tile. Send the three SVGs and only `assets/` + `Sidebar.jsx` change. See `guidelines/brand-wordmark.card.html`.
- **No font binaries.** Space Grotesk, IBM Plex Sans and IBM Plex Mono load from Google Fonts — all three are the real families named (IBM Plex Mono is my addition; see Typography).
- **No status colours in the brand sheet.** Success / warning / danger had to exist for an order-and-stock product, so they are **derived**, deliberately desaturated to stay inside the technical register (`--green-*`, `--amber-*`, `--red-*`). Info reuses Azul Nortiq. Flag if you want different hues.
- **No codebase, Figma file or repo.** The component inventory is authored from the brief, not extracted from a source library.
- **No product screens, photography or illustration.** The UI kit is a hi-fi proposal with plausible pt-BR shop data. Screens with no reference at all (Relatórios, Ajustes) are left blank on purpose with an on-screen disclaimer rather than invented.

---

## Index

**Root** — `styles.css` (the single entry point consumers link; `@import` lines only), `readme.md`, `SKILL.md`, `thumbnail.html`

**`tokens/`** — `fonts.css`, `colors.css`, `typography.css`, `spacing.css`, `radii.css`, `elevation.css`, `motion.css`, `base.css`

**`components/`** — 22 primitives in 5 groups. Each has `<Name>.jsx`, `<Name>.d.ts`, `<Name>.prompt.md`; each directory has one `@dsCard` showcase.
- `core/` — `Icon`, `Button`, `IconButton`, `Badge`, `Card`, `SectionHeader`
- `forms/` — `Input`, `Select`, `Checkbox`, `Switch`, `SearchField`
- `data/` — `StatCard`, `DataTable`, `BarChart`, `DonutStat`, `ProgressMeter`
- `navigation/` — `Sidebar`, `TopBar`, `Tabs`, `BottomNav`
- `feedback/` — `EmptyState`, `Dialog`

**`ui_kits/nortiq-app/`** — clickable recreation of the proposed **desktop** product: `index.html` (entry, navigable), `AppShell.jsx`, `Painel.jsx`, `Pedidos.jsx`, `Produtos.jsx`, `VendaRapida.jsx`, `Extras.jsx` (Estoque, Clientes, blank-screen disclaimer), `data.js`, `README.md`.

**`ui_kits/nortiq-mobile/`** — the same product on a 390×844 phone, bottom-tab navigation, sharing `nortiq-app/data.js`: `index.html`, `MobileShell.jsx`, `MPainel.jsx` (Painel + Pedidos), `MProdutos.jsx` (Produtos, Venda rápida, Mais, Clientes, Estoque), `README.md`.

**`guidelines/`** — foundation specimen cards (Colors, Type, Spacing, Surfaces, Brand).

### Intentional additions
No source defined a component inventory, so the set is a from-scratch standard kit sized to a retail back-office. Three additions worth naming:
- **`Icon`** — a wrapper over Lucide so icon usage is enforced and colourable; without it, contributors hand-roll SVG (which the brand sheet forbids).
- **`ProgressMeter`** — stock level is the most-repeated visual in this product, so it's a primitive, not a one-off.
- **`BottomNav`** — the mobile app needs a primary navigation and `Sidebar` doesn't fit 390px; it mirrors the sidebar's active treatment so both read as one system.
- **IBM Plex Mono** — the sheet names no mono face, but SKUs, order numbers and keyboard hints need one; Plex Mono is the family-mate of the named body face, so it's the lowest-risk pick.

Deliberately **not** built (no evidence of need, would be invention): Toast, Tooltip, Avatar, Accordion, Breadcrumb, DatePicker, Stepper, Pagination-as-component.

---

## CONTENT FUNDAMENTALS

**Language.** pt-BR, always. No English in the product UI — not "dashboard" (→ *Painel*), not "checkout" (→ *Finalizar venda*), not "insights". The one exception is untranslatable domain shorthand the audience already uses: *SKU*, *PIX*, *PVC*, *cv*, *un*.

**Person.** Speak to the user as **você**, implicitly — imperative verbs carry most instructions, so the pronoun rarely needs to appear: *"Cadastre seu primeiro produto"*, *"Repor até sexta"*, *"Gerar pedido de compra"*. The system never says "eu" / "nós", and never refers to itself by name inside the UI ("O Nortiq sugere…" is wrong; "Sugestão de compra" is right).

**Casing.** Sentence case everywhere — buttons, titles, menu items, dialog titles. `Novo pedido`, not `Novo Pedido` or `NOVO PEDIDO`. The only uppercase is the 11px overline / table-header micro-type (`VISÃO GERAL`, `PRODUTO`, `SKU`), where uppercase + 0.1em tracking *is* the label mechanism.

**Length.** Buttons 1–3 words. Table headers 1–2 words. Empty-state description ≤ 2 short sentences, always ending by naming the next action. Card subtitles are factual, not motivational: *"1 a 30 de setembro"*, *"Atualizado há 3 minutos"*, *"Loja Centro · última contagem em 24/09"*.

**Tone.** Plain, concrete, calm, shop-counter Portuguese. Assume competence at the *business*, zero patience for software vocabulary. State facts and consequences, not system internals.

| Avoid | Prefer |
|---|---|
| "Erro 422: payload inválido" | "Falta preencher o preço de venda." |
| "Sincronizar inventário SKU-level" | "Atualizar o estoque da loja" |
| "Dashboard de analytics avançado" | "Como suas vendas estão indo" |
| "Vamos decolar! 🚀" | "Pedido registrado." |
| "Confirmar operação?" | "3 itens serão retirados do estoque da loja Centro." |

**Numbers and money.** pt-BR formatting, always: `R$ 1.890,00` (dot thousands, comma decimals), `R$ 84,3 mil` when abbreviating, dates as `30/09` or `1 a 30 de setembro`. Money and counts use tabular figures (`.nq-num`) and are right-aligned in tables. Units follow the number with a space: `6 un`, `1/2 cv`, `7500 W`, `25 mm`. Per the brand sheet, the number is the hero: set KPIs large (38px display, 700) and skip the decorative chart when a number will do.

**Status vocabulary** (fixed — do not paraphrase per screen): *Pago*, *Aguardando pagamento*, *Em rota*, *Entregue*, *Cancelado*, *Rascunho* for orders; *Saudável*, *Abaixo do mínimo*, *Crítico* for stock.

**Emoji: never** — the brand sheet says so explicitly, and it applies to UI, empty states and docs alike. Status is a coloured dot + word, never 🟢/🔴. No exclamation marks except in a genuine warning.

**Vibe.** A well-run counter: everything labelled, nothing shouting, the number you need already on screen.

---

## VISUAL FOUNDATIONS

**The one-line summary.** Branco-gelo paper, Azul Nortiq as the only action colour, flat 20px cards with hairline cinza-névoa rings and barely-there cool shadows, Space Grotesk numbers over IBM Plex Sans text, thin geometric icons, motion short enough to go unnoticed.

**Colour.** Seven official colours, and everything else is a derived step from them — see `guidelines/color-oficial.card.html`.
- **Azul Nortiq** `#0E2A47` (`--navy-500`) is the primary and the *only* colour that means "action". Hover is `--navy-600 #0A2139`, press `--navy-700 #071B2E`. Never tint a button by lowering opacity.
- **Tinta** `#0A1826` (`--gray-900`) is ink and the darkest surface. **Branco-gelo** `#F7F8FA` (`--gray-50`) is the app background; white `--gray-0` is the card surface. **Cinza-névoa** `#E3E6EB` (`--gray-200`) is every divider, table rule and card ring. **Cinza-médio** `#6B7280` (`--gray-500`) is secondary text and every label. **Azul-neblina** `#DCE4EE` (`--navy-100`) is subtle highlight, hover and badge fill — it's what the active sidebar row and the "Em rota" badge are made of.
- Neutrals are **cool**. There is no warm grey, no beige and no pure black anywhere.
- Status hues are **derived and desaturated**: `--green-*` success, `--amber-*` warning, `--red-*` danger, and info reuses Azul Nortiq. They appear only in badges, meters and error text — never as a surface or a button.
- **Application rule, straight from the sheet:** max **two** background colours per screen (`--surface-app` + `--surface-card`), and **one** accent/action colour per screen. If the hero KPI tile is navy-filled, the primary button is still navy (it's the only action) — but nothing else gets a fill. **No gradients. No heavy shadows. No "generic SaaS" vibrant purple/blue.**

**Typography.**
- **Space Grotesk** (`--font-display`) — titles, wordmark, and the dashboard's featured numbers. **Weights 500 and 700 only**, tracking `-0.015em` to `-0.03em`.
- **IBM Plex Sans** (`--font-sans`) — body 15px/400, UI and tables 13px/500, section titles 17px/600, caption 12px, overline 11px uppercase. **Weights 400, 500, 600 only.**
- **IBM Plex Mono** (`--font-mono`) — SKUs, order numbers, keyboard hints, token names. *My addition; flag if unwanted.*
- Floor: **12px**, and 11px only for uppercase overlines. Line height 1.5 for prose, 1.25–1.35 for UI, 1.08 for display. Money/quantities always `.nq-num`.
- All three load from Google Fonts because no binaries were supplied — if Nortiq licenses files, only `tokens/fonts.css` changes.

**Spacing & layout.** 4px base. 16px card gap, 24px page gutter and section spacing, 12–14px inside cards. Sidebar fixed 248px; top bar 64px min; content max 1440px. Grid tracks use `minmax(0,1fr)` so tables can shrink — the system is responsive and no content block has a fixed pixel width. Controls: 34 / 44 / 52px, **44px default** because the system is used standing up, often on a tablet; `--tap-min` is 44px and nothing interactive goes below it.

**Backgrounds.** Flat tints only — branco-gelo and white. **No gradient backgrounds** (the sheet forbids them), no full-bleed photography, no illustration, no pattern, no grain. The single decorative flourish in the whole system is one 10%-white circle bleeding off the corner of the navy hero KPI tile. Until Nortiq supplies product photography, product identity is a thin Lucide glyph in an azul-neblina tile — never a stock photo or a generated image.

**Cards.** 20px radius (`--radius-card`), white surface, **1px inset ring** in cinza-névoa (`--ring-card`) plus a very light cool shadow (`--shadow-sm`), 20px padding. That's the whole recipe. Variants: `sunken` (gray-100 + border, for groups inside a card), `accentSoft` (azul-neblina, for calm highlights), `accent` (navy fill, hero only), `dark` (tinta, the plan card), `outline`. **Never a coloured left border.** Never more than two levels of card nesting.

**Borders.** Hairlines, always 1px, always cool: gray-200 for subtle (table rules, card rings, dividers), gray-300 for control borders, gray-400 only where a control must feel heavier. Dashed borders appear twice: the PDV total separator and the 44px tap-target annotation.

**Shadows.** Deliberately faint and cool — `rgba(10,24,38,.04–.16)`, per "evitar sombras pesadas". `xs` on buttons, `sm` on cards, `md` on popovers, `lg` on hover lift, `xl` on modals, `--shadow-accent` (navy at 18%) only under navy fills. One inner shadow in the system: the donut's centre well. No neumorphism, no glow.

**Radii.** `xs 6` (inline chips, kbd), `sm 10` (controls, buttons, tiles), `md 14` (sub-panels), `lg 20` (cards), `xl 28` (modals), `pill 999` (badges, search field, icon buttons, segmented tabs, meters). Pills plus 20px cards are the shape signature — geometric and even, echoing the symbol's thin-stroke geometry.

**Hover states.** Surfaces step one tint (`transparent → gray-50 → gray-100`); filled buttons step one shade darker navy; nav rows take gray-100 unless active (azul-neblina stays); interactive cards lift 2px to `--shadow-lg`; chart groups dim siblings to 45%. **Opacity is never the hover mechanism for a control** — only for chart de-emphasis.

**Press states.** `transform: scale(.975)` plus the next darker navy step. No ripple, no bounce, no colour flash.

**Focus.** `--focus-ring`: 3px navy glow at 22% (`box-shadow`, never `outline`), plus the field border switching to navy-500. Visible on every interactive element.

**Animation.** Short, functional, unremarkable. 140ms control colour, 220ms surfaces/modals, 360ms bars and meters filling. Easing `cubic-bezier(.2,.8,.25,1)` or `cubic-bezier(.16,1,.3,1)`. Modal entrance: fade + 12px rise + 0.98 scale. **No bounce, no spring, no ambient loop, no scroll-jacking.** Everything collapses to 0 under `prefers-reduced-motion`.

**Transparency & blur.** Two places only: the modal overlay (tinta `rgba(10,24,38,.52)` + `blur(8px)`) and the white flourish/dividers inside the navy tile. No frosted panels, no glassmorphism, no protection gradients — text always sits on a solid fill, which is why contrast holds at 4.5:1 without tricks.

**Fixed elements.** Sidebar and top bar persist; the product-detail panel and the PDV cart are `position: sticky` at 16px. Modals are absolutely positioned inside the app frame so the kit stays self-contained.

**Data visualisation.** Near-monochrome by design — the brand asks for clear numbers, not decorative graphics. The ramp is fixed: `navy-500 → navy-300 → navy-200 → gray-400 → navy-100 → gray-300`, on gray-200 grid lines. Bars get a 4px top radius and 10–18px width; donuts a 14–20px ring with the total in the well; meters a 6–8px pill track. Max 5 slices, max 2 bar series. Colour enters a chart only when it encodes *status*. Tooltips are tinta with gray-50 text at 12px.

---

## ICONOGRAPHY

**System: Lucide, pinned.** `lucide-static@0.544.0`, loaded from unpkg and applied as a **CSS mask** so every glyph inherits `currentColor`:

```jsx
<Icon name="flame" size={18} />   /* components/core/Icon.jsx */
```

- **Substitution flag:** no icon files were provided. The brand sheet requires icons in the spirit of the symbol — *traço fino, geométrico* — and **Lucide** (uniform ~2px stroke, geometric construction, rounded caps) is the closest CDN-available match, so it is the substitution. If Nortiq commissions its own set, drop the SVGs into `assets/icons/` and rewrite `Icon.jsx`; nothing else changes.
- **Format:** single-colour outline SVG via mask. No icon font, no sprite, no PNG icon. Sizes: 11–13px in badges, 15–17px in controls, 18px default, 22–26px in empty states and dialogs.
- **Colour:** icons inherit text colour. In nav they are gray-500, turning navy-500 when active. Inside azul-neblina tiles they are navy-500/600. Never two colours, never a gradient, never a shadow, **never a 3D effect** (explicitly forbidden).
- **Chips:** icons often sit in a `--radius-sm` or `--radius-pill` container filled gray-100 or azul-neblina.
- **The working set for this domain:** `flame` (aquecedores), `droplets` / `shower-head` (água), `wrench` (hidráulica), `cylinder` (tubos), `git-fork` (conexões), `circle-dot` (registros), `fan` (bombas), `container` (reservatórios), `sun` (solar), `package` / `boxes` / `package-open`, `truck`, `receipt`, `shopping-cart`, `users` / `store`, `layout-dashboard`, `chart-no-axes-column`, `trending-up`, `triangle-alert`, `search`, `plus`, `minus`, `funnel`, `bell`, `settings`, `circle-help`, `printer`, `eye`, `chevron-*`.
- **Never:** hand-rolled SVG paths, emoji-as-icon, Unicode dingbats (✓ ✗ ★ → use `check`, `x`, `star`), coloured/duotone/3D icons, or an icon-only button without a `label`.
- **Unicode that IS allowed** (typographic, not iconographic): `·` as a metadata separator, `−` as a true minus in totals, `×` in "3× item".

---

## Using this system

```html
<link rel="stylesheet" href="styles.css">
<script src="_ds_bundle.js"></script>
```
```jsx
const { Button, Card, StatCard, DataTable, Sidebar } = window.NortiqDesignSystem_5a3b8e;
```

Read `<Component>.prompt.md` next to any component for its "what & when", a usage snippet and its variants. Start from `ui_kits/nortiq-app/index.html` for a full screen.
