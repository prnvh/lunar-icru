"""Generate standalone LaTeX from journal-manuscript.tex and numeric results."""
from pathlib import Path
import csv
import json
ROOT=Path(__file__).resolve().parents[1]

def read(name): return json.loads((ROOT/'results'/name).read_text(encoding='utf-8'))
def csvrows(name): return list(csv.DictReader((ROOT/'results'/name).open()))
def pt(x,y): return f'({x:.4f},{y:.4f})'

def kornuta_table():
    rows=csvrows('kornuta_reproduction.csv')
    names=['Moon','EML1','LEO','LEO + Moon','EML1 + LEO','Moon + EML1','All customers']
    out=[r'''\begin{table*}[t]
\caption{Reproduction of the Kornuta report's financial scenarios. Revenue and NPV are in millions of source dollars (currency year unresolved). Scenario names indicate customer markets; the mining company's sale boundary is the lunar surface. EML1: Earth--Moon Lagrange point 1; LEO: low Earth orbit.}
\label{tab:kornuta}\centering\small
\begin{tabular}{@{}lrrrrrrr@{}}\toprule
Scenario & Annual revenue & Printed NPV & Reconstructed NPV & $\Delta$ NPV & $\epsilon$ (\%) & IRR (\%) & Printed IRR (\%) \\
\midrule''']
    for name,rev,irr,r in zip(names,[750,1050,630,1380,1680,1800,2430],[9,19,4,28,37,40,56],rows):
        old=float(r['reported_npv'])/1e6;new=float(r['calculated_npv'])/1e6
        out.append(f"{name} & {rev:,} & {old:,.0f} & {new:,.2f} & {new-old:+.2f} & {float(r['relative_error_percent']):.4f} & {float(r['calculated_ror_percent']):.2f} & {irr}"+r' \\')
    return '\n'.join(out+[r'\bottomrule\end{tabular}\end{table*}'])

def timing_table():
    costs=read('surface_offtake_bounds.json')['sowers_partial_identification']['cost_endpoints']
    out=[r'''\begin{table}[t]
\caption{Sowers expenditure windows relative to commissioning ($t=0$), and capital values accumulated to commissioning at 10\%. Monetary values are million common account units. Earlier payment increases capital value at commissioning.}
\label{tab:timing}\centering\footnotesize
\begin{tabular}{@{}lrrr@{}}\toprule
Expenditure & Years & Latest payment & Earliest payment \\
\midrule''']
    for name,c in costs.items():
        out.append(f"{name.capitalize()} & $[{c['earliest_time']},{c['latest_time']}]$ & {c['pv_if_late']/1e6:,.2f} & {c['pv_if_early']/1e6:,.2f}"+r' \\')
    return '\n'.join(out+[r'\bottomrule\end{tabular}\end{table}'])

def axes(ymin,ymax,ticks,labels,xs):
    y=lambda v:(v-ymin)/(ymax-ymin)*4.5
    out=[r'\begin{tikzpicture}[x=1cm,y=1cm,font=\footnotesize]']
    for tick in ticks:
        out += [r'\draw[black!15,line width=.3pt] '+pt(0,y(tick))+'--'+pt(6.4,y(tick))+';',r'\node[anchor=east] at '+pt(-.12,y(tick))+f' {{{tick:g}}};']
    out.append(r'\draw[line width=.5pt] (0,4.5)--(0,0)--(6.4,0);')
    out.append(r'\draw[black!65,densely dashed] '+pt(0,y(0))+'--'+pt(6.4,y(0))+';')
    for label,x in zip(labels,xs):
        out.extend([r'\draw '+pt(x,0)+'--'+pt(x,-.08)+';',r'\node[anchor=north] at '+pt(x,-.1)+f' {{{label}}};'])
    out.append(r'\node[rotate=90] at (-.9,2.25) {NPV (billion account units)};')
    return out,y

def price_figure(rows):
    rs=sorted([r for r in rows if float(r['rate'])==.1 and float(r['relative_cost_multiplier_sowers'])==1],key=lambda r:float(r['price']))
    x=lambda p:(p-300)/700*6.4
    out,y=axes(-3,4,range(-3,5),[300,500,750,1000],[x(p) for p in [300,500,750,1000]])
    lower=[pt(x(float(r['price'])),y(float(r['sowers_npv_lower'])/1e9)) for r in rs]
    upper=[pt(x(float(r['price'])),y(float(r['sowers_npv_upper'])/1e9)) for r in rs]
    out.append(r'\fill[black!17] '+'--'.join(lower+list(reversed(upper)))+'--cycle;')
    for edge in (lower,upper):out.append(r'\draw[black!65,line width=.55pt] '+'--'.join(edge)+';')
    k=[pt(x(float(r['price'])),y(float(r['kornuta_npv'])/1e9)) for r in rs]
    out.append(r'\draw[line width=.8pt] '+'--'.join(k)+';')
    for c in k:out.append(r'\fill '+c+' circle (1.3pt);')
    out += [r'\node at (3.2,-.62) {Surface sale price (account units/kg)};',
      r'\draw[line width=.8pt] (.3,4.18)--(.95,4.18);\node[anchor=west] at (1.02,4.18) {Kornuta, modified case};',
      r'\fill[black!17] (.3,3.70) rectangle (.95,3.88);\node[anchor=west] at (1.02,3.79) {Sowers, timing interval};',r'\end{tikzpicture}']
    return '\n'.join([r'\begin{figure}[t]\centering',*out,r'''\caption{Conditional NPV versus surface sale price at 1,100 tonnes/year, ten operating years and 10\% discounting. Points are stored Kornuta scenario outputs; the grey band spans Sowers expenditure allocations. Straight segments are exact for this fixed-quantity calculation. Common account units do not imply verified currency or physical equivalence.}\label{fig:price}\end{figure}'''])

def rate_figure(rows):
    rs=sorted([r for r in rows if float(r['price'])==500 and float(r['relative_cost_multiplier_sowers'])==1],key=lambda r:float(r['rate']))
    xs=[.3+5.8*float(r['rate'])/.217 for r in rs]
    out,y=axes(-4,3,range(-4,4),['0','5','10','15','21.7'],xs)
    for r,x in zip(rs,xs):
        lo=y(float(r['sowers_npv_lower'])/1e9);hi=y(float(r['sowers_npv_upper'])/1e9)
        out.append(r'\draw[line width=1.3pt,black!65] '+pt(x+.07,lo)+'--'+pt(x+.07,hi)+';')
        for v in (lo,hi):out.append(r'\draw[black!65] '+pt(x-.04,v)+'--'+pt(x+.18,v)+';')
        out.append(r'\fill '+pt(x-.07,y(float(r['kornuta_npv'])/1e9))+' circle (1.7pt);')
    out += [r'\node at (3.2,-.62) {Discount rate (\%)};',
       r'\fill (2.65,4.15) circle (1.7pt);\node[anchor=west] at (2.85,4.15) {Kornuta, modified case};',
       r'\draw[black!65,line width=1.3pt] (2.65,3.6)--(2.65,3.85);\node[anchor=west] at (2.85,3.73) {Sowers, timing interval};',r'\end{tikzpicture}']
    return '\n'.join([r'\begin{figure}[t]\centering',*out,r'''\caption{Conditional NPV at the five stored discount rates, for a surface price of 500 account units/kg and unit relative-cost multiplier. Vertical intervals describe expenditure timing, not statistical error bars. Symbols are displaced slightly horizontally for visibility. The interval collapses at zero discounting.}\label{fig:rates}\end{figure}'''])

def main():
    rows=csvrows('surface_offtake_sensitivity.csv')
    source=(ROOT/'research/journal-manuscript.tex').read_text(encoding='utf-8')
    replacements={'KORNUTA_TABLE':kornuta_table(),'TIMING_TABLE':timing_table(),'PRICE_FIGURE':price_figure(rows),'RATE_FIGURE':rate_figure(rows)}
    for key,value in replacements.items(): source=source.replace('@@'+key+'@@',value)
    assert '@@' not in source
    out=ROOT/'research/final-manuscript.tex'
    out.write_text(source,encoding='utf-8')
    print(out)
if __name__=='__main__': main()
