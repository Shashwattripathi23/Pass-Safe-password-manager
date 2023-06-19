const ad = document.getElementById("add");
const box = document.getElementById("box");

ad.addEventListener("click", function () {
  box.style.transform = "translateX(0vh)";
  box.style.transform = "scale(1.5)";
  //   document.querySelector("#main").style.opacity=""
  document.querySelector("#main").style.filter = "blur(5px)";
  document.querySelector("#nav").style.filter = "blur(5px)";
});
