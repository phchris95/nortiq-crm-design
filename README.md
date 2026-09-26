# Nortiq CRM — design

Protótipo navegável (só a parte visual) do **Nortiq CRM**, sistema por assinatura para lojas de aquecedores e material hidráulico.

**Ver online:** https://phchris95.github.io/nortiq-crm-design/

## O que tem no protótipo
- **Login** por loja (cada loja com seu endereço próprio), com **Esqueci minha senha**
- **Loja:** Início, Orçamentos (funil), Clientes (equipamentos, garantia e manutenção), Tarefas, Faturamento, Metas, Meu plano, Configurações (perfil, segurança, equipe, dados da loja e exportação dos dados)
- **Dono e funcionário:** o funcionário vê só o atendimento (sem faturamento, metas, plano e equipe)
- **Administração Nortiq** (login próprio com senha e código do celular): Visão geral, Contas assinantes (cobrança pelo Asaas ou pagamento direto por Pix, transferência ou dinheiro, e atendimento para ajudar a loja a entrar), Notificações, Plano

Para ver outras situações, use o quadro **"Protótipo · ver outras situações"** embaixo do login: situação do login, entrar como dono ou funcionária, assinatura em dia, em atraso ou pausada, como a loja paga e o botão **Ir para o login da administração** (no protótipo, qualquer senha e qualquer código de 6 números funcionam).

Os dados são de exemplo (loja fictícia "Casa do Aquecedor"). Banco de dados e back-end ainda não foram feitos.

## Arquivos
- `index.html` — telas e dados de exemplo
- `support.js` — runtime que monta as telas (React)
- `ds/` — design system Nortiq (tokens de cor, tipografia, espaçamento e componentes); ver `ds/README.md`
- `PENDENCIAS.md` — telas e fluxos que ainda faltam desenhar
- `logo.png` — símbolo branco com fundo transparente; `assets/logo-original.jpg` é o arquivo original
