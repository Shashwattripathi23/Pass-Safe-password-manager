var sw = false;
if (sw === true) {
  document.querySelector("#Sin").style.backgroundColor = "rgb(161, 161, 161)";
} else {
  document.querySelector("#Sin").style.backgroundColor = "transparent";
}
window.onload = function () {
  sw = true;
  // document.querySelector(".fpage ").style.transform = "scale(0) ";
  document.querySelector("#Sin").style.backgroundColor = "#393E46";
  document.querySelector("#main").style.transform = "scale(1)";
  document.querySelector("#main").style.left = "700px";
};
// function shrink() {
//   sw = true;
//   // document.querySelector(".fpage ").style.transform = "scale(0) ";
//   document.querySelector("#Sin").style.backgroundColor = "rgb(161, 161, 161)";
//   document.querySelector("#main").style.transform = "scale(1)";
//   document.querySelector("#main").style.left = "700px";
// }

const login = document.querySelector("#Sin");
login.addEventListener("click", function () {
  login.style.backgroundColor = "#393E46";
  document.querySelector("#Sup").style.backgroundColor = "transparent";
  if (sw === false) {
    document.querySelector("#logg ").style.transform = "translateX(0px)";
    document.querySelector("#sigg ").style.transform = "translateX(0px)";
    sw = true;
  }
});

const sigin = document.querySelector("#Sup");
sigin.addEventListener("click", function () {
  sigin.style.backgroundColor = "#393E46";
  login.style.backgroundColor = "transparent";
  if (sw === true) {
    document.querySelector("#logg ").style.transform = "translateX( -400px)";
    document.querySelector("#sigg ").style.transform = "translateX(-400px)";
    sw = false;
  }
});
