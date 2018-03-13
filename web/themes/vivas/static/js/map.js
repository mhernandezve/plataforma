var map = L.map('map-wrapper').setView([-1.8, -83], 6)
L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
  attribution: '© Contribuidores de <a href="http://openstreetmap.org">OpenStreetMap</a>',
  minZoom: 6,
  maxZoom: 15
}).addTo(map)

var coordinates = [
  [0.011944, -78.431389],
  [-0.002222, -78.455833],
  [-2.18093, -79.877929],
  [-2.194061, -79.879874],
  [-2.1890881,-79.9362873],
  [-2.9014, -79.00679],
  [-3.986703, -79.198936],
  [-0.457212, -90.274332],
  [-1.2975, -90.434167]
]

var clusterGroup = L.markerClusterGroup()

coordinates.forEach(function(coordinate) {
  L.marker(coordinate).bindTooltip('Clic para más información')
  .on('click', function() {
    UIkit.modal('#map-modal').show()
  }).addTo(clusterGroup)
})

clusterGroup.addTo(map)
