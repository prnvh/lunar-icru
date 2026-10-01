"""Build research/final-manuscript.tex from the markdown manuscript and supplement."""

from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent


def dedent_file(path: Path) -> str:
    lines = path.read_text(encoding="utf-8").splitlines()
    if lines and all((not line) or line.startswith("    ") for line in lines):
        lines = [line[4:] if line.startswith("    ") else line for line in lines]
        path.write_text("\n".join(lines) + "\n", encoding="utf-8")
    return "\n".join(lines) + "\n"


def escape(text: str) -> str:
    placeholders: list[str] = []

    def hold(token: str) -> str:
        placeholders.append(token)
        return f"\x00{len(placeholders) - 1}\x00"

    text = re.sub(r"https?://\S+", lambda m: hold(m.group(0).rstrip(").,")), text)
    text = re.sub(r"`([^`]+)`", lambda m: hold("TT:" + m.group(1)), text)
    text = re.sub(r"\*\*([^*]+)\*\*", lambda m: hold("BF:" + m.group(1)), text)
    text = text.replace("\\", r"\textbackslash{}")
    for char, repl in (
        ("&", r"\&"),
        ("%", r"\%"),
        ("$", r"\$"),
        ("#", r"\#"),
        ("_", r"\_"),
        ("{", r"\{"),
        ("}", r"\}"),
        ("~", r"\textasciitilde{}"),
        ("^", r"\textasciicircum{}"),
    ):
        text = text.replace(char, repl)
    text = text.replace("\u2013", "--").replace("\u2014", "---")
    text = text.replace("\u2212", "-").replace("\u00d7", r"$\times$")
    text = text.replace("\u2264", r"$\leq$").replace("\u2265", r"$\geq$")
    text = text.replace("\u201c", "``").replace("\u201d", "''")
    text = text.replace("\u2018", "`").replace("\u2019", "'")

    def restore(match: re.Match[str]) -> str:
        token = placeholders[int(match.group(1))]
        if token.startswith("BF:"):
            return r"\textbf{" + escape(token[3:]) + "}"
        if token.startswith("TT:"):
            inner = token[3:].replace("\\", r"\textbackslash{}")
            for char, repl in (("&", r"\&"), ("%", r"\%"), ("$", r"\$"), ("#", r"\#"), ("_", r"\_"), ("{", r"\{"), ("}", r"\}")):
                inner = inner.replace(char, repl)
            return r"\texttt{" + inner + "}"
        return r"\url{" + token + "}"

    return re.sub(r"\x00(\d+)\x00", restore, text)


def table_to_latex(rows: list[list[str]]) -> str:
    header, body = rows[0], rows[1:]
    ncol = len(header)
    escaped = [[escape(cell.strip()) for cell in row] for row in [header] + body]
    if ncol == 2:
        spec = r"@{}p{0.32\textwidth}p{0.64\textwidth}@{}"
        size = r"\small"
    elif ncol >= 7:
        spec = "c" * ncol
        size = r"\scriptsize"
    elif ncol >= 5:
        spec = r"@{}p{0.18\textwidth}p{0.18\textwidth}p{0.16\textwidth}p{0.2\textwidth}p{0.2\textwidth}@{}"
        size = r"\footnotesize"
    else:
        spec = "l" + "c" * (ncol - 1)
        size = r"\small"
    lines = [size, r"\begin{tabular}{" + spec + "}", r"\toprule"]
    lines.append(" & ".join(r"\textbf{" + cell + "}" for cell in escaped[0]) + r" \\")
    lines.append(r"\midrule")
    for row in escaped[1:]:
        while len(row) < ncol:
            row.append("")
        lines.append(" & ".join(row[:ncol]) + r" \\")
    lines.append(r"\bottomrule")
    lines.append(r"\end{tabular}")
    if ncol >= 7:
        return "\\noindent\\resizebox{\\textwidth}{!}{%\n" + "\n".join(lines) + "\n}"
    return "\\begin{center}\n" + "\n".join(lines) + "\n\\end{center}"


def blocks_to_latex(markdown: str, title_mode: bool) -> str:
    lines = markdown.splitlines()
    out: list[str] = []
    i = 0
    title_done = not title_mode
    while i < len(lines):
        line = lines[i]
        if not line.strip():
            i += 1
            continue
        if line.startswith("```"):
            chunk: list[str] = []
            i += 1
            while i < len(lines) and not lines[i].startswith("```"):
                chunk.append(lines[i])
                i += 1
            i += 1
            body = "\n".join(chunk).strip()
            if any(tok in body for tok in ("=", "PV", "NPV", "Q =")):
                math = body.replace("×", r" \times ").replace("−", "-").replace("–", "-")
                math = math.replace("≤", r" \leq ").replace("≥", r" \geq ")
                math = math.replace("%", r"\%")
                out.append("\\begin{quote}\\ttfamily\\raggedright")
                out.append(escape(body).replace(r"\textbackslash{}", "\\"))
                out.append("\\end{quote}")
            else:
                out.append("\\begin{verbatim}")
                out.append(body)
                out.append("\\end{verbatim}")
            continue
        if line.startswith("|"):
            rows: list[list[str]] = []
            while i < len(lines) and lines[i].startswith("|"):
                raw = lines[i].strip().strip("|")
                cells = [c.strip() for c in raw.split("|")]
                if not all(set(c) <= set("-: ") for c in cells):
                    rows.append(cells)
                i += 1
            out.append(table_to_latex(rows))
            continue
        if line.startswith("# "):
            title = line[2:].strip()
            i += 1
            subtitle = ""
            if i < len(lines) and lines[i].strip() and not lines[i].startswith("#"):
                subtitle = lines[i].strip()
                i += 1
            if not title_done:
                out.append("\\title{" + escape(title) + "}")
                if subtitle:
                    out.append("\\subtitle{" + escape(subtitle) + "}")
                out.append("\\author{}")
                out.append("\\date{}")
                out.append("\\maketitle")
                title_done = True
            else:
                out.append("\\section*{" + escape(title.lstrip("# ").strip()) + "}")
            continue
        if line.startswith("## "):
            heading = line[3:].strip()
            i += 1
            if heading == "Abstract":
                paras = []
                buf: list[str] = []
                while i < len(lines) and not lines[i].startswith("## "):
                    if lines[i].startswith("**Keywords:**"):
                        if buf:
                            paras.append(" ".join(buf))
                            buf = []
                        kw = lines[i].split("**Keywords:**", 1)[1].strip().strip("*")
                        paras.append("KEYWORDS:" + kw)
                        i += 1
                        continue
                    if not lines[i].strip():
                        if buf:
                            paras.append(" ".join(buf))
                            buf = []
                    else:
                        buf.append(lines[i].strip())
                    i += 1
                if buf:
                    paras.append(" ".join(buf))
                out.append("\\begin{abstract}")
                for para in paras:
                    if para.startswith("KEYWORDS:"):
                        out.append("\\vspace{0.6em}\\noindent\\textbf{Keywords:} " + escape(para[9:]))
                    else:
                        out.append(escape(para) + "\n")
                out.append("\\end{abstract}")
            elif heading.startswith("Appendix"):
                out.append("\\appendix")
                out.append("\\section{" + escape(heading.split(".", 1)[-1].strip()) + "}")
            elif heading == "References":
                out.append("\\begin{thebibliography}{99}")
            else:
                name = re.sub(r"^\d+\.\s*", "", heading)
                out.append("\\section{" + escape(name) + "}")
            continue
        if line.startswith("### "):
            heading = re.sub(r"^\d+\.\d+\s*", "", line[4:].strip())
            out.append("\\subsection{" + escape(heading) + "}")
            i += 1
            continue
        if re.match(r"^\[\d+\] ", line):
            body = line.strip()
            num = re.match(r"^\[(\d+)\] ", body).group(1)
            rest = body.split("] ", 1)[1]
            out.append("\\bibitem{" + num + "} " + escape(rest))
            i += 1
            continue
        if line.startswith("- "):
            out.append("\\begin{itemize}")
            while i < len(lines) and lines[i].startswith("- "):
                out.append("\\item " + escape(lines[i][2:].strip()))
                i += 1
            out.append("\\end{itemize}")
            continue
        if re.match(r"^\d+\. ", line):
            out.append("\\begin{enumerate}")
            while i < len(lines) and re.match(r"^\d+\. ", lines[i]):
                item = re.sub(r"^\d+\. ", "", lines[i]).strip()
                out.append("\\item " + escape(item))
                i += 1
            out.append("\\end{enumerate}")
            continue
        para = [line.strip()]
        i += 1
        while i < len(lines) and lines[i].strip() and not lines[i].startswith(("#", "|", "-", "```")) and not re.match(r"^(\d+\. |\[\d+\] )", lines[i]):
            para.append(lines[i].strip())
            i += 1
        text = " ".join(para)
        if text == "References are numbered in order of first appearance, in the style of \\textit{Acta Astronautica}. All authors are listed.":
            continue
        out.append(escape(text) + "\n")
    if "\\begin{thebibliography}" in "\n".join(out):
        out.append("\\end{thebibliography}")
    return "\n\n".join(out)


def main() -> None:
    import runpy
    runpy.run_path(str(ROOT.parent / "analysis/build_latex_paper.py"), run_name="__main__")


if __name__ == "__main__":
    main()
