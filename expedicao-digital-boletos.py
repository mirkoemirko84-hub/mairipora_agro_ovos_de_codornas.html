# -*- coding: utf-8 -*-
import os
from datetime import datetime, timedelta
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, Image
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib import colors

def gerar_boleto_pdf():
    nome_arquivo = "boleto_mairipora_agro.pdf"
    
    # Nome da imagem correspondente ao que salvamos na mesma pasta
    caminho_qrcode_png = "qrcode-para-boletos.png"
    
    # -------------------------------------------------------------------------
    # PARAMETRIZAÇÃO DO SISTEMA
    # -------------------------------------------------------------------------
    CONDICAO_AVISTA = False  
    VALOR_TESTE = "R$ 1,99"   
    
    COD_BANCO = "237-7"
    NOME_BANCO = "Bradesco"
    COR_BANCO = colors.HexColor('#cc092f') 
    
    # -------------------------------------------------------------------------
    # Regra de Negócio: Vencimento Comercial (21 dias)
    # -------------------------------------------------------------------------
    data_doc_str = "23/09/2026"
    data_doc_obj = datetime.strptime(data_doc_str, "%d/%m/%Y")
    
    if CONDICAO_AVISTA:
        data_venc_str = "A VISTA"
    else:
        data_venc_obj = data_doc_obj + timedelta(days=21)
        data_venc_str = data_venc_obj.strftime("%d/%m/%Y")
    
    doc = SimpleDocTemplate(
        nome_arquivo,
        pagesize=letter,
        rightMargin=30,
        leftMargin=30,
        topMargin=25,
        bottomMargin=25,
        title="Mairiporã Agro - Faturamento Inovador V2"
    )
    
    story = []
    styles = getSampleStyleSheet()
    
    style_normal = ParagraphStyle('NormalCustom', parent=styles['Normal'], fontSize=8, leading=10)
    style_bold = ParagraphStyle('BoldCustom', parent=styles['Normal'], fontSize=8, leading=10, fontName='Helvetica-Bold')
    style_title = ParagraphStyle('TitleCustom', parent=styles['Normal'], fontSize=14, leading=18, fontName='Helvetica-Bold', alignment=1)
    style_sub = ParagraphStyle('SubCustom', parent=styles['Normal'], fontSize=8.5, leading=11, alignment=1, textColor=colors.HexColor('#666666'))
    style_right_bold = ParagraphStyle('RightBoldCustom', parent=styles['Normal'], fontSize=9, leading=11, fontName='Helvetica-Bold', alignment=2)
    style_obs = ParagraphStyle('ObsCustom', parent=styles['Normal'], fontSize=7.5, leading=11)
    style_agradecimento = ParagraphStyle('AgraCustom', parent=styles['Normal'], fontSize=8.5, leading=12, fontName='Helvetica-Oblique', alignment=1, textColor=colors.HexColor('#1e293b'))

    # 1. Cabeçalho
    story.append(Paragraph("<b>Mairiporã Agro - Sistema de Faturamento</b>", style_title))
    story.append(Paragraph("Ambiente de Homologação / Teste Técnico Local via VS Code & Python", style_sub))
    story.append(Spacer(1, 10))
    
    # 2. Recibo do Sacado (Topo)
    dados_topo = [
        [Paragraph(f"<b>Beneficiário:</b> Mairiporã Agro (Operação via {NOME_BANCO})", style_normal), Paragraph(f"<b>Vencimento:</b> {data_venc_str}", style_bold if CONDICAO_AVISTA else style_normal)],
        [Paragraph("<b>Pagador:</b> Cliente de Teste Homologação", style_normal), Paragraph("<b>Número do Pedido:</b> #749201", style_normal)],
        [Paragraph("<b>Espécie:</b> R$ (Real)", style_normal), Paragraph(f"<b>Valor Cobrado:</b> {VALOR_TESTE}", style_right_bold)]
    ]
    
    t_topo = Table(dados_topo, colWidths=[350, 200])
    t_topo.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), colors.HexColor('#f8fafc')),
        ('BOX', (0,0), (-1,-1), 1, colors.HexColor('#cbd5e1')),
        ('INNERGRID', (0,0), (-1,-1), 0.5, colors.HexColor('#e2e8f0')),
        ('PADDING', (0,0), (-1,-1), 5),
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
    ]))
    story.append(t_topo)
    story.append(Spacer(1, 10))
    
    story.append(Paragraph("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - Recorte na Linha Pontilhada - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -", ParagraphStyle('Corte', fontSize=7, alignment=1, textColor=colors.HexColor('#94a3b8'))))
    story.append(Spacer(1, 10))
    
    # 3. Ficha de Compensação Bancária com o QR Code no Topo Esquerdo
    if os.path.exists(caminho_qrcode_png):
        img_qrcode = Image(caminho_qrcode_png, width=45, height=45)
    else:
        img_qrcode = Paragraph("[Aguardando qrcode-para-boletos.png]", style_normal)
    
    linha1 = [
        img_qrcode,
        Paragraph(f"<b>{NOME_BANCO} &nbsp; {COD_BANCO}</b>", ParagraphStyle('BancoReg', fontSize=12, fontName='Helvetica-Bold', textColor=COR_BANCO, alignment=0)),
        Paragraph("23791.79001 01043.513184 91020.150008 7 98480000008500", ParagraphStyle('Linha', fontSize=8.5, fontName='Helvetica-Bold', alignment=2))
    ]
    
    texto_observacoes = (
        "<b>Campo Obs (Controle de Produção e Romaneio):</b><br/>"
        "[  ] Ovos de codornas IN NATURA — Qtd: ________ cartelas<br/>"
        "[  ] CONSERVAS (Vendas Normais / Estilo Refil) — Qtd: ________ SACOS PLÁSTICOS<br/>"
        "[  ] CONSERVAS (Vendas Especiais / Encomendas) — Qtd: ________ VIDRO / POTES LINHA ESPECIAIS<br/>"
        "[  ] Diversos: esterco de codornas (<b>RETIRADA A COMBINAR POR VOLUME/PESO</b>) — Qtd: ________ KILOS<br/>"
        "<b>Logística de Expedição:</b> [ X ] ENTREGA EM MÃOS  —  Data do Recebimento: ____/____/____<br/>"
        f"<font color='{COR_BANCO.hexval()}'><b>[ X ] ASSINATURA DIGITAL VIA CELULAR DE ACEITE (MOBILE-ID):</b></font><br/>"
        "<i>Status: Confirmado via aplicativo logístico — Hash: 9a8b7c6d_MairiporaAgro_2026</i>"
    )
    
    tabela_boleto_dados = [
        linha1,
        [Paragraph("<b>Local de Pagamento:</b> Qualquer Banco ou Casa Lotérica até o vencimento", style_normal), "", Paragraph(f"<b>Vencimento:</b> {data_venc_str}", style_bold)],
        [Paragraph("<b>Beneficiário:</b> Mairiporã Agro - JOSÉ CARLOS SUGUIMOTO - (Conta de Depósito PF)", style_normal), "", Paragraph("<b>Agência/Código Beneficiário:</b> 0449 / 0080619-6", style_normal)],
        [Paragraph(f"<b>Data do Doc:</b> {data_doc_str}", style_normal), Paragraph("<b>Nº Documento:</b> 749201", style_normal), Paragraph("<b>Espécie Doc:</b> DM", style_normal)],
        [Paragraph("<b>Uso do Banco:</b>", style_normal), Paragraph("<b>Carteira:</b> 109", style_normal), Paragraph("<b>Espécie:</b> R$", style_normal)],
        [Paragraph("<b>Instruções de Responsabilidade do Beneficiário:</b><br/>• Teste técnico de layout local para validação no VS Code.<br/>• Pagamento válido para crédito em conta Bradesco PF.<br/>• <b>Liberação imediata da mercadoria realizada por pura fidelidade (relação de confiança).</b>", style_normal), "", Paragraph(f"<b>(=) Valor do Documento:</b> {VALOR_TESTE}", style_bold)],
        [Paragraph(texto_observacoes, style_obs), "", Paragraph("<b>(-) Descontos / Abatimentos:</b>", style_normal)],
        ["", "", Paragraph("<b>(+) Multa / Juros:</b>", style_normal)],
        ["", "", Paragraph(f"<b>(=) Valor Cobrado:</b> {VALOR_TESTE}", style_bold)]
    ]
    
    t_boleto = Table(tabela_boleto_dados, colWidths=[55, 185, 310])
    t_boleto.setStyle(TableStyle([
        ('VALIGN', (0,0), (-1,-1), 'TOP'),
        ('ALIGN', (0,0), (0,0), 'LEFT'),
        ('VALIGN', (0,0), (-1,0), 'MIDDLE'),
        ('BOTTOMPADDING', (0,0), (-1,0), 6),
        ('LINEBELOW', (0,0), (-1,0), 2, COR_BANCO),
        
        ('SPAN', (0,1), (1,1)),
        ('SPAN', (0,2), (1,2)),
        ('SPAN', (0,5), (1,5)),
        ('SPAN', (0,6), (1,8)),
        
        ('BOX', (0,1), (-1,-1), 1, colors.black),
        ('INNERGRID', (0,1), (-1,-1), 0.5, colors.HexColor('#cbd5e1')),
        ('PADDING', (0,1), (-1,-1), 4),
        ('BACKGROUND', (2,1), (2,1), colors.HexColor('#f8fafc')),
        ('BACKGROUND', (2,5), (2,5), colors.HexColor('#f1f5f9')),
        ('BACKGROUND', (2,8), (2,8), colors.HexColor('#f1f5f9')),
    ]))
    story.append(t_boleto)
    story.append(Spacer(1, 15))
    
    # 4. Código de Barras
    barra_dados = [["|||| || ||||| |||| ||| ||||||| |||| || ||||| |||| ||| ||||||| |||| || ||||| |||| ||| ||||||| |||| || ||||| |||| ||| ||||||| |||| || |||||"]]
    t_barra = Table(barra_dados, colWidths=[550])
    t_barra.setStyle(TableStyle([
        ('ALIGN', (0,0), (-1,-1), 'CENTER'),
        ('FONTNAME', (0,0), (-1,-1), 'Courier-Bold'),
        ('FONTSIZE', (0,0), (-1,-1), 20),
        ('BOTTOMPADDING', (0,0), (-1,-1), 0),
        ('TOPPADDING', (0,0), (-1,-1), 0),
    ]))
    story.append(t_barra)
    story.append(Spacer(1, 15))
    
    # 5. Rodapé Comercial
    story.append(Paragraph("<b>Mairiporã Agro agradece a preferência! <font color='#cc092f'>♥</font> Bom apetite e obrigado por apoiar o comércio e o produtor local!</b>", style_agradecimento))
    
    doc.build(story)
    print("Sucesso: PDF gerado na pasta expedicao-digital com o script expedicao-digital-boletos.py!")

if __name__ == '__main__':
    gerar_boleto_pdf()
