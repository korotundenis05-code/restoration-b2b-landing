const header = document.querySelector("[data-header]");
const navToggle = document.querySelector("[data-nav-toggle]");
const nav = document.querySelector("[data-nav]");
const lightbox = document.querySelector("[data-lightbox]");
const lightboxImage = document.querySelector("[data-lightbox-image]");
const lightboxClose = document.querySelector("[data-lightbox-close]");
const gallery = document.querySelector(".gallery");
const galleryToggle = document.querySelector("[data-gallery-toggle]");

function updateHeader() {
  header.classList.toggle("is-scrolled", window.scrollY > 12);
}

window.addEventListener("scroll", updateHeader, { passive: true });
updateHeader();

navToggle.addEventListener("click", () => {
  header.classList.toggle("is-open");
});

nav.addEventListener("click", (event) => {
  if (event.target.closest("a")) {
    header.classList.remove("is-open");
  }
});

function loadDeferredGalleryImages() {
  document.querySelectorAll(".gallery img[data-src]").forEach((image) => {
    image.src = image.dataset.src;
    image.removeAttribute("data-src");
  });
}

document.querySelectorAll("[data-gallery]").forEach((button) => {
  button.addEventListener("click", () => {
    lightboxImage.src = button.dataset.gallery;
    lightbox.hidden = false;
    document.body.style.overflow = "hidden";
  });
});

if (gallery && galleryToggle) {
  galleryToggle.addEventListener("click", () => {
    const expanded = gallery.classList.toggle("is-expanded");
    if (expanded) {
      loadDeferredGalleryImages();
    }

    galleryToggle.textContent = expanded ? "Скрыть" : "Показать больше";

    if (!expanded) {
      document.querySelector("#cases").scrollIntoView({ behavior: "smooth", block: "start" });
    }
  });
}

function closeLightbox() {
  lightbox.hidden = true;
  lightboxImage.src = "";
  document.body.style.overflow = "";
}

lightboxClose.addEventListener("click", closeLightbox);
lightbox.addEventListener("click", (event) => {
  if (event.target === lightbox) {
    closeLightbox();
  }
});

document.addEventListener("keydown", (event) => {
  if (event.key === "Escape" && !lightbox.hidden) {
    closeLightbox();
  }
});
