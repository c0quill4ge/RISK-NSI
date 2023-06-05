// const pays = ['eastern_australia', 'indonesia', 'new_guinea', 'alaska', 'ontario', 'northwest_territory', 'venezuela', 'madagascar', 'north_africa', 'greenland', 'iceland', 'great_britain', 'scandinavia', 'japan', 'yakursk', 'kamchatka', 'siberia', 'ural', 'afghanistan', 'middle_east', 'india', 'siam', 'china', 'mongolia', 'irkutsk', 'ukraine', 'southern_europe', 'western_europe', 'northern_europe', 'egypt', 'east_africa', 'congo', 'south_africa', 'brazil', 'argentina', 'eastern_united_states', 'western_united_states', 'quebec', 'central_america', 'peru', 'western_australia', 'alberta'];
const pays = [];
const continents = {
    europa: ['great_britain', 'iceland', 'northern_europe', 'scandinavia', 'southern_europe', 'ukraine', 'western_europe'],
    oceania: ['eastern_australia', 'indonesia', 'new_guinea', 'western_australia'],
    africa: ['congo', 'east_africa', 'egypt', 'madagascar', 'north_africa', 'south_africa'],
    asia: ['middle_east', 'india', 'siam', 'china', 'afghanistan', 'ural', 'siberia', 'mongolia', 'japan', 'kamchatka', 'irkutsk', 'yakursk'],
    north_america: ['greenland', 'northwest_territory', 'alaska', 'alberta', 'ontario', 'quebec', 'eastern_united_states', 'western_united_states', 'central_america'],
    south_america: ['venezuela', 'peru', 'brazil', 'argentina']
};
const half = {}
// const half = {
//     indonesia: {x: 416.0439453125, y: 247.7602081298828},
//     great_britain: {x: 370.923095703125, y: 226.00039672851562},
//     yakursk: {x: 408.0541076660156, y: 222.15835571289062},
//     kamchatka: {x: 95.6987075805664, y: 86.92676544189453},
//     siberia: {x: 156.35897827148438, y: 108.22835540771484},
//     ural: {x: 122.86228942871094, y: 81.8744888305664},
//     afghanistan: {x: 158.62890625, y: 190.4375},
//     middle_east: {x: 313.442138671875, y: 262.56787109375},
//     india: {x: 236.4832763671875, y: 185.5},
//     siam: {x: 188.29393005371094, y: 68.57536315917969},
//     china: {x: 234.97531127929688, y: 104.81877899169922},
//     mongolia: {x: 224.8826904296875, y: 122.02777862548828},
//     irkutsk: {x: 258.88653564453125, y: 92.59090423583984},
//     ukraine: {x: 412.3205871582031, y: 126.9850845336914},
//     southern_europe: {x: 371.3095397949219, y: 78.24330139160156},
//     western_europe: {x: 390.7427978515625, y: 83.96475982666016},
//     northern_europe: {x: 337.2638854980469, y: 72.7572250366211},
//     egypt: {x: 329.6111145019531, y: 84.375},
//     east_africa: {x: 314.3939514160156, y: 132.95753479003906},
//     congo: {x: 285.5090026855469, y: 170.30194091796875},
//     south_africa: {x: 335.69580078125, y: 166.4220428466797},
//     brazil: {x: 372.0848693847656, y: 185.70611572265625},
//     argentina: {x: 348.5326232910156, y: 140.20187377929688},
//     eastern_united_states: {x: 368.5231018066406, y: 127.81149291992188},
//     western_united_states: {x: 365.64251708984375, y: 106.41654968261719},
//     quebec: {x: 280.92657470703125, y: 93.5363998413086},
//     central_america: {x: 258.30499267578125, y: 150.8422088623047},
//     peru: {x: 232.71005249023438, y: 150.875},
//     western_australia: {x: 255.0625, y: 126.6875},
//     alberta: {x: 269.1244812011719, y: 192.6875},
//     alaska : {x:0,y:0},
//     northwest_territory : {x:0,y:0},
//     ontario : {x:0,y:0},
//     greenland : {x:0,y:0},
//     venezuela : {x:0,y:0},
//     north_africa : {x:0,y:0},
//     iceland : {x:0,y:0},
//     scandinavia : {x:0,y:0},
//     japan : {x:0,y:0},
//     madagascar : {x:0,y:0},
//     new_guinea : {x:0,y:0},
//     eastern_australia: {x:0,y:0}
// }


// Récupérer l'élément path
const svgBoard = document.querySelector("#main_game__board");
// Parcourir tous les éléments <path> du SVG
const paths = svgBoard.querySelectorAll("path");
paths.forEach((path) => {
    // Récupérer l'ID du path
    const id = path.getAttribute("id");

    // Obtenir la boîte englobante du path
    const bbox = path.getBBox();

    // Calculer le centre du path
    const centerX = bbox.x + bbox.width / 2;
    const centerY = bbox.y + bbox.height / 2;

    // Ajouter les coordonnées x et y dans le dictionnaire half avec l'ID du path
    half[id] = { x: centerX, y: centerY };
});



function init(num_joueur){ //num_joueur : str (j1,j2,j3,j4,j5,j6)
    $nom_joueur = num_joueur;
    for (let id_pays in pays){
        let nom_pays = pays[id_pays];
        let pays_selectionne = document.getElementById(nom_pays);
        if(pays_selectionne !== null){
            pays_selectionne.style.removeProperty('fill');
            pays_selectionne.style.removeProperty('fill-opacity');
            pays_selectionne.style.removeProperty('stroke');
            pays_selectionne.classList.add('empty');
            pays_selectionne.onclick = select_territoire_loop(nom_pays);
            half[nom_pays] = coord_centre(nom_pays); // remplis le dictionnaire half avec les coordonnées des centres des pays
        }else{
            alert(nom_pays);
        }
    }
}

function get_continent(nom_pays){
    for(let c in continents){
        if(continents[c].includes(nom_pays)){
            return c;
        }
    }
}


function change_classe(nom_territoire,classe){
    territoire = document.getElementById(nom_territoire);
    if(territoire !== null){
        territoire.classList.remove('empty','j1','j2','j3','j4','j5','j6');
        territoire.classList.add(classe);
    }
}

function select_territoire(nom_territoire){
    L = document.getElementsByClassName('selected');
    while(L.length>0){
        L[0].classList.remove('selected');
    }
    territoire = document.getElementById(nom_territoire);
    if(territoire !== null){
        territoire.classList.add('selected');
    }
    document.getElementById('label_pays_selectionne').innerHTML = 'Pays sélectionné: '.concat(L[0].id);
    document.getElementById('label_continent').innerHTML = 'Continent: '.concat(get_continent(L[0].id));
}

function conquerir(){
    let pays_selectionne = document.getElementsByClassName('selected');
    if (pays_selectionne.length > 0){
        change_classe(pays_selectionne[0].id,$nom_joueur);
    }
}

function change_classe_loop(nom_pays,nom_classe){ // permet d'attribuer à chaque territoire la fonction change_classe appropriée (dans la boucle)
    return function () {change_classe(nom_pays,nom_classe)};
}

function select_territoire_loop(nom_pays){ // permet d'attribuer à chaque territoire la fonction select_territoire appropriée (dans la boucle)
    return function () {select_territoire(nom_pays)};
}

function mode_continent(){ //met l'affichage de la carte en mode continent (on ne voit pas les territoires des joueurs)
    for (let id_pays in pays){
        let pays_selectionne = document.getElementById(pays[id_pays]);
        pays_selectionne.classList.add('continent');
    }
    const bouton_mode_carte = document.getElementById('bouton_mode_carte');
    bouton_mode_carte.innerHTML = 'Mode Joueurs';
    bouton_mode_carte.onclick = function () {mode_joueurs()};
}

function mode_joueurs(){ //met l'affichage de la carte en mode joueur (on voit les territoires des joueurs)
    for (let id_pays in pays){
        let pays_selectionne = document.getElementById(pays[id_pays]);
        pays_selectionne.classList.remove('continent');
    }
    const bouton_mode_carte = document.getElementById('bouton_mode_carte');
    bouton_mode_carte.innerHTML = 'Mode Continent';
    bouton_mode_carte.onclick = function () {mode_continent()};
}

function update_troop_number(nom_pays,nb_troupes){
    let texte_cercle_selectionne = document.getElementById('texte_cercle_'+nom_pays);
    texte_cercle_selectionne.innerHTML = nb_troupes;
}

function create_troop_circle() {
    for (let id_pays in pays) {
        let nom_pays = pays[id_pays];
        groupe = document.createElementNS("http://www.w3.org/2000/svg","g");
        groupe.setAttribute('id', 'cercle_' + nom_pays);
        cercle = document.createElementNS("http://www.w3.org/2000/svg","circle");
        texte = document.createElementNS("http://www.w3.org/2000/svg","text");
        cercle.setAttribute("cx", half[nom_pays].x);
        cercle.setAttribute("cy", half[nom_pays].y);
        texte.innerHTML = '0';

        texte.setAttribute('x', half[nom_pays].x-5);
        texte.setAttribute('y', half[nom_pays].y+5);
        texte.setAttribute('font-size', 15);
        texte.setAttribute('fill', 'white');
        texte.setAttribute('id', 'texte_cercle_' + nom_pays);

        groupe.appendChild(cercle);

        groupe.appendChild(texte);

        document.getElementById("layer4").appendChild(groupe);
        cercle.setAttribute("r", texte.getBBox().width*1.5);
    }
}


function change_nb_troupes(nom_pays,nb_troupes){
    let texte = document.getElementById('texte_cercle_'+nom_pays);
    texte.innerHTML = nb_troupes;
}

function coord_centre(nom_territoire){ // renvoie les coordonnées du centre d'un objet svg
    let territoire = document.getElementById(nom_territoire);
    let bbox = territoire.getBBox(); // dictionnaire {x:float y:float width:float height:float}
    return {x:bbox.x+bbox.width/2,y:bbox.y+bbox.height/2};
}

function cacher_cercles(){
    for (let i in pays){
        let nom_pays = pays[i];
        let groupe = document.getElementById('groupe_cercle_'+nom_pays);
        document.getElementById('groupe_cercle_'+nom_pays).classList.add('continent');
        //let bouton_cercles = document.getElementById('bouton_mode_cercles');
        //bouton_cercles.innerHTML = 'Montrer les cercles';
        //bouton_cercles.onclick = function () {montrer_cercles()};
    }
}

function montrer_cercles(){
    for (let i in pays){
        let nom_pays = pays[i];
        let groupe = document.getElementById('groupe_cercle_'+nom_pays);
        document.getElementById('groupe_cercle_'+nom_pays).classList.remove('continent');
        //let bouton_cercles = document.getElementById('bouton_mode_cercles');
        //bouton_cercles.innerHTML = 'Cacher les cercles';
        //bouton_cercles.onclick = function () {cacher_cercles()};
    }
}