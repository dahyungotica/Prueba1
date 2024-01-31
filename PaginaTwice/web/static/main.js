const app = document.getElementById('typewriter');
const typewriter = new Typewriter(app, {
    loop: true,
    delay: 75
});

typewriter
 .typeString('¡One in a million!')
 .pauseFor(200)
 .start();

document.getElementById("twiceButton").addEventListener("click", function() {
    window.open("https://twice.jype.com/", "_blank");
});
  
document.getElementById("loginButton").addEventListener("click", function() {
    window.location.href = "form.html";
});
  