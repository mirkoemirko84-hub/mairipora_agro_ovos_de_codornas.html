# 🌾 Mairiporã Agro • Manual Técnico e Comercial da Esteira

Bem-vindo ao repositório oficial de gestão e faturamento do ecossistema **Mairiporã Agro**. Este documento serve como guia estratégico para a operação de balcão e triagem de pedidos online, blindando o sistema contra quebras de estoque e bloqueios de comunicação.

---

## 📊 1. Engenharia de Preços e Margens (Parceria Estratégica)
O sistema foi projetado para atuar em duas frentes distintas, atendendo públicos com necessidades diferentes e garantindo fluxo de caixa contínuo:

*   🍳 **Balcão Tradicional (Culinária):** Cartelas de ovos *in natura* comercializadas pelo preço cheio de **R\$ 13,00**. Focado em famílias e pessoas que gostam de cozinhar.
*   🛒 **Atacado de Parceiro Terceirizado:** Venda em lote para o produtor associado pelo valor estratégico de **R\$ 11,00** por cartela bruta, gerando giro rápido de maquinário.
*   🫙 **Linha de Conservas Temperadas (Praticidade/Solo):** Focado em pessoas que moram sozinhas ou buscam conveniência. Os ovos do atacado recebem manejo artesanal e são vendidos em formato Refil:
    *   **Refil Tempero Básico (30 un):** Comercializado a **R\$ 17,00** (R\$ 11,00 do custo do ovo + R\$ 6,00 de lucro líquido puro para o parceiro).
    *   **Refil Algo a Mais (30 un):** Comercializado a **R\$ 23,00** (agrega margem cheia com insumos especiais).
    *   **Linha Corporate (Pote de Vidro):** Quantidades e valores sob consulta direta.

---

## 🔬 2. Critério Técnico de Maturação (Regra dos 4 Dias)
Para garantir o direito de informar o padrão de excelência gastronômica aos clientes, os lotes de conserva seguem rigorosamente a seguinte linha do tempo:
1.  **Dias 1 e 2:** Manejo, cozimento e descasque técnico dos ovos.
2.  **Dias 3 e 4:** Período de repouso e maturação hermética para que o tempero incorpore perfeitamente na degustação. Total do ciclo: **4 dias**.

---

## 🛡️ 3. Política Antibanimento e Manobra de WhatsApp
Para neutralizar o "faro" do algoritmo antifraude da Meta contra robôs de disparo em massa, o fluxo foi descentralizado em duas etapas nativas:
*   O arquivo `conservas.html` envia os parâmetros leves de quantidade para a página intermediária `zap.html`.
*   A página `zap.html` monta o texto dinamicamente e vincula à API oficial `https://wa.me`. 
*   **Segurança:** O clique do botão parte do navegador do próprio cliente, simulando um comportamento 100% humano e deixando o número comercial imune a bloqueios (B.O. de DNS ou NXDOMAIN).

---

## 📋 4. Scripts de Atendimento e Comando de Guarita

O operador do sistema detém o comando absoluto para dar o "OK" final na esteira. Ao receber a mensagem automática de dados preenchidos pelo cliente no WhatsApp, o operador aplica os scripts oficiais abaixo após o check-list físico:

### 📩 Mensagem A: Confirmação e Check-list de Estoque Liberado
*(Enviar se o produto estiver disponível para pronta entrega)*

```text
🌾 Mairiporã Agro • Status da Esteira Sequencial 🌾

Olá, chefe! Recebemos os dados do seu pedido enviados pelo site. 

🔍 Status Atual:
🟢 Pedido aceito e em preparação!

O seu lote já passou pelo nosso check-list técnico de balcão e foi aprovado para separação. Estamos embalando com todo o cuidado para garantir a máxima qualidade. Logo avisamos assim que estiver pronto para retirada/envio!

Obrigado por apoiar o comércio local • O pequeno produtor agradece! 🍳🫙
```

### 🔄 Mensagem B: Substituição Ativa de Demanda (Estoque Zerado)
*(Enviar se as cartelas de balcão acabarem, migrando o cliente para os refis prontos de maior lucro)*

```text
🌾 Mairiporã Agro • Informação de Esteira 🌾

Olá, chefe! Tudo bem? Passando para te dar uma posição sobre a sua esteira de pedido.

Devido à altíssima procura de hoje, o nosso lote de cartelas de ovos in natura esgotou no balcão técnico mais cedo! 

🚀 Para você não ficar sem produto: Nós temos disponível agora na esteira o nosso Refil de Conserva Temperada (Básico ou Algo a Mais). Eles já vêm totalmente cozidos, descascados e maturados no tempero por 4 dias — praticidade máxima, pronto para consumo imediato!

Como você já realizou o pagamento de R$ 13,00 pela cartela de balcão:
👉 Você pode migrar para o Refil Tempero Básico (que custa R$ 17,00) pagando apenas a diferença de R$ 4,00 aqui pelo Zap mesmo!

O que acha de aproveitarmos essa facilidade para você conhecer a nossa linha gourmet e não perder a viagem? Se preferir o reembolso do Pix, fazemos na hora para você sem burocracia.

No aguardo do seu comando, chefe! 🦉💰
```

### ⏳ Mensagem C: Retenção por Ciclo de Maturação
*(Enviar caso o pedido entre durante o período de descanso obrigatório de 4 dias das conservas)*

```text
🌾 Mairiporã Agro • Status da Esteira Sequencial 🌾

Olá, chefe! Recebemos os dados do seu pedido enviados pelo site. 

🔍 Status Atual:
🟡 Aguardando próxima produção / Lote em maturação!

O seu pedido foi registrado! Para garantir o padrão de excelência da Mairiporã Agro, informamos que este lote está finalizando o ciclo técnico de repouso e cozimento. 

⏳ Previsão de liberação: [Inserir o prazo, ex: Próxima Terça-feira]

Dessa forma, garantimos que o tempo da natureza seja respeitado e que o tempero incorpore perfeitamente para a sua degustação! Obrigado por aguardar e apoiar o comércio local! 🍳🫙
```

---
*Mairiporã Agro © 2026 • Sistema de Gestão Sequencial Blindado.*
