var pays = ['eastern_australia', 'indonesia', 'new_guinea', 'alaska', 'ontario', 'northwest_territory', 'venezuela', 'madagascar', 'north_africa', 'greenland', 'iceland', 'great_britain', 'scandinavia', 'japan', 'yakursk', 'kamchatka', 'siberia', 'ural', 'afghanistan', 'middle_east', 'india', 'siam', 'china', 'mongolia', 'irkutsk', 'ukraine', 'southern_europe', 'western_europe', 'northern_europe', 'egypt', 'east_africa', 'congo', 'south_africa', 'brazil', 'argentina', 'eastern_united_states', 'western_united_states', 'quebec', 'central_america', 'peru', 'western_australia', 'alberta'];


function change_couleur(nom_territoire,couleur){
	territoire = document.getElementById(nom_territoire);
	if(territoire !== null){
		territoire.style.fill = couleur;
	}
}



function init(){
	for (i in pays){
		n = pays[i]
		e = document.getElementById(n);
		if(e !== null){
		e.classList.add('empty');
		e.onclick = function () {change_couleur(n,'black')};
		}else{
			alert(n);
		}
	}
}

function test(){
	alert('test');
}
