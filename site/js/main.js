//initialize the map, sets up layers for trees and You Are Here, and feeds it a null
function initMap() {
    //anything over 10000 points, use canvas (default is SVG renderer)
    const map = L.map('map', { maxZoom: 22, preferCanvas: true }).setView([39.95764876954889, -75.1629638671875], 13);

    const mapboxAccount = 'mapbox';
    const mapboxStyle = 'light-v10';
    const mapboxToken = 'pk.eyJ1IjoiY29udHJhaWwtZW50aHVzaWFzdCIsImEiOiJjbDlsbTRteXEwMWh0M3VwZjBqc2JrbWZ4In0.MCAs44cMD-2XioBijyx_Iw';

    L.tileLayer(`https://api.mapbox.com/styles/v1/${mapboxAccount}/${mapboxStyle}/tiles/256/{z}/{x}/{y}@2x?access_token=${mapboxToken}`, {
        maxZoom: 22,
        attribution: '© <a href="https://www.mapbox.com/about/maps/">Mapbox</a> © <a href="http://www.openstreetmap.org/copyright">OpenStreetMap</a> <strong><a href="https://www.mapbox.com/map-feedback/" target="_blank">Improve this map</a></strong>',
    }).addTo(map);


    map.treeLayer = L.geoJSON(null, {
        pointToLayer: (feature, latlng) => L.circleMarker(latlng),
    }).addTo(map);

    map.positionLayer = L.geoJSON(null).addTo(map);

    return map;
}

//clearing current environment, setting variables of focus
let app = {
    currentTree: null,
    notes: JSON.parse(localStorage.getItem('notes') || `{}`),
};

function downloadInventory() {
    fetch('data/tree_inventory.geojson')
        .then(resp => resp.json())
        .then(data => {
            map.treeLayer.addData(data);
        });
};

function userPositionSuccess(pos) {
    map.positionLayer.addData({
        'type': 'Point',
        'coordinates': [pos.coords.longitude, pos.coords.latitude]
    });
    map.setView([pos.coords.latitude, pos.coords.longitude], 18);
}

function userPositionFailure(err) {
    console.log(err);
    //add alert for "Please Give Us Your Data"
}

//On map load, gets users location, and then loads above functions
function setupGeolocationEvent() {
    navigator.geolocation.getCurrentPosition(
        userPositionSuccess,
        userPositionFailure
    )
}

const treeNameEle = document.getElementById('tree-name');
const treeNotesEle = document.getElementById('tree-notes');
const saveTreeButton = document.getElementById('save-tree-notes');

//console logs event, feeds in tree to various variables
function onTreeClicked(evt) {
    console.log(evt);
    const tree = evt.layer.feature;
    const treeID = tree.properties['OBJECTID'];
    const treeName = tree.properties['TREE_NAME'];
    console.log(`This tree is named `, treeName, ` and this tree's ID is`, treeID)
    app.currentTree = evt.layer.feature;

    treeNameEle.innerHTML = treeName;
    treeNotesEle.value = app.notes[treeID] || "";
}

//fell behind here, about 30minutes from end of class
function onSaveButtonClicked(evt) {
    const treeNote = treeNotesEle.value;
    const treeID = app.currentTree.properties['OBJECTID']
    app.notes[treeID] = treeNote;
    // console.log(treeNote);

    localStorage.setItem('notes', JSON.stringify(app.notes));
}

function setupTreeInfoForm() {
    saveTreeButton.addEventListener('click', onSaveButtonClicked)
};


//actually calling the functions

downloadInventory();

setupGeolocationEvent();
setupTreeInfoForm();
const map = initMap();
map.treeLayer.addEventListener('click', onTreeClicked);

window.app = app;
