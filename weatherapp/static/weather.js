window.addEventListener('load', () =>{
	let lang;
	let lat; //lattitude and langitude as variables

	if(navigator.geolocation){
		navigator.geolocation.getCurrentPosition(position =>{ //now we got current loaction but not assingned for process
			long = position.coords.longitude;// coords are co ordinates assigning the loaction as a varibles values
			lat = position.coords.lattitude;
		})

	}else{
		alert('Allow loaction')
	}


});

var parent = document.querySelector(".container"),
	x= document.querySelector(".x"),

x.addEventListener("click", disappearx); // when the x is clicked the pop up x only will be disappeared
function disappearx(){
	parent.style.display="none";
}