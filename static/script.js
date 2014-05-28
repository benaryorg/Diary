window.onload = function() {
	resetStyle();
}

window.onresize = function() {
	resetStyle();
}

var resetStyle = function() {
	document.getElementById("mainContainer").style.minHeight = window.innerHeight + "px";
}
