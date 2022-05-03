var display = document.getElementById('display')
var clear = document.getElementById('C')
var one = document.getElementById('1')
var two = document.getElementById('2')
var three = document.getElementById('3')
var four = document.getElementById('4')
var five = document.getElementById('5')
var six = document.getElementById('6')
var seven = document.getElementById('7')
var eight = document.getElementById('8')
var nine = document.getElementById('9')
var zero = document.getElementById('0')
var add = document.getElementById('+')
var sub = document.getElementById('-')
var mul = document.getElementById('*')
var div = document.getElementById('/')
var eq = document.getElementById('=')

var out = ""

clear.addEventListener('click', function(){
    out=""
    display.innerHTML = out;
} )

one.addEventListener('click', function(){
    out+="1"
    display.innerHTML = out;
} )

two.addEventListener('click', function(){
    out+="2"
    display.innerHTML = out;
} )

three.addEventListener('click', function(){
    out+="3"
    display.innerHTML = out;
} )
four.addEventListener('click', function(){
    out+="4"
    display.innerHTML = out;
} )
five.addEventListener('click', function(){
    out+="5"
    display.innerHTML = out;
} )
six.addEventListener('click', function(){
    out+="6"
    display.innerHTML = out;
} )

seven.addEventListener('click', function(){
    out+="7"
    display.innerHTML = out;
} )

eight.addEventListener('click', function(){
    out+="8"
    display.innerHTML = out;
} )

nine.addEventListener('click', function(){
    out+="9"
    display.innerHTML = out;
} )

zero.addEventListener('click', function(){
    out+="0"
    display.innerHTML = out;
} )

add.addEventListener('click', function(){
    out+="+"
    display.innerHTML = out;
} )

sub.addEventListener('click', function(){
    out+="-"
    display.innerHTML = out;
} )

mul.addEventListener('click', function(){
    out+="*"
    display.innerHTML = out;
} )

div.addEventListener('click', function(){
    out+="/"
    display.innerHTML = out;
} )

eq.addEventListener('click', function(){
    display.innerHTML = eval(out)
    out= eval(out)
})
