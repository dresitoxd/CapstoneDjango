'use strict';



// preaload

const preloader = document.querySelector("[data-preaload]");

window.addEventListener("load", function() {
    preloader.classList.add("loaded");
    document.body.classList.add("loaded");
})



// añadiendo nuevo evento en multiples elementos

const addEventOnElements = function(elements, eventType, callback) {
    for (let i = 0, len = elements.length; i < len; i++) {
        elements[i].addEventListener(eventType, callback);
    }
}

// navbar

const navbar = document.querySelector("[data-navbar]");
const navTogglers = document.querySelectorAll("[data-nav-toggler]");
const overlay = document.querySelector("[data-overlay]");

const toggleNavbar = function() {
    navbar.classList.toggle("active");
    overlay.classList.toggle("active");
    document.body.classList.toggle("nav-active");
}

addEventOnElements(navTogglers, "click", toggleNavbar);

// Activar el enlace correspondiente en la navbar
const navbarLinks = document.querySelectorAll('.navbar-link');

const activateLink = function() {
    const currentPath = window.location.pathname; // Obtener la ruta actual

    navbarLinks.forEach(link => {
        const linkPath = link.getAttribute('href'); // Obtener el atributo href de cada enlace

        if (linkPath === currentPath) {
            link.classList.add('active'); // Agregar clase activa si coincide
        } else {
            link.classList.remove('active'); // Quitar clase activa si no coincide
        }
    });
}

activateLink(); // Llamar a la función para activar el enlace correcto


// header

const header = document.querySelector("[data-header]");

let lastScrollPos = 0;

const hideHeader = function () {
    const isScrollBottom = lastScrollPos <= window.scrollY;
    if (isScrollBottom) {
        header.classList.add("hide")
    }else {
        header.classList.remove("hide");
    }

    lastScrollPos = window.scrollY;
}

window.addEventListener("scroll", function (){
    if (window.scrollY > 50){
        header.classList.add("active");
        hideHeader();
    }else {
        header.classList.remove("active");
    }
})


// carrusel

const heroSlider = document.querySelector("[data-hero-slider]");
const heroSliderItems = document.querySelectorAll("[data-hero-slider-item]");
const heroSliderPrevBtn = document.querySelector("[data-prev-btn");
const heroSliderNextBtn = document.querySelector("[data-next-btn]");

let currentSlidePos = 0;
let lastActiveSliderItem = heroSliderItems[0];

const updateSliderPos = function () {
    lastActiveSliderItem.classList.remove("active");
    heroSliderItems[currentSlidePos].classList.add("active");
    lastActiveSliderItem = heroSliderItems[currentSlidePos];
}

const slideNext = function () {
    if (currentSlidePos >= heroSliderItems.length - 1)
        currentSlidePos = 0;
    else {
        currentSlidePos++;
    }

    updateSliderPos();
}

heroSliderNextBtn.addEventListener("click", slideNext);

const slidePrev = function () {
    if (currentSlidePos ) {
        currentSlidePos = heroSliderItems.length - 1;
    } else {
        currentSlidePos--;
    }

    updateSliderPos();
}

heroSliderPrevBtn.addEventListener("click", slidePrev);


// Carrusel Automatico

let autoSlideInterval;

const autoSlide = function () {
    autoSlideInterval = setInterval(function () {
        slideNext();
    }, 7000);
}

addEventOnElements([heroSliderNextBtn, heroSliderPrevBtn], "mouseover", function(){
    clearInterval(autoSlideInterval);
});

addEventOnElements([heroSliderNextBtn, heroSliderPrevBtn], "mouseout", autoSlide);

window.addEventListener("load", autoSlide);


// Contador restante subastas

function startCountdown(element, endTime) {
    function updateCountdown() {
        const now = new Date().getTime();
        const endTimeDate = new Date(endTime).getTime();
        const distance = endTimeDate - now;

        if (distance < 0) {
            element.innerHTML = "Subasta finalizada";
            return;
        }

        const hours = Math.floor((distance % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
        const minutes = Math.floor((distance % (1000 * 60 * 60)) / (1000 * 60));
        const seconds = Math.floor((distance % (1000 * 60)) / 1000);

        element.innerHTML = hours + "h " + minutes + "m " + seconds + "s";
    }

    updateCountdown();
    setInterval(updateCountdown, 1000);
}

document.addEventListener("DOMContentLoaded", function() {
    const countdownElements = document.querySelectorAll('.countdown');
    countdownElements.forEach(function(element) {
        const endTime = element.getAttribute('data-end-time');
        startCountdown(element, endTime);
    });
});