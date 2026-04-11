# Skill: Programmatic Excel Generation (Professional/Corporate Grade)

> Usado por [[agents/kobe/IDENTITY|Kobe]]

> Reference document for AI agents generating .xlsx files via Python (openpyxl) or Node.js (ExcelJS).
> Last updated: 2026-03-30

---

## 1. Library Comparison

### Python

| Library | Read | Write | Formatting | Charts | Sparklines | Performance | Best For |
|---------|------|-------|------------|--------|------------|-------------|----------|
| **openpyxl** | Yes | Yes | Alto | Yes | No | Medio | Read+Write+Modify, general purpose |
| **xlsxwriter** | No | Yes | Muito Alto | Yes | Yes | Alto | Write-only com formatacao maxima |
| **pandas + openpyxl** | Yes | Yes | Via engine | Via engine | No | Alto p/ dados | DataFrames -> Excel rapido |

**Recomendacao Python**: `openpyxl` para uso geral (leitura + escrita + modificacao). `xlsxwriter` se precisa de sparklines ou performance maxima em write-only.

### Node.js

| Library | Read | Write | Formatting | Charts | Streaming | Best For |
|---------|------|-------|------------|--------|-----------|----------|
| **ExcelJS** | Yes | Yes | Alto | No | Yes | Reports formatados, streaming |
| **SheetJS (xlsx)** | Yes | Yes | Basico | No | No | Multi-format, compatibilidade |
| **xlsx-populate** | Yes | Yes | Medio | Preserva | No | Templates pre-formatados |

**Recomendacao Node.js**: `ExcelJS` para gerar do zero com formatacao profissional. `xlsx-populate` se trabalha com templates.

### Veredito Final
- **Maximo controle de formatacao**: xlsxwriter (Python) ou ExcelJS (Node.js)
- **Mais versatil**: openpyxl (Python)
- **Para templates**: xlsx-populate (Node.js)

---

## 2. Design Principles para Planilhas Profissionais

### 2.1 Regras de Ouro

1. **Consistencia absoluta** - mesmas fontes, cores, bordas, alinhamentos em todo o documento
2. **Menos e mais** - cor so onde tem funcao; branco/cinza para o resto
3. **Hierarquia visual clara** - titulo > subtitulo > header > dados > totais
4. **Respiracao** - padding interno, linhas em branco entre secoes, sem gridlines desnecessarios
5. **Numeros a direita, texto a esquerda** - regra universal de legibilidade
6. **Uma fonte, dois pesos** - Regular para dados, Bold para headers/totais

### 2.2 Paleta de Cores Corporativa

```
PALETA UNIVERSAL (funciona para qualquer marca)
================================================
Background geral:     FFFFFF (branco)
Header bg:            1F4E79 (azul escuro) ou 2D3436 (grafite)
Header text:          FFFFFF (branco)
Subheader bg:         D6E4F0 (azul claro) ou F0F0F0 (cinza claro)
Subheader text:       1F4E79 (azul escuro)
Zebra stripe:         F2F7FB (azul quase branco) ou F9F9F9 (cinza quase branco)
Accent/Totals bg:     E2EFDA (verde suave)
Accent text/border:   548235 (verde escuro)
Negative values:      C00000 (vermelho escuro)
Positive values:      548235 (verde escuro)
Border lines:         D9D9D9 (cinza claro) - NUNCA preto!
Separator lines:      B4C6E7 (azul medio)
```

**5 Regras de Cor para Dashboards:**
1. Cinza e o seu melhor amigo - use para tudo que nao precisa de destaque
2. Nao use vermelho/verde a nao ser que signifique bom/ruim
3. Adicione cor apenas onde precisa trazer a mensagem
4. Humanos distinguem ~4 tons da mesma cor - nao exagere em gradientes
5. 8% dos homens tem daltonismo vermelho/verde - use icones + cor, nunca so cor

### 2.3 Tipografia

```
FONTE PRIMARIA:    Calibri (padrao Office, segura)
ALTERNATIVAS:      Segoe UI, Arial, Aptos (novo padrao Office 365)

HIERARQUIA:
- Titulo do relatorio:  16pt, Bold, cor do header
- Subtitulo/secao:      13pt, Bold, cor do header
- Header de tabela:     11pt, Bold, branco sobre fundo escuro
- Dados:                10-11pt, Regular, preto #333333
- Totais:               11pt, Bold, preto
- Notas de rodape:      9pt, Italic, cinza #808080
- Numeros:              Usar number_format SEMPRE (nunca texto bruto)
```

### 2.4 Bordas Profissionais

```
REGRA: Nunca usar bordas pretas grossas. Planilhas profissionais usam:
- Header inferior:      Borda media, cor do header (ex: 1F4E79)
- Entre colunas:        SEM borda (use padding/alignment)
- Linhas de dados:      Borda fina inferior cinza claro (D9D9D9) OU zebra stripes
- Linha de total:       Borda dupla superior, cor de destaque
- Contorno externo:     Opcional, borda fina cinza medio
```

---

## 3. Codigo Python (openpyxl) - Templates Prontos

### 3.1 Setup Base - Constantes e Helpers

```python
from openpyxl import Workbook
from openpyxl.styles import (
    Font, PatternFill, Border, Side, Alignment, NamedStyle, Protection, numbers
)
from openpyxl.styles.differential import DifferentialStyle
from openpyxl.formatting.rule import (
    ColorScaleRule, CellIsRule, FormulaRule, IconSetRule, DataBarRule, Rule
)
from openpyxl.worksheet.table import Table, TableStyleInfo
from openpyxl.worksheet.datavalidation import DataValidation
from openpyxl.chart import BarChart, LineChart, PieChart, Reference
from openpyxl.comments import Comment
from openpyxl.drawing.image import Image
from openpyxl.utils import get_column_letter
from copy import copy

# ============================================================
# PALETA CORPORATIVA
# ============================================================
class Colors:
    WHITE = "FFFFFF"
    BLACK = "333333"

    # Headers
    HEADER_BG = "1F4E79"
    HEADER_TEXT = "FFFFFF"

    # Sub-headers
    SUBHEADER_BG = "D6E4F0"
    SUBHEADER_TEXT = "1F4E79"

    # Data
    ZEBRA = "F2F7FB"
    BORDER = "D9D9D9"
    SEPARATOR = "B4C6E7"

    # Accent
    ACCENT_BG = "E2EFDA"
    ACCENT_TEXT = "548235"

    # Status
    POSITIVE = "548235"
    NEGATIVE = "C00000"
    WARNING = "BF8F00"

    # Neutrals
    LIGHT_GRAY = "F0F0F0"
    MED_GRAY = "808080"


# ============================================================
# ESTILOS PRE-DEFINIDOS
# ============================================================
def create_named_styles(wb):
    """Registra todos os NamedStyles no workbook. Chamar uma vez."""

    # --- Title ---
    title_style = NamedStyle(name="title_style")
    title_style.font = Font(name="Calibri", size=16, bold=True, color=Colors.HEADER_BG)
    title_style.alignment = Alignment(horizontal="left", vertical="center")
    wb.add_named_style(title_style)

    # --- Subtitle ---
    subtitle_style = NamedStyle(name="subtitle_style")
    subtitle_style.font = Font(name="Calibri", size=13, bold=True, color=Colors.HEADER_BG)
    subtitle_style.alignment = Alignment(horizontal="left", vertical="center")
    wb.add_named_style(subtitle_style)

    # --- Header ---
    header_style = NamedStyle(name="header_style")
    header_style.font = Font(name="Calibri", size=11, bold=True, color=Colors.HEADER_TEXT)
    header_style.fill = PatternFill("solid", fgColor=Colors.HEADER_BG)
    header_style.alignment = Alignment(horizontal="center", vertical="center", wrap_text=True)
    header_style.border = Border(
        bottom=Side(style="medium", color=Colors.HEADER_BG),
        left=Side(style="thin", color=Colors.HEADER_BG),
        right=Side(style="thin", color=Colors.HEADER_BG),
    )
    wb.add_named_style(header_style)

    # --- Subheader ---
    subheader_style = NamedStyle(name="subheader_style")
    subheader_style.font = Font(name="Calibri", size=10, bold=True, color=Colors.SUBHEADER_TEXT)
    subheader_style.fill = PatternFill("solid", fgColor=Colors.SUBHEADER_BG)
    subheader_style.alignment = Alignment(horizontal="center", vertical="center")
    wb.add_named_style(subheader_style)

    # --- Data (normal) ---
    data_style = NamedStyle(name="data_style")
    data_style.font = Font(name="Calibri", size=10, color=Colors.BLACK)
    data_style.alignment = Alignment(vertical="center")
    data_style.border = Border(bottom=Side(style="thin", color=Colors.BORDER))
    wb.add_named_style(data_style)

    # --- Data (zebra) ---
    data_zebra_style = NamedStyle(name="data_zebra_style")
    data_zebra_style.font = Font(name="Calibri", size=10, color=Colors.BLACK)
    data_zebra_style.fill = PatternFill("solid", fgColor=Colors.ZEBRA)
    data_zebra_style.alignment = Alignment(vertical="center")
    data_zebra_style.border = Border(bottom=Side(style="thin", color=Colors.BORDER))
    wb.add_named_style(data_zebra_style)

    # --- Currency ---
    currency_style = NamedStyle(name="currency_style")
    currency_style.font = Font(name="Calibri", size=10, color=Colors.BLACK)
    currency_style.alignment = Alignment(horizontal="right", vertical="center")
    currency_style.number_format = 'R$ #,##0.00'
    currency_style.border = Border(bottom=Side(style="thin", color=Colors.BORDER))
    wb.add_named_style(currency_style)

    # --- Percentage ---
    pct_style = NamedStyle(name="pct_style")
    pct_style.font = Font(name="Calibri", size=10, color=Colors.BLACK)
    pct_style.alignment = Alignment(horizontal="right", vertical="center")
    pct_style.number_format = '0.0%'
    pct_style.border = Border(bottom=Side(style="thin", color=Colors.BORDER))
    wb.add_named_style(pct_style)

    # --- Total row ---
    total_style = NamedStyle(name="total_style")
    total_style.font = Font(name="Calibri", size=11, bold=True, color=Colors.BLACK)
    total_style.fill = PatternFill("solid", fgColor=Colors.ACCENT_BG)
    total_style.alignment = Alignment(vertical="center")
    total_style.border = Border(
        top=Side(style="double", color=Colors.ACCENT_TEXT),
        bottom=Side(style="double", color=Colors.ACCENT_TEXT),
    )
    wb.add_named_style(total_style)

    # --- Negative number ---
    negative_style = NamedStyle(name="negative_style")
    negative_style.font = Font(name="Calibri", size=10, color=Colors.NEGATIVE)
    negative_style.alignment = Alignment(horizontal="right", vertical="center")
    negative_style.number_format = 'R$ #,##0.00'
    wb.add_named_style(negative_style)

    # --- Note/footnote ---
    note_style = NamedStyle(name="note_style")
    note_style.font = Font(name="Calibri", size=9, italic=True, color=Colors.MED_GRAY)
    note_style.alignment = Alignment(horizontal="left", vertical="center")
    wb.add_named_style(note_style)


# ============================================================
# HELPER FUNCTIONS
# ============================================================
def auto_fit_columns(ws, min_width=8, max_width=50, padding=3):
    """Ajusta largura das colunas baseado no conteudo."""
    for col in ws.columns:
        max_length = 0
        col_letter = get_column_letter(col[0].column)
        for cell in col:
            if cell.value:
                cell_len = len(str(cell.value))
                if cell_len > max_length:
                    max_length = cell_len
        adjusted = min(max(max_length + padding, min_width), max_width)
        ws.column_dimensions[col_letter].width = adjusted


def apply_zebra_stripes(ws, start_row, end_row, start_col=1, end_col=None):
    """Aplica listras zebra nas linhas de dados."""
    if end_col is None:
        end_col = ws.max_column
    zebra_fill = PatternFill("solid", fgColor=Colors.ZEBRA)
    for row_idx in range(start_row, end_row + 1):
        if (row_idx - start_row) % 2 == 1:
            for col_idx in range(start_col, end_col + 1):
                cell = ws.cell(row=row_idx, column=col_idx)
                cell.fill = zebra_fill


def setup_print(ws, orientation="landscape", paper="A4", fit_to_width=True):
    """Configura pagina para impressao profissional."""
    ws.page_setup.orientation = (
        ws.ORIENTATION_LANDSCAPE if orientation == "landscape"
        else ws.ORIENTATION_PORTRAIT
    )
    ws.page_setup.paperSize = ws.PAPERSIZE_A4 if paper == "A4" else ws.PAPERSIZE_LETTER
    if fit_to_width:
        ws.page_setup.fitToWidth = 1
        ws.page_setup.fitToHeight = 0  # quantas paginas precisar
    ws.page_margins.left = 0.5
    ws.page_margins.right = 0.5
    ws.page_margins.top = 0.75
    ws.page_margins.bottom = 0.75
    ws.page_margins.header = 0.3
    ws.page_margins.footer = 0.3


def add_header_footer(ws, title="Report", company=""):
    """Adiciona header/footer para impressao."""
    ws.oddHeader.center.text = title
    ws.oddHeader.center.size = 10
    ws.oddFooter.left.text = f"&D - {company}" if company else "&D"
    ws.oddFooter.right.text = "Pagina &P de &N"


def add_excel_table(ws, ref, name, style_name="TableStyleMedium9"):
    """Adiciona Table (ListObject) com auto-filter."""
    tab = Table(displayName=name, ref=ref)
    style = TableStyleInfo(
        name=style_name,
        showFirstColumn=False,
        showLastColumn=False,
        showRowStripes=True,
        showColumnStripes=False,
    )
    tab.tableStyleInfo = style
    ws.add_table(tab)
```

### 3.2 Template: Relatorio Corporativo Completo

```python
def generate_corporate_report(data, title="Relatorio Mensal", filename="report.xlsx"):
    """
    Gera relatorio corporativo completo.

    data: list of dicts com as colunas do relatorio
    Exemplo: [{"Produto": "A", "Vendas": 1000, "Meta": 1200, "Margem": 0.15}, ...]
    """
    wb = Workbook()
    create_named_styles(wb)
    ws = wb.active
    ws.title = "Relatorio"
    ws.sheet_properties.tabColor = Colors.HEADER_BG

    # --- TITULO ---
    ws.merge_cells("A1:F1")
    ws["A1"] = title
    ws["A1"].style = "title_style"
    ws.row_dimensions[1].height = 35

    # --- SUBTITULO ---
    ws.merge_cells("A2:F2")
    ws["A2"] = "Gerado automaticamente em 30/03/2026"
    ws["A2"].style = "note_style"
    ws.row_dimensions[2].height = 20

    # --- Linha em branco ---
    ws.row_dimensions[3].height = 10

    # --- HEADERS ---
    header_row = 4
    if data:
        headers = list(data[0].keys())
    else:
        headers = ["Coluna"]

    for col_idx, header in enumerate(headers, 1):
        cell = ws.cell(row=header_row, column=col_idx, value=header)
        cell.style = "header_style"
    ws.row_dimensions[header_row].height = 30

    # --- DADOS ---
    for row_idx, record in enumerate(data, header_row + 1):
        for col_idx, key in enumerate(headers, 1):
            cell = ws.cell(row=row_idx, column=col_idx, value=record.get(key))

            # Detectar tipo e aplicar formato
            val = record.get(key)
            if isinstance(val, float) and abs(val) < 1:
                cell.style = "pct_style"
            elif isinstance(val, (int, float)) and key.lower() in ("vendas", "receita", "custo", "meta", "valor", "total"):
                cell.style = "currency_style"
            else:
                cell.style = "data_style"
                if isinstance(val, str):
                    cell.alignment = Alignment(horizontal="left", vertical="center")
                else:
                    cell.alignment = Alignment(horizontal="right", vertical="center")

    last_data_row = header_row + len(data)
    num_cols = len(headers)

    # --- ZEBRA STRIPES ---
    apply_zebra_stripes(ws, header_row + 1, last_data_row, 1, num_cols)

    # --- LINHA DE TOTAL ---
    total_row = last_data_row + 1
    ws.cell(row=total_row, column=1, value="TOTAL").style = "total_style"
    for col_idx in range(2, num_cols + 1):
        col_letter = get_column_letter(col_idx)
        cell = ws.cell(row=total_row, column=col_idx)
        cell.value = f"=SUM({col_letter}{header_row+1}:{col_letter}{last_data_row})"
        cell.style = "total_style"
        # Herdar number_format da coluna
        ref_cell = ws.cell(row=header_row + 1, column=col_idx)
        cell.number_format = ref_cell.number_format

    # --- CONDITIONAL FORMATTING ---
    # Highlight negativos em vermelho
    red_font = Font(color=Colors.NEGATIVE, bold=True)
    red_fill = PatternFill(bgColor="FFC7CE")
    dxf = DifferentialStyle(font=red_font, fill=red_fill)
    for col_idx in range(2, num_cols + 1):
        col_letter = get_column_letter(col_idx)
        rng = f"{col_letter}{header_row+1}:{col_letter}{last_data_row}"
        ws.conditional_formatting.add(rng,
            CellIsRule(operator="lessThan", formula=["0"], fill=red_fill, font=red_font))

    # --- FREEZE PANES ---
    ws.freeze_panes = f"A{header_row + 1}"

    # --- AUTO-FIT ---
    auto_fit_columns(ws)

    # --- PRINT SETUP ---
    setup_print(ws)
    add_header_footer(ws, title)
    ws.print_title_rows = f"{header_row}:{header_row}"  # Repetir header ao imprimir
    ws.print_area = f"A1:{get_column_letter(num_cols)}{total_row}"

    # --- PROTEGER ESTRUTURA ---
    ws.protection.sheet = True
    ws.protection.password = ""  # Protecao leve, sem senha

    wb.save(filename)
    return filename


# USO:
# data = [
#     {"Produto": "Widget A", "Vendas": 45000, "Meta": 50000, "Margem": 0.23},
#     {"Produto": "Widget B", "Vendas": 32000, "Meta": 30000, "Margem": 0.18},
#     {"Produto": "Widget C", "Vendas": -5000, "Meta": 10000, "Margem": -0.05},
# ]
# generate_corporate_report(data, "Vendas Q1 2026")
```

### 3.3 Template: Dashboard com Charts

```python
def generate_dashboard(monthly_data, filename="dashboard.xlsx"):
    """
    Gera dashboard com KPIs, tabela e graficos.

    monthly_data: list of dicts
    Exemplo: [{"Mes": "Jan", "Receita": 100000, "Custo": 70000, "Lucro": 30000}, ...]
    """
    wb = Workbook()
    create_named_styles(wb)
    ws = wb.active
    ws.title = "Dashboard"
    ws.sheet_properties.tabColor = Colors.HEADER_BG

    # Esconder gridlines para visual limpo
    ws.sheet_view.showGridLines = False

    # --- TITULO ---
    ws.merge_cells("A1:H1")
    ws["A1"] = "DASHBOARD FINANCEIRO"
    ws["A1"].style = "title_style"
    ws.row_dimensions[1].height = 40

    # --- KPI CARDS (row 3) ---
    kpi_row = 3
    ws.row_dimensions[kpi_row].height = 50

    # Calcular KPIs
    total_receita = sum(d["Receita"] for d in monthly_data)
    total_custo = sum(d["Custo"] for d in monthly_data)
    total_lucro = sum(d["Lucro"] for d in monthly_data)
    margem = total_lucro / total_receita if total_receita else 0

    kpis = [
        ("Receita Total", total_receita, 'R$ #,##0'),
        ("Custo Total", total_custo, 'R$ #,##0'),
        ("Lucro Liquido", total_lucro, 'R$ #,##0'),
        ("Margem", margem, '0.0%'),
    ]

    kpi_fill = PatternFill("solid", fgColor=Colors.SUBHEADER_BG)
    kpi_border = Border(
        left=Side(style="thin", color=Colors.SEPARATOR),
        right=Side(style="thin", color=Colors.SEPARATOR),
        top=Side(style="thin", color=Colors.SEPARATOR),
        bottom=Side(style="medium", color=Colors.HEADER_BG),
    )

    for i, (label, value, fmt) in enumerate(kpis):
        col = i * 2 + 1
        # Label
        cell_label = ws.cell(row=kpi_row, column=col, value=label)
        cell_label.font = Font(name="Calibri", size=9, color=Colors.MED_GRAY)
        cell_label.fill = kpi_fill
        cell_label.border = kpi_border
        cell_label.alignment = Alignment(horizontal="center", vertical="top")
        # Value
        cell_val = ws.cell(row=kpi_row, column=col + 1, value=value)
        cell_val.font = Font(name="Calibri", size=16, bold=True, color=Colors.HEADER_BG)
        cell_val.fill = kpi_fill
        cell_val.border = kpi_border
        cell_val.number_format = fmt
        cell_val.alignment = Alignment(horizontal="center", vertical="center")
        ws.merge_cells(start_row=kpi_row, start_column=col, end_row=kpi_row, end_column=col+1)
        # Reapply value after merge
        ws.cell(row=kpi_row, column=col).value = f"{label}\n"
        ws.cell(row=kpi_row, column=col).font = Font(name="Calibri", size=9, color=Colors.MED_GRAY)

    # --- TABELA DE DADOS (row 5+) ---
    table_start = 5
    headers = list(monthly_data[0].keys())
    for col_idx, h in enumerate(headers, 1):
        ws.cell(row=table_start, column=col_idx, value=h).style = "header_style"

    for row_idx, record in enumerate(monthly_data, table_start + 1):
        for col_idx, key in enumerate(headers, 1):
            cell = ws.cell(row=row_idx, column=col_idx, value=record[key])
            cell.style = "data_style"
            if isinstance(record[key], (int, float)) and key != "Mes":
                cell.number_format = 'R$ #,##0'
                cell.alignment = Alignment(horizontal="right", vertical="center")

    last_data_row = table_start + len(monthly_data)
    apply_zebra_stripes(ws, table_start + 1, last_data_row, 1, len(headers))

    # --- BAR CHART ---
    chart = BarChart()
    chart.type = "col"
    chart.grouping = "clustered"
    chart.title = "Receita vs Custo por Mes"
    chart.y_axis.title = "Valor (R$)"
    chart.x_axis.title = "Mes"
    chart.style = 10  # Clean style
    chart.width = 20
    chart.height = 12

    data_ref = Reference(ws, min_col=2, max_col=3,
                         min_row=table_start, max_row=last_data_row)
    cats_ref = Reference(ws, min_col=1, min_row=table_start + 1, max_row=last_data_row)
    chart.add_data(data_ref, titles_from_data=True)
    chart.set_categories(cats_ref)

    # Cores das series
    from openpyxl.chart.series import DataPoint
    chart.series[0].graphicalProperties.solidFill = Colors.HEADER_BG  # Receita
    chart.series[1].graphicalProperties.solidFill = Colors.NEGATIVE    # Custo

    ws.add_chart(chart, f"E{table_start}")

    # --- LINE CHART (Lucro) ---
    line_chart = LineChart()
    line_chart.title = "Evolucao do Lucro"
    line_chart.y_axis.title = "Lucro (R$)"
    line_chart.style = 10
    line_chart.width = 20
    line_chart.height = 12

    lucro_ref = Reference(ws, min_col=4, max_col=4,
                          min_row=table_start, max_row=last_data_row)
    line_chart.add_data(lucro_ref, titles_from_data=True)
    line_chart.set_categories(cats_ref)
    line_chart.series[0].graphicalProperties.line.solidFill = Colors.ACCENT_TEXT

    ws.add_chart(line_chart, f"E{table_start + 16}")

    # --- CONFIG ---
    auto_fit_columns(ws)
    ws.freeze_panes = f"A{table_start + 1}"
    setup_print(ws)

    wb.save(filename)
    return filename
```

### 3.4 Tecnicas Avancadas Individuais

#### Data Validation (Dropdowns)

```python
def add_dropdown(ws, cell_range, options, prompt_title="", prompt_msg=""):
    """Adiciona dropdown de validacao."""
    formula = '"' + ','.join(options) + '"'
    dv = DataValidation(type="list", formula1=formula, allow_blank=True)
    dv.prompt = prompt_msg
    dv.promptTitle = prompt_title
    dv.error = "Valor invalido. Selecione da lista."
    dv.errorTitle = "Erro de validacao"
    dv.showInputMessage = True
    dv.showErrorMessage = True
    ws.add_data_validation(dv)
    dv.add(cell_range)

# Uso:
# add_dropdown(ws, "D2:D100", ["Aprovado", "Pendente", "Rejeitado"],
#              "Status", "Selecione o status")
```

#### Data Validation (Referencia de outra sheet)

```python
from openpyxl.utils import quote_sheetname

def add_dropdown_from_sheet(ws, cell_range, source_sheet_name, source_range):
    """Dropdown referenciando lista em outra aba."""
    formula = f"{quote_sheetname(source_sheet_name)}!{source_range}"
    dv = DataValidation(type="list", formula1=formula, allow_blank=True)
    dv.showInputMessage = True
    dv.showErrorMessage = True
    ws.add_data_validation(dv)
    dv.add(cell_range)
```

#### Named Ranges

```python
from openpyxl.workbook.defined_name import DefinedName

def add_named_range(wb, name, sheet_title, cell_range):
    """Cria named range no workbook."""
    ref = f"'{sheet_title}'!{cell_range}"
    defn = DefinedName(name, attr_text=ref)
    wb.defined_names.add(defn)

# Uso:
# add_named_range(wb, "DadosVendas", "Relatorio", "$A$5:$F$100")
```

#### Grouped Rows (Outline)

```python
def add_row_groups(ws, groups):
    """
    Agrupa linhas para collapse/expand.
    groups: list of tuples (start_row, end_row, outline_level)
    """
    for start, end, level in groups:
        for row in range(start, end + 1):
            ws.row_dimensions[row].outlineLevel = level
    ws.sheet_properties.outlinePr.summaryBelow = True

# Uso: agrupar detalhes por categoria
# add_row_groups(ws, [(6, 10, 1), (12, 15, 1), (17, 20, 1)])
```

#### Cell Comments

```python
def add_comment(ws, cell_ref, text, author="Sistema", width=300, height=100):
    """Adiciona comentario a uma celula."""
    comment = Comment(text, author)
    comment.width = width
    comment.height = height
    ws[cell_ref].comment = comment

# Uso:
# add_comment(ws, "B5", "Valor calculado com base na media dos ultimos 3 meses")
```

#### Images / Logo

```python
def add_logo(ws, image_path, cell="A1", width=150, height=50):
    """Insere logo/imagem na planilha."""
    img = Image(image_path)
    img.width = width
    img.height = height
    ws.add_image(img, cell)
```

#### Conditional Formatting Avancado

```python
def add_traffic_light_formatting(ws, col_letter, start_row, end_row):
    """Semaforo verde/amarelo/vermelho baseado em valor."""
    rng = f"{col_letter}{start_row}:{col_letter}{end_row}"

    # Verde > 80%
    green_fill = PatternFill(bgColor="C6EFCE")
    green_font = Font(color="006100")
    ws.conditional_formatting.add(rng, CellIsRule(
        operator="greaterThan", formula=["0.8"],
        fill=green_fill, font=green_font))

    # Amarelo 50-80%
    yellow_fill = PatternFill(bgColor="FFEB9C")
    yellow_font = Font(color="9C5700")
    ws.conditional_formatting.add(rng, CellIsRule(
        operator="between", formula=["0.5", "0.8"],
        fill=yellow_fill, font=yellow_font))

    # Vermelho < 50%
    red_fill = PatternFill(bgColor="FFC7CE")
    red_font = Font(color="9C0006")
    ws.conditional_formatting.add(rng, CellIsRule(
        operator="lessThan", formula=["0.5"],
        fill=red_fill, font=red_font))


def add_data_bars(ws, col_letter, start_row, end_row, color="638EC6"):
    """Barras de dados dentro das celulas."""
    rng = f"{col_letter}{start_row}:{col_letter}{end_row}"
    rule = DataBarRule(
        start_type="min", end_type="max",
        color=color, showValue=True
    )
    ws.conditional_formatting.add(rng, rule)


def add_color_scale(ws, col_letter, start_row, end_row):
    """Gradiente de cor vermelho -> amarelo -> verde."""
    rng = f"{col_letter}{start_row}:{col_letter}{end_row}"
    rule = ColorScaleRule(
        start_type="min", start_color="F8696B",
        mid_type="percentile", mid_value=50, mid_color="FFEB84",
        end_type="max", end_color="63BE7B"
    )
    ws.conditional_formatting.add(rng, rule)


def add_icon_set(ws, col_letter, start_row, end_row):
    """Icones de seta (5 niveis)."""
    rng = f"{col_letter}{start_row}:{col_letter}{end_row}"
    rule = IconSetRule("5Arrows", "percent", [0, 20, 40, 60, 80])
    ws.conditional_formatting.add(rng, rule)
```

#### Table (ListObject) com Estilos

```python
def add_formatted_table(ws, start_cell, data, headers, table_name,
                         style="TableStyleMedium2"):
    """
    Cria Table Excel com auto-filter e estilo.

    Estilos disponiveis:
    - TableStyleLight1-21   (leves, fundo branco)
    - TableStyleMedium1-28  (medios, cores suaves) << RECOMENDADO
    - TableStyleDark1-11    (escuros, headers coloridos)

    Melhores para corporativo:
    - TableStyleMedium2  (azul classico)
    - TableStyleMedium9  (azul escuro)
    - TableStyleMedium15 (cinza elegante)
    - TableStyleMedium3  (laranja corporativo)
    """
    from openpyxl.utils import get_column_letter

    start_row = ws.cell(coordinate=start_cell).row
    start_col = ws.cell(coordinate=start_cell).column

    # Escrever headers
    for i, h in enumerate(headers):
        ws.cell(row=start_row, column=start_col + i, value=h)

    # Escrever dados
    for row_idx, row_data in enumerate(data):
        for col_idx, val in enumerate(row_data):
            ws.cell(row=start_row + 1 + row_idx, column=start_col + col_idx, value=val)

    # Definir range da tabela
    end_col_letter = get_column_letter(start_col + len(headers) - 1)
    end_row = start_row + len(data)
    ref = f"{start_cell}:{end_col_letter}{end_row}"

    tab = Table(displayName=table_name, ref=ref)
    tab.tableStyleInfo = TableStyleInfo(
        name=style,
        showFirstColumn=False, showLastColumn=False,
        showRowStripes=True, showColumnStripes=False
    )
    ws.add_table(tab)
```

---

## 4. Codigo Node.js (ExcelJS) - Template Pronto

```javascript
const ExcelJS = require('exceljs');

// ============================================================
// PALETA (mesma do Python)
// ============================================================
const Colors = {
  HEADER_BG: 'FF1F4E79',
  HEADER_TEXT: 'FFFFFFFF',
  SUBHEADER_BG: 'FFD6E4F0',
  SUBHEADER_TEXT: 'FF1F4E79',
  ZEBRA: 'FFF2F7FB',
  BORDER: 'FFD9D9D9',
  ACCENT_BG: 'FFE2EFDA',
  ACCENT_TEXT: 'FF548235',
  NEGATIVE: 'FFC00000',
  LIGHT_GRAY: 'FFF0F0F0',
};

const thinBorder = { style: 'thin', color: { argb: Colors.BORDER } };

async function generateReport(data, headers, title, filename) {
  const wb = new ExcelJS.Workbook();
  wb.creator = 'AI Agent';
  wb.created = new Date();

  const ws = wb.addWorksheet('Relatorio', {
    properties: { tabColor: { argb: Colors.HEADER_BG } },
    pageSetup: {
      orientation: 'landscape',
      paperSize: 9, // A4
      fitToPage: true,
      fitToWidth: 1,
      fitToHeight: 0,
      margins: { left: 0.5, right: 0.5, top: 0.75, bottom: 0.75, header: 0.3, footer: 0.3 }
    }
  });

  // --- TITULO ---
  ws.mergeCells('A1:F1');
  const titleCell = ws.getCell('A1');
  titleCell.value = title;
  titleCell.font = { name: 'Calibri', size: 16, bold: true, color: { argb: Colors.HEADER_BG } };
  titleCell.alignment = { horizontal: 'left', vertical: 'middle' };
  ws.getRow(1).height = 35;

  // --- HEADERS (row 3) ---
  const headerRow = ws.getRow(3);
  headers.forEach((h, i) => {
    const cell = headerRow.getCell(i + 1);
    cell.value = h;
    cell.font = { name: 'Calibri', size: 11, bold: true, color: { argb: Colors.HEADER_TEXT } };
    cell.fill = { type: 'pattern', pattern: 'solid', fgColor: { argb: Colors.HEADER_BG } };
    cell.alignment = { horizontal: 'center', vertical: 'middle', wrapText: true };
    cell.border = { bottom: { style: 'medium', color: { argb: Colors.HEADER_BG } } };
  });
  headerRow.height = 30;

  // --- DADOS ---
  data.forEach((row, rowIdx) => {
    const wsRow = ws.getRow(4 + rowIdx);
    row.forEach((val, colIdx) => {
      const cell = wsRow.getCell(colIdx + 1);
      cell.value = val;
      cell.font = { name: 'Calibri', size: 10, color: { argb: 'FF333333' } };
      cell.border = { bottom: thinBorder };
      if (typeof val === 'number') {
        cell.alignment = { horizontal: 'right', vertical: 'middle' };
        cell.numFmt = '#,##0.00';
      } else {
        cell.alignment = { horizontal: 'left', vertical: 'middle' };
      }
    });
    // Zebra
    if (rowIdx % 2 === 1) {
      row.forEach((_, colIdx) => {
        wsRow.getCell(colIdx + 1).fill = {
          type: 'pattern', pattern: 'solid', fgColor: { argb: Colors.ZEBRA }
        };
      });
    }
  });

  // --- AUTO-WIDTH ---
  ws.columns.forEach((col, i) => {
    let maxLen = headers[i] ? headers[i].length : 10;
    data.forEach(row => {
      const val = row[i];
      if (val) maxLen = Math.max(maxLen, String(val).length);
    });
    col.width = Math.min(Math.max(maxLen + 3, 8), 50);
  });

  // --- FREEZE ---
  ws.views = [{ state: 'frozen', ySplit: 3 }];

  // --- CONDITIONAL FORMATTING ---
  // Exemplo: highlight negativos
  ws.addConditionalFormatting({
    ref: `B4:F${3 + data.length}`,
    rules: [{
      type: 'cellIs',
      operator: 'lessThan',
      formulae: [0],
      style: {
        font: { color: { argb: Colors.NEGATIVE }, bold: true },
        fill: { type: 'pattern', pattern: 'solid', bgColor: { argb: 'FFFFC7CE' } }
      }
    }]
  });

  await wb.xlsx.writeFile(filename);
  return filename;
}

// USO:
// await generateReport(
//   [['Widget A', 45000, 50000, 0.23], ['Widget B', 32000, 30000, 0.18]],
//   ['Produto', 'Vendas', 'Meta', 'Margem'],
//   'Relatorio Q1 2026',
//   'report.xlsx'
// );
```

---

## 5. Tabela de Estilos de Table (ListObject)

| Style Name | Visual | Uso Recomendado |
|---|---|---|
| TableStyleMedium2 | Azul classico, rows striped | **Padrao corporativo** |
| TableStyleMedium9 | Azul escuro, bold header | Relatorios executivos |
| TableStyleMedium15 | Cinza elegante | Financeiro, contabilidade |
| TableStyleMedium3 | Laranja/terra | Marketing, criativo |
| TableStyleMedium4 | Verde corporativo | Sustentabilidade, KPIs positivos |
| TableStyleLight1 | Minimalista cinza | Planilhas auxiliares, anexos |
| TableStyleLight9 | Azul suave | Dados de suporte |
| TableStyleDark1 | Header preto forte | Alto contraste, apresentacoes |
| TableStyleDark2 | Azul escuro total | Dashboard cards |

---

## 6. Checklist de Qualidade

Antes de entregar qualquer planilha gerada, verificar:

- [ ] **Freeze panes** no header da tabela principal
- [ ] **Auto-filter** ativo (via Table ou ws.auto_filter.ref)
- [ ] **Column widths** ajustadas ao conteudo (auto_fit_columns)
- [ ] **Number formats** em todas as celulas numericas (moeda, %, data)
- [ ] **Alignment** consistente (texto esquerda, numeros direita, headers centro)
- [ ] **Fonte unica** (Calibri) com hierarquia clara de tamanhos
- [ ] **Cores limitadas** a paleta definida (max 4-5 cores)
- [ ] **Bordas suaves** (cinza claro, nunca preto grosso)
- [ ] **Zebra stripes** OU bordas entre linhas (nunca os dois)
- [ ] **Print setup** configurado (landscape, fit-to-width, margins, header/footer)
- [ ] **Titulo** do relatorio visivel
- [ ] **Data de geracao** incluida
- [ ] **Gridlines desativadas** se for dashboard (ws.sheet_view.showGridLines = False)
- [ ] **Tab color** da aba configurada
- [ ] **Conditional formatting** para valores criticos (negativos, fora de meta)
- [ ] **Sem celulas vazias** no header (confunde auto-filter)
- [ ] **Named ranges** para areas referenciadas por formulas

---

## 7. Features por Biblioteca (Matrix de Suporte)

| Feature | openpyxl | xlsxwriter | ExcelJS | SheetJS |
|---|---|---|---|---|
| Read .xlsx | Yes | No | Yes | Yes |
| Write .xlsx | Yes | Yes | Yes | Yes |
| Fonts/Colors | Yes | Yes | Yes | Basic |
| Borders | Yes | Yes | Yes | Basic |
| Conditional Formatting | Yes | Yes | Partial | No |
| Charts | Yes | Yes | No | No |
| Sparklines | **No** | Yes | No | No |
| Tables (ListObject) | Yes | Yes | No | Partial |
| Data Validation | Yes | Yes | Yes | No |
| Images | Yes | Yes | Yes | No |
| Comments | Yes | Yes | No | No |
| Named Ranges | Yes | Yes | Yes | Yes |
| Freeze Panes | Yes | Yes | Yes | No |
| Print Setup | Yes | Yes | Yes | No |
| Row Grouping | Yes | Yes | Yes | No |
| Page Breaks | Yes | Yes | Yes | No |
| Streaming (large files) | Yes | Yes | Yes | No |
| Modify existing | Yes | No | Yes | Yes |
| Rich text in cell | **No** | Yes | Yes | No |
| VBA/Macros | Read only | Yes | No | No |

---

## 8. Performance Tips

1. **Dados grandes (>50k rows)**: Use `ws.append()` em loop (openpyxl) ou streaming mode (ExcelJS)
2. **Estilos repetidos**: Criar `NamedStyle` e reusar em vez de criar objetos por celula
3. **Evitar merge cells** em areas de dados - so para titulos
4. **Charts**: Maximo ~5 charts por sheet para nao pesar o arquivo
5. **Images**: Comprimir antes de inserir (max 100KB por logo)
6. **Conditional formatting**: Aplicar em ranges grandes, nao celula por celula
7. **xlsxwriter**: Use `constant_memory=True` para arquivos enormes

---

## 9. Number Formats Uteis

```python
# Moeda BR
cell.number_format = 'R$ #,##0.00'

# Moeda USD
cell.number_format = '$#,##0.00'

# Percentual
cell.number_format = '0.0%'

# Numero com separador de milhar
cell.number_format = '#,##0'

# Data BR
cell.number_format = 'DD/MM/YYYY'

# Data e hora
cell.number_format = 'DD/MM/YYYY HH:MM'

# Numero negativo em vermelho (built-in)
cell.number_format = '#,##0.00;[Red]-#,##0.00'

# Contabil (alinhado com cifrao)
cell.number_format = '_-R$ * #,##0.00_-;-R$ * #,##0.00_-;_-R$ * "-"??_-;_-@_-'

# Telefone
cell.number_format = '(##) #####-####'

# CPF
cell.number_format = '###.###.###-##'

# CNPJ
cell.number_format = '##.###.###/####-##'
```
