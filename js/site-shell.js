/* VELTRIX LIVINGSTON — Shared Website Shell */

const headerSlot = document.getElementById("siteHeader");
const footerSlot = document.getElementById("siteFooter");

/* Shared website header */
if (headerSlot) {
  headerSlot.innerHTML = `
    <header class="site-header">
      <a href="index.html" class="brand" aria-label="VELTRIX LIVINGSTON home">
        <span class="brand-name">VELTRIX</span>
        <span class="brand-sub">L I V I N G S T O N</span>
      </a>

      <button class="menu-toggle" id="menuToggle"
        aria-label="Open navigation" aria-expanded="false"
        aria-controls="navigation">
        <span></span><span></span>
      </button>

      <nav class="navigation" id="navigation" aria-label="Main navigation">
        <a href="index.html">Home</a>
        <a href="about.html">About</a>

        <details class="nav-dropdown">
          <summary>Services <span>⌄</span></summary>
          <div class="dropdown-panel">
            <a href="services.html">All Services</a>
            <a href="residential.html">Residential Design</a>
            <a href="commercial.html">Commercial Design</a>
            <a href="styling.html">Space Styling</a>
            <a href="architecture.html">Interior Architecture</a>
          </div>
        </details>

        <details class="nav-dropdown">
          <summary>Explore <span>⌄</span></summary>
          <div class="dropdown-panel">
            <a href="projects.html">Our Projects</a>
            <a href="project-details.html">Project Details</a>
            <a href="process.html">Our Process</a>
            <a href="materials.html">Materials & Finishes</a>
            <a href="journal.html">Journal</a>
            <a href="article.html">Featured Article</a>
            <a href="faq.html">FAQs</a>
          </div>
        </details>

        <a href="contact.html" class="nav-contact">
          Let's Talk <span>↗</span>
        </a>
      </nav>

      <button class="theme-toggle" id="themeToggle"
        aria-label="Switch colour theme">
        <span id="themeIcon">☼</span>
      </button>
    </header>
  `;
}

/* Shared website footer */
if (footerSlot) {
  footerSlot.innerHTML = `
    <footer class="site-footer">
      <div class="footer-top">
        <a href="index.html" class="brand footer-brand">
          <span class="brand-name">VELTRIX</span>
          <span class="brand-sub">L I V I N G S T O N</span>
        </a>
        <p>Redefining Modern Living.</p>
        <a href="#top" class="back-top">BACK TO TOP ↑</a>
      </div>

      <div class="footer-contact">
        <a href="tel:0716397341">Call 0716397341</a>
        <a href="https://wa.me/254716397341"
          target="_blank" rel="noopener noreferrer">
          WhatsApp ↗
        </a>
        <a href="contact.html">Request a consultation ↗</a>
      </div>

      <div class="footer-bottom">
        <span>© <span id="year"></span> VELTRIX LIVINGSTON</span>
        <span>INTERIOR DESIGN · MODERN LIVING</span>
        <span>CRAFTED WITH INTENTION.</span>
      </div>
    </footer>
  `;
}

/* Theme controls */
const root = document.documentElement;
const themeToggle = document.getElementById("themeToggle");
const themeIcon = document.getElementById("themeIcon");

function applyTheme(theme) {
  const selectedTheme = theme === "light" ? "light" : "dark";

  root.setAttribute("data-theme", selectedTheme);

  if (themeIcon) {
    themeIcon.textContent = selectedTheme === "dark" ? "☼" : "☾";
  }

  if (themeToggle) {
    themeToggle.setAttribute(
      "aria-label",
      selectedTheme === "dark"
        ? "Switch to light theme"
        : "Switch to dark theme"
    );
  }

  const themeColor = document.querySelector('meta[name="theme-color"]');

  if (themeColor) {
    themeColor.setAttribute(
      "content",
      selectedTheme === "dark" ? "#17191c" : "#f2f1ed"
    );
  }
}

let savedTheme = "dark";

try {
  savedTheme = localStorage.getItem("veltrix-theme") || "dark";
} catch (error) {
  savedTheme = "dark";
}

applyTheme(savedTheme);

if (themeToggle) {
  themeToggle.addEventListener("click", () => {
    const nextTheme =
      root.getAttribute("data-theme") === "dark" ? "light" : "dark";

    applyTheme(nextTheme);

    try {
      localStorage.setItem("veltrix-theme", nextTheme);
    } catch (error) {
      /* Theme still works for the current page. */
    }
  });
}

/* Mobile navigation */
const menuToggle = document.getElementById("menuToggle");
const navigation = document.getElementById("navigation");

function closeNavigation() {
  if (!menuToggle || !navigation) return;

  navigation.classList.remove("open");
  menuToggle.setAttribute("aria-expanded", "false");
  menuToggle.setAttribute("aria-label", "Open navigation");
}

if (menuToggle && navigation) {
  menuToggle.addEventListener("click", () => {
    const isOpen = navigation.classList.toggle("open");

    menuToggle.setAttribute("aria-expanded", String(isOpen));
    menuToggle.setAttribute(
      "aria-label",
      isOpen ? "Close navigation" : "Open navigation"
    );
  });

  navigation.querySelectorAll("a").forEach(link => {
    link.addEventListener("click", closeNavigation);
  });

  document.addEventListener("keydown", event => {
    if (event.key === "Escape") {
      closeNavigation();
    }
  });
}

/* Highlight the current page */
const pathParts = location.pathname.split("/").filter(Boolean);
const currentPage =
  !pathParts.length || location.pathname.endsWith("/")
    ? "index.html"
    : pathParts[pathParts.length - 1];

document.querySelectorAll("#navigation a").forEach(link => {
  const linkPage = link.getAttribute("href");

  if (linkPage === currentPage) {
    link.classList.add("active");
    link.setAttribute("aria-current", "page");

    const dropdown = link.closest("details");

    if (dropdown) {
      dropdown.open = true;
    }
  }
});

/* Current year */
const yearElement = document.getElementById("year");

if (yearElement) {
  yearElement.textContent = new Date().getFullYear();
}
