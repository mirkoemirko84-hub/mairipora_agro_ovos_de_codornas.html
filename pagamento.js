document.addEventListener('DOMContentLoaded', () => {
    // 1. Recupera a quantidade e o total salvos na página anterior (index.html)
    const qtd = localStorage.getItem('compra_qtd');
    const total = localStorage.getItem('compra_total');

    // 2. Elementos da tela de pagamento
    const txtQtd = document.getElementById('txt-resumo-qtd');
    const txtTotal = document.getElementById('txt-resumo-total');
    const btnWhats = document.getElementById('btn-whatsapp');

    // Se o cliente tentar acessar o pagamento sem escolher a quantidade, joga ele de volta pro início
    if (!qtd || !total) {
        window.location.href = 'index.html';
        return;
    }

    // 3. Atualiza os textos da tela com os valores reais da compra
    if (txtQtd) txtQtd.innerText = `${qtd} Cartela(s)`;
    if (txtTotal) txtTotal.innerText = `R$ ${total}`;

    // 4. Configura o botão do WhatsApp dinamicamente com os dados do pedido
    const numeroWhats = "5511999999999"; // ⚠️ COLOQUE SEU NÚMERO DO WHATSAPP COM DDD AQUI
    const mensagem = encodeURIComponent(`Olá! Fiz um pedido de ${qtd} cartela(s) de Ovos de Codorna Jumbo no valor total de R$ ${total}. Segue o comprovante do Pix em anexo.`);
    
    if (btnWhats) {
        btnWhats.href = `https://wa.me{numeroWhats}?text=${mensagem}`;
    }
});

// 5. Função para o botão "Copiar Código PIX"
function copiarPix() {
    const códigoPix = "3d4ee862-439d-481d-9f5b-07d69a7182f6";
    
    navigator.clipboard.writeText(códigoPix).then(() => {
        alert("📋 Código PIX copiado com sucesso! Abra o aplicativo do seu banco para colar.");
    }).catch(err => {
        console.error("Erro ao copiar o PIX: ", err);
        alert("Não foi possível copiar automaticamente. Por favor, selecione o texto e copie manualmente.");
    });
}
