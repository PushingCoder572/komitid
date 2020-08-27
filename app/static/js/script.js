function swap_form() {
  let l_form = document.getElementById("login_form");
  let s_form = document.getElementById("signup_form");

  let temp = l_form.style.display
  l_form.style.display = s_form.style.display;
  s_form.style.display = temp
}
