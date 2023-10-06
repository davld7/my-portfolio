document.addEventListener("DOMContentLoaded", function () {
    const indexLink = document.getElementById("index");
    const projectsLink = document.getElementById("projects");
    const aboutLink = document.getElementById("about");
    const contactLink = document.getElementById("contact");

    indexLink.addEventListener("click", function (e) {
        e.preventDefault();
        window.location.href = "/";
    });

    projectsLink.addEventListener("click", function (e) {
        e.preventDefault();
        window.location.href = "/projects/";
    });

    aboutLink.addEventListener("click", function (e) {
        e.preventDefault();
        window.location.href = "/about/";
    });

    contactLink.addEventListener("click", function (e) {
        e.preventDefault();
        window.location.href = "/contact/";
    });
});