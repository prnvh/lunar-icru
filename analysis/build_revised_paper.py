"""Build the revised paper PDF from Markdown, with vector diagrams and result data.

Requires reportlab; run after analysis/run_papers.py. Page breaks are deliberate.
"""
from pathlib import Path
import csv
import json
import re
import shutil
from xml.sax.saxutils import escape

from reportlab.lib import colors
from reportlab.lib.enums import TA_LEFT
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, PageBreak, Table, TableStyle, Flowable

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / 'output/pdf/legacy-reportlab-preview.pdf'
NAVY = colors.HexColor('#19334A')
TEAL = colors.HexColor('#167D8D')
INK = colors.HexColor('#24323D')
MUTED = colors.HexColor('#526472')
PALE = colors.HexColor('#EFF5F7')
RULE = colors.HexColor('#CFDCE2')
W = A4[0] - 108

fontdir = Path('C:/Windows/Fonts')
if (fontdir / 'georgia.ttf').exists():
    for name, file in [('Body', 'georgia.ttf'), ('Body-Bold', 'georgiab.ttf'), ('Body-Italic', 'georgiai.ttf')]:
        pdfmetrics.registerFont(TTFont(name, str(fontdir / file)))
    pdfmetrics.registerFontFamily('Body', normal='Body', bold='Body-Bold', italic='Body-Italic', boldItalic='Body-Bold')
    BODY = 'Body'
else:
    BODY = 'Times-Roman'

STYLES = {
    'body': ParagraphStyle('body', fontName=BODY, fontSize=9.6, leading=13.25, textColor=INK, spaceAfter=7, alignment=TA_LEFT),
    'h1': ParagraphStyle('h1', fontName='Helvetica-Bold', fontSize=23, leading=27, textColor=NAVY, spaceAfter=16),
    'h2': ParagraphStyle('h2', fontName='Helvetica-Bold', fontSize=15, leading=19, textColor=NAVY, spaceBefore=6, spaceAfter=10, keepWithNext=True),
    'h3': ParagraphStyle('h3', fontName='Helvetica-Bold', fontSize=10.4, leading=14, textColor=NAVY, spaceBefore=7, spaceAfter=6, keepWithNext=True),
    'caption': ParagraphStyle('caption', fontName='Helvetica', fontSize=8, leading=10.6, textColor=MUTED, spaceAfter=10),
    'cell': ParagraphStyle('cell', fontName='Helvetica', fontSize=8.25, leading=11, textColor=INK),
    'headcell': ParagraphStyle('headcell', fontName='Helvetica-Bold', fontSize=8.1, leading=10.8, textColor=colors.white),
    'ref': ParagraphStyle('ref', fontName=BODY, fontSize=8.6, leading=11.5, textColor=INK, spaceAfter=8),
    'author': ParagraphStyle('author', fontName='Helvetica', fontSize=10, leading=14, textColor=MUTED, spaceAfter=5),
    'eq': ParagraphStyle('eq', fontName='Helvetica', fontSize=10.5, leading=18, textColor=NAVY),
}

def inline(s):
    s = s.replace('\u201c', '"').replace('\u201d', '"').replace('\u2019', "'")
    s = escape(s)
    s = re.sub(r'\*\*(.+?)\*\*', r'<b>\1</b>', s)
    s = re.sub(r'`(.+?)`', r'<font name="Courier" size="8.1">\1</font>', s)
    s = re.sub(r'https?://[^\s<>]+', lambda m: '<link href="'+m[0]+'" color="#167D8D">'+m[0]+'</link>', s)
    return s

def para(s, style='body'):
    return Paragraph(inline(s), STYLES[style])

class Diagram(Flowable):
    def __init__(self, kind):
        super().__init__()
        self.kind = kind
        self.width = W
        self.height = {'workflow': 127, 'boundary': 137, 'intervals': 153}[kind]

    def label(self, x, y, s, size=9, bold=False, color=INK, center=False):
        c = self.canv
        c.setFillColor(color)
        c.setFont('Helvetica-Bold' if bold else 'Helvetica', size)
        (c.drawCentredString if center else c.drawString)(x, y, s)

    def box(self, x, y, w, h, title, sub):
        c = self.canv
        c.setFillColor(PALE)
        c.setStrokeColor(RULE)
        c.roundRect(x, y, w, h, 5, fill=1, stroke=1)
        self.label(x+w/2, y+h-17, title, 9, True, NAVY, True)
        self.label(x+w/2, y+12, sub, 8, False, MUTED, True)

    def arrow(self, x1, y, x2):
        c=self.canv
        c.setStrokeColor(TEAL)
        c.setLineWidth(1.2)
        c.line(x1,y,x2,y)
        c.line(x2-4,y+3,x2,y)
        c.line(x2-4,y-3,x2,y)

    def draw(self):
        c=self.canv
        if self.kind == 'workflow':
            bw=(W-36)/3
            for i,(a,b) in enumerate([('1. Recover a case','Version, equations, inputs'),('2. Reproduce headline','Intermediates + native metric'),('3. Check comparability','Boundary + independent lineage')]):
                x=i*(bw+18)
                self.box(x,66,bw,49,a,b)
                if i<2: self.arrow(x+bw+2,91,x+bw+16)
            self.label(8,43,'Incomplete or ambiguous?',8.5,True)
            self.label(8,27,'Report partial evidence, branches, or bounds.',8.5)
            self.label(W/2+15,43,'Both gates passed?',8.5,True,TEAL)
            self.label(W/2+15,27,'Run a controlled common-input comparison.',8.5)
            c.setStrokeColor(RULE)
            c.line(0,12,W,12)
        elif self.kind=='boundary':
            bw=(W-48)/4
            items=[('Resource recovery','Ice or regolith'),('Processing','Source-defined product'),('Surface sale','Producer/customer handoff'),('Transport + use','Orbit or mission demand')]
            for i,(a,b) in enumerate(items):
                x=i*(bw+16)
                self.box(x,67,bw,49,a,b)
                if i<3: self.arrow(x+bw+1,91,x+bw+14)
            c.setStrokeColor(TEAL)
            c.setLineWidth(2)
            c.line(4,56,3*bw+30,56)
            self.label(4,40,'Producer cash flows -> NPV / IRR',8.5,True,TEAL)
            c.setStrokeColor(NAVY)
            c.line(4,25,W-4,25)
            self.label(4,9,'Broader delivery or mission boundary -> delivered cost / campaign-cost ratio',8.3,True,NAVY)
        else:
            data=json.loads((ROOT/'results/surface_offtake_bounds.json').read_text())
            k=data['kornuta_modified_surface_offtake']['npv_source_currency']/1e6
            s=data['sowers_partial_identification']
            lo,hi=s['npv_lower']/1e6,s['npv_upper']/1e6
            left,right=130,W-28
            def x(v): return left+(v+1600)/1800*(right-left)
            for t in [-1500,-1000,-500,0]:
                c.setStrokeColor(RULE)
                c.setLineWidth(0.6)
                c.line(x(t),38,x(t),130)
                self.label(x(t),22,f'{t:,}',8,False,MUTED,True)
            c.setDash(3,3)
            c.setStrokeColor(NAVY)
            c.line(x(0),38,x(0),134)
            c.setDash()
            self.label(0,106,'Kornuta',9,True)
            self.label(0,92,'Modified scenario',8,False,MUTED)
            self.label(0,64,'Sowers',9,True)
            self.label(0,50,'Allowed timing class',8,False,MUTED)
            c.setFillColor(NAVY)
            c.circle(x(k),102,4,fill=1,stroke=0)
            self.label(x(k),116,f'{k:,.2f}',8.5,True,NAVY,True)
            c.setStrokeColor(TEAL)
            c.setLineWidth(5)
            c.line(x(lo),60,x(hi),60)
            c.setLineWidth(1.5)
            for v in [lo,hi]:c.line(x(v),54,x(v),66)
            self.label((x(lo)+x(hi))/2,76,f'[{lo:,.2f}, +{hi:,.2f}]',8.5,True,TEAL,True)
            self.label((left+right)/2,4,'NPV (million common account units)',8.4,False,MUTED,True)

def equation(kind):
    text={
        'kornuta':'I = 30,000 (100,000 + 35,000) = 4,050 million<br/>A = sum of (1.10)<super>-t</super>, t = 1,...,10 = 6.144567<br/><b>NPV = -I + (R - 129 million) A</b>',
        'bounds':'PV(C, t) = C / (1 + r)<super>t</super><br/><b>C / (1 + r)<super>b</super> &lt;= PV(C, t) &lt;= C / (1 + r)<super>a</super></b>'
    }[kind]
    t=Table([[Paragraph(text, STYLES['eq'])]],colWidths=[W])
    t.setStyle(TableStyle([('BACKGROUND',(0,0),(-1,-1),PALE),('BOX',(0,0),(-1,-1),0.5,RULE),('LEFTPADDING',(0,0),(-1,-1),13),('TOPPADDING',(0,0),(-1,-1),8),('BOTTOMPADDING',(0,0),(-1,-1),8)]))
    return t

def table(lines):
    rows=[[x.strip() for x in s.strip().strip('|').split('|')] for s in lines]
    rows=[r for r in rows if not all(re.fullmatch(r'[-: ]+',x) for x in r)]
    n=len(rows[0])
    proportions={2:[.2,.8],3:[.30,.35,.35],5:[.25,.14,.17,.21,.23]}[n]
    if rows[0][0]=='Output': proportions=[.45,.275,.275]
    t=Table([[para(x,'headcell' if i==0 else 'cell') for x in r] for i,r in enumerate(rows)],colWidths=[W*p for p in proportions],repeatRows=1,hAlign='LEFT')
    t.setStyle(TableStyle([('BACKGROUND',(0,0),(-1,0),NAVY),('VALIGN',(0,0),(-1,-1),'TOP'),('LEFTPADDING',(0,0),(-1,-1),7),('RIGHTPADDING',(0,0),(-1,-1),7),('TOPPADDING',(0,0),(-1,-1),6),('BOTTOMPADDING',(0,0),(-1,-1),6),('ROWBACKGROUNDS',(0,1),(-1,-1),[colors.white,PALE]),('LINEBELOW',(0,-1),(-1,-1),.6,RULE)]))
    return t

def furniture(c,doc):
    c.saveState()
    c.setStrokeColor(RULE)
    c.setLineWidth(.6)
    c.line(54, A4[1]-37, A4[0]-54,A4[1]-37)
    c.setFont('Helvetica',7.4)
    c.setFillColor(MUTED)
    c.drawString(54,A4[1]-28,'LUNAR-PROPELLANT ECONOMICS')
    c.drawRightString(A4[0]-54,A4[1]-28,'REPRODUCIBILITY AUDIT')
    c.line(54,40,A4[0]-54,40)
    c.drawString(54,27,'Harikumar, Panda & Shankdharan')
    c.drawRightString(A4[0]-54,27,str(doc.page))
    c.restoreState()

def build():
    OUT.parent.mkdir(parents=True,exist_ok=True)
    source=(ROOT/'research/revised-paper.md').read_text(encoding='utf-8')
    story=[]
    lines=source.splitlines()
    i=0
    in_refs=False
    while i<len(lines):
        s=lines[i].strip()
        i+=1
        if not s:continue
        if s=='<!-- PAGE -->':story.append(PageBreak());continue
        m=re.fullmatch(r'<!-- (FIGURE|EQUATION) (\w+) -->',s)
        if m:
            story.extend([Diagram(m[2]) if m[1]=='FIGURE' else equation(m[2]),Spacer(1,7)])
            continue
        if s.startswith('|'):
            block=[s]
            while i<len(lines) and lines[i].strip().startswith('|'):
                block.append(lines[i].strip());i+=1
            story.extend([table(block),Spacer(1,7)])
            continue
        if s.startswith('# '):story.append(para(s[2:],'h1'));continue
        if s.startswith('## '):
            in_refs=s=='## References'
            story.append(para(s[3:],'h2'));continue
        if s.startswith('### '):story.append(para(s[4:],'h3'));continue
        if s.startswith('**Figure') or s.startswith('**Table'):style='caption'
        elif in_refs:style='ref'
        elif s.startswith('Pranav Harikumar') or s=='Independent Researcher, Toram Labs':style='author'
        else:style='body'
        story.append(para(s,style))
    doc=SimpleDocTemplate(str(OUT),pagesize=A4,rightMargin=54,leftMargin=54,topMargin=51,bottomMargin=53,
                          title='Reproducibility and Comparability of Lunar-Propellant Economic Models',
                          author='Pranav Harikumar; Biswa Ranjan Panda; Adwik Shankdharan',pageCompression=1)
    doc.build(story,onFirstPage=furniture,onLaterPages=furniture)
    # This legacy ReportLab preview must not overwrite the LaTeX-built paper.
    print(OUT)

if __name__=='__main__':build()
