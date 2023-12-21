
const arabutton = document.getElementById("search-form").addEventListener("submit", function (event) {
    event.preventDefault();
    
    var searchTerm = document.getElementById("search").value;
    
    if (searchTerm) {
        // Google'da arama yapmak için aşağıdaki satırı kullanabilirsiniz.
        window.open("https://www.google.com/search?q=" + searchTerm, "_blank");
    } else {
        alert("Search.");
    }
});

const $ = (selector) => {
    return document.querySelector(selector);
}
const hour = $('.hour');
const dot = $('.dot');
const min = $('.min');
const week = $('.week');
let showDot = true;

function update() {
    showDot = !showDot;
    const now = new Date();

    if (showDot) {
        dot.classList.add('invsible');
    } else {
        dot.classList.remove('invsible');
    }
    hour.textContent = String(now.getHours())
     .padStart(2, '0');
    min.textContent = String(now.getMinutes())
     .padStart(2, '0')

    Array
     .from(week.children)
     .forEach(
        (ele) => {
           ele.classList.remove('active');
        }
     );
     
  week
    .children[now.getDay()]
    .classList
    .add('active');   
}

setInterval(update, 500);
