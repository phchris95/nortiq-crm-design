# Nortiq CRM — design

Protótipo navegável (só a parte visual) do **Nortiq CRM**, sistema por assinatura para lojas de aquecedores e material hidráulico.

**Ver online:** https://phchris95.github.io/nortiq-crm-design/

## O que tem no protótipo
- **Login** por loja (cada loja com seu endereço próprio), com **Esqueci minha senha**
- **Loja:** Início, Orçamentos (funil, produtos do estoque, editar e excluir com desfazer), Clientes (novo, editar, excluir e restaurar, equipamentos, garantia e manutenção), Tarefas (nova, editar, excluir), Agenda (editar, marcar como feito, cancelar com motivo e técnicos), Estoque (ficha com histórico, movimentações, importação de planilha, desativar e baixa automática na venda), Faturamento (a receber, a pagar, recebimentos, estorno e cancelamento), Metas, Meu plano, Configurações (perfil, segurança, equipe, dados da loja e exportação dos dados)
- **Dono e funcionário:** o funcionário vê só o atendimento (sem faturamento, metas, plano e equipe)
- **Administração Nortiq** (login próprio com senha e código do celular): Visão geral, Contas assinantes (cobrança pelo Asaas ou pagamento direto por Pix, transferência ou dinheiro, e atendimento para ajudar a loja a entrar), Receitas (assinaturas do CRM e outros serviços: sites, automações, agentes de IA, com parcelas e contratos mensais), Notificações, Plano
- **Estados gerais:** loja nova com **Primeiros passos** e telas vazias que explicam o primeiro passo, telas carregando, sem conexão, erro ao salvar, erro ao abrir uma tela (com código para o suporte) e página não encontrada

Para ver outras situações, use o quadro **"Protótipo · ver outras situações"** embaixo do login: situação do login, entrar como dono ou funcionária, estado das telas (loja nova, carregando, sem conexão, erros), assinatura em dia, em atraso ou pausada, como a loja paga e o botão **Ir para o login da administração** (no protótipo, qualquer senha e qualquer código de 6 números funcionam).

Os dados são de exemplo (loja fictícia "Casa do Aquecedor"). O banco de dados, a API e as telas de verdade ficam em um repositório separado e privado. Já estão ligados ao banco: o login da loja e da administração, **Orçamentos**, **Clientes**, **Estoque**, **Tarefas**, **Agenda**, **Faturamento** e **Início**; as outras telas vão sendo ligadas uma a uma, seguindo este protótipo.

## Arquivos
- `index.html` — telas e dados de exemplo
- `support.js` — runtime que monta as telas (React)
- `ds/` — design system Nortiq (tokens de cor, tipografia, espaçamento e componentes); ver `ds/README.md`
- `PENDENCIAS.md` — o que foi desenhado em cada etapa, decisões e o que ficou para depois
- `logo.png` — símbolo branco com fundo transparente; `assets/logo-original.jpg` é o arquivo original
