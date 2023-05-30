// Navbar
const menuIcon = document.getElementById("menu");
const listContainer = document.getElementById("list");
const closeIcon = document.getElementById("close");

console.log(menuIcon);

menuIcon.addEventListener("click", () => {
  menuIcon.classList.add("display-none");
  listContainer.classList.add("display__menu-cel");
  closeIcon.classList.add("display-show");
  console.log("HOLS");
});

closeIcon.addEventListener("click", () => {
  listContainer.classList.replace("display__menu-cel", "display-none");
  menuIcon.classList.remove("display-none");
});

const divContainer = document.getElementById("imglogo-container");
const imgLogo = document.getElementById("main-logo");
const inviteTitle = document.getElementById("invitar");

divContainer.addEventListener("mouseenter", () => {
  imgLogo.classList.add("logoEffect");
  inviteTitle.classList.add("titleEffect");
});

divContainer.addEventListener("mouseleave", () => {
  imgLogo.classList.remove("logoEffect");
  inviteTitle.classList.remove("titleEffect");
});
