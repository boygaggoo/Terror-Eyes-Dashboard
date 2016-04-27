initial1="""
<!DOCTYPE html>
<html>
  <head>
    <meta charset="utf-8">
    <title>Heatmaps</title>
    <style>
      html, body {
        height: 100%;
        margin: 0;
        padding: 0;
      }
      #map {
        height: 100%;
      }
      #floating-panel {
        position: absolute;
        top: 10px;
        left: 25%;
        z-index: 5;
        background-color: #fff;
        padding: 5px;
        border: 1px solid #999;
        text-align: center;
        font-family: 'Roboto','sans-serif';
        line-height: 30px;
        padding-left: 10px;
      }

      #floating-panel {
        background-color: #fff;
        border: 1px solid #999;
        left: 25%;
        padding: 5px;
        position: absolute;
        top: 10px;
        z-index: 5;
      }
    </style>
  </head>

  <body>
    <div id="floating-panel">
      <button onclick="toggleHeatmapRisky()">Toggle RiskyLocs</button>
	  <button onclick="toggleHeatmapTwitter()">Toggle TwitterLocs</button>
      <button onclick="changeRadius()">Change Radius</button>
      <button onclick="changeOpacity()">Change Opacity</button>
    </div>
    <div id="map"></div>
    <script>

    var map, heatmap;

    function initMap() {
    var bounds = new google.maps.LatLngBounds();
      map = new google.maps.Map(document.getElementById('map'), {
        zoom: 3,
        center: {lat:0,lng:0},
        mapTypeId: google.maps.MapTypeId.ROADMAP
      });
      
      function fitForBounds(data){
    	for (var i = 0; i < data.length; i++) {
    		bounds.extend(data[i]);
    	}
    }
    fitForBounds(getPoints());
    fitForBounds(getPointsTwitter());
    map.setCenter(bounds.getCenter());
    map.fitBounds(bounds);
      
      heatmap = new google.maps.visualization.HeatmapLayer({
        data: getPoints(),
        map: map
      });
      heatmap2 = new google.maps.visualization.HeatmapLayer({
      data: getPointsTwitter(),
      map: map
      });
      changeGradient();
      changeRadius();
    }

    function toggleHeatmapRisky() {
      heatmap.setMap(heatmap.getMap() ? null : map);
    }
    function toggleHeatmapTwitter() {
      heatmap2.setMap(heatmap.getMap() ? null : map);
    }

    function changeGradient() {
      var gradient = [
        'rgba(0, 255, 255, 0)',
        'rgba(0, 255, 255, 1)',
        'rgba(0, 191, 255, 1)',
        'rgba(0, 127, 255, 1)',
        'rgba(0, 63, 255, 1)',
        'rgba(0, 0, 255, 1)',
        'rgba(0, 0, 223, 1)',
        'rgba(0, 0, 191, 1)',
        'rgba(0, 0, 159, 1)',
        'rgba(0, 0, 127, 1)',
        'rgba(63, 0, 91, 1)',
        'rgba(127, 0, 63, 1)',
        'rgba(191, 0, 31, 1)',
        'rgba(255, 0, 0, 1)'
      ]
      heatmap2.set('gradient', heatmap.get('gradient') ? null : gradient);
    }

    function changeRadius() {
      heatmap.set('radius', heatmap.get('radius') ? null : 20);
    }

    function changeOpacity() {
      heatmap.set('opacity', heatmap.get('opacity') ? null : 0.2);
    }

    // Heatmap data: 500 Points
    function getPoints() {
        return [

"""

#gps coords go here

initial2="""
    ];}
    function getPointsTwitter() {
      return [
      ];
    }
    </script>
    <script async defer
        src="https://maps.googleapis.com/maps/api/js?key=AIzaSyCWC988fyeewFRL_xQPNaV0xHX3T_MKgRk&signed_in=true&libraries=visualization&callback=initMap">
    </script>
  </body>
</html>
"""

twitter1="""
];
}
function getPointsTwitter() {
  return [
"""


endTwitter="""
];
}
    </script>
    <script async defer
        src="https://maps.googleapis.com/maps/api/js?key=AIzaSyCWC988fyeewFRL_xQPNaV0xHX3T_MKgRk&signed_in=true&libraries=visualization&callback=initMap">
    </script>
  </body>
</html>
"""
