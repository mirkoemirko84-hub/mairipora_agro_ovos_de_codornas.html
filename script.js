// 1. RELÓGIO DINÂMICO EM TEMPO REAL
function iniciarRelogio() {
    setInterval(function() {
        var agora = new Date();
        var h = String(agora.getHours()).padStart(2, '0');
        var m = String(agora.getMinutes()).padStart(2, '0');
        var s = String(agora.getSeconds()).padStart(2, '0');
        var el = document.getElementById('live-clock');
        if (el) { el.innerHTML = h + ":" + m + ":" + s; }
    }, 1000);
}

// 2. FUNÇÃO DO BOTÃO COPIAR PIX
function copiarPix() {
    var campo = document.getElementById("chavePixTexto");
    if (campo) {
        campo.select();
        campo.setSelectionRange(0, 99999);
        try {
            navigator.clipboard.writeText(campo.value);
        } catch (err) {
            document.execCommand("copy");
        }
        var btn = document.getElementById("btnCopiarPix");
        if (btn) {
            btn.innerHTML = "✅ Código Copiado!";
            btn.style.backgroundColor = "#27ae60";
            setTimeout(function() {
                btn.innerHTML = "📋 Copiar Código PIX";
                btn.style.backgroundColor = "#007bff";
            }, 2000);
        }
    }
}

// 3. FUNÇÃO DA BARRA DE PROGRESSO E WHATSAPP
function abrirJanelaCompartilhar() {
    var container = document.getElementById("container-progresso");
    var barra = document.getElementById("barra-progresso");
    var texto = document.getElementById("texto-progresso");
    
    if (container && barra && texto) {
        container.style.display = "block";
        barra.style.width = "0%";
        texto.innerHTML = "🔌 Conectando ao WhatsApp...";

        var progresso = 0;
        var acao = setInterval(function() {
            progresso += 25;
            barra.style.width = progresso + "%";

            if (progresso >= 100) {
                clearInterval(acao);
                setTimeout(function() {
                    container.style.display = "none";
                    var cel = "5511964856312"; 
                    var msg = "Olá! Quero confirmar meu pedido de ovos artesanais de codorna Jumbo! 🥚";
                    window.open("https://wa.me" + cel + "?text=" + encodeURIComponent(msg), "_blank");
                }, 200);
            }
        }, 100);
    }
}

// 4. SISTEMA SECRETO DO PAINEL ADM
let cliques = 0;
function revelarPainel() {
    cliques++;
    if (cliques >= 5) {
        var btnAdm = document.getElementById('botao-secreto-adm');
        if (btnAdm) {
            btnAdm.style.display = 'block';
            btnAdm.scrollIntoView({ behavior: 'smooth' });
        }
    }
}

// DISPARAR O RELÓGIO AUTOMATICAMENTE
window.onload = iniciarRelogio;
