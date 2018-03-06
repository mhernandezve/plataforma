var map = L.map('map-wrapper').setView([-1.8, -83], 6)
L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
  attribution: '© Contribuidores de <a href="http://openstreetmap.org">OpenStreetMap</a>',
  minZoom: 6,
  maxZoom: 15
}).addTo(map)
