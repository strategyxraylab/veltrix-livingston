from pathlib import Path
from html import escape

PAGES = {
    "about.html": {
        "title": "About VELTRIX LIVINGSTON | Our Design Philosophy",
        "description": "Discover the VELTRIX LIVINGSTON philosophy, our approach to modern interiors and our commitment to intentional design.",
        "eyebrow": "THE THINKING BEHIND THE SPACE",
        "heading": "Designing spaces.<br><em>Defining lifestyles.</em>",
        "intro": "We believe exceptional spaces do more than look beautiful. They influence how we feel, connect, work and experience everyday life.",
        "image": "photo-1600210492486-724fe5c67fb0",
        "section_label": "OUR PHILOSOPHY",
        "section_heading": "Beauty with a purpose.",
        "section_copy": "VELTRIX LIVINGSTON brings together visual harmony, thoughtful planning and modern sensibility. Every design decision should have a reason, every material should contribute to the experience, and every space should feel naturally connected to the people who use it.",
        "cards": [
            ("01", "Intentional design", "We begin with purpose, understanding the people, needs and character behind every space."),
            ("02", "Timeless character", "We favour considered proportions, enduring materials and details that outlive passing trends."),
            ("03", "Modern living", "We explore how light, texture, comfort and functionality can work together beautifully.")
        ],
        "closing": "A considered approach to the spaces we call home."
    },
    "services.html": {
        "title": "Interior Design Services | VELTRIX LIVINGSTON",
        "description": "Explore residential interiors, commercial design, space styling and interior architecture by VELTRIX LIVINGSTON.",
        "eyebrow": "WHAT WE BRING TO LIFE",
        "heading": "Considered services.<br><em>Exceptional spaces.</em>",
        "intro": "From a single room to a complete environment, explore design services that bring clarity, character and purpose to modern spaces.",
        "image": "photo-1600607687939-ce8a6c25118c",
        "section_label": "OUR EXPERTISE",
        "section_heading": "One vision. Many possibilities.",
        "section_copy": "Our service approach connects aesthetics with everyday function. Choose a focused design direction or explore how different disciplines can work together to shape a cohesive environment.",
        "cards": [
            ("01", "Residential design", "Personal interiors shaped around comfort, character and the rhythm of everyday life.", "residential.html"),
            ("02", "Commercial design", "Distinctive environments for businesses, hospitality and professional spaces.", "commercial.html"),
            ("03", "Space styling", "Finishing touches, furniture, colour and accessories that bring a room together.", "styling.html"),
            ("04", "Interior architecture", "Spatial planning, architectural details and considered interior structure.", "architecture.html")
        ],
        "closing": "The right design begins with the right conversation."
    },
    "residential.html": {
        "title": "Residential Interior Design | VELTRIX LIVINGSTON",
        "description": "Explore thoughtful residential interior design for contemporary homes, apartments and private living spaces.",
        "eyebrow": "RESIDENTIAL DESIGN",
        "heading": "A home that feels<br><em>distinctly yours.</em>",
        "intro": "A home should reflect the people who live in it. We explore the balance of comfort, visual identity and practical details that make everyday living feel considered.",
        "image": "photo-1600607687920-4e2a09cf159d",
        "section_label": "THE ART OF HOME",
        "section_heading": "Personal spaces. Lasting impressions.",
        "section_copy": "From welcoming living areas to peaceful bedrooms and refined dining spaces, residential design is about creating a natural connection between atmosphere and function.",
        "cards": [
            ("01", "Living spaces", "Balanced layouts, inviting textures and comfortable places to gather."),
            ("02", "Private retreats", "Calm bedroom environments with thoughtful lighting and tactile finishes."),
            ("03", "Everyday details", "Storage, furniture and finishing choices designed around daily routines.")
        ],
        "closing": "Your space. Your rhythm. Your definition of home."
    },
    "commercial.html": {
        "title": "Commercial Interior Design | VELTRIX LIVINGSTON",
        "description": "Discover modern commercial interior design for offices, retail environments and hospitality spaces.",
        "eyebrow": "COMMERCIAL DESIGN",
        "heading": "Spaces that work.<br><em>Experiences that last.</em>",
        "intro": "The environments where people work, shop and connect shape how they experience a brand. Thoughtful commercial interiors bring identity and function into alignment.",
        "image": "photo-1497366754035-f200968a6e72",
        "section_label": "DESIGN FOR BUSINESS",
        "section_heading": "Where identity meets function.",
        "section_copy": "We approach commercial environments with attention to circulation, atmosphere, material choices and the needs of the people who use them. The aim is a coherent space that supports its purpose and communicates its character.",
        "cards": [
            ("01", "Work environments", "Professional spaces designed to support focus, collaboration and comfort."),
            ("02", "Retail environments", "Memorable customer-facing spaces with a clear visual identity."),
            ("03", "Hospitality spaces", "Welcoming settings that consider atmosphere, movement and guest experience.")
        ],
        "closing": "Give your business a space that speaks its language."
    }
    ,
    "styling.html": {
        "title": "Space Styling | VELTRIX LIVINGSTON",
        "description": "Explore considered furniture, colour, lighting and accessories for beautifully balanced interiors.",
        "eyebrow": "THE FINISHING ART",
        "heading": "The details make<br><em>the difference.</em>",
        "intro": "Space styling brings a room's character into focus through furniture, colour, lighting, textures and carefully selected details.",
        "image": "photo-1616486338812-3dadae4b4ace",
        "section_label": "THE ART OF STYLING",
        "section_heading": "A room, thoughtfully composed.",
        "section_copy": "Styling is where the atmosphere of a space comes together. It connects individual elements into a visual story, creating a sense of balance without losing personality.",
        "cards": [
            ("01", "Furniture & layout", "Considered furniture choices and arrangements that create balance and comfortable movement."),
            ("02", "Colour & texture", "Layered tones and tactile materials that give interiors warmth and depth."),
            ("03", "Finishing touches", "Lighting, artwork and accessories that complete the atmosphere.")
        ],
        "closing": "Thoughtful details. A more complete space."
    },
    "architecture.html": {
        "title": "Interior Architecture | VELTRIX LIVINGSTON",
        "description": "Discover interior architecture concepts focused on spatial planning, proportions, light and material relationships.",
        "eyebrow": "INTERIOR ARCHITECTURE",
        "heading": "Form follows<br><em>the way we live.</em>",
        "intro": "The structure of an interior shapes every experience within it. We explore the relationship between space, proportion, light and the details that define an environment.",
        "image": "photo-1600607687920-4e2a09cf159d",
        "section_label": "SPACE & STRUCTURE",
        "section_heading": "The architecture of experience.",
        "section_copy": "Interior architecture considers how spaces connect and function. From circulation and spatial organisation to surfaces and built-in elements, each decision contributes to a coherent whole.",
        "cards": [
            ("01", "Spatial planning", "Explore layouts that make movement intuitive and use available space thoughtfully."),
            ("02", "Architectural details", "Consider doors, partitions, built-in elements and transitions between spaces."),
            ("03", "Light & proportion", "Understand how natural light, scale and volume influence an interior.")
        ],
        "closing": "A stronger foundation for modern living."
    },
    "projects.html": {
        "title": "Design Inspiration Gallery | VELTRIX LIVINGSTON",
        "description": "Explore an editorial gallery of interior design inspiration, contemporary spaces and material ideas.",
        "eyebrow": "A VISUAL COLLECTION",
        "heading": "Ideas shaped into<br><em>inspiration.</em>",
        "intro": "Explore a curated visual direction for modern living, from calm residential interiors to expressive commercial environments.",
        "image": "photo-1600210492486-724fe5c67fb0",
        "section_label": "THE COLLECTION",
        "section_heading": "A study in contemporary spaces.",
        "section_copy": "This gallery presents visual inspiration and conceptual directions. Images are illustrative references, not a claim that these are completed VELTRIX LIVINGSTON commissions.",
        "cards": [
            ("01", "Quiet residential", "Natural textures, soft light and understated contemporary living."),
            ("02", "Modern workspace", "A considered balance of professional character and everyday comfort."),
            ("03", "Warm minimalism", "Simple forms, tactile finishes and a restrained material palette."),
            ("04", "Hospitality mood", "Welcoming environments shaped around atmosphere and experience.")
        ],
        "closing": "Every great space begins with an idea."
    },
    "project-details.html": {
        "title": "Concept Study | VELTRIX LIVINGSTON",
        "description": "Explore an illustrative residential interior concept study and the thinking behind its design direction.",
        "eyebrow": "FEATURED CONCEPT STUDY",
        "heading": "A quieter kind<br><em>of luxury.</em>",
        "intro": "An illustrative contemporary living concept exploring natural textures, warm neutrals, clean geometry and a calm sense of balance.",
        "image": "photo-1600607687939-ce8a6c25118c",
        "section_label": "THE DESIGN STORY",
        "section_heading": "Comfort through considered choices.",
        "section_copy": "This concept study explores how a restrained palette and carefully layered materials can create an inviting living environment. The direction combines soft natural light, tactile surfaces and functional furniture arrangements.",
        "cards": [
            ("01", "Design direction", "Contemporary minimalism with warm, natural character."),
            ("02", "Material palette", "A conceptual mix of timber tones, stone textures and soft fabrics."),
            ("03", "Spatial experience", "An open, welcoming arrangement designed around comfort and connection.")
        ],
        "closing": "Good design is felt as much as it is seen."
    }

    ,
    "process.html": {
        "title": "Our Design Process | VELTRIX LIVINGSTON",
        "description": "Discover the VELTRIX LIVINGSTON design process, from the first conversation to the final interior details.",
        "eyebrow": "HOW WE APPROACH DESIGN",
        "heading": "Thoughtful from<br><em>start to finish.</em>",
        "intro": "A considered process helps turn an initial idea into a coherent design direction. Every stage has a purpose, from understanding your needs to refining the details.",
        "image": "photo-1600210492486-724fe5c67fb0",
        "section_label": "THE JOURNEY",
        "section_heading": "Clarity at every stage.",
        "section_copy": "Every project begins with listening. We explore the brief, priorities, practical requirements and desired atmosphere before developing a visual direction. The process described here is our proposed approach and can be tailored to the scope of a project.",
        "cards": [
            ("01", "Discover", "Discuss your space, objectives, preferences, practical needs and inspiration."),
            ("02", "Develop", "Explore concepts, layouts, visual references and material directions."),
            ("03", "Refine", "Review the proposed direction and make considered adjustments."),
            ("04", "Deliver", "Agree on the final scope, specifications and next steps for implementation.")
        ],
        "closing": "A clear vision begins with a good conversation."
    },
    "materials.html": {
        "title": "Materials & Finishes | VELTRIX LIVINGSTON",
        "description": "Explore interior material inspiration, natural textures, finishes and colour palettes for contemporary spaces.",
        "eyebrow": "MATERIALS & FINISHES",
        "heading": "Character in every<br><em>surface.</em>",
        "intro": "Materials influence how a space looks, feels and ages. Explore a considered palette of textures, finishes and tones for modern interiors.",
        "image": "photo-1618221195710-dd6b41faaea6",
        "section_label": "THE MATERIAL STORY",
        "section_heading": "Texture creates atmosphere.",
        "section_copy": "A successful material palette considers more than appearance. Durability, maintenance, lighting, tactile quality and the relationship between surfaces all contribute to a balanced interior.",
        "cards": [
            ("01", "Natural timber", "Warm wood tones introduce texture, visual depth and a sense of natural character."),
            ("02", "Stone & surfaces", "Stone-inspired finishes bring visual structure and a distinctive material presence."),
            ("03", "Glass & metal", "Reflective and refined surfaces can add contrast, light and contemporary detail."),
            ("04", "Textiles & colour", "Fabrics and colour bring softness, warmth and personality to an environment.")
        ],
        "closing": "The right materials make a space feel complete."
    },
    "journal.html": {
        "title": "The Journal | VELTRIX LIVINGSTON",
        "description": "Ideas and inspiration on interior design, architecture, materials and modern living from VELTRIX LIVINGSTON.",
        "eyebrow": "NOTES ON MODERN LIVING",
        "heading": "Ideas worth<br><em>living with.</em>",
        "intro": "A collection of thoughts and inspiration exploring the spaces we inhabit, the materials we choose and the details that shape everyday experiences.",
        "image": "photo-1600607687939-ce8a6c25118c",
        "section_label": "EDITORIAL",
        "section_heading": "A closer look at considered spaces.",
        "section_copy": "The VELTRIX journal explores design principles, practical ideas and visual inspiration for contemporary interiors. Our articles are intended to encourage thoughtful decisions about the places we live and work.",
        "cards": [
            ("01", "The beauty of restraint", "How a thoughtful approach to minimalism can create calm, characterful interiors.", "article.html"),
            ("02", "Understanding natural light", "Explore the relationship between daylight, surfaces and the atmosphere of a room.", "article.html"),
            ("03", "Choosing a material palette", "A practical introduction to balancing texture, colour and finish.", "materials.html")
        ],
        "closing": "Stay curious about the spaces around you."
    }

}


def image_url(photo_id, width=1800):
    return (
        f"https://images.unsplash.com/{photo_id}"
        f"?auto=format&fit=crop&w={width}&q=85"
    )


def card_html(card):
    number, heading, copy, *link = card
    destination = link[0] if link else "contact.html"
    label = "Explore service" if link else "Start a conversation"
    return f"""
      <article class="page-card">
        <span class="card-number">{escape(number)}</span>
        <h3>{escape(heading)}</h3>
        <p>{escape(copy)}</p>
        <a href="{escape(destination)}">{label} ↗</a>
      </article>
    """


def build_page(filename, page):
    cards = "\n".join(card_html(card) for card in page["cards"])
    hero_image = image_url(page["image"])

    html = f"""<!DOCTYPE html>
<html lang="en" data-theme="dark">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta name="theme-color" content="#17191c">
  <meta name="description" content="{escape(page['description'], quote=True)}">
  <title>{escape(page['title'])}</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700&family=Manrope:wght@400;500;600;700;800&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="css/style.css">
  <link rel="stylesheet" href="css/pages.css">
  <script src="js/site-shell.js" defer></script>
</head>
<body id="top">
  <div id="siteHeader"></div>

  <main class="page-main">
    <section class="page-hero" style="--page-image: url('{hero_image}')">
      <p class="eyebrow">{escape(page['eyebrow'])}</p>
      <h1>{page['heading']}</h1>
      <p class="hero-description">{escape(page['intro'])}</p>
      <nav class="breadcrumbs" aria-label="Breadcrumb">
        <a href="index.html">Home</a>
        <span> / </span>
        <span aria-current="page">{escape(filename.removesuffix('.html').replace('-', ' ').title())}</span>
      </nav>
    </section>

    <section class="page-section">
      <div class="page-columns">
        <div>
          <p class="section-kicker">{escape(page['section_label'])}</p>
          <h2 class="editorial-heading">{escape(page['section_heading'])}</h2>
        </div>
        <div>
          <p class="editorial-copy">{escape(page['section_copy'])}</p>
          <a class="page-button" href="contact.html">DISCUSS YOUR PROJECT ↗</a>
        </div>
      </div>
    </section>

    <section class="page-section">
      <div class="section-heading">
        <p class="section-kicker">THE DETAILS</p>
        <h2 class="editorial-heading">A more thoughtful approach.</h2>
      </div>
      <div class="page-card-grid">
        {cards}
      </div>
    </section>

    <section class="page-cta">
      <p class="section-kicker">VELTRIX LIVINGSTON</p>
      <h2>{escape(page['closing'])}</h2>
      <p>Redefining Modern Living.</p>
      <a class="page-button" href="contact.html">LET'S TALK ↗</a>
    </section>
  </main>

  <div id="siteFooter"></div>
</body>
</html>
"""

    Path(filename).write_text(html, encoding="utf-8")


for filename, page in PAGES.items():
    build_page(filename, page)
    print(f"Created: {filename}")

print(f"\\nSuccessfully generated {len(PAGES)} pages.")
