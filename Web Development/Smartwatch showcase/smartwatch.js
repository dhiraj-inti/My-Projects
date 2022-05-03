var blue_btn = document.getElementById('blue')
var black_btn = document.getElementById('black')
var red_btn = document.getElementById('red')
var purple_btn = document.getElementById('purple')
var watch_img = document.getElementById('watch-img')
var watch_display = document.getElementById('watch-display')
var time_btn = document.getElementById('time')
var heart_btn = document.getElementById('heart')
var today = new Date();
var time = today.getHours() + ":" + today.getMinutes() + ":" + today.getSeconds();
watch_display.innerHTML = "Feature";
var time_interval = setInterval(function(){},1000)

function display(x){
    var today = new Date();
    var time = today.getHours() + ":" + today.getMinutes() + ":" + today.getSeconds();
    return x%2===0 ? "72 BPM" :time;
}

function time_display(){
    watch_display.innerHTML = display(1)
}

time_btn.addEventListener('click',function(){
    time_interval = setInterval(time_display,1000)
})

heart_btn.addEventListener('click',function(){
    clearInterval(time_interval)
    watch_display.innerHTML = display(2)
})

blue_btn.addEventListener('click', function(){
    watch_img.src = "blue_watch.png"
})

black_btn.addEventListener('click', function(){
    watch_img.src = "black_watch.png"
})

purple_btn.addEventListener('click', function(){
    watch_img.src = "purple_watch.png"
})

red_btn.addEventListener('click', function(){
    watch_img.src = "red_watch.png"
})