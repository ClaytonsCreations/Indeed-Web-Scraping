var myMap = L.map("map", {
  center: [33.39, -118.42],
  zoom: 11
});

L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
    attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
}).addTo(myMap);  

var markers = L.markerClusterGroup()

d3.csv("Indeed_coordinates.csv", function(data) {
  var lat = data.lat
  var lon = data.lng
  markers.addLayer(L.marker([lat, lon]).bindPopup("Job Title: "  + data.jobtitle + "<br>Company: " + data.company));

  myMap.addLayer(markers);
 
});

