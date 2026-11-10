from pathlib import Path
from html import escape

COMMON = """
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<meta name="theme-color" content="#17191c">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700&family=Manrope:wght@400;500;600;700;800&display=swap" rel="stylesheet">
<link rel="stylesheet" href="css/style.css">
<link rel="stylesheet" href="css/pages.css">
<script src="js/site-shell.js" defer></script>
"""

def page(title, description, eyebrow, heading, intro, image, content, closing, filename):
    return f"""<!DOCTYPE html>
<html lang="en" data-theme="dark">
<head>
{COMMON}
<meta name="description" content="{escape(description, quote=True)}">
<title>{escape(title)}</title>
</head>
<body id="top">
<div id="siteHeader"></div>
<main class="page-main">
<section class="page-hero" style="--page-image: url('https://images.unsplash.com/{image}?auto=format&fit=crop&w=1800&q=85')">
<p class="eyebrow">{eyebrow}</p>
<h1>{heading}</h1>
<p class="hero-description">{escape(intro)}</p>
<nav class="breadcrumbs" aria-label="Breadcrumb">
<a href="index.html">Home</a><span> / </span>
<span aria-current="page">{escape(filename.replace('.html','').replace('-', ' ').title())}</span>
</nav>
</section>
{content}
<section class="page-cta">
<p class="section-kicker">VELTRIX LIVINGSTON</p>
<h2>{escape(closing)}</h2>
<p>Redefining Modern Living.</p>
<a class="page-button" href="contact.html">LET'S TALK ↗</a>
</section>
</main>
<div id="siteFooter"></div>
</body>
</html>
"""

# 13 — Editorial article
article_sections = [
    ("A quieter visual language", "Restraint in interior design is not about removing personality. It is about choosing elements carefully and allowing each one to contribute to the atmosphere of a room. A balanced space gives the eye room to rest while preserving warmth and character."),
    ("The importance of natural materials", "Timber, stone, linen and other tactile surfaces introduce depth without relying on excessive decoration. Their natural variations bring interest to a restrained palette and help a room feel welcoming rather than empty."),
    ("Light, proportion and space", "Natural light can reveal the qualities of a material and change the mood of a room throughout the day. Thoughtful furniture placement, clear circulation and balanced proportions help create an environment that feels comfortable and intuitive."),
    ("Choosing with intention", "Before introducing a new element, consider its purpose, scale, quality and relationship with the rest of the room. A few carefully selected pieces can create a stronger result than a collection of unrelated details."),
    ("A lasting approach to modern living", "The most successful interiors respond to the people who use them. Start with everyday needs, build a coherent material palette and allow personal character to emerge through meaningful details.")
]

article_content = """
<article class="article-content">
<p class="article-intro">Why considered simplicity can create interiors with more character, comfort and lasting appeal.</p>
"""
for heading, paragraph in article_sections:
    article_content += f"<section><h2>{escape(heading)}</h2><p>{escape(paragraph)}</p></section>\n"
article_content += """
<p class="article-note">VELTRIX LIVINGSTON · REDEFINING MODERN LIVING</p>
</article>
"""

Path("article.html").write_text(page(
    "The Beauty of Restraint | VELTRIX LIVINGSTON Journal",
    "Discover how thoughtful minimalism, natural materials and considered details create timeless interiors.",
    "JOURNAL / DESIGN PHILOSOPHY",
    "The beauty of<br><em>restraint.</em>",
    "Why considered simplicity can create interiors with more character, comfort and lasting appeal.",
    "photo-1600210492486-724fe5c67fb0",
    article_content,
    "Make room for what matters.",
    "article.html"
), encoding="utf-8")

# 14 — Frequently asked questions
faqs = [
    ("What services does VELTRIX LIVINGSTON explore?", "Our design focus includes residential interiors, commercial spaces, space styling and interior architecture. The right scope depends on your space and objectives."),
    ("How do I start a project?", "Contact us with a short description of your space, what you would like to achieve and any inspiration you have. We can then discuss suitable next steps."),
    ("Do you work on residential and commercial spaces?", "Yes. Our design direction includes homes, workspaces, retail environments and hospitality spaces."),
    ("Can I request help with one room?", "You can enquire about a single room or a wider interior project. The proposed scope can be discussed before any commitment."),
    ("What should I prepare before a consultation?", "Photographs, approximate room dimensions, your priorities, preferred style references and an indicative budget can help make the conversation more useful."),
    ("Are the images in the gallery completed projects?", "The current gallery contains illustrative design inspiration and conceptual references. They should not be interpreted as a portfolio of completed VELTRIX LIVINGSTON commissions."),
    ("How can I contact the studio?", "You can call 0716397341 or start a conversation on WhatsApp using the contact links on this website.")
]

faq_content = """
<section class="page-section faq-section">
<div class="section-heading">
<p class="section-kicker">HELPFUL INFORMATION</p>
<h2 class="editorial-heading">Frequently asked questions.</h2>
</div>
<div class="faq-list">
"""
for question, answer in faqs:
    faq_content += f"""<details class="faq-item">
<summary>{escape(question)}</summary>
<p>{escape(answer)}</p>
</details>
"""
faq_content += "</div></section>"

Path("faq.html").write_text(page(
    "Frequently Asked Questions | VELTRIX LIVINGSTON",
    "Answers to common questions about interior design consultations, project planning and services.",
    "A FEW USEFUL ANSWERS",
    "Good questions.<br><em>Clear direction.</em>",
    "A helpful starting point for understanding our design approach, services and the first steps towards your space.",
    "photo-1600607687939-ce8a6c25118c",
    faq_content,
    "Still have a question? Let's talk.",
    "faq.html"
), encoding="utf-8")

# 15 — Contact and consultation
contact_content = """
<section class="page-section contact-details">
<div class="section-heading">
<p class="section-kicker">GET IN TOUCH</p>
<h2 class="editorial-heading">Let's discuss your vision.</h2>
<p class="editorial-copy">Reach out directly using either contact option below.</p>
</div>
<div class="contact-method-grid">
<article class="contact-method">
<span class="card-number">01 / CALL</span>
<h2>Speak with us.</h2>
<p>Call VELTRIX LIVINGSTON to introduce your project and discuss your enquiry.</p>
<a class="page-button" href="tel:0716397341">CALL 0716397341 ↗</a>
</article>
<article class="contact-method">
<span class="card-number">02 / WHATSAPP</span>
<h2>Start a conversation.</h2>
<p>Send a WhatsApp message with a few details about your space and ideas.</p>
<a class="page-button" href="https://wa.me/254716397341?text=Hello%20VELTRIX%20LIVINGSTON%2C%20I%20would%20like%20to%20discuss%20an%20interior%20design%20project." target="_blank" rel="noopener noreferrer">MESSAGE ON WHATSAPP ↗</a>
</article>
</div>
<p class="contact-reminder">Helpful starting points: your location, type of space, project goals and any design inspiration.</p>
</section>
"""

Path("contact.html").write_text(page(
    "Contact & Consultation | VELTRIX LIVINGSTON",
    "Contact VELTRIX LIVINGSTON to discuss interior design ideas, residential spaces and commercial environments.",
    "LET'S BEGIN A CONVERSATION",
    "Tell us about<br><em>your space.</em>",
    "Every considered space begins with a conversation. Share your ideas, your priorities and what you would like your environment to become.",
    "photo-1600607687920-4e2a09cf159d",
    contact_content,
    "We look forward to hearing your ideas.",
    "contact.html"
), encoding="utf-8")

# Add styles only once.
css_path = Path("css/pages.css")
css = css_path.read_text(encoding="utf-8")
marker = "/* FINAL THREE PAGES */"

if marker not in css:
    css += """

/* FINAL THREE PAGES */
.article-content {
  width: min(820px, calc(100% - 40px));
  margin: 0 auto;
  padding: 80px 0 90px;
}
.article-content .article-intro {
  font-size: 1.3rem;
  line-height: 1.8;
  margin-bottom: 48px;
}
.article-content section { margin: 0 0 42px; }
.article-content section h2 {
  font-family: "Manrope", sans-serif;
  font-size: clamp(1.35rem, 3vw, 1.8rem);
  margin-bottom: 14px;
}
.article-content section p,
.article-note,
.contact-reminder {
  color: var(--muted, #a7abb1);
  line-height: 1.9;
}
.article-note {
  padding-top: 25px;
  border-top: 1px solid var(--line, #444);
  font-size: .75rem;
  letter-spacing: .15em;
}
.faq-section { max-width: 950px; margin: auto; }
.faq-list { display: grid; gap: 13px; margin-top: 35px; }
.faq-item {
  border: 1px solid var(--line, #444);
  border-radius: 12px;
  background: var(--surface, #202328);
  padding: 21px 24px;
}
.faq-item summary {
  cursor: pointer;
  font-family: "Manrope", sans-serif;
  font-weight: 700;
  line-height: 1.6;
  list-style: none;
}
.faq-item summary::-webkit-details-marker { display: none; }
.faq-item summary::after {
  content: "+";
  float: right;
  color: var(--accent, #aeb5bf);
  font-size: 1.3rem;
  margin-left: 12px;
}
.faq-item[open] summary::after { content: "−"; }
.faq-item p {
  color: var(--muted, #a7abb1);
  line-height: 1.8;
  margin: 16px 0 0;
}
.contact-details { max-width: 1100px; margin: auto; }
.contact-method-grid {
  display: grid;
  grid-template-columns: repeat(2, minmax(0, 1fr));
  gap: 22px;
  margin-top: 35px;
}
.contact-method {
  padding: 34px;
  border: 1px solid var(--line, #444);
  border-radius: 16px;
  background: var(--surface, #202328);
}
.contact-method h2 {
  font-family: "Manrope", sans-serif;
  margin: 20px 0 12px;
}
.contact-method p {
  color: var(--muted, #a7abb1);
  line-height: 1.8;
  margin-bottom: 24px;
}
.contact-method .page-button { display: inline-flex; }
.contact-reminder { margin-top: 28px; }
@media (max-width: 650px) {
  .article-content { padding: 55px 0 65px; }
  .contact-method-grid { grid-template-columns: 1fr; }
  .contact-method { padding: 25px; }
  .faq-item { padding: 18px; }
}
"""
    css_path.write_text(css, encoding="utf-8")

print("Created article.html")
print("Created faq.html")
print("Created contact.html")
print("Updated final-page styles.")
