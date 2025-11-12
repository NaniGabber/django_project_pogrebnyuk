
document.addEventListener("DOMContentLoaded", () => {

  //message_block logic
  function fadeOut(element) {
    if (!element.classList.contains("fade_out")) {
      element.classList.add("fade_out");
      element.addEventListener("transitionend", () => {
        element.remove();
      }, { once: true });
    }
  }

  const message_block = document.querySelector(".messages_block p")
  if (message_block) {
    const autoHide = setTimeout(() => fadeOut(message_block), 3000);
    message_block.addEventListener("click", () => {
      clearTimeout(autoHide);
      fadeOut(message_block);
    });
  }
  ////////
//load scroll position
  const scrollY = localStorage.getItem('scrollY');
  if(scrollY !== null){
    window.scrollTo(0, parseInt(scrollY));
  }

  const observer = new MutationObserver((mutationsList) => {
    for (const mutation of mutationsList) {
      for (const node of mutation.addedNodes) {
        //cart_button visibility restore (MutationObserver is needed because the cart (and messages) appears after a fetch request, with some delay.)
        if (node.nodeType === 1 && node.classList.contains("cart")) {
          if (localStorage.getItem('cartVisible') === "true")
            node.style.visibility = "visible";

          //cart_close_button
          document.querySelector(".cart_close_button").addEventListener("click", () => {
            document.querySelector(".cart").style.visibility = "hidden";
            localStorage.setItem('cartVisible', "false");
          });
          return;
        }

      }
    }
    observer.disconnect();
  });
  observer.observe(document.body, { childList: true, subtree: true });

});

//cart_button
document.querySelector(".cart_button").addEventListener("click", () => {
  const cart = document.querySelector(".cart");
  if (cart)
    if (cart.style.visibility === "visible")
      cart.style.visibility = "hidden";
    else cart.style.visibility = "visible";
  localStorage.setItem("cartVisible", cart.style.visibility === "visible" ? "true" : "false");
});

//save scroll position
window.addEventListener('beforeunload', () => {
  localStorage.setItem("scrollY", window.scrollY);
});

