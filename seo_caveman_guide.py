from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.lib import colors
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, HRFlowable, PageBreak
)
from reportlab.lib.enums import TA_CENTER, TA_LEFT

OUTPUT = "/home/user/smart-skill-user/SEO_Caveman_Guide.pdf"

doc = SimpleDocTemplate(
    OUTPUT,
    pagesize=letter,
    rightMargin=0.75 * inch,
    leftMargin=0.75 * inch,
    topMargin=0.75 * inch,
    bottomMargin=0.75 * inch,
)

# ── Styles ──────────────────────────────────────────────────────────────────
styles = getSampleStyleSheet()

DARK = colors.HexColor("#1A1A2E")
ACCENT = colors.HexColor("#E94560")
LIGHT_BG = colors.HexColor("#F4F4F8")
MID_BG = colors.HexColor("#E8E8F0")
WHITE = colors.white
GREEN = colors.HexColor("#2ECC71")
ORANGE = colors.HexColor("#E67E22")
BLUE = colors.HexColor("#2980B9")

title_style = ParagraphStyle(
    "Title", fontSize=26, textColor=WHITE, alignment=TA_CENTER,
    fontName="Helvetica-Bold", leading=32, spaceAfter=4
)
sub_style = ParagraphStyle(
    "Sub", fontSize=12, textColor=colors.HexColor("#CCCCDD"),
    alignment=TA_CENTER, fontName="Helvetica", spaceAfter=0
)
section_style = ParagraphStyle(
    "Section", fontSize=16, textColor=WHITE, fontName="Helvetica-Bold",
    leading=20, spaceAfter=4
)
h2_style = ParagraphStyle(
    "H2", fontSize=13, textColor=DARK, fontName="Helvetica-Bold",
    leading=16, spaceAfter=2, spaceBefore=6
)
h3_style = ParagraphStyle(
    "H3", fontSize=11, textColor=ACCENT, fontName="Helvetica-Bold",
    leading=14, spaceAfter=2, spaceBefore=4
)
body_style = ParagraphStyle(
    "Body", fontSize=10, textColor=DARK, fontName="Helvetica",
    leading=14, spaceAfter=2
)
bullet_style = ParagraphStyle(
    "Bullet", fontSize=10, textColor=DARK, fontName="Helvetica",
    leading=13, leftIndent=14, spaceAfter=2,
    bulletText="•"
)
caveman_style = ParagraphStyle(
    "Caveman", fontSize=11, textColor=DARK, fontName="Helvetica-Bold",
    leading=15, spaceAfter=2, leftIndent=8
)
note_style = ParagraphStyle(
    "Note", fontSize=9, textColor=colors.HexColor("#555566"),
    fontName="Helvetica-Oblique", leading=12, spaceAfter=2
)
price_style = ParagraphStyle(
    "Price", fontSize=10, textColor=GREEN, fontName="Helvetica-Bold",
    leading=13
)


def dark_banner(text, sub=None):
    """Full-width dark header banner."""
    inner = [Paragraph(text, title_style)]
    if sub:
        inner.append(Paragraph(sub, sub_style))
    t = Table([[inner]], colWidths=[7.0 * inch])
    t.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, -1), DARK),
        ("ROWPADDING", (0, 0), (-1, -1), 14),
        ("TOPPADDING", (0, 0), (-1, -1), 18),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 18),
    ]))
    return t


def section_banner(text, color=ACCENT):
    t = Table([[Paragraph(text, section_style)]], colWidths=[7.0 * inch])
    t.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, -1), color),
        ("ROWPADDING", (0, 0), (-1, -1), 8),
    ]))
    return t


def info_box(lines, bg=LIGHT_BG):
    """Shaded box with list of Paragraph objects or strings."""
    content = []
    for l in lines:
        if isinstance(l, str):
            content.append(Paragraph(l, body_style))
        else:
            content.append(l)
    t = Table([[content]], colWidths=[7.0 * inch])
    t.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, -1), bg),
        ("ROWPADDING", (0, 0), (-1, -1), 8),
        ("LEFTPADDING", (0, 0), (-1, -1), 12),
        ("RIGHTPADDING", (0, 0), (-1, -1), 12),
    ]))
    return t


def option_block(num, site, da, price, why, angle):
    """Single guest post option card."""
    header = Paragraph(f"OPTION {num}:  {site}", h2_style)
    da_p = Paragraph(f"<b>Domain Authority:</b>  {da}", body_style)
    price_p = Paragraph(f"<b>Price:</b>  {price}", price_style)
    why_p = Paragraph(f"<b>Why it works:</b>  {why}", body_style)
    angle_p = Paragraph(f"<b>What to write about:</b>  {angle}", body_style)

    t = Table([[
        [header, Spacer(1, 4), da_p, price_p, Spacer(1, 4), why_p, angle_p]
    ]], colWidths=[7.0 * inch])
    t.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, -1), LIGHT_BG),
        ("LEFTPADDING", (0, 0), (-1, -1), 12),
        ("RIGHTPADDING", (0, 0), (-1, -1), 12),
        ("TOPPADDING", (0, 0), (-1, -1), 10),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 10),
        ("BOX", (0, 0), (-1, -1), 1.5, ACCENT),
    ]))
    return t


def pricing_table(rows, title="PRICING SUMMARY"):
    header_row = [
        Paragraph(title, ParagraphStyle("TH", fontSize=9, textColor=WHITE,
                                        fontName="Helvetica-Bold", alignment=TA_CENTER)),
        Paragraph("DA", ParagraphStyle("TH", fontSize=9, textColor=WHITE,
                                       fontName="Helvetica-Bold", alignment=TA_CENTER)),
        Paragraph("PRICE", ParagraphStyle("TH", fontSize=9, textColor=WHITE,
                                          fontName="Helvetica-Bold", alignment=TA_CENTER)),
        Paragraph("PRIORITY", ParagraphStyle("TH", fontSize=9, textColor=WHITE,
                                             fontName="Helvetica-Bold", alignment=TA_CENTER)),
    ]
    table_data = [header_row]
    for r in rows:
        table_data.append([
            Paragraph(r[0], ParagraphStyle("TD", fontSize=8, fontName="Helvetica", leading=11)),
            Paragraph(r[1], ParagraphStyle("TD", fontSize=8, fontName="Helvetica-Bold",
                                           textColor=BLUE, alignment=TA_CENTER, leading=11)),
            Paragraph(r[2], ParagraphStyle("TD", fontSize=8, fontName="Helvetica-Bold",
                                           textColor=GREEN, alignment=TA_CENTER, leading=11)),
            Paragraph(r[3], ParagraphStyle("TD", fontSize=8, fontName="Helvetica-Bold",
                                           textColor=ACCENT, alignment=TA_CENTER, leading=11)),
        ])

    t = Table(table_data, colWidths=[2.8 * inch, 1.2 * inch, 1.6 * inch, 1.4 * inch])
    t.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, 0), DARK),
        ("ROWBACKGROUNDS", (0, 1), (-1, -1), [WHITE, LIGHT_BG]),
        ("GRID", (0, 0), (-1, -1), 0.5, MID_BG),
        ("TOPPADDING", (0, 0), (-1, -1), 6),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 6),
        ("LEFTPADDING", (0, 0), (-1, -1), 6),
    ]))
    return t


# ── Build Story ──────────────────────────────────────────────────────────────
story = []

# ── COVER ────────────────────────────────────────────────────────────────────
story.append(dark_banner(
    "LOCAL SEO BACKLINK GUIDE",
    "THE CAVEMAN VERSION  |  3 CLIENTS  |  MAY 2026"
))
story.append(Spacer(1, 14))

story.append(info_box([
    Paragraph("WHAT IS THIS?", h3_style),
    Paragraph(
        "You want Google and AI to find your business when local people search for you. "
        "Backlinks are links from other websites pointing TO your site. "
        "The bigger and more trusted that website — the more Google trusts YOU.",
        body_style
    ),
    Spacer(1, 6),
    Paragraph("THE SIMPLE RULE:", h3_style),
    Paragraph(
        "Big website talks about you + links to you = Google thinks you are important. "
        "More important = you show up higher. Higher = more customers.",
        caveman_style
    ),
]))
story.append(Spacer(1, 10))

story.append(info_box([
    Paragraph("YOUR 3 SITES — WHERE THEY STAND RIGHT NOW", h3_style),
], bg=MID_BG))
story.append(Spacer(1, 4))

snapshot_data = [
    ["WEBSITE", "MONTHLY VISITORS", "KEYWORDS RANKING", "STATUS"],
    ["toothology.care\n(Brooklyn, NY)", "94", "74", "Just starting"],
    ["atlascareaba.com\n(Iowa)", "40", "84", "Very new"],
    ["waynesroofingco.com\n(North Jersey)", "684", "369", "Growing"],
]
snap_t = Table(snapshot_data, colWidths=[2.2 * inch, 1.7 * inch, 1.7 * inch, 1.4 * inch])
snap_t.setStyle(TableStyle([
    ("BACKGROUND", (0, 0), (-1, 0), DARK),
    ("TEXTCOLOR", (0, 0), (-1, 0), WHITE),
    ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
    ("FONTSIZE", (0, 0), (-1, -1), 9),
    ("ROWBACKGROUNDS", (0, 1), (-1, -1), [WHITE, LIGHT_BG]),
    ("GRID", (0, 0), (-1, -1), 0.5, MID_BG),
    ("TOPPADDING", (0, 0), (-1, -1), 7),
    ("BOTTOMPADDING", (0, 0), (-1, -1), 7),
    ("LEFTPADDING", (0, 0), (-1, -1), 8),
    ("ALIGN", (1, 0), (-1, -1), "CENTER"),
    ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
]))
story.append(snap_t)
story.append(Spacer(1, 6))
story.append(Paragraph(
    "All 3 sites are early-stage. This is GOOD NEWS — even 3-5 quality backlinks "
    "will make a noticeable difference fast.",
    note_style
))

story.append(PageBreak())

# ── CLIENT 1: TOOTHOLOGY ────────────────────────────────────────────────────
story.append(section_banner("CLIENT 1:  TOOTHOLOGY.CARE  —  WILLIAMSBURG, BROOKLYN NY", ACCENT))
story.append(Spacer(1, 8))

story.append(info_box([
    Paragraph("WHAT THEY DO:", h3_style),
    Paragraph("Dentist office in Williamsburg, Brooklyn. Needs local people to find them when searching for a dentist nearby.", body_style),
    Spacer(1, 4),
    Paragraph("THE PROBLEM:", h3_style),
    Paragraph("Only 94 people visit the site per month. Lots of competition in Brooklyn. Google does not know they exist yet.", body_style),
    Spacer(1, 4),
    Paragraph("THE FIX:", h3_style),
    Paragraph("Get links from NYC health websites, Brooklyn news sites, and big health blogs. Google sees those links = Google trusts Toothology more.", caveman_style),
]))
story.append(Spacer(1, 10))

story.append(option_block(
    "1", "Patch.com — Brooklyn/Williamsburg Local News",
    "DA 70-75", "$300 – $600",
    "Patch is a neighborhood news site. Google uses it to learn what is happening in each neighborhood. "
    "A link here tells Google: this dentist is a real local business in Williamsburg.",
    '"5 Things Williamsburg Residents Should Know About Dental Health" — local angle, practical tips.'
))
story.append(Spacer(1, 8))

story.append(option_block(
    "2", "NewYorkFamily.com — NYC Parenting & Family Site",
    "DA 45-55", "$350 – $750",
    "NYC families search here for child health info. A dentist article here reaches parents actively looking "
    "for healthcare in Brooklyn.",
    '"When Should Brooklyn Kids Get Their First Dental Visit?" — expert answer, links back to practice.'
))
story.append(Spacer(1, 8))

story.append(option_block(
    "3", "Healthline.com or Medical News Today",
    "DA 91-93", "$800 – $2,500",
    "These are the BIGGEST health websites on the internet. AI assistants like ChatGPT and Google AI "
    "cite them constantly. One link from here = massive trust signal.",
    '"How NYC Tap Water Affects Your Teeth" — local angle on a national health platform.'
))
story.append(Spacer(1, 8))

story.append(option_block(
    "4", "BrooklynEagle.com — Local Brooklyn Newspaper",
    "DA ~45", "$200 – $400",
    "Local newspaper = Google trusts this as a real neighborhood authority. "
    "Cheap, fast, and highly geo-targeted.",
    '"Why Dental Health in Williamsburg Deserves More Attention" — community health op-ed.'
))
story.append(Spacer(1, 10))

story.append(pricing_table([
    ["Patch.com (Brooklyn)", "DA 70-75", "$300-$600", "HIGH"],
    ["NewYorkFamily.com", "DA 45-55", "$350-$750", "HIGH"],
    ["Healthline / MNT", "DA 91-93", "$800-$2,500", "MEDIUM"],
    ["Brooklyn Eagle", "DA ~45", "$200-$400", "HIGH"],
], "TOOTHOLOGY — PLACEMENT"))

story.append(PageBreak())

# ── CLIENT 2: ATLASCAREABA ──────────────────────────────────────────────────
story.append(section_banner("CLIENT 2:  ATLASCAREABA.COM  —  IOWA", colors.HexColor("#6C3483")))
story.append(Spacer(1, 8))

story.append(info_box([
    Paragraph("WHAT THEY DO:", h3_style),
    Paragraph("ABA therapy for children with autism in Iowa. Helps families get behavioral support and therapy services.", body_style),
    Spacer(1, 4),
    Paragraph("THE PROBLEM:", h3_style),
    Paragraph(
        "Only 40 people visit the site per month. This is a medical/healthcare niche — "
        "Google is EXTRA strict here. It needs to see that this site is trusted by experts before ranking it.",
        body_style
    ),
    Spacer(1, 4),
    Paragraph("THE FIX:", h3_style),
    Paragraph(
        "Get links from autism organizations, therapy blogs, and Iowa parenting sites. "
        "This tells Google: real healthcare experts vouch for this business.",
        caveman_style
    ),
]))
story.append(Spacer(1, 10))

story.append(option_block(
    "1", "Autism Speaks — National Autism Organization",
    "DA ~72", "$0 (earned) or $500-$1,200 via PR agency",
    "Autism Speaks is THE most trusted autism website. AI assistants cite it constantly. "
    "A link from here = instant credibility for a therapy provider. Worth the effort to earn.",
    '"Choosing ABA Therapy in Rural Iowa: What Midwest Families Need to Know" — practical, local, helpful.'
))
story.append(Spacer(1, 8))

story.append(option_block(
    "2", "VeryWell Family / VeryWell Mind",
    "DA 85-88", "$600 – $1,800",
    "These are huge health and parenting sites. When parents Google 'ABA therapy Iowa' or ask AI assistants "
    "about autism therapy — VeryWell articles show up. A link from there = you show up too.",
    '"What Iowa Parents Should Know Before Starting ABA Therapy" — straightforward expert guide.'
))
story.append(Spacer(1, 8))

story.append(option_block(
    "3", "IowaParent.com / Des Moines Parent",
    "DA 30-40", "$150 – $350",
    "Small site but it is specifically for Iowa parents. Google LOVES local relevance. "
    "A backlink from an Iowa parenting site + Iowa therapy provider = strong local match.",
    '"Iowa ABA Therapy Resources: A Guide for Families" — local resource list, easy to write, easy to place.'
))
story.append(Spacer(1, 8))

story.append(option_block(
    "4", "GoodTherapy.org",
    "DA 55-65", "$300 – $700",
    "A respected mental health and therapy directory with editorial content. "
    "Google trusts it as a legitimate healthcare reference. Great for building therapy niche authority.",
    '"ABA Therapy in the Midwest: Closing the Gap for Iowa Families" — addresses real access challenges.'
))
story.append(Spacer(1, 10))

story.append(pricing_table([
    ["Autism Speaks", "DA ~72", "$0-$1,200", "CRITICAL"],
    ["VeryWell Family/Mind", "DA 85-88", "$600-$1,800", "HIGH"],
    ["IowaParent.com", "DA 30-40", "$150-$350", "HIGH"],
    ["GoodTherapy.org", "DA 55-65", "$300-$700", "MEDIUM"],
], "ATLASCAREABA — PLACEMENT"))

story.append(PageBreak())

# ── CLIENT 3: WAYNES ROOFING ────────────────────────────────────────────────
story.append(section_banner("CLIENT 3:  WAYNESROOFINGCO.COM  —  NORTH JERSEY", colors.HexColor("#1A6B3C")))
story.append(Spacer(1, 8))

story.append(info_box([
    Paragraph("WHAT THEY DO:", h3_style),
    Paragraph("Roofing contractor serving North Jersey homeowners. Repairs, replacements, storm damage.", body_style),
    Spacer(1, 4),
    Paragraph("THE PROBLEM:", h3_style),
    Paragraph(
        "Most established of the three (684 monthly visits, 369 keywords) but still needs more authority "
        "to beat bigger competitors in the NJ market. North Jersey has lots of roofing companies fighting for the same searches.",
        body_style
    ),
    Spacer(1, 4),
    Paragraph("THE FIX:", h3_style),
    Paragraph(
        "Get links from New Jersey news, big home improvement sites, and contractor platforms. "
        "This site is ready to GROW FAST with the right backlinks.",
        caveman_style
    ),
]))
story.append(Spacer(1, 10))

story.append(option_block(
    "1", "NJ.com / The Star-Ledger",
    "DA 82-85", "$500 – $1,500 (or FREE with strong pitch)",
    "NJ.com is the biggest news site in New Jersey. Google and AI Overviews cite it constantly for "
    "NJ-related searches. One link from NJ.com can push rankings for every 'roofing NJ' keyword.",
    '"What North Jersey Homeowners Must Do After a Storm: A Roofer\'s Guide" — timely, local, useful.'
))
story.append(Spacer(1, 8))

story.append(option_block(
    "2", "Bob Vila / This Old House",
    "DA 78-85", "$600 – $1,800",
    "Bob Vila and This Old House are the most trusted home improvement brands online. "
    "AI assistants like ChatGPT cite them when answering roofing questions. A link here = Wayne shows up in AI answers.",
    '"How to Choose a Roofing Contractor in New Jersey: What to Check Before You Sign" — expert checklist.'
))
story.append(Spacer(1, 8))

story.append(option_block(
    "3", "Angi Editorial Blog (formerly Angie\'s List)",
    "DA 80-85", "$400 – $1,000",
    "Angi is WHERE homeowners go to find contractors. Their blog ranks for nearly every "
    "'how to find a roofer' search. Getting cited there = direct lead pipeline + SEO authority.",
    '"Flat Roof vs. Pitched Roof in New Jersey: What Contractors Actually Recommend" — practical, shareable.'
))
story.append(Spacer(1, 8))

story.append(option_block(
    "4", "TAPinto.net — Hyperlocal NJ News Network",
    "DA 30-45", "$100 – $300",
    "TAPinto runs 100+ local NJ news sites (Bergen, Morris, Passaic, Essex counties). "
    "Super affordable. Super local. Tells Google exactly WHERE Wayne operates.",
    '"How North Jersey Homeowners Can Spot Roof Damage Before It Gets Expensive" — seasonal, practical.'
))
story.append(Spacer(1, 10))

story.append(pricing_table([
    ["NJ.com / Star-Ledger", "DA 82-85", "$500-$1,500", "CRITICAL"],
    ["Bob Vila / This Old House", "DA 78-85", "$600-$1,800", "HIGH"],
    ["Angi Editorial Blog", "DA 80-85", "$400-$1,000", "HIGH"],
    ["TAPinto NJ (local)", "DA 30-45", "$100-$300", "HIGH"],
], "WAYNES ROOFING — PLACEMENT"))

story.append(PageBreak())

# ── FINAL CHEAT SHEET ────────────────────────────────────────────────────────
story.append(section_banner("THE CHEAT SHEET  —  START HERE", DARK))
story.append(Spacer(1, 10))

story.append(info_box([
    Paragraph("3 MOVES TO DO THIS WEEK:", h3_style),
    Spacer(1, 4),
    Paragraph(
        "1.  TOOTHOLOGY.CARE  —  Submit a free community article to Patch.com Brooklyn. "
        "No cost. Takes 1 hour. Big local signal.",
        caveman_style
    ),
    Spacer(1, 4),
    Paragraph(
        "2.  ATLASCAREABA.COM  —  Buy a guest post on IowaParent.com ($150-$350). "
        "Write a simple Iowa ABA therapy guide. Fast, affordable, geo-targeted.",
        caveman_style
    ),
    Spacer(1, 4),
    Paragraph(
        "3.  WAYNESROOFINGCO.COM  —  Pitch NJ.com with a storm damage article. "
        "Free if accepted. $500-$1,500 as sponsored. Biggest ROI move on this list.",
        caveman_style
    ),
]))
story.append(Spacer(1, 10))

story.append(info_box([
    Paragraph("WHERE TO BUY GUEST POSTS (IF YOU DON'T WANT TO DO OUTREACH YOURSELF):", h3_style),
    Spacer(1, 4),
], bg=MID_BG))

marketplace_data = [
    ["PLATFORM", "BEST FOR", "PRICE RANGE"],
    ["Authority.Builders", "High-DA niche placements", "$150 – $2,000+"],
    ["Loganix", "Editorial quality control", "$200 – $1,500"],
    ["FatJoe", "Volume at mid-tier DA", "$80 – $600"],
    ["OutreachMama", "Health / medical niches", "$300 – $1,200"],
    ["GetMeLinks", "Niche-targeted outreach", "$150 – $800"],
]
mt = Table(marketplace_data, colWidths=[2.1 * inch, 2.9 * inch, 2.0 * inch])
mt.setStyle(TableStyle([
    ("BACKGROUND", (0, 0), (-1, 0), DARK),
    ("TEXTCOLOR", (0, 0), (-1, 0), WHITE),
    ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
    ("FONTNAME", (0, 1), (-1, -1), "Helvetica"),
    ("FONTSIZE", (0, 0), (-1, -1), 9),
    ("ROWBACKGROUNDS", (0, 1), (-1, -1), [WHITE, LIGHT_BG]),
    ("GRID", (0, 0), (-1, -1), 0.5, MID_BG),
    ("TOPPADDING", (0, 0), (-1, -1), 7),
    ("BOTTOMPADDING", (0, 0), (-1, -1), 7),
    ("LEFTPADDING", (0, 0), (-1, -1), 8),
]))
story.append(mt)
story.append(Spacer(1, 10))

story.append(info_box([
    Paragraph("REMEMBER THE SIMPLE RULE:", h3_style),
    Paragraph(
        "Big relevant website  +  links to you  +  mentions your city  =  Google trusts you more  =  "
        "you show up higher  =  more customers find you.",
        caveman_style
    ),
    Spacer(1, 4),
    Paragraph(
        "DA = Domain Authority. Higher number = bigger/more trusted website. Aim for DA 40+ minimum. "
        "DA 70+ is excellent. DA 80+ is elite.",
        note_style
    ),
], bg=LIGHT_BG))

story.append(Spacer(1, 8))
story.append(Paragraph(
    "Data sourced from Semrush — May 27, 2026  |  Strategy prepared for Toothology.care, AtlasCareABA.com, WaynesRoofingCo.com",
    note_style
))

# ── Build ────────────────────────────────────────────────────────────────────
doc.build(story)
print(f"PDF written to {OUTPUT}")
