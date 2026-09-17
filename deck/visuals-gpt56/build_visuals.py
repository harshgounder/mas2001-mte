#!/usr/bin/env python3
"""Build exact SVG study visuals for the MAS2001 visual companion."""

import math
import pathlib


ROOT = pathlib.Path(__file__).resolve().parent
ASSETS = ROOT / "assets"
W, H = 1200, 720

COLORS = {
    "ink": "#172033",
    "muted": "#64748b",
    "grid": "#dbe3ee",
    "blue": "#2563eb",
    "cyan": "#0891b2",
    "green": "#16a34a",
    "orange": "#ea580c",
    "purple": "#7c3aed",
    "red": "#dc2626",
    "paper": "#ffffff",
    "soft": "#f8fafc",
}


def esc(value):
    return str(value).replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def text(x, y, value, size=24, weight=400, anchor="start", fill=None):
    fill = fill or COLORS["ink"]
    return (
        f'<text x="{x}" y="{y}" font-family="Inter,Arial,sans-serif" '
        f'font-size="{size}" font-weight="{weight}" text-anchor="{anchor}" '
        f'fill="{fill}">{esc(value)}</text>'
    )


def line(x1, y1, x2, y2, color=None, width=3, dash=None):
    extra = f' stroke-dasharray="{dash}"' if dash else ""
    return (
        f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" '
        f'stroke="{color or COLORS["ink"]}" stroke-width="{width}"{extra}/>'
    )


def box(x, y, w, h, label, color="blue", sub=None):
    out = [
        f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="18" '
        f'fill="{COLORS[color]}18" stroke="{COLORS[color]}" stroke-width="3"/>',
        text(x + w / 2, y + 38, label, 23, 500, "middle"),
    ]
    if sub:
        out.append(text(x + w / 2, y + 68, sub, 17, 400, "middle", COLORS["muted"]))
    return "".join(out)


def svg(name, title, body, height=H, desc=""):
    ASSETS.mkdir(parents=True, exist_ok=True)
    content = (
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {height}" '
        f'role="img" aria-labelledby="title desc">'
        f'<title id="title">{esc(title)}</title><desc id="desc">{esc(desc)}</desc>'
        f'<rect width="{W}" height="{height}" fill="{COLORS["paper"]}"/>'
        + body
        + "</svg>\n"
    )
    (ASSETS / name).write_text(content, encoding="utf-8")


def course_map():
    b = [text(60, 62, "MAS2001 MTE concept map", 34, 500)]
    b.append(box(455, 95, 290, 86, "Probability foundations", "blue", "sample spaces, counting, rules"))
    nodes = [
        (70, 260, "Random variables", "pmf, pdf, cdf", "cyan"),
        (350, 260, "Expectation", "mean, variance, transforms", "purple"),
        (630, 260, "Distributions", "B, Poi, U, N, Exp", "orange"),
        (910, 260, "Bounds", "Chebyshev", "red"),
        (230, 470, "Sampling", "SE and CLT", "green"),
        (690, 470, "Estimation", "bias, consistency, efficiency", "blue"),
    ]
    for x, y, label, sub, color in nodes:
        b.append(box(x, y, 220, 90, label, color, sub))
    for x in (180, 460, 740, 1020):
        b.append(line(600, 181, x, 260, COLORS["grid"], 4))
    b.extend([line(460, 350, 340, 470, COLORS["grid"], 4), line(740, 350, 800, 470, COLORS["grid"], 4)])
    b.append(text(600, 650, "Overview only. Read connectors as prerequisites, not as claims of independence.", 20, 400, "middle", COLORS["muted"]))
    svg("course-map.svg", "MAS2001 MTE concept map", "".join(b), desc="Prerequisite map from foundations to sampling and estimation")


def probability_tree():
    b = [text(60, 60, "Conditional probability tree", 34, 500)]
    root = (130, 340)
    b.append(box(55, 300, 150, 70, "Start", "blue"))
    branches = [(390, 190, "A", "P(A)"), (390, 490, "not A", "1-P(A)")]
    for x, y, label, prob in branches:
        b.append(line(205, 335, x, y + 30, COLORS["blue"], 4))
        b.append(text(285, (335 + y + 30) / 2 - 8, prob, 20, 500, "middle", COLORS["blue"]))
        b.append(box(x, y, 170, 70, label, "cyan"))
    leaves = [(770, 95, "B", "P(B|A)"), (770, 275, "not B", "1-P(B|A)"), (770, 405, "B", "P(B|not A)"), (770, 585, "not B", "1-P(B|not A)")]
    for i, (x, y, label, prob) in enumerate(leaves):
        sy = 225 if i < 2 else 525
        b.append(line(560, sy, x, y + 30, COLORS["cyan"], 4))
        b.append(text(660, (sy + y + 30) / 2 - 7, prob, 17, 500, "middle", COLORS["cyan"]))
        b.append(box(x, y, 190, 65, label, "green"))
    b.append(text(1060, 164, "P(A and B)", 20, 500, "middle"))
    b.append(text(1060, 194, "= P(A)P(B|A)", 20, 400, "middle", COLORS["muted"]))
    b.append(line(960, 128, 1010, 164, COLORS["green"], 3))
    svg("probability-tree.svg", "Conditional probability tree", "".join(b), desc="Two-stage probability tree with multiplication along branches")


def dice_heatmap():
    b = [text(60, 58, "Two dice: 36 ordered outcomes", 34, 500)]
    x0, y0, cell = 265, 120, 72
    palette = ["#eff6ff", "#dbeafe", "#bfdbfe", "#93c5fd", "#60a5fa", "#3b82f6"]
    for i in range(6):
        b.append(text(x0 - 42, y0 + i * cell + 46, str(i + 1), 20, 500, "middle"))
        b.append(text(x0 + i * cell + 36, y0 - 22, str(i + 1), 20, 500, "middle"))
        for j in range(6):
            s = i + j + 2
            shade = palette[5 - min(abs(s - 7), 5)]
            b.append(f'<rect x="{x0+j*cell}" y="{y0+i*cell}" width="{cell}" height="{cell}" fill="{shade}" stroke="#ffffff" stroke-width="3"/>')
            b.append(text(x0 + j * cell + 36, y0 + i * cell + 43, f"({i+1},{j+1})", 16, 500, "middle"))
    b.append(text(x0 + 216, 92, "die 2", 20, 500, "middle", COLORS["muted"]))
    b.append(text(160, y0 + 220, "die 1", 20, 500, "middle", COLORS["muted"]))
    b.append(text(x0 + 216, 585, "cell = ordered pair; colour = sum", 17, 400, "middle", COLORS["muted"]))
    counts = [1, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1]
    bx, by = 760, 575
    for idx, count in enumerate(counts):
        h = count * 55
        b.append(f'<rect x="{bx+idx*34}" y="{by-h}" width="27" height="{h}" fill="{COLORS["orange"]}" opacity="0.8"/>')
        b.append(text(bx + idx * 34 + 13, by + 25, idx + 2, 14, 400, "middle"))
    b.append(text(945, 145, "sum frequencies", 22, 500, "middle"))
    b.append(text(945, 630, "sum", 17, 400, "middle", COLORS["muted"]))
    svg("dice-sum.svg", "Two dice ordered-outcome heatmap", "".join(b), desc="Heatmap of ordered dice outcomes and triangular sum frequencies")


def pmf_cdf():
    b = [text(60, 58, "PMF accumulates into a CDF", 34, 500)]
    xs = list(range(7)); ps = [.05, .10, .15, .25, .20, .15, .10]
    for panel, title, vals, step in [(70, "PMF p(x)", ps, False), (650, "CDF F(x)", [sum(ps[:i+1]) for i in xs], True)]:
        x0, y0, pw, ph = panel, 150, 470, 430
        b.extend([text(x0, 115, title, 24, 500), line(x0, y0+ph, x0+pw, y0+ph, COLORS["ink"], 2), line(x0, y0, x0, y0+ph, COLORS["ink"], 2)])
        if step:
            first_x = x0 + 45
            first_y = y0 + ph - vals[0] * 360
            b.append(line(x0 + 10, y0 + ph, first_x, y0 + ph, COLORS["purple"], 5))
            b.append(line(first_x, y0 + ph, first_x, first_y, COLORS["purple"], 2, "7 7"))
        for i, v in enumerate(vals):
            x = x0 + 45 + i * 58
            y = y0 + ph - v * (360 if step else 1350)
            if step:
                nx = x0 + 45 + (i + 1) * 58 if i < 6 else x0 + pw - 15
                b.append(line(x, y, nx, y, COLORS["purple"], 5))
                if i < 6:
                    b.append(line(nx, y, nx, y0 + ph - vals[i+1] * 360, COLORS["purple"], 2, "7 7"))
            else:
                b.append(line(x, y0+ph, x, y, COLORS["blue"], 12))
                b.append(f'<circle cx="{x}" cy="{y}" r="8" fill="{COLORS["blue"]}"/>')
            b.append(text(x, y0 + ph + 30, i, 15, 400, "middle"))
        b.append(text(x0 + pw / 2, y0 + ph + 65, "x", 18, 500, "middle"))
    svg("pmf-to-cdf.svg", "PMF to CDF", "".join(b), desc="Side-by-side discrete mass and cumulative step plots")


def distribution_gallery():
    b = [text(60, 58, "Five distribution shapes", 34, 500)]
    panels = [(45, "Binomial", "B(5, 0.5)", "blue"), (280, "Poisson", "Poi(2), k=0..5", "cyan"), (515, "Uniform", "U(0, 1)", "green"), (750, "Normal", "N(0, 1)", "purple"), (985, "Exponential", "Exp(1)", "orange")]
    for x0, label, parameter, color in panels:
        b.append(text(x0 + 85, 115, label, 21, 500, "middle"))
        b.append(text(x0 + 85, 142, parameter, 16, 400, "middle", COLORS["muted"]))
        b.extend([line(x0, 540, x0 + 180, 540, COLORS["ink"], 2), line(x0, 160, x0, 540, COLORS["ink"], 2)])
        if label in ("Binomial", "Poisson"):
            vals = ([.03125,.15625,.3125,.3125,.15625,.03125] if label == "Binomial" else [math.exp(-2) * 2**k / math.factorial(k) for k in range(6)])
            for i, v in enumerate(vals):
                b.append(f'<rect x="{x0+18+i*26}" y="{540-v*850}" width="18" height="{v*850}" fill="{COLORS[color]}"/>')
        elif label == "Uniform":
            b.append(f'<path d="M{x0+20},540 L{x0+20},285 L{x0+160},285 L{x0+160},540" fill="none" stroke="{COLORS[color]}" stroke-width="6"/>')
        elif label == "Normal":
            pts=[]
            for i in range(181):
                z=(i-90)/27; y=math.exp(-z*z/2); pts.append(f"{x0+i},{540-y*310}")
            b.append(f'<polyline points="{" ".join(pts)}" fill="none" stroke="{COLORS[color]}" stroke-width="6"/>')
        else:
            pts=[]
            for i in range(161):
                y=math.exp(-i/42); pts.append(f"{x0+12+i},{540-y*340}")
            b.append(f'<polyline points="{" ".join(pts)}" fill="none" stroke="{COLORS[color]}" stroke-width="6"/>')
    b.append(text(262, 635, "Discrete counts", 19, 500, "middle", COLORS["muted"]))
    b.append(line(80, 605, 445, 605, COLORS["grid"], 3))
    b.append(text(840, 635, "Continuous measurements or waiting time", 19, 500, "middle", COLORS["muted"]))
    b.append(line(540, 605, 1140, 605, COLORS["grid"], 3))
    svg("distribution-gallery.svg", "Five distribution shapes", "".join(b), desc="Small multiples for binomial, Poisson, uniform, normal, and exponential distributions")


def normal_tables():
    b = [text(60, 58, "Two normal-table conventions", 34, 500)]
    for x0, title, left in [(70, "p022: cumulative P(Z < z)", True), (650, "p023: centre area P(0 < Z < z)", False)]:
        base=510; pts=[]
        for i in range(460):
            z=(i-230)/75; y=math.exp(-z*z/2); pts.append((x0+i,base-y*300))
        poly=" ".join(f"{x},{y}" for x,y in pts)
        shade=[p for p in pts if (p[0] <= x0+350 if left else x0+230 <= p[0] <= x0+350)]
        area=f"{shade[0][0]},{base} "+" ".join(f"{x},{y}" for x,y in shade)+f" {shade[-1][0]},{base}"
        b.append(text(x0+230, 115, title, 22, 500, "middle"))
        b.append(f'<polygon points="{area}" fill="{COLORS["blue"]}" opacity="0.25"/>')
        b.append(f'<polyline points="{poly}" fill="none" stroke="{COLORS["blue"]}" stroke-width="5"/>')
        b.append(line(x0, base, x0+460, base, COLORS["ink"], 2))
        b.append(line(x0+230, base-8, x0+230, base+8, COLORS["ink"], 2))
        b.append(line(x0+350, base-8, x0+350, base+8, COLORS["ink"], 2))
        b.append(text(x0+230, base+32, "0", 16, 400, "middle")); b.append(text(x0+350, base+32, "z", 16, 400, "middle"))
        b.append(text(x0+230, 610, "z=2: " + ("0.9772" if left else "0.4772"), 22, 500, "middle"))
    svg("normal-table-conventions.svg", "Two normal table conventions", "".join(b), desc="Cumulative-left and centre-to-z shaded areas")


def sampling_clt():
    b=[text(60,58,"Sampling distributions narrow as n grows",34,500)]
    for idx,(n,sd,color) in enumerate([(5,1.0,"orange"),(50,math.sqrt(5/50),"cyan"),(500,math.sqrt(5/500),"blue")]):
        x0=80+idx*380; base=520; pts=[]
        for i in range(300):
            z=(i-150)/55; y=math.exp(-z*z/(2*sd*sd)); pts.append(f"{x0+i},{base-y*330}")
        b.append(text(x0+150,115,f"n = {n}",23,500,"middle"))
        b.append(f'<polyline points="{" ".join(pts)}" fill="none" stroke="{COLORS[color]}" stroke-width="6"/>')
        b.append(line(x0,base,x0+300,base,COLORS["ink"],2))
        b.append(line(x0+150,base-350,x0+150,base+8,COLORS["grid"],2,"8 8"))
    b.append(text(600,620,"centre stays at mu; widths use the exact 1 / sqrt(n) ratio",24,500,"middle"))
    svg("sampling-clt.svg","Sampling distribution and CLT","".join(b),desc="Three sample-mean distributions with decreasing standard error")


def estimator_comparison():
    b=[text(60,58,"Estimator set 2: all unbiased, compare variance",34,500)]
    b.append(box(430,95,340,78,"T1, T2, and T3","blue","compute each expectation"))
    b.append(line(600,173,600,235,COLORS["grid"],4))
    b.append(box(430,235,340,88,"All are unbiased","green","choose the smallest variance"))
    vals=[("T3",1/3,"green"),("T1",3,"cyan"),("T2",29,"purple")]
    y=410
    for label,val,color in vals:
        width=35+430*math.log1p(val)/math.log(30)
        b.append(text(150,y+27,label,22,500,"end")); b.append(f'<rect x="175" y="{y}" width="{width}" height="38" fill="{COLORS[color]}" opacity="0.82"/>'); b.append(text(190+width,y+27,f"{val:.3g} sigma^2",18,400))
        y+=72
    b.append(text(600,665,"Consistency needs a sequence T_n as n grows; fixed n=3 cannot prove it.",21,500,"middle",COLORS["muted"]))
    svg("estimator-comparison.svg","Estimator comparison workflow","".join(b),desc="Decision flow and variance bars for three estimators")


def chebyshev():
    b=[text(60,58,"Chebyshev: guaranteed mass around the mean",34,500)]
    cx,base=600,485
    pts=[]
    for i in range(900):
        z=(i-450)/95
        y=.62*math.exp(-((z+1.25)/.68)**2)+.62*math.exp(-((z-1.25)/.68)**2)+.10/(1+z*z)
        pts.append((150+i,base-y*270))
    inner=[p for p in pts if 360<=p[0]<=840]
    area=f"{inner[0][0]},{base} "+" ".join(f"{x},{y}" for x,y in inner)+f" {inner[-1][0]},{base}"
    b.append(f'<polygon points="{area}" fill="{COLORS["green"]}" opacity="0.25"/>')
    b.append(f'<polyline points="{" ".join(f"{x},{y}" for x,y in pts)}" fill="none" stroke="{COLORS["purple"]}" stroke-width="5"/>')
    b.append(line(150,base,1050,base,COLORS["ink"],2)); b.append(line(cx,150,cx,base+10,COLORS["grid"],2,"8 8"))
    for x,label in [(360,"µ-kσ"),(600,"µ"),(840,"µ+kσ")]:
        b.append(line(x,base-10,x,base+10,COLORS["ink"],2)); b.append(text(x,base+38,label,17,400,"middle"))
    b.append(text(600,595,"P(|X-µ| < kσ) ≥ 1 - 1/k²",27,500,"middle",COLORS["green"]))
    b.append(text(600,635,"valid for any distribution with finite mean and variance",19,400,"middle",COLORS["muted"]))
    b.append(text(600,668,"schematic density, not a normal-distribution assumption",18,400,"middle",COLORS["red"]))
    svg("chebyshev-bound.svg","Chebyshev inequality","".join(b),desc="Distribution-free central mass guaranteed by Chebyshev inequality")


def study_roadmap():
    b=[text(60,58,"Study order with dependency gates",34,500)]
    steps=[("0","Prerequisites","Chebyshev, indep."),("1","Foundations","counting, conditional"),("2","Random vars","pmf, cdf, moments"),("3","Distributions","five-model shelf"),("4","Sampling + CLT","SE, averages"),("5","Estimation","bias, consistency"),("6","Timed mock","diagnose gaps")]
    y=105
    colors=["red","blue","cyan","orange","green","purple","blue"]
    for i,(num,label,sub) in enumerate(steps):
        x=90+(i%4)*275; yy=y+(i//4)*245
        b.append(f'<circle cx="{x+38}" cy="{yy+42}" r="34" fill="{COLORS[colors[i]]}"/>')
        b.append(text(x+38,yy+50,num,24,500,"middle",COLORS["paper"]))
        b.append(box(x+82,yy,175,84,label,colors[i],sub))
        if i<6:
            nx=90+((i+1)%4)*275; ny=y+((i+1)//4)*245
            if i==3:
                b.append(line(x+257,yy+42,1115,yy+42,COLORS["grid"],3)); b.append(line(1115,yy+42,1115,ny+42,COLORS["grid"],3)); b.append(line(1115,ny+42,nx,ny+42,COLORS["grid"],3))
            else:
                b.append(line(x+257,yy+42,nx,ny+42,COLORS["grid"],3))
    b.append(text(600,650,"advance only after the gate for the current pass is met",22,500,"middle",COLORS["muted"]))
    svg("study-roadmap.svg","MAS2001 study roadmap","".join(b),desc="Seven-stage study sequence from prerequisites to timed mock")


def formula_landscape():
    b = [text(60, 58, "Formula landscape: classify first, then compute", 34, 500)]
    b.append(box(455, 88, 290, 76, "Read the ask", "blue", "name the object and target"))
    cards = [
        (65, 220, "Probability", "P(A|B), counting, independence", "cyan"),
        (625, 220, "Random variables", "pmf, pdf, CDF, E(X), Var(X)", "purple"),
        (65, 410, "Five distributions", "B, Poi, U, N, Exp", "orange"),
        (625, 410, "Bounds and inference", "Chebyshev, SE, CLT, estimators", "green"),
    ]
    for x, y, label, sub, color in cards:
        b.append(line(600, 164, x + 240, y, COLORS["grid"], 4))
        b.append(box(x, y, 480, 92, label, color, sub))
    checks = [("support", 160), ("boundary", 380), ("units", 600), ("exact value", 820)]
    for label, x in checks:
        b.append(box(x, 590, 180, 64, label, "blue"))
    b.append(text(600, 690, "final gate: support, boundary word, units, and exact value", 20, 500, "middle", COLORS["muted"]))
    svg("formula-landscape.svg", "MAS2001 formula landscape", "".join(b), desc="Four-part map for choosing the correct probability or statistics formula")


def method_decision_tree():
    b = [text(60, 58, "Question-solving decision path", 34, 500)]
    b.append(box(50, 105, 220, 78, "1. Identify", "blue", "named model or event?"))
    b.append(line(270, 144, 345, 144, COLORS["grid"], 5))
    b.append(box(345, 105, 250, 78, "2. Choose form", "cyan", "pmf, pdf, CDF, tree"))
    b.append(line(595, 144, 670, 144, COLORS["grid"], 5))
    b.append(box(670, 105, 220, 78, "3. Solve", "purple", "formula or algebra"))
    b.append(line(890, 144, 965, 144, COLORS["grid"], 5))
    b.append(box(965, 105, 185, 78, "4. Check", "green", "three loops"))
    branches = [
        (70, 270, "Discrete", "Binomial or Poisson", "point, tail, interval"),
        (350, 270, "Continuous", "Uniform, Normal, Exp", "area, standardise"),
        (630, 270, "Event", "count or condition", "sets, tree, complement"),
        (910, 270, "Estimator", "bias before variance", "name the winner"),
    ]
    for x, y, label, sub, move in branches:
        b.append(box(x, y, 220, 88, label, "orange", sub))
        b.append(text(x + 110, y + 130, move, 18, 500, "middle", COLORS["muted"]))
    loops = [("SUPPORT", "inside the allowed range"), ("BOUNDARY", "at least versus more than"), ("SANITY", "P in [0,1], variance ≥ 0")]
    for i, (label, sub) in enumerate(loops):
        b.append(box(135 + i * 325, 520, 280, 90, label, ["red", "orange", "green"][i], sub))
    b.append(text(600, 675, "keep exact values until the final line", 22, 500, "middle", COLORS["muted"]))
    svg("method-decision-tree.svg", "Question-solving decision path", "".join(b), desc="Identify, choose, solve, and check workflow with model branches")


def mutation_operator_map():
    b = [text(60, 58, "Question mutation map", 34, 500)]
    b.append(box(55, 105, 300, 90, "Question skeleton", "blue", "model, target, solve path"))
    b.append(box(55, 255, 300, 90, "Surface details", "cyan", "numbers, names, units, story"))
    b.append(text(205, 405, "M0 changes the surface", 21, 500, "middle", COLORS["green"]))
    b.append(text(205, 438, "type usually stays fixed", 19, 400, "middle", COLORS["muted"]))
    ops = [
        ("M1", "INVERT", "swap given and asked", "x to P becomes P to x"),
        ("M2", "RE-CONDITION", "change a structural condition", "replacement, sample size"),
        ("M3", "RE-TARGET", "same setup, new target", "point, tail, conditional"),
        ("M4", "COMPOSE", "nest two models", "solve the inner model first"),
    ]
    for i, (code, name, action, example) in enumerate(ops):
        y = 105 + i * 132
        b.append(box(500, y, 150, 84, code, "purple", name))
        b.append(line(650, y + 42, 705, y + 42, COLORS["grid"], 4))
        b.append(box(705, y, 425, 84, action, "orange", example))
    b.append(line(355, 150, 500, 150, COLORS["grid"], 4))
    b.append(line(355, 300, 430, 300, COLORS["grid"], 4))
    b.append(text(600, 675, "source match confidence belongs to the evidence ledger, not to visual similarity alone", 20, 500, "middle", COLORS["red"]))
    svg("mutation-operators.svg", "Question mutation operators", "".join(b), desc="Difference between surface reskins and structural question mutations")


def exam_timeline():
    b = [text(60, 58, "Ninety-minute practice budget", 34, 500)]
    segments = [("Read", 3, "blue"), ("Section A", 20, "cyan"), ("Section B", 35, "green"), ("Section C", 25, "orange"), ("Check", 7, "purple")]
    x0, y, total_w = 75, 230, 1050
    elapsed = 0
    for label, minutes, color in segments:
        width = total_w * minutes / 90
        b.append(f'<rect x="{x0}" y="{y}" width="{width}" height="120" fill="{COLORS[color]}" opacity="0.88"/>')
        b.append(text(x0 + width / 2, y + 52, label, 22 if width > 100 else 17, 500, "middle", COLORS["paper"]))
        b.append(text(x0 + width / 2, y + 85, f"{minutes} min", 18 if width > 80 else 14, 500, "middle", COLORS["paper"]))
        b.append(text(x0, y + 150, str(elapsed), 17, 500, "middle"))
        elapsed += minutes
        x0 += width
    b.append(text(1125, y + 150, "90", 17, 500, "middle"))
    b.append(text(600, 430, "3 + 20 + 35 + 25 + 7 = 90 minutes", 25, 500, "middle"))
    b.append(box(155, 510, 380, 90, "Section C is an 8-mark block", "orange", "its topic may change"))
    b.append(box(665, 510, 380, 90, "Leave seven minutes to check", "purple", "boundaries, units, missed parts"))
    svg("exam-timeline.svg", "Ninety-minute exam practice budget", "".join(b), desc="Proportional ninety-minute timeline for reading, three sections, and checking")


def expectation_variance():
    b = [text(60, 58, "Mean is the balance point; variance is squared spread", 34, 500)]
    x0, base = 120, 265
    weights = [(1, .10), (2, .20), (3, .40), (4, .20), (5, .10)]
    b.append(line(x0, base, x0 + 430, base, COLORS["ink"], 5))
    for value, probability in weights:
        x = x0 + (value - 1) * 107
        b.append(f'<circle cx="{x}" cy="{base}" r="10" fill="{COLORS["blue"]}"/>')
        b.append(f'<rect x="{x-18}" y="{base-probability*260}" width="36" height="{probability*260}" fill="{COLORS["cyan"]}"/>')
        b.append(text(x, base + 35, value, 17, 500, "middle"))
    mean_x = x0 + 2 * 107
    b.append(line(mean_x, 105, mean_x, base + 15, COLORS["red"], 3, "8 6"))
    b.append(text(mean_x, 95, "E(X) = 3", 22, 500, "middle", COLORS["red"]))
    b.append(text(335, 330, "probability weights balance at the mean", 19, 400, "middle", COLORS["muted"]))
    distributions = [(720, "small variance", [(-1,.2),(0,.6),(1,.2)], "green"), (980, "large variance", [(-2,.2),(0,.6),(2,.2)], "purple")]
    for cx, label, points, color in distributions:
        b.append(text(cx, 135, label, 21, 500, "middle"))
        b.append(line(cx - 120, base, cx + 120, base, COLORS["ink"], 3))
        for offset, probability in points:
            x = cx + offset * 52
            b.append(f'<rect x="{x-16}" y="{base-probability*210}" width="32" height="{probability*210}" fill="{COLORS[color]}"/>')
        b.append(text(cx, base + 35, "same mean", 17, 500, "middle", COLORS["muted"]))
    b.append(box(150, 455, 400, 105, "Expectation", "blue", "E[h(X)] = sum or integral of h(x) times weight"))
    b.append(box(650, 455, 400, 105, "Variance", "purple", "Var(X) = E(X²) - [E(X)]²"))
    b.append(text(600, 650, "shifts preserve variance; multiplying by a scales variance by a²", 22, 500, "middle"))
    svg("expectation-variance.svg", "Expectation and variance", "".join(b), desc="Probability balance point and two distributions with the same mean but different variance")


def continuous_pdf_cdf():
    b = [text(60, 58, "Continuous probability: area, accumulation, derivative", 34, 500)]
    b.append(box(70, 115, 300, 95, "PDF f(x)", "cyan", "nonnegative; total area = 1"))
    b.append(box(450, 115, 300, 95, "Probability", "green", "area from a to b"))
    b.append(box(830, 115, 300, 95, "CDF F(x)", "purple", "area to the left of x"))
    b.append(line(370, 162, 450, 162, COLORS["grid"], 5))
    b.append(text(410, 145, "integrate", 16, 500, "middle", COLORS["muted"]))
    b.append(line(750, 162, 830, 162, COLORS["grid"], 5))
    b.append(text(790, 145, "accumulate", 16, 500, "middle", COLORS["muted"]))
    b.append(text(600, 285, "F(x) = integral from -infinity to x of f(t) dt", 25, 500, "middle"))
    b.append(text(600, 330, "f(x) = F'(x), where an absolutely continuous F is differentiable", 22, 500, "middle", COLORS["purple"]))
    b.append(box(70, 410, 315, 100, "Endpoints", "blue", "P(a<X<b) = P(a≤X≤b)"))
    b.append(box(442, 410, 315, 100, "Support", "orange", "clip intervals to where f is nonzero"))
    b.append(box(815, 410, 315, 100, "Point mass", "red", "P(X=c)=0 is not impossible"))
    b.append(text(600, 590, "continuous interval: F(b) - F(a)", 24, 500, "middle"))
    b.append(text(600, 635, "integer-valued interval: F(b) - F(a-1)", 24, 500, "middle", COLORS["red"]))
    svg("continuous-pdf-cdf.svg", "Continuous PDF and CDF relationships", "".join(b), desc="Relationship between density, interval area, cumulative distribution, and differentiation")


BUILDERS = [course_map, probability_tree, dice_heatmap, pmf_cdf, distribution_gallery,
            normal_tables, sampling_clt, estimator_comparison, chebyshev, study_roadmap,
            formula_landscape, method_decision_tree, mutation_operator_map, exam_timeline,
            expectation_variance, continuous_pdf_cdf]


def main():
    for builder in BUILDERS:
        builder()
    print(f"wrote {len(BUILDERS)} SVG files to {ASSETS}")


if __name__ == "__main__":
    main()
