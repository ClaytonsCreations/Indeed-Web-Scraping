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
  var lng = data.lng
  markers.addLayer(L.marker([lat, lng]).bindPopup("Job Title: "  + data.jobtitle + "Company: " + data.company));

  myMap.addLayer(markers);
 
});
