const loginMenu = document.getElementById("login-menu");
const loginForm = document.getElementById("login-form");

// Tambahkan event listener untuk menampilkan atau menyembunyikan menu login saat menu diklik
loginMenu.addEventListener("click", function() {
  if (loginForm.style.display === "none") {
    loginForm.style.display = "block";
  } else {
    loginForm.style.display = "none";
  }
});
