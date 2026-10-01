# Nortiq CRM — design

Protótipo navegável (só a parte visual) do **Nortiq CRM**, sistema por assinatura para lojas de aquecedores e material hidráulico.

**Ver online:** https://phchris95.github.io/nortiq-crm-design/

## O que tem no protótipo
- **Login** por loja (cada loja com seu endereço próprio), com **Esqueci minha senha**
- **Loja:** Início, Orçamentos (funil, produtos do estoque, editar e excluir com desfazer), Clientes (novo, editar, excluir e restaurar, equipamentos, garantia e manutenção), Tarefas (nova, editar, excluir), Agenda (editar, marcar como feito, cancelar com motivo e técnicos), Estoque (ficha com histórico, movimentações, importação de planilha, desativar e baixa automática na venda), Faturamento (a receber, a pagar, recebimentos, estorno e cancelamento), Metas, Meu plano (os três planos, Básico, Profissional e Pro, por mês ou por ano, com Trocar de plano), Configurações (perfil com Google Agenda e Usar sem internet, segurança, equipe por setor, dados da loja e exportação dos dados)
- **Dono e setores da equipe:** o dono vê tudo; cada funcionário fica num setor com cor (Vendas, Técnicos de campo, Estoque e compras, Administrativo ou outro criado pelo dono), e o dono escolhe o que cada setor vê. Mude o setor da Camila em Configurações, Equipe e entre como ela para ver o menu mudar
- **Planos:** no Básico, Metas e Relatórios aparecem com a etiqueta "Profissional" e levam à troca de plano
- **Administração Nortiq** (login próprio com senha e código do celular): Visão geral, Contas assinantes (cobrança pelo Asaas ou pagamento direto por Pix, transferência ou dinheiro, e atendimento para ajudar a loja a entrar), Receitas (assinaturas do CRM e outros serviços: sites, automações, agentes de IA, com parcelas e contratos mensais), Notificações, Planos (os três, com lojas e receita de cada um), **Mapa de assinantes** (Brasil por estado e mundo por país, com cidades e lojas) e **Prospecção** (busca de lojas no Google, lista de leads com situação e anotações, mensagens prontas que abrem no WhatsApp Web)
- **Estados gerais:** loja nova com **Primeiros passos** e telas vazias que explicam o primeiro passo, telas carregando, sem conexão, erro ao salvar, erro ao abrir uma tela (com código para o suporte) e página não encontrada

Para ver outras situações, use o quadro **"Protótipo · ver outras situações"** embaixo do login: situação do login, entrar como dono ou funcionária, estado das telas (loja nova, carregando, sem conexão, erros), assinatura em dia, em atraso ou pausada, como a loja paga e o botão **Ir para o login da administração** (no protótipo, qualquer senha e qualquer código de 6 números funcionam).

Os dados são de exemplo (loja fictícia "Casa do Aquecedor"). O banco de dados, a API e as telas de verdade ficam em um repositório separado e privado. Já estão ligados ao banco: o login da loja e da administração, **Orçamentos**, **Clientes**, **Estoque**, **Tarefas**, **Agenda**, **Faturamento**, **Início**, **Configurações**, **Meu plano** e, no painel Nortiq, **Visão geral** e **Contas assinantes**; as outras telas vão sendo ligadas uma a uma, seguindo este protótipo.

## Arquivos
- `index.html` — telas e dados de exemplo
- `support.js` — runtime que monta as telas (React)
- `ds/` — design system Nortiq (tokens de cor, tipografia, espaçamento e componentes); ver `ds/README.md`
- `PENDENCIAS.md` — o que foi desenhado em cada etapa, decisões e o que ficou para depois
- `mapas.js` — contornos dos estados do Brasil e dos países, para o Mapa de assinantes
- `logo.png` — símbolo branco com fundo transparente; `assets/logo-original.jpg` é o arquivo original
