const btnSingnIn = document.getElementById("sign-in");
      btnSingnUp = document.getElementById("sign-up");
      formRegister = document.querySelector(".register"),
      formLogin = document.querySelector(".login")
btnSingnIn.addEventListener("click",e => {
    formRegister.classList.add("hide");
    formLogin.classList.remove("hide")
})
btnSingnUp.addEventListener("click",e => {
    formLogin.classList.add("hide");
    formRegister.classList.remove("hide")
})