window.addEventListener("load", function () {
  const loader = document.getElementById("loader");
  const duration = Math.floor(Math.random() * 3000) + 1000;
  setTimeout(function () {
    loader.classList.add("exiting");
    setTimeout(function () {
      loader.style.zIndex = -1;
    }, 500);
  }, duration);
});