function encode() {
    var input = document.getElementById("input").value;
    document.getElementById("output").value = btoa(input);
}

function decode() {
    var output = document.getElementById("output").value;
    document.getElementById("input").value = atob(output)
}