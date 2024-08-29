const btn = document.querySelector(".btn-share");
const form = document.querySelector(".share-fact");

btn.addEventListener('click', function() {
    // console.log("CLICK");
    if (form.classList.contains("hidden")) {
        form.classList.remove("hidden");
        btn.textContent = "Close"
    } else {
        form.classList.add("hidden")
        btn.textContent = "Share Something Cool."
    }
})

