"use strict";

const root = document.documentElement;
const themeToggle = document.getElementById("themeToggle");
const themeIcon = document.getElementById("themeIcon");
const menuToggle = document.getElementById("menuToggle");
const navigation = document.getElementById("navigation");
const contactForm = document.getElementById("contactForm");
const formFeedback = document.getElementById("formFeedback");

// Theme management
function applyTheme(theme) {
  root.dataset.theme = theme;
  themeIcon.textContent = theme === "dark" ? "☼" : "☾";
  themeToggle.setAttribute(
    "aria-label",
    theme === "dark" ? "Switch to light theme" : "Switch to dark theme"
  );

  document.querySelector('meta[name="theme-color"]')
    .setAttribute("content", theme === "dark" ? "#17191c" : "#f2f1ed");
}

let savedTheme = "dark";

try {
  savedTheme = localStorage.getItem("veltrix-theme") || "dark";
} catch (error) {
  console.warn("Theme preference storage unavailable.");
}

applyTheme(savedTheme);

themeToggle.addEventListener("click", () => {
  const nextTheme = root.dataset.theme === "dark" ? "light" : "dark";
  applyTheme(nextTheme);

  try {
    localStorage.setItem("veltrix-theme", nextTheme);
  } catch (error) {
    console.warn("Theme preference could not be saved.");
  }
});

// Mobile navigation
menuToggle.addEventListener("click", () => {
  const isOpen = navigation.classList.toggle("open");

  menuToggle.setAttribute("aria-expanded", String(isOpen));
  menuToggle.setAttribute(
    "aria-label",
    isOpen ? "Close navigation" : "Open navigation"
  );
});

navigation.querySelectorAll("a").forEach(link => {
  link.addEventListener("click", () => {
    navigation.classList.remove("open");
    menuToggle.setAttribute("aria-expanded", "false");
    menuToggle.setAttribute("aria-label", "Open navigation");
  });
});

// Close mobile navigation with Escape
// Close mobile navigation with Escape
document.addEventListener("keydown", event => {
  if (event.key === "Escape" && navigation.classList.contains("open")) {
    navigation.classList.remove("open");
    menuToggle.setAttribute("aria-expanded", "false");
    menuToggle.setAttribute("aria-label", "Open navigation");
    menuToggle.focus();
  }
});

// Footer year
document.getElementById("year").textContent = new Date().getFullYear();

// Enquiry form validation
contactForm.addEventListener("submit", event => {
  event.preventDefault();

  if (!contactForm.checkValidity()) {
    contactForm.reportValidity();
    return;
  }

  const data = new FormData(contactForm);
  const name = data.get("name").trim();

  formFeedback.textContent =
    `Thank you, ${name}. Your enquiry details are valid. ` +
    "The website is currently in preview mode; online delivery will be connected after contact details and backend are configured.";

  formFeedback.setAttribute("aria-live", "polite");
});
