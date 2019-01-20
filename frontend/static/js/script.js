
function confirmReports() {
  // if no reports within tight radius,
  // document.getElementById("reportOverlay").style.display = "block";
  // if possible duplicate report,
  document.getElementById("dupConfOverlay").style.display = "block";  
}

function continueReport() {
  document.getElementById("dupConfOverlay").style.display = "none";
  document.getElementById("reportOverlay").style.display = "block";
}

function discardReport() {
  document.getElementById("reportOverlay").style.display = "none";
  document.getElementById("dupConfOverlay").style.display = "none";
  // delete data from table
}

function submitReport() {
  // submit form data to tables
  
  // if there are more reports, bring up the next one;
  //  bring up the appropriate overlay based on it's potential
  //  duplicate status
  
  // document.getElementById("reportOverlay").style.display = "none";
  
  // if not, display the thanks page for 3 seconds
  document.getElementById("reportOverlay").style.display = "none";
  document.getElementById("thanksReportOverlay").style.display = "block";
  setTimeout(thanksFade(), 3000);
  
}

// NOT CURRENTLY FUNCTIONING
function thanksFade() {
  $(document.getElementById("thanksReportOverlay")).fadeout(2000);
  document.getElementById("thanksReportOverlay").style.display = "none";
}



// Rachit
/*
var map, infoWindow, heatmap, tracking;

  function initMap() {
    map = new google.maps.Map(document.getElementById('map'), {
      center: {lat: 42.728351, lng: -84.481976},
      zoom: 6
    });
    infoWindow = new google.maps.InfoWindow;
    tracking = true;
    heatmap = new google.maps.visualization.HeatmapLayer({
        data: getPoints(),
          map: map
        });

    // Try HTML5 geolocation.
    if (navigator.geolocation) {
      navigator.geolocation.getCurrentPosition(function(position) {
        var pos = {
          lat: position.coords.latitude,
          lng: position.coords.longitude
        };

        map.setCenter(pos);
      }, function() {
        handleLocationError(true, infoWindow, map.getCenter());
      });
    } else {
      // Browser doesn't support Geolocation
      handleLocationError(false, infoWindow, map.getCenter());
    }
  }

  function selectRoad() {
      heatmap = new google.maps.visualization.HeatmapLayer({
        data: getRoadPoints(),
          map: map
        });
  }

  function selectAccidents() {
      heatmap = new google.maps.visualization.HeatmapLayer({
        data: getAccidentPoints(),
          map: map
        });
  }


  function handleLocationError(browserHasGeolocation, infoWindow, pos) {
    infoWindow.setPosition(pos);
    infoWindow.setContent(browserHasGeolocation ?
                          'Error: The Geolocation service failed.' :
                          'Error: Your browser doesn\'t support geolocation.');
    infoWindow.open(map);
  }

  function getRoadPoints() {
      return {{ all_road_points }}
  }

  function getAccidentPoints() {
      return {{ all_accident_points }}
  }

  function toggleTracking() {
      if (tracking) {
          tracking = false;
      } else {
          tracking = true;
      }
  }

  setInterval(function() {
    if (tracking) {
      if (navigator.geolocation) {
        navigator.geolocation.getCurrentPosition(function (position) {
          var pos = {
            lat: position.coords.latitude,
            lng: position.coords.longitude
          };

          map.setCenter(pos);
        }, function () {
          handleLocationError(true, infoWindow, map.getCenter());
        });
      } else {
        // Browser doesn't support Geolocation
        handleLocationError(false, infoWindow, map.getCenter());
      }
    }
  }, 3000)
  
  */